import time
import psutil
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# IMPLEMENTATION OF THE 3 ARCHITECTURE TIERS
# ==========================================

class Tier1_DeviceLayer:
    """Represents the Student's Mobile Device"""
    def __init__(self):
        self.base_cpu = 2.0  # Normal idle CPU

    def generate_request(self, batch_size, offload_to_edge=True):
        """If not offloaded, device is forced to do heavy ZKP math."""
        psutil.cpu_percent(interval=None) # Reset monitor
        
        if offload_to_edge:
            # Device just signs a lightweight request (Fast)
            time.sleep(0.001 * batch_size) 
            cpu_used = psutil.cpu_percent(interval=None) + self.base_cpu
        else:
            # Device struggles to do heavy ZKP math (Slow & Heavy)
            time.sleep(0.05 * batch_size) 
            cpu_used = psutil.cpu_percent(interval=None) + 85.0 
            
        return cpu_used


class Tier2_EdgeFogLayer:
    """Represents the Local ISP/University Servers"""
    def __init__(self):
        pass

    def process_computation(self, batch_size, edge_enabled=True):
        """Edge handles ZKP generation if enabled."""
        if edge_enabled:
            # Edge does the math instantly
            time.sleep(0.001 * batch_size)
            
    def retrieve_document(self, batch_size, fog_enabled=True):
        """Fog handles local storage retrieval."""
        if fog_enabled:
            # Instant local retrieval
            time.sleep(0.005 * batch_size) 
        else:
            # Slow global IPFS retrieval
            time.sleep(0.1 * batch_size) 


class Tier3_BlockchainLayer:
    """Represents the zkEVM Blockchain"""
    def __init__(self, base_throughput=280):
        self.base_throughput = base_throughput # The 280 TPS limit from Base Paper

    def verify_transactions(self, data_batch, sharding_enabled=True):
        """If sharding is enabled, process in parallel based on region."""
        if sharding_enabled:
            # Count unique regions in this batch to simulate parallel shards
            active_shards = data_batch['shard_region'].nunique()
            # Throughput multiplies by the number of active shards
            return self.base_throughput * active_shards
        else:
            # Monolithic bottleneck
            return self.base_throughput


# ==========================================
# MAIN SIMULATION ENGINE
# ==========================================

class LEFC_Simulator:
    def __init__(self):
        # Initialize our 3 explicit layers
        self.device_layer = Tier1_DeviceLayer()
        self.edge_fog_layer = Tier2_EdgeFogLayer()
        self.blockchain_layer = Tier3_BlockchainLayer()

    def run_configuration(self, data_batch, use_edge, use_fog, use_shard):
        start_time = time.time()
        batch_size = len(data_batch)
        
        # 1. Device Layer Execution
        device_cpu = self.device_layer.generate_request(batch_size, offload_to_edge=use_edge)
        
        # 2. Edge / Fog Layer Execution
        self.edge_fog_layer.process_computation(batch_size, edge_enabled=use_edge)
        self.edge_fog_layer.retrieve_document(batch_size, fog_enabled=use_fog)
        
        # 3. Blockchain Layer Execution
        tps = self.blockchain_layer.verify_transactions(data_batch, sharding_enabled=use_shard)
        
        total_time = time.time() - start_time
        return {"latency": total_time, "cpu": min(device_cpu, 100), "tps": tps}


# ==========================================
# EXECUTION AND ABLATION STUDY
# ==========================================

def run_ablation_study():
    # Load dataset
    print("Loading dataset from requests_dataset.csv...")
    try:
        df = pd.read_csv("requests_dataset.csv")
    except FileNotFoundError:
        print("Error: Run dataset_generator.py first!")
        return
        
    test_batch = df.sample(100)
    simulator = LEFC_Simulator()
    
    print("\nRunning Ablation Study Simulations...")
    results = {
        "Base (ZKBAR-V)": simulator.run_configuration(test_batch, False, False, False),
        "LEFC: No Edge":  simulator.run_configuration(test_batch, False, True, True),
        "LEFC: No Fog":   simulator.run_configuration(test_batch, True, False, True),
        "LEFC: No Shard": simulator.run_configuration(test_batch, True, True, False),
        "LEFC: Full Prop.": simulator.run_configuration(test_batch, True, True, True)
    }
    
    # Print Results to Terminal
    print(f"\n{'Configuration':<20} | {'Latency (s)':<12} | {'Device CPU %':<12} | {'TPS':<5}")
    print("-" * 55)
    for config, metrics in results.items():
        print(f"{config:<20} | {metrics['latency']:<12.3f} | {metrics['cpu']:<12.1f} | {metrics['tps']:<5}")
        
    return results

def generate_visualizations(results):
    print("\nGenerating 400 DPI Graphs...")
    labels = list(results.keys())
    latencies = [res["latency"] for res in results.values()]
    cpus = [res["cpu"] for res in results.values()]
    tps = [res["tps"] for res in results.values()]

    # Graph 1: Latency and CPU (Dual Axis)
    fig, ax1 = plt.subplots(figsize=(10, 6), dpi=400)
    ax1.bar(labels, latencies, color='tab:blue', alpha=0.6, label="Latency (s)")
    ax1.set_ylabel('Execution Time / Latency (seconds)', color='tab:blue', fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.plot(labels, cpus, color='tab:red', marker='o', linewidth=2, label="Device CPU %")
    ax2.set_ylabel('Device CPU Consumption (%)', color='tab:red', fontweight='bold')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title('Ablation Study: Processing Latency vs Device CPU Overhead', fontweight='bold')
    fig.tight_layout()
    plt.savefig('latency_cpu_metrics.png', dpi=400)

    # Graph 2: Throughput (TPS)
    plt.figure(figsize=(8, 5), dpi=400)
    plt.bar(labels, tps, color=['#e63946', '#f4a261', '#f4a261', '#f4a261', '#2a9d8f'])
    plt.title('Scalability Comparison: Transactions Per Second (TPS)', fontweight='bold')
    plt.ylabel('TPS (Higher is Better)', fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('throughput_metrics.png', dpi=400)
    print("Saved 'latency_cpu_metrics.png' and 'throughput_metrics.png'")

if __name__ == "__main__":
    study_results = run_ablation_study()
    if study_results:
        generate_visualizations(study_results)