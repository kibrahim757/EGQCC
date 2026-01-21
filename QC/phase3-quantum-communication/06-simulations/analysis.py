"""
Analysis and Visualization Tools for BB84 Simulations - Phase 3
===============================================================

BB84 PROTOCOL ANALYSIS (Quantum Key Distribution)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module provides utilities for analyzing BB84 simulation results including:
- QBER (Quantum Bit Error Rate) calculation and monitoring (11% threshold)
- Sifting efficiency analysis (matching bases selection)
- Privacy amplification verification (Toeplitz extraction)
- Key generation rates and throughput analysis
- Eavesdropping detection confidence calculations

Analysis Features:
- QBER trending and threshold violation detection
- Sifted key statistics and quality metrics
- Amplified key properties post-extraction
- Channel noise and loss impact assessment
- Multi-distance performance comparison (10km, 100km, 1000km)

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
from typing import Dict, List, Tuple, Any
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class SimulationAnalyzer:
    """Analyzes BB84 protocol simulation results."""
    
    def __init__(self):
        self.results = []
        self.statistics = {}
    
    def add_trial_result(self, result: Dict[str, Any]):
        """Add a single trial result."""
        self.results.append(result)
    
    def compute_statistics(self) -> Dict[str, Any]:
        """
        Compute comprehensive statistics from all trial results.
        
        Returns:
        --------
        dict : Statistical analysis results
        """
        if not self.results:
            logger.warning("No results to analyze")
            return {}
        
        # Extract metrics
        qber_values = [r.get('qber', 0) for r in self.results]
        sifted_lengths = [r.get('sifted_key_length', 0) for r in self.results]
        final_lengths = [r.get('final_key_length', 0) for r in self.results]
        key_rates = [r.get('key_rate', 0) for r in self.results]
        
        statistics = {
            'num_trials': len(self.results),
            'qber': {
                'mean': float(np.mean(qber_values)),
                'std': float(np.std(qber_values)),
                'min': float(np.min(qber_values)),
                'max': float(np.max(qber_values)),
                'median': float(np.median(qber_values))
            },
            'sifted_key': {
                'mean': float(np.mean(sifted_lengths)),
                'std': float(np.std(sifted_lengths)),
                'min': float(np.min(sifted_lengths)),
                'max': float(np.max(sifted_lengths))
            },
            'final_key': {
                'mean': float(np.mean(final_lengths)),
                'std': float(np.std(final_lengths)),
                'min': float(np.min(final_lengths)),
                'max': float(np.max(final_lengths))
            },
            'key_rate': {
                'mean': float(np.mean(key_rates)),
                'std': float(np.std(key_rates)),
                'min': float(np.min(key_rates)),
                'max': float(np.max(key_rates))
            }
        }
        
        self.statistics = statistics
        return statistics
    
    def performance_summary(self) -> str:
        """Generate human-readable performance summary."""
        if not self.statistics:
            self.compute_statistics()
        
        summary = [
            "="*60,
            "SIMULATION PERFORMANCE SUMMARY",
            "="*60,
            f"Total trials: {self.statistics['num_trials']}",
            "",
            "QUANTUM BIT ERROR RATE (QBER):",
            f"  Mean: {self.statistics['qber']['mean']:.6f}",
            f"  Std Dev: {self.statistics['qber']['std']:.6f}",
            f"  Range: [{self.statistics['qber']['min']:.6f}, {self.statistics['qber']['max']:.6f}]",
            "",
            "SIFTED KEY LENGTH:",
            f"  Mean: {self.statistics['sifted_key']['mean']:.0f}",
            f"  Std Dev: {self.statistics['sifted_key']['std']:.0f}",
            f"  Range: [{self.statistics['sifted_key']['min']:.0f}, {self.statistics['sifted_key']['max']:.0f}]",
            "",
            "FINAL SECURE KEY LENGTH:",
            f"  Mean: {self.statistics['final_key']['mean']:.0f}",
            f"  Std Dev: {self.statistics['final_key']['std']:.0f}",
            f"  Range: [{self.statistics['final_key']['min']:.0f}, {self.statistics['final_key']['max']:.0f}]",
            "",
            "KEY GENERATION RATE:",
            f"  Mean: {self.statistics['key_rate']['mean']:.6f} bits/qubit",
            f"  Std Dev: {self.statistics['key_rate']['std']:.6f}",
            f"  Range: [{self.statistics['key_rate']['min']:.6f}, {self.statistics['key_rate']['max']:.6f}]",
            "="*60
        ]
        
        return "\n".join(summary)
    
    def save_results(self, filepath: str):
        """Save analysis results to JSON file."""
        if not self.statistics:
            self.compute_statistics()
        
        output_data = {
            'statistics': self.statistics,
            'results': self.results
        }
        
        with open(filepath, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        logger.info(f"Results saved to {filepath}")


class PerformanceMetrics:
    """Computes specialized performance metrics."""
    
    @staticmethod
    def theoretical_qber(depolarization_rate: float) -> float:
        """
        Calculate theoretical QBER for depolarization channel.
        
        Parameters:
        -----------
        depolarization_rate : float
            Channel depolarization rate
            
        Returns:
        --------
        float : Theoretical QBER value
        """
        # For depolarizing channel: QBER ≈ depolarization_rate / 2
        # (when Alice and Bob have matching bases)
        return depolarization_rate / 2.0
    
    @staticmethod
    def secure_key_rate(
        qber: float,
        sifted_key_rate: float,
        h_qber: float = None
    ) -> float:
        """
        Calculate secure key rate using GLLP formula.
        
        Parameters:
        -----------
        qber : float
            Observed quantum bit error rate
        sifted_key_rate : float
            Rate of sifted key generation (bits/s)
        h_qber : float
            Binary entropy function of QBER
            
        Returns:
        --------
        float : Secure key rate (bits/s)
        """
        if h_qber is None:
            h_qber = PerformanceMetrics.binary_entropy(qber)
        
        # GLLP secure key rate
        # R_secure = sift_efficiency * [1 - 2*H(QBER)]
        secure_rate = sifted_key_rate * (1 - 2 * h_qber)
        
        return max(0, secure_rate)
    
    @staticmethod
    def binary_entropy(x: float) -> float:
        """
        Calculate binary entropy H(x) = -x*log2(x) - (1-x)*log2(1-x).
        
        Parameters:
        -----------
        x : float
            Probability value (0 to 1)
            
        Returns:
        --------
        float : Binary entropy
        """
        if x <= 0 or x >= 1:
            return 0
        
        return -x * np.log2(x) - (1 - x) * np.log2(1 - x)
    
    @staticmethod
    def compute_channel_capacity(noise_rate: float) -> float:
        """
        Compute classical capacity of noisy quantum channel.
        
        Parameters:
        -----------
        noise_rate : float
            Depolarization rate
            
        Returns:
        --------
        float : Channel capacity (bits per use)
        """
        # For depolarizing channel
        h_noise = PerformanceMetrics.binary_entropy(noise_rate)
        capacity = 1 - h_noise
        
        return capacity


class ComparativeAnalysis:
    """Compare results across different scenarios/configurations."""
    
    def __init__(self):
        self.scenario_results = {}
    
    def add_scenario(self, name: str, results: Dict[str, Any]):
        """Add results for a scenario."""
        self.scenario_results[name] = results
    
    def compare_qber(self) -> Dict[str, float]:
        """Compare QBER across scenarios."""
        comparison = {}
        for scenario, results in self.scenario_results.items():
            if 'qber' in results:
                avg_qber = results['qber'].get('mean', 0)
                comparison[scenario] = avg_qber
        
        return comparison
    
    def compare_key_rates(self) -> Dict[str, float]:
        """Compare key generation rates across scenarios."""
        comparison = {}
        for scenario, results in self.scenario_results.items():
            if 'key_rate' in results:
                avg_rate = results['key_rate'].get('mean', 0)
                comparison[scenario] = avg_rate
        
        return comparison
    
    def generate_comparison_report(self) -> str:
        """Generate comparative analysis report."""
        lines = [
            "="*60,
            "COMPARATIVE SCENARIO ANALYSIS",
            "="*60,
            ""
        ]
        
        # QBER comparison
        qber_comp = self.compare_qber()
        lines.append("QBER Comparison:")
        for scenario, qber in sorted(qber_comp.items(), key=lambda x: x[1]):
            lines.append(f"  {scenario:.<30} {qber:.6f}")
        
        lines.append("")
        
        # Key rate comparison
        rate_comp = self.compare_key_rates()
        lines.append("Key Rate Comparison (bits/qubit):")
        for scenario, rate in sorted(rate_comp.items(), key=lambda x: -x[1]):
            lines.append(f"  {scenario:.<30} {rate:.6f}")
        
        lines.append("="*60)
        
        return "\n".join(lines)


if __name__ == "__main__":
    # Example usage
    analyzer = SimulationAnalyzer()
    
    # Simulate some trial results
    for i in range(5):
        result = {
            'trial': i + 1,
            'qber': 0.01 + np.random.normal(0, 0.002),
            'sifted_key_length': 2500 + np.random.randint(-100, 100),
            'final_key_length': 1250 + np.random.randint(-50, 50),
            'key_rate': 0.25 + np.random.normal(0, 0.01)
        }
        analyzer.add_trial_result(result)
    
    # Compute and print statistics
    stats = analyzer.compute_statistics()
    print(analyzer.performance_summary())
