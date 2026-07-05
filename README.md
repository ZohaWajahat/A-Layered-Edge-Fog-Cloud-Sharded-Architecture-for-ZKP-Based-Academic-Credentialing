# A Layered Edge-Fog-Cloud Sharded Architecture for ZKP-Based Academic Credentialing

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Academic Project](https://img.shields.io/badge/Type-Academic_Research-green.svg)]()

## 📌 Project Overview
This repository contains the Python-based network simulation and architectural research for **LEFC-ZK (Layered Edge-Fog-Cloud Sharded Architecture)**.

Modern privacy-preserving academic credentialing systems (such as the base paper ZKBAR-V) utilize Zero-Knowledge Proofs (zk-SNARKs) and zkEVM blockchains to verify degrees without leaking sensitive student metadata. However, these monolithic systems suffer from crippling bottlenecks:
1. **Computational Overhead:** Forcing mobile devices to generate complex cryptographic proofs drains battery and memory.
2. **Throughput Bottlenecks:** Single smart-contract queues cap network scalability at roughly 280 Transactions Per Second (TPS).
3. **Storage Latency:** Relying on the global peer-to-peer IPFS network causes unpredictable document retrieval delays.

**LEFC-ZK** solves these issues by shifting the system from a flat blockchain model to a scalable 3-tier hierarchy.

## 🏗️ System Architecture
The LEFC-ZK framework introduces three specialized tiers:
* **Tier 1 (Device Layer):** Lightweight mobile clients acting merely as Decentralized Identifier (DID) managers. Zero heavy cryptographic math is performed here.
* **Tier 2 (Edge/Fog Layer):** * **Edge Nodes** intercept requests and absorb the massive computational burden of generating zk-SNARKs.
  * **Fog Nodes** run localized IPFS pinning services to ensure instant, local document retrieval.
* **Tier 3 (Cloud/Blockchain Layer):** Geographic Sharding partitions the blockchain consensus layer, allowing parallel smart contracts to verify transactions simultaneously, shattering the 280 TPS limit.

## 🚀 Repository Structure
* `dataset_generator.py` : Dynamically generates a mock dataset of thousands of concurrent verification requests (using simulated DIDs and IPFS hashes) to stress-test the network.
* `lefc_evaluation.py` : The core Object-Oriented simulation engine. It models the three tiers, processes the dataset, and conducts a rigorous Ablation Study.
* `requests_dataset.csv` : The generated mock payload data representing graduation-day traffic.

## ⚙️ Installation & Setup
To replicate this study, clone the repository and install the required Python dependencies:

```bash
# Clone the repository
git clone [https://github.com/YourUsername/A-Layered-Edge-Fog-Cloud-Sharded-Architecture-for-ZKP-Based-Academic-Credentialing.git](https://github.com/YourUsername/A-Layered-Edge-Fog-Cloud-Sharded-Architecture-for-ZKP-Based-Academic-Credentialing.git)
cd A-Layered-Edge-Fog-Cloud-Sharded-Architecture-for-ZKP-Based-Academic-Credentialing

# Install dependencies (Pandas, Matplotlib, Psutil)
pip install pandas matplotlib psutil

## 💻 Usage & Execution

**Step 1: Generate the Load-Testing Data**
Run the generator to create the simulated transaction dataset (`requests_dataset.csv`).
```bash
python dataset_generator.py
