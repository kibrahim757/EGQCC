# 🔐 Triangle of Quantum Security

## Overview
This project demonstrates the **Triangle of Quantum Security**, a holistic approach to next-generation cryptography that integrates three critical technologies:

1.  **QRNG (Quantum Random Number Generator)**: Generates truly random keys using quantum mechanics (superposition and measurement).
2.  **PQC (Post-Quantum Cryptography)**: Protects data against future quantum computer attacks using mathematical complexity (Lattice-based cryptography).
3.  **QC (Quantum Communication / QKD)**: Ensures secure key distribution through the laws of physics (BB84 protocol).

## 📂 Repository Contents
*   `triangle_of_quantum_security.ipynb`: The main interactive Jupyter Notebook containing code, simulations, and visualizations.
*   `images/`: Directory containing generated visualizations and diagrams.

## 🚀 Features
*   **True Randomness**: Implementation of a quantum circuit using Hadamard gates to generate unbiased random numbers.
*   **Quantum-Safe Encryption**: Simplified demonstration of Kyber-like Key Encapsulation Mechanism (KEM) based on the Learning With Errors (LWE) problem.
*   **Unbreakable Keys**: Simulation of the BB84 Quantum Key Distribution protocol with eavesdropper detection.
*   **Interactive Visualizations**:
    *   Quantum Circuit diagrams (Qiskit)
    *   Process flows and architecture diagrams (Mermaid)
    *   Statistical analysis plots (Matplotlib)

## 🛠️ Tech Stack & Requirements
*   **Python 3.8+**
*   **Qiskit**: For quantum circuit simulation.
*   **NumPy**: For numerical operations and polynomial arithmetic.
*   **Matplotlib**: For plotting randomness distribution and signal analysis.
*   **Mermaid**: For architectural flowcharts and sequence diagrams.

## 📖 How to Run
1.  Clone the repository.
2.  Install the required dependencies:
    ```bash
    pip install qiskit qiskit-aer numpy matplotlib jupyterlab
    ```
3.  Open the notebook:
    ```bash
    jupyter notebook triangle_of_quantum_security.ipynb
    ```
4.  Run all cells to see the simulations and visualizations in action.

## 📊 Visualizations
The notebook includes detailed visualizations for:
*   QRNG Circuit Design
*   Randomness Distribution Analysis
*   PQC Key Encapsulation/Decapsulation Flow
*   QKD BB84 Protocol Sequence
*   The Unified Triangle of Quantum Security Architecture

---
*Created as part of the EgQCC-QC Track.*
