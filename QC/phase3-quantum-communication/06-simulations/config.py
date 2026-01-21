"""
Configuration file for BB84 Protocol Simulations - Phase 3
===========================================================

BB84 PROTOCOL (Quantum Key Distribution)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module centralizes all simulation parameters for BB84 Prepare and Measure mechanics,
QBER monitoring with 11% threshold for eavesdropping detection, and privacy amplification.

Key Configuration Parameters:
- QBER Threshold: 11% for eavesdropping detection
- Bases: {'+': rectilinear, 'x': diagonal} for quantum state preparation
- Sifting: Matching bases for final key derivation
- Privacy Amplification: Toeplitz matrix extraction (4:1 compression ratio)
- Performance Target: 850 kbps @ 10km, 85 kbps @ 100km, 0.85 kbps @ 1000km

Security Specifications:
- Eavesdropping Detection: >99.99% confidence
- Privacy Amplification: 2^-256 security level
- QBER Calculation: Real-time monitoring of bit error rate
- Key Rate: Depends on channel length, noise, loss

Author Attribution
==================
Engineer Mohamed Helmy
GitHub: https://github.com/7elmie
LinkedIn: https://www.linkedin.com/in/7elmie/
For: Engineer Sameh Zaghloul & Engineer Ragda

Date: 2026
"""

import json
from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class SimulationConfig:
    """Configuration parameters for BB84 simulations."""
    
    # Quantum channel parameters
    num_qubits: int = 10000
    depolarization_rate: float = 0.01
    photon_loss_rate: float = 0.0
    
    # Protocol parameters
    num_trials: int = 10
    qber_threshold: float = 0.11
    sift_efficiency_target: float = 0.25
    
    # Performance analysis
    measure_timing: bool = True
    track_eavesdropping: bool = True
    
    # Output settings
    save_results: bool = True
    results_dir: str = "./results"
    enable_logging: bool = True
    log_level: str = "INFO"


@dataclass
class ChannelModel:
    """Quantum channel model specifications."""
    
    # Noise model
    noise_type: str = "depolarizing"  # depolarizing, amplitude_damping, phase_damping
    noise_rate: float = 0.01
    
    # Loss model
    has_loss: bool = False
    loss_rate: float = 0.0
    
    # Distance model (for future use)
    distance_km: float = 0.0
    attenuation_db_per_km: float = 0.0
    
    def describe(self) -> str:
        """Return description of channel model."""
        desc = f"{self.noise_type.upper()} Channel (rate={self.noise_rate})"
        if self.has_loss:
            desc += f", Loss={self.loss_rate}"
        return desc


@dataclass
class ExperimentalSetup:
    """Experimental setup and equipment parameters."""
    
    # Source specifications
    source_type: str = "ideal_source"  # ideal_source, attenuated_laser
    photons_per_pulse: float = 1.0
    
    # Detector specifications
    detector_efficiency: float = 1.0
    dark_count_rate: float = 0.0
    dead_time: float = 0.0  # microseconds
    
    # Timing
    pulse_rate_mhz: float = 1.0
    
    def describe(self) -> str:
        """Return description of setup."""
        return (
            f"{self.source_type} | "
            f"Det Eff: {self.detector_efficiency*100:.1f}% | "
            f"Pulse Rate: {self.pulse_rate_mhz} MHz"
        )


# Default configurations for different scenarios
IDEAL_SCENARIO = SimulationConfig(
    num_qubits=10000,
    depolarization_rate=0.0,
    photon_loss_rate=0.0,
    num_trials=10,
    qber_threshold=0.11
)

REALISTIC_SCENARIO = SimulationConfig(
    num_qubits=10000,
    depolarization_rate=0.01,
    photon_loss_rate=0.0,
    num_trials=10,
    qber_threshold=0.11
)

NOISY_SCENARIO = SimulationConfig(
    num_qubits=10000,
    depolarization_rate=0.05,
    photon_loss_rate=0.1,
    num_trials=20,
    qber_threshold=0.11
)

LONG_DISTANCE_SCENARIO = SimulationConfig(
    num_qubits=50000,
    depolarization_rate=0.02,
    photon_loss_rate=0.3,
    num_trials=20,
    qber_threshold=0.15
)

# Channel models
IDEAL_CHANNEL = ChannelModel(noise_type="ideal", noise_rate=0.0)
REALISTIC_CHANNEL = ChannelModel(
    noise_type="depolarizing",
    noise_rate=0.01,
    has_loss=True,
    loss_rate=0.05
)
NOISY_CHANNEL = ChannelModel(
    noise_type="depolarizing",
    noise_rate=0.05,
    has_loss=True,
    loss_rate=0.15
)

# Experimental setups
IDEAL_SETUP = ExperimentalSetup(
    source_type="ideal_source",
    photons_per_pulse=1.0,
    detector_efficiency=1.0,
    dark_count_rate=0.0
)

REALISTIC_SETUP = ExperimentalSetup(
    source_type="attenuated_laser",
    photons_per_pulse=0.1,
    detector_efficiency=0.85,
    dark_count_rate=100.0,  # counts/second
    pulse_rate_mhz=1.0
)


class ConfigManager:
    """Manages configuration for simulations."""
    
    def __init__(self, config: SimulationConfig = None):
        self.config = config or REALISTIC_SCENARIO
        self.channel = REALISTIC_CHANNEL
        self.setup = REALISTIC_SETUP
    
    def set_scenario(self, scenario_name: str):
        """
        Set configuration for predefined scenario.
        
        Parameters:
        -----------
        scenario_name : str
            One of: 'ideal', 'realistic', 'noisy', 'long_distance'
        """
        scenarios = {
            'ideal': IDEAL_SCENARIO,
            'realistic': REALISTIC_SCENARIO,
            'noisy': NOISY_SCENARIO,
            'long_distance': LONG_DISTANCE_SCENARIO
        }
        
        if scenario_name not in scenarios:
            raise ValueError(f"Unknown scenario: {scenario_name}")
        
        self.config = scenarios[scenario_name]
        
        # Also set corresponding channel
        if scenario_name == 'ideal':
            self.channel = IDEAL_CHANNEL
            self.setup = IDEAL_SETUP
        elif scenario_name == 'realistic':
            self.channel = REALISTIC_CHANNEL
            self.setup = REALISTIC_SETUP
        else:
            self.channel = NOISY_CHANNEL
            self.setup = REALISTIC_SETUP
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            'simulation': asdict(self.config),
            'channel': asdict(self.channel),
            'setup': asdict(self.setup)
        }
    
    def save_to_json(self, filepath: str):
        """Save configuration to JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    def __str__(self) -> str:
        """String representation."""
        return (
            f"SimConfig: qubits={self.config.num_qubits}, "
            f"trials={self.config.num_trials}, "
            f"noise={self.config.depolarization_rate}\n"
            f"Channel: {self.channel.describe()}\n"
            f"Setup: {self.setup.describe()}"
        )


if __name__ == "__main__":
    # Example usage
    manager = ConfigManager()
    
    print("Default configuration:")
    print(manager)
    print()
    
    # Switch to different scenario
    manager.set_scenario('noisy')
    print("Noisy scenario:")
    print(manager)
    print()
    
    # Save configuration
    manager.save_to_json('bb84_config.json')
    print("Configuration saved to bb84_config.json")
