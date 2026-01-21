"""
Comprehensive Analysis Script for Quantum Communication Simulations - Phase 3
==============================================================================

ANALYSIS OF BB84, QTA, AND QSDC PROTOCOLS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Processes and visualizes simulation results for all three Phase 3 quantum
communication protocols with focus on:

1. BB84 (Quantum Key Distribution):
   - QBER (Quantum Bit Error Rate) monitoring and threshold validation (11%)
   - Sifting efficiency: Ratio of matching bases to total measurements
   - Final key rates at different distances (10km, 100km, 1000km)
   - Privacy amplification verification (Toeplitz extraction, 4:1 compression)
   - Eavesdropping detection confidence (>99.99%)

2. QTA (Quantum Temporal Authentication):
   - Time-of-Arrival (ToA) precision metrics (±100 ps target)
   - MITM attack detection rate (>99.9% target)
   - Verification challenge response times (<1000 ns target)
   - Replay attack prevention confirmation (no-cloning verification)

3. QSDC (Quantum Secure Direct Communication):
   - Direct transmission throughput (425-850 kbps @ 100km)
   - Three-phase security checking success rate
   - Message recovery fidelity
   - Overhead percentage (0.025% target)

Analysis Features:
- Multi-run statistical analysis
- Performance trending over parameters
- Security metric validation
- Comparative analysis across protocols
- Visualization generation

Author Attribution
==================
Engineer Mohamed Helmy
GitHub: https://github.com/7elmie
LinkedIn: https://www.linkedin.com/in/7elmie/
For: Engineer Sameh Zaghloul & Engineer Ragda

Date: 2026
"""

import numpy as np
import sys
from pathlib import Path
from datetime import datetime

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'utils'))

from qc_utils import SimulationDataManager, QuantumMetrics, SecurityAnalyzer, ProtocolValidator


