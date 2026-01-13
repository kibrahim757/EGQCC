# 🌐 EgQCC Quantum Security Master Glossary
> **Version 1.0 | Comprehensive Reference for PQC, QKD, QRNG, and Quantum Risk Assessment.**

This glossary provides a deep technical dive into the terms, protocols, and mathematical foundations required for the EgQCC Quantum Security Track.

---

## 🏗️ Section 1: Quantum Mechanics & Physics Foundations
1. **Qubit (Quantum Bit):** The basic unit of quantum information.
2. **Superposition:** A fundamental principle where a quantum system exists in multiple states simultaneously.
3. **Entanglement:** A physical phenomenon where pairs or groups of particles remain connected, such that the state of one instantly influences the other.
4. **No-Cloning Theorem:** The impossibility of creating an identical copy of an arbitrary unknown quantum state.
5. **Heisenberg’s Uncertainty Principle:** The trade-off where measuring one property (like position) disturbs another (like momentum).
6. **Decoherence:** The loss of quantum coherence due to interaction with the external environment.
7. **Bloch Sphere:** A geometric representation of the pure state space of a two-level quantum mechanical system.
8. **Hilbert Space:** An abstract vector space used to describe quantum states.
9. **Bell States:** Four specific maximally entangled quantum states of two qubits.
10. **Quantum Tunneling:** A phenomenon where a particle passes through a potential barrier that it classically could not surmount.
11. **Wavefunction (Ψ):** A mathematical description of the quantum state of an isolated quantum system.
12. **Schrödinger Equation:** The fundamental equation of motion for quantum systems.
13. **Measurement Postulate:** The process that collapses a wavefunction into a definite classical state.
14. **Density Matrix:** A tool used to describe the statistical state of a quantum system in mixed states.
15. **Pauli Matrices (X, Y, Z):** A set of three 2x2 complex matrices used to describe spin and qubit rotations.
16. **Fidelity:** A measure of the "closeness" of two quantum states.
17. **Teleportation:** The transfer of quantum information using entanglement and classical communication.
18. **Phase Kickback:** A technique used in quantum algorithms to transfer information from a target qubit to a control qubit.
19. **Unitary Operator:** A linear operator that preserves the inner product, representing reversible quantum evolution.
20. **Interferometry:** A family of techniques using the interference of waves to extract information.

## 🔐 Section 2: Post-Quantum Cryptography (PQC) & Lattice Math
21. **Lattice-Based Cryptography:** Cryptography based on the hardness of problems in geometric lattices.
22. **Learning With Errors (LWE):** A foundational mathematical problem used to build PQC schemes.
23. **Shortest Vector Problem (SVP):** The core computational challenge in lattice-based crypto.
24. **Closest Vector Problem (CVP):** Finding a point in a lattice closest to a given non-lattice point.
25. **ML-KEM (FIPS 203):** Module-Lattice Key Encapsulation Mechanism (formerly Kyber).
26. **ML-DSA (FIPS 204):** Module-Lattice Digital Signature Algorithm (formerly Dilithium).
27. **SLH-DSA (FIPS 205):** Stateless Hash-based Digital Signature Algorithm (formerly SPHINCS+).
28. **NIST PQC Standardization:** The global effort to select quantum-resistant algorithms.
29. **Code-Based Cryptography:** Schemes based on error-correcting codes (e.g., McEliece).
30. **Multivariate Public Key Cryptography (MPKC):** Security based on solving systems of multivariate quadratic equations.
31. **Isogeny-Based Cryptography:** Using mappings between elliptic curves for key exchange.
32. **Hamming Quasi-Cyclic (HQC):** A code-based KEM submitted to NIST.
33. **Ring-LWE (RLWE):** An algebraic variant of LWE for improved efficiency.
34. **Module-LWE:** A trade-off between standard LWE and RLWE used in Kyber/Dilithium.
35. **NTT (Number Theoretic Transform):** An algorithm used for fast polynomial multiplication in PQC.
36. **Rejection Sampling:** A technique used in PQC signatures to ensure security without leaking secret information.
37. **IND-CCA2:** Indistinguishability under adaptive chosen-ciphertext attack (High-level security).
38. **Fujisaki-Okamoto (FO) Transform:** A method to convert a weak KEM into a CCA-secure one.
39. **Shor’s Algorithm:** An algorithm for integer factorization that breaks RSA/ECC.
40. **Grover’s Algorithm:** An algorithm for searching unstructured databases (affects symmetric key strength).

