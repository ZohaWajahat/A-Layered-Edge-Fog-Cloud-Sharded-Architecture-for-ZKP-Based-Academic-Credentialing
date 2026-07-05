# A-Layered-Edge-Fog-Cloud-Sharded-Architecture-for-ZKP-Based-Academic-Credentialing

## 📌Project overview
This repository contains the Python-based network simulation and architectural research for LEFC-ZK (Layered Edge-Fog-Cloud Sharded Architecture).

Modern privacy-preserving academic credentialing systems (such as the base paper ZKBAR-V) utilize Zero-Knowledge Proofs (zk-SNARKs) and zkEVM blockchains to verify degrees without leaking sensitive student metadata. However, these monolithic systems suffer from crippling bottlenecks:
1. Computational Overhead: Forcing mobile devices to generate complex cryptographic proofs drains battery and memory.
2. Throughput Bottlenecks: Single smart-contract queues cap network scalability at roughly 280 Transactions Per Second (TPS).
3. Storage Latency: Relying on the global peer-to-peer IPFS network causes unpredictable document retrieval delays.