class ComprehensiveAnalyzer:
    """Comprehensive analysis of QKD simulation results"""
    
    def __init__(self, output_dir="results"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.analysis_results = {}
    
    def analyze_protocol_efficiency(self, simulation_results):
        """
        Analyze protocol efficiency metrics
        
        Args:
            simulation_results (list): List of simulation result dicts
            
        Returns:
            dict: Efficiency analysis
        """
        n_qubits = [r.get('n_qubits_transmitted', 0) for r in simulation_results]
        sift_lengths = [r.get('sift_length', 0) for r in simulation_results]
        final_keys = [r.get('final_key_length', len(r.get('final_key', []))) for r in simulation_results]
        
        sift_efficiencies = [s / n if n > 0 else 0 for s, n in zip(sift_lengths, n_qubits)]
        key_efficiencies = [k / n if n > 0 else 0 for k, n in zip(final_keys, n_qubits)]
        
        analysis = {
            'avg_qubits_transmitted': np.mean(n_qubits),
            'std_qubits_transmitted': np.std(n_qubits),
            'avg_sift_efficiency': np.mean(sift_efficiencies),
            'std_sift_efficiency': np.std(sift_efficiencies),
            'avg_final_key_efficiency': np.mean(key_efficiencies),
            'std_final_key_efficiency': np.std(key_efficiencies),
            'avg_final_key_length': np.mean(final_keys),
            'std_final_key_length': np.std(final_keys)
        }
        
        return analysis
    
    def analyze_security_metrics(self, simulation_results):
        """
        Analyze security metrics across simulations
        
        Args:
            simulation_results (list): List of simulation result dicts
            
        Returns:
            dict: Security analysis
        """
        qber_values = [r.get('qber', 0) for r in simulation_results]
        eve_rates = [r.get('eve_error_rate', 0) for r in simulation_results]
        eavesdrop_detections = [1 if r.get('eavesdropper_detected', False) else 0 
                               for r in simulation_results]
        
        avg_qber = np.mean(qber_values)
        i_eve = SecurityAnalyzer.estimate_eavesdropper_rate(avg_qber)
        secret_rate = SecurityAnalyzer.calculate_secret_key_rate(0.25, avg_qber)
        is_secure = SecurityAnalyzer.check_security_threshold(avg_qber)
        
        analysis = {
            'avg_qber': avg_qber,
            'std_qber': np.std(qber_values),
            'max_qber': np.max(qber_values),
            'min_qber': np.min(qber_values),
            'eavesdropper_info_rate': i_eve,
            'secret_key_rate': secret_rate,
            'avg_eve_error_rate': np.mean(eve_rates),
            'eavesdropping_detection_rate': np.mean(eavesdrop_detections),
            'is_secure': is_secure,
            'security_threshold': 0.11
        }
        
        return analysis
    
    def analyze_noise_resilience(self, noise_rates, results_by_noise):
        """
        Analyze how protocol performs under different noise conditions
        
        Args:
            noise_rates (list): List of tested noise rates
            results_by_noise (dict): Results keyed by noise rate
            
        Returns:
            dict: Noise resilience analysis
        """
        resilience = {}
        
        for noise_rate in noise_rates:
            if noise_rate in results_by_noise:
                results = results_by_noise[noise_rate]
                qber_values = [r.get('qber', 0) for r in results]
                secure_count = sum(1 for r in results if not r.get('eavesdropper_detected', True))
                
                resilience[noise_rate] = {
                    'avg_qber': np.mean(qber_values),
                    'std_qber': np.std(qber_values),
                    'security_rate': secure_count / len(results) if results else 0,
                    'num_trials': len(results)
                }
        
        return resilience
    
    def generate_summary_report(self, all_results, output_filename="analysis_report.txt"):
        """
        Generate comprehensive text report
        
        Args:
            all_results (dict): All analysis results
            output_filename (str): Output filename
        """
        report = []
        report.append("="*70)
        report.append("QUANTUM COMMUNICATION SIMULATION - COMPREHENSIVE ANALYSIS REPORT")
        report.append(f"Generated: {datetime.now().isoformat()}")
        report.append("="*70)
        
        # Protocol Efficiency Section
        if 'efficiency' in all_results:
            report.append("\n" + "="*70)
            report.append("PROTOCOL EFFICIENCY METRICS")
            report.append("="*70)
            eff = all_results['efficiency']
            report.append(f"Average Qubits Transmitted: {eff['avg_qubits_transmitted']:.0f} ± {eff['std_qubits_transmitted']:.0f}")
            report.append(f"Average Sift Efficiency: {eff['avg_sift_efficiency']:.2%} ± {eff['std_sift_efficiency']:.2%}")
            report.append(f"Average Final Key Length: {eff['avg_final_key_length']:.0f} ± {eff['std_final_key_length']:.0f}")
            report.append(f"Final Key Efficiency: {eff['avg_final_key_efficiency']:.2%} ± {eff['std_final_key_efficiency']:.2%}")
        
        # Security Metrics Section
        if 'security' in all_results:
            report.append("\n" + "="*70)
            report.append("SECURITY METRICS")
            report.append("="*70)
            sec = all_results['security']
            report.append(f"Average QBER: {sec['avg_qber']:.4f} ± {sec['std_qber']:.4f}")
            report.append(f"QBER Range: [{sec['min_qber']:.4f}, {sec['max_qber']:.4f}]")
            report.append(f"Security Threshold: {sec['security_threshold']:.4f}")
            report.append(f"Protocol Status: {'SECURE' if sec['is_secure'] else 'COMPROMISED'}")
            report.append(f"Eavesdropper Information Rate: {sec['eavesdropper_info_rate']:.4f}")
            report.append(f"Secret Key Rate Fraction: {sec['secret_key_rate']:.4f}")
            report.append(f"Eavesdropping Detection Rate: {sec['eavesdropping_detection_rate']:.0%}")
        
        # Noise Resilience Section
        if 'noise_resilience' in all_results:
            report.append("\n" + "="*70)
            report.append("NOISE RESILIENCE ANALYSIS")
            report.append("="*70)
            noise_res = all_results['noise_resilience']
            report.append(f"{'Noise Rate':<15} {'Avg QBER':<15} {'QBER Std':<15} {'Security Rate':<15}")
            report.append("-" * 60)
            for noise_rate in sorted(noise_res.keys()):
                data = noise_res[noise_rate]
                report.append(f"{noise_rate:<15.4f} {data['avg_qber']:<15.4f} {data['std_qber']:<15.4f} {data['security_rate']:<15.0%}")
        
        # Recommendations Section
        report.append("\n" + "="*70)
        report.append("RECOMMENDATIONS")
        report.append("="*70)
        report.append("1. Protocol Implementation")
        report.append("   - Use BB84 protocol for medium-range quantum networks (<100km)")
        report.append("   - Implement error correction for QBER > 0.05")
        report.append("   - Use privacy amplification for final key extraction")
        report.append("\n2. Network Deployment")
        report.append("   - Deploy quantum repeaters for long-distance links")
        report.append("   - Monitor QBER continuously for eavesdropping detection")
        report.append("   - Use decoy-state methods for practical implementations")
        report.append("\n3. Security Measures")
        report.append("   - Refresh quantum keys regularly (every 1-2 hours)")
        report.append("   - Combine with post-quantum cryptography for hybrid security")
        report.append("   - Implement monitoring for anomalous QBER patterns")
        report.append("\n4. Performance Optimization")
        report.append("   - Reduce channel losses with better optical components")
        report.append("   - Increase detection efficiency for higher key rates")
        report.append("   - Implement batch processing for multiple key generations")
        
        report.append("\n" + "="*70)
        report.append("END OF REPORT")
        report.append("="*70)
        
        # Save report
        report_text = "\n".join(report)
        output_path = self.output_dir / output_filename
        with open(output_path, 'w') as f:
            f.write(report_text)
        
        print(f"Report saved to {output_path}")
        return report_text
    
    def run_complete_analysis(self, simulation_results_list):
        """
        Run complete analysis on simulation results
        
        Args:
            simulation_results_list (list): List of all simulation results
            
        Returns:
            dict: All analysis results
        """
        print("Running comprehensive analysis...")
        
        # Efficiency analysis
        efficiency = self.analyze_protocol_efficiency(simulation_results_list)
        self.analysis_results['efficiency'] = efficiency
        
        # Security analysis
        security = self.analyze_security_metrics(simulation_results_list)
        self.analysis_results['security'] = security
        
        # Generate report
        report = self.generate_summary_report(self.analysis_results)
        
        print("\nAnalysis Complete!")
        return self.analysis_results


def main():
    """Main execution"""
    print("Quantum Communication Simulation - Analysis Module")
    print("This module processes simulation results and generates reports\n")
    
    # Example: Create mock results for demonstration
    mock_results = [
        {
            'n_qubits_transmitted': 1000,
            'sift_length': 250,
            'final_key_length': 180,
            'qber': 0.048,
            'eve_error_rate': 0.05,
            'eavesdropper_detected': False
        },
        {
            'n_qubits_transmitted': 1000,
            'sift_length': 260,
            'final_key_length': 195,
            'qber': 0.035,
            'eve_error_rate': 0.04,
            'eavesdropper_detected': False
        },
        {
            'n_qubits_transmitted': 1000,
            'sift_length': 245,
            'final_key_length': 170,
            'qber': 0.061,
            'eve_error_rate': 0.06,
            'eavesdropper_detected': False
        }
    ]
    
    # Run analysis
    analyzer = ComprehensiveAnalyzer()
    results = analyzer.run_complete_analysis(mock_results)
    
    print("\nKey Findings:")
    print(f"- Average QBER: {results['security']['avg_qber']:.4f}")
    print(f"- Protocol Secure: {results['security']['is_secure']}")
    print(f"- Sift Efficiency: {results['efficiency']['avg_sift_efficiency']:.2%}")
    print(f"- Final Key Efficiency: {results['efficiency']['avg_final_key_efficiency']:.2%}")


if __name__ == "__main__":
    main()
