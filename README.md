# A Layered Edge-Fog-Cloud Sharded Architecture for ZKP-Based Academic Credentialing

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Academic Project](https://img.shields.io/badge/Type-Academic_Research-green.svg)]()

## 📌 Project Overview

This repository contains the implementation and evaluation framework for **LEFC-ZK (Layered Edge-Fog-Cloud Sharded Architecture)**, a scalable privacy-preserving academic credential verification architecture based on **Zero-Knowledge Proofs (zk-SNARKs)**.

Current blockchain-based academic credentialing systems, such as **ZKBAR-V**, enable institutions to verify academic credentials without revealing sensitive student information. Although these systems provide strong privacy guarantees, they face several scalability challenges when deployed in large-scale environments.

The primary limitations include:

- **High Computational Cost:** Mobile devices are required to generate computationally expensive zk-SNARK proofs, resulting in excessive CPU usage, memory consumption, and battery drain.
- **Limited Network Throughput:** A single blockchain verification queue creates a bottleneck, restricting transaction processing to approximately **280 Transactions Per Second (TPS)**.
- **Unpredictable Storage Latency:** Dependence on the global IPFS network introduces inconsistent document retrieval times due to distributed peer availability.

The proposed **LEFC-ZK** architecture addresses these limitations through a hierarchical **Device–Edge–Fog–Cloud** framework that distributes computational workloads, minimizes latency, and enables parallel blockchain verification.

---

# 🏗️ System Architecture

LEFC-ZK introduces a three-tier architecture designed to improve scalability and efficiency.

## Tier 1 – Device Layer

Lightweight mobile clients function primarily as **Decentralized Identifier (DID)** managers.

Responsibilities include:

- Managing user identities
- Initiating verification requests
- Signing lightweight transactions

No expensive zk-SNARK generation is performed on user devices.

---

## Tier 2 – Edge/Fog Layer

### Edge Nodes

Edge nodes receive incoming verification requests and perform computationally intensive operations including:

- zk-SNARK proof generation
- Request preprocessing
- Load balancing

This significantly reduces resource consumption on mobile devices.

### Fog Nodes

Fog nodes maintain localized IPFS pinning services to:

- Cache frequently accessed credentials
- Reduce document retrieval latency
- Improve network reliability during high-demand periods

---

## Tier 3 – Cloud/Blockchain Layer

The cloud layer employs **geographic blockchain sharding**, allowing multiple smart contracts to process verification requests concurrently.

Key benefits include:

- Parallel transaction verification
- Increased throughput
- Reduced blockchain congestion
- Improved scalability for nationwide credential verification systems

---

# 🚀 Repository Structure

```text
.
├── dataset_generator.py      # Generates simulated verification requests
├── lefc_implementation.py        # Simulation engine and ablation study
├── requests_dataset.csv      # Generated workload dataset
├── README.md
├── latency_cpu_metrics.png
├── throughput_metrics.png
└── Project.pdf
```

### Files

| File | Description |
|------|-------------|
| `dataset_generator.py` | Generates thousands of simulated DID and IPFS-based verification requests for stress testing. |
| `lefc_evaluation.py` | Implements the complete LEFC-ZK simulation, including Edge, Fog, Cloud, and Blockchain components along with the ablation study. |
| `requests_dataset.csv` | Mock dataset representing concurrent graduation-day verification traffic. |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ZohaWajahat/A-Layered-Edge-Fog-Cloud-Sharded-Architecture-for-ZKP-Based-Academic-Credentialing.git

cd A-Layered-Edge-Fog-Cloud-Sharded-Architecture-for-ZKP-Based-Academic-Credentialing
```

Install the required dependencies:

```bash
pip install pandas matplotlib psutil
```

---

# 💻 Usage

## Step 1 – Generate the Dataset

Create a synthetic workload representing thousands of concurrent credential verification requests.

```bash
python dataset_generator.py
```

This generates:

```text
requests_dataset.csv
```

---

## Step 2 – Run the Simulation

Execute the LEFC-ZK simulation.

```bash
python lefc_implementation.py
```

The simulator processes the generated workload and evaluates system performance under different architectural configurations.

---

# 📊 Evaluation

The simulation compares the proposed architecture against several ablation configurations, including:

- Baseline ZKBAR-V
- Edge-only architecture
- Edge + Fog architecture
- Edge + Sharding architecture
- Complete LEFC-ZK architecture

Performance metrics include:

- Transactions Per Second (TPS)
- Average Latency
- CPU Utilization
- Memory Usage
- Storage Retrieval Time
- Scalability under Increasing Load

---

# 🔬 Research Contributions

The proposed architecture contributes the following improvements:

- Offloading zk-SNARK generation from mobile devices to edge infrastructure
- Localized IPFS caching through fog computing
- Geographic blockchain sharding for parallel verification
- Improved throughput with reduced verification latency
- Better resource utilization across distributed computing layers

---

# 📄 Citation

If you use this work in your research, please cite:

```bibtex
@article{LEFCZK2026,
  title={A Layered Edge-Fog-Cloud Sharded Architecture for ZKP-Based Academic Credentialing},
  author={Zoha Binte Wajahat},
  year={2026},
  journal={Research Project}
}
```

---

# 👨‍💻 Author

**Zoha Binte Wajahat**

BS Artificial Intelligence

Research Project on Privacy-Preserving Academic Credential Verification using Zero-Knowledge Proofs and Distributed Computing.
