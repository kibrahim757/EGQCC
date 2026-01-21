"""
Quantum Communication Simulation Utilities - Phase 3
====================================================

UTILITY FUNCTIONS FOR BB84, QTA, AND QSDC PROTOCOLS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module provides common functions and utilities for quantum communication
simulations across all three Phase 3 protocols:

1. BB84 (Quantum Key Distribution):
   - Prepare and Measure mechanics: Basis selection, state preparation
   - QBER calculation: Real-time error rate monitoring
   - Sifting: Base-matching algorithm for key derivation
   - Privacy Amplification: Toeplitz matrix operations

2. QTA (Quantum Temporal Authentication):
   - Time-of-Arrival (ToA) measurement and precision handling (±100 ps)
   - Temporal verification: Challenge-response mechanics
   - Timestamp validation and synchronization

3. QSDC (Quantum Secure Direct Communication):
   - Message encoding in quantum states (no prior key)
   - Three-phase security checking implementation
   - Sifting and amplification for direct transmission

Utilities Include:
- Data serialization (JSON, CSV formats)
- File I/O and result persistence
- Statistical calculations
- Logging and monitoring
- Configuration management

Author Attribution
==================
Engineer Mohamed Helmy
GitHub: https://github.com/7elmie
LinkedIn: https://www.linkedin.com/in/7elmie/
For: Engineer Sameh Zaghloul & Engineer Ragda

Date: 2026
"""

import numpy as np
import json
import csv
from datetime import datetime
from pathlib import Path


class SimulationDataManager:
    """Manage simulation data and file I/O"""
    
    @staticmethod
    def save_results_json(results, filename):
        """Save results to JSON file"""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"Results saved to {filename}")
    
    @staticmethod
    def save_results_csv(results_list, filename):
        """Save results to CSV file"""
        if not results_list:
            return
        
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results_list[0].keys())
            writer.writeheader()
            writer.writerows(results_list)
        print(f"Results saved to {filename}")
    
    @staticmethod
    def load_results_json(filename):
        """Load results from JSON file"""
        with open(filename, 'r') as f:
            return json.load(f)


class QuantumMetrics:
    """Calculate quantum information metrics"""
    
    @staticmethod
    def calculate_von_neumann_entropy(density_matrix):
        """
        Calculate von Neumann entropy of density matrix
        S(ρ) = -Tr(ρ log₂(ρ))
        """
        eigenvalues = np.linalg.eigvalsh(density_matrix)
        eigenvalues = eigenvalues[eigenvalues > 1e-10]  # Remove numerical zeros
        entropy = -np.sum(eigenvalues * np.log2(eigenvalues + 1e-10))
        return entropy
    
    @staticmethod
    def calculate_fidelity(state1, state2):
        """
        Calculate fidelity between two quantum states
        F = |<ψ|φ>|²
        """
        inner_product = np.abs(np.vdot(state1, state2))
        return inner_product ** 2
    
    @staticmethod
    def calculate_mutual_information(joint_prob, marginal1, marginal2):
        """
        Calculate classical mutual information
        I(X;Y) = Σ p(x,y) log(p(x,y)/(p(x)p(y)))
        """
        mi = 0
        for i, p_joint in enumerate(joint_prob):
            if p_joint > 0:
                for j in range(len(marginal1)):
                    if i % len(marginal1) == j and marginal1[j] > 0 and marginal2[i // len(marginal1)] > 0:
                        ratio = p_joint / (marginal1[j] * marginal2[i // len(marginal1)])
                        mi += p_joint * np.log2(ratio)
        return mi


class SecurityAnalyzer:
    """Analyze security of QKD protocols"""
    
    @staticmethod
    def estimate_eavesdropper_rate(qber, depolarization_model=True):
        """
        Estimate eavesdropper information from QBER
        
        For BB84 with depolarizing channel:
        I_Eve ≈ 1 - H(QBER)
        where H is binary entropy
        """
        h_qber = -qber * np.log2(qber + 1e-10) - (1 - qber) * np.log2(1 - qber + 1e-10)
        i_eve = 1 - h_qber
        return max(0, i_eve)
    
    @staticmethod
    def calculate_secret_key_rate(sift_rate, qber, n_steps=10):
        """
        Calculate final secret key rate after error correction and privacy amplification
        
        R_secret = sift_rate * (1 - 2H(QBER))
        """
        h_qber = -qber * np.log2(qber + 1e-10) - (1 - qber) * np.log2(1 - qber + 1e-10)
        secret_fraction = 1 - 2 * h_qber
        return max(0, sift_rate * secret_fraction)
    
    @staticmethod
    def check_security_threshold(qber, threshold=0.11):
        """
        Check if QBER is below security threshold
        Typical threshold for BB84: 11% (0.11)
        """
        return qber < threshold


class ProtocolValidator:
    """Validate QKD protocol implementations"""
    
    @staticmethod
    def validate_bb84_simulation(results):
        """Validate BB84 simulation results"""
        errors = []
        warnings = []
        
        # Check for required fields
        required_fields = ['n_qubits_transmitted', 'sift_length', 'qber', 'is_secure']
        for field in required_fields:
            if field not in results:
                errors.append(f"Missing required field: {field}")
        
        # Check value ranges
        if 'sift_length' in results and 'n_qubits_transmitted' in results:
            sift_efficiency = results['sift_length'] / results['n_qubits_transmitted']
            if sift_efficiency < 0.2 or sift_efficiency > 0.3:
                warnings.append(f"Unexpected sift efficiency: {sift_efficiency:.2%} (expected ~25%)")
        
        if 'qber' in results:
            if results['qber'] < 0 or results['qber'] > 1:
                errors.append(f"QBER out of range: {results['qber']}")
        
        return {'valid': len(errors) == 0, 'errors': errors, 'warnings': warnings}


class NetworkSimulationUtils:
    """Utilities for quantum network simulations"""
    
    @staticmethod
    def calculate_network_overhead(n_nodes, protocol='BB84'):
        """
        Calculate communication overhead for network protocol
        
        Args:
            n_nodes (int): Number of nodes in network
            protocol (str): Protocol name
            
        Returns:
            dict: Overhead metrics
        """
        if protocol == 'BB84':
            # BB84 requires: basis announcement + sifting comparison
            # Overhead ≈ 2 * message transmissions
            basis_messages = n_nodes * (n_nodes - 1)
            sift_messages = n_nodes * (n_nodes - 1)
            total_overhead = basis_messages + sift_messages
            
            return {
                'protocol': protocol,
                'n_nodes': n_nodes,
                'basis_messages': basis_messages,
                'sift_messages': sift_messages,
                'total_classical_bits': total_overhead
            }
        
        return None
    
    @staticmethod
    def estimate_quantum_channel_capacity(loss_rate, error_rate, bandwidth_ghz=100):
        """
        Estimate quantum channel capacity considering losses
        
        Args:
            loss_rate (float): Probability of qubit loss (0.0-1.0)
            error_rate (float): Quantum error rate (0.0-1.0)
            bandwidth_ghz (float): Channel bandwidth in GHz
            
        Returns:
            dict: Capacity estimates
        """
        transmission_prob = (1 - loss_rate) * (1 - error_rate)
        effective_bandwidth = bandwidth_ghz * transmission_prob
        
        return {
            'transmission_probability': transmission_prob,
            'effective_bandwidth_ghz': effective_bandwidth,
            'loss_rate': loss_rate,
            'error_rate': error_rate
        }


if __name__ == "__main__":
    print("Quantum Communication Utilities Module")
    print("Import this module to use simulation utilities")