## 📡 Section 3: Quantum Communication & QKD Protocols
41. **QKD (Quantum Key Distribution):** Securely distributing cryptographic keys using quantum mechanics.
42. **BB84 Protocol:** The first QKD protocol using four polarized states.
43. **E91 Protocol:** QKD based on entangled particle pairs.
44. **QBER (Quantum Bit Error Rate):** The primary metric for detecting eavesdropping in QKD.
45. **Sifting Phase:** Discarding bits where the sender and receiver used different bases.
46. **Privacy Amplification:** Shortening a key to reduce an eavesdropper's potential knowledge.
47. **Information Reconciliation:** Error correction phase to ensure Alice and Bob have identical keys.
48. **B92 Protocol:** A QKD protocol using only two non-orthogonal states.
49. **COW Protocol (Coherent One-Way):** A protocol designed for practical fiber implementations.
50. **QTA (Quantum Temporal Authentication):** Using photon arrival time to prevent MITM attacks.
51. **QSDC (Quantum Secure Direct Communication):** Sending secret messages directly without a key.
52. **Quantum Repeater:** A device to extend the range of quantum communication beyond fiber limits.
53. **Dark Counts:** False detection signals in single-photon detectors.
54. **Polarization Basis (Rectilinear/Diagonal):** Different orientations used to encode qubits in photons.
55. **SNSPD:** Superconducting Nanowire Single-Photon Detector (High efficiency).
56. **Free-Space QKD:** Transmitting quantum states through the atmosphere or space.
57. **Phase-Encoding:** Encoding information in the phase of a photon rather than polarization.
58. **Trojan Horse Attack:** An active attack where light is sent into a QKD system to read internal states.
59. **Detector Blinding Attack:** An attack that forces detectors into classical mode to hide eavesdropping.
60. **Continuous-Variable QKD (CV-QKD):** QKD using wave properties rather than single particles.

## 🎲 Section 4: Quantum Randomness & Entropy (QRNG)
61. **QRNG (Quantum Random Number Generator):** Using quantum noise to produce true randomness.
62. **Entropy Source:** The physical process (vacuum noise, beam splitting) providing randomness.
63. **Min-Entropy:** A conservative measure of the amount of randomness in a probability distribution.
64. **NIST SP 800-90B:** A standard for evaluating entropy sources.
65. **ISO/IEC 23837:** International standard for QRNG security requirements.
66. **Beam Splitter:** An optical device used in QRNG to create a 50/50 probability path.
67. **Vacuum Fluctuations:** Using the inherent noise of a vacuum as a quantum entropy source.
68. **Metastability:** A classical state used for randomness, often compared to quantum methods.
69. **Health Testing:** Real-time monitoring of entropy sources to detect hardware failure.
70. **Extraction (Randomness Extractor):** A mathematical function that converts raw entropy into uniform bits.

## 🏛️ Section 5: Strategy, Risk & Enterprise Migration
71. **HNDL (Harvest Now, Decrypt Later):** The threat of storing encrypted data today to decrypt it with future QC.
72. **CBOM (Cryptographic Bill of Materials):** An inventory of all cryptographic assets in an organization.
73. **Mosca’s Theorem ($X+Y > Z$):** A formula to calculate the urgency of quantum migration.
74. **Crypto-Agility:** The ability of a system to quickly switch cryptographic algorithms.
75. **Quantum Risk Assessment (QRA):** The process of identifying quantum-vulnerable systems.
76. **Hybrid Cryptography:** Combining classical (RSA/ECC) with PQC to ensure multi-layered defense.
77. **Migration Path:** The strategic roadmap for upgrading an enterprise to quantum-safe standards.
78. **CSAF (Cybersecurity Advisory):** Guidance issued by agencies (like CISA/NSA) regarding quantum threats.
79. **Hardware Security Module (HSM):** Physical devices that must be upgraded to support PQC.
80. **Certificate Authority (CA) Transition:** The process of issuing quantum-safe digital certificates.

---
*This glossary is part of the EgQCC Quantum Security Track documentation.*