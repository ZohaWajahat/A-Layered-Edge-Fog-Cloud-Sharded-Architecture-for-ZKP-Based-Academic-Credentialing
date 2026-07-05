# A-Layered-Edge-Fog-Cloud-Sharded-Architecture-for-ZKP-Based-Academic-Credentialing

## 📌Project overview
This repository contains the Python-based network simulation and architectural research for LEFC-ZK (Layered Edge-Fog-Cloud Sharded Architecture).

Modern privacy-preserving academic credentialing systems (such as the base paper ZKBAR-V) utilize Zero-Knowledge Proofs (zk-SNARKs) and zkEVM blockchains to verify degrees without leaking sensitive student metadata. However, these monolithic systems suffer from crippling bottlenecks:
1. Computational Overhead: Forcing mobile devices to generate complex cryptographic proofs drains battery and memory.
2. Throughput Bottlenecks: Single smart-contract queues cap network scalability at roughly 280 Transactions Per Second (TPS).
3. Storage Latency: Relying on the global peer-to-peer IPFS network causes unpredictable document retrieval delays.

LEFC-ZK solves these issues by shifting the system from a flat blockchain model to a scalable 3-tier hierarchy.

## System Architecture
The LEFC-ZK framework introduces three specialized tiers:
• Tier 1 (Device Layer): Lightweight mobile clients acting merely as Decentralized Identifier (DID) managers. Zero heavy cryptographic math is performed here.
• Tier 2 (Edge/Fog Layer): * Edge Nodes intercept requests and absorb the massive computational burden of generating zk-SNARKs.
  • Fog Nodes run localized IPFS pinning services to ensure instant, local document retrieval.
• Tier 3 (Cloud/Blockchain Layer): Geographic Sharding partitions the blockchain consensus layer, allowing parallel smart contracts to verify transactions simultaneously, shattering the 280 TPS limit.
