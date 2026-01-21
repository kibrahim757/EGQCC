# Phase 3 Quantum Communication - Simulations Module

## Overview

This module contains comprehensive simulations of the BB84 Quantum Key Distribution (QKD) protocol implemented in two different quantum network simulators: **NetSquid** and **QuNetSim**. The simulations evaluate protocol security, performance, and feasibility under various noise and loss conditions.

## Project Structure

```
06-simulations/
├── README.md                    # This file
├── config.py                    # Centralized configuration management
├── analysis.py                  # Analysis and metrics computation
│
├── netsquid/
│   ├── README.md               # NetSquid-specific documentation
│   └── bb84_simulation.py       # NetSquid BB84 implementation
│
└── qunetsim/
    ├── README.md               # QuNetSim-specific documentation
    └── bb84_simulation.py       # QuNetSim BB84 implementation
```

## Quick Start

### 1. Environment Setup

```bash
# Create virtual environment
python -m venv quantum_sim_env

# Activate (Windows)
quantum_sim_env\Scripts\activate

# Activate (Linux/macOS)
source quantum_sim_env/bin/activate

# Install dependencies
pip install numpy scipy matplotlib
```

### 2. Run NetSquid Simulation

```bash
cd netsquid
pip install netsquid
python bb84_simulation.py
```

### 3. Run QuNetSim Simulation

```bash
cd ../qunetsim
pip install qunetsim
python bb84_simulation.py
```

## BB84 Protocol Overview

The BB84 Quantum Key Distribution protocol enables secure key establishment using quantum mechanics:

### Protocol Steps

**Step 1: State Preparation** - Alice randomly generates bits and chooses random measurement bases

**Step 2: Basis Selection** - Bob randomly selects measurement bases for each incoming quantum state

**Step 3: Quantum Transmission** - Alice sends quantum-encoded bits to Bob through quantum channel

**Step 4: Measurement** - Bob measures received states in his chosen bases

**Step 5: Basis Reconciliation** - Alice and Bob publicly compare bases; retain only matching-basis results (sifting)

**Step 6: Eavesdropping Detection** - Estimate QBER; abort if exceeds threshold

**Step 7: Privacy Amplification** - Apply error correction and amplification to generate secure key

### Security Properties

- **Information-Theoretic Security**: No computational assumptions required
- **Eavesdropping Detection**: Any measurement attempt introduces detectable errors
- **QBER Threshold**: Typical threshold is 11% for secure operation

## Core Modules

### 1. `bb84_simulation.py` (NetSquid)

**Features:**
- Discrete-event quantum network simulation
- Comprehensive noise modeling (depolarization, amplitude damping)
- Realistic quantum channel properties
- Multiple independent trials for statistical analysis

**Usage:**
```python
from netsquid.bb84_simulation import BB84Simulation

sim = BB84Simulation(num_qubits=10000, depolarization_rate=0.01, num_trials=10)
results = sim.run_all_trials()
summary = sim.get_summary()
```

### 2. `bb84_simulation.py` (QuNetSim)

**Features:**
- High-level protocol framework
- Educational-friendly implementation
- Simplified but physically accurate modeling
- Extensible for protocol modifications

**Usage:**
```python
from qunetsim.bb84_simulation import BB84Protocol, run_multiple_trials

protocol = BB84Protocol(key_length=10000, noise_rate=0.01)
result = protocol.execute()

stats = run_multiple_trials(num_trials=10, key_length=10000, noise_rate=0.01)
```

### 3. `config.py`

**Purpose:** Centralized configuration management

**Features:**
- Predefined scenarios (ideal, realistic, noisy, long-distance)
- Channel models with various noise characteristics
- Experimental setup specifications
- Easy parameter switching

**Usage:**
```python
from config import ConfigManager

manager = ConfigManager()
manager.set_scenario('realistic')
print(manager.to_dict())  # View all parameters
manager.save_to_json('simulation_config.json')
```

### 4. `analysis.py`

**Purpose:** Statistical analysis and performance metrics

**Features:**
- Comprehensive statistics computation
- Performance metric calculations (QBER, key rate, etc.)
- Scenario comparison tools
- Report generation

**Classes:**
- `SimulationAnalyzer`: Statistical analysis of results
- `PerformanceMetrics`: Key performance indicators
- `ComparativeAnalysis`: Compare across scenarios

**Usage:**
```python
from analysis import SimulationAnalyzer, PerformanceMetrics

analyzer = SimulationAnalyzer()
# Add trial results...
stats = analyzer.compute_statistics()
print(analyzer.performance_summary())

# Theoretical metrics
qber = PerformanceMetrics.theoretical_qber(depol_rate=0.01)
secure_rate = PerformanceMetrics.secure_key_rate(qber, sifted_rate=2500)
```

## Simulation Parameters

### Quantum Channel Parameters

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `depolarization_rate` | 0.0 - 1.0 | 0.01 | Probability of bit flip per qubit |
| `photon_loss_rate` | 0.0 - 1.0 | 0.0 | Probability of photon loss |
| `channel_length_km` | 0.0+ | 0.0 | Distance for attenuation calculation |

### Protocol Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `num_qubits` | 1000-100000 | Quantum bits per trial |
| `num_trials` | 1-50 | Independent repetitions |
| `qber_threshold` | 0.11 | Eavesdropping detection threshold |

### Measurement Metrics

| Metric | Unit | Description |
|--------|------|-------------|
| QBER | Ratio | Quantum bit error rate |
| Sift Efficiency | % | Bits retained after basis matching |
| Key Rate | bits/qubit | Final secure key per quantum bit |
| Key Length | bits | Total secure key generated |

## Predefined Scenarios

### Ideal Scenario
- **Noise Rate**: 0% (ideal conditions)
- **Loss Rate**: 0%
- **Use Case**: Theoretical baseline
- **Expected Key Rate**: 0.25 (maximum possible)

### Realistic Scenario
- **Noise Rate**: 1% (typical quantum channel)
- **Loss Rate**: 0-5%
- **Use Case**: Standard QKD implementation
- **Expected Key Rate**: 0.20-0.24

### Noisy Scenario
- **Noise Rate**: 5% (high-noise environment)
- **Loss Rate**: 10-15%
- **Use Case**: Long-distance or difficult conditions
- **Expected Key Rate**: 0.15-0.20

### Long-Distance Scenario
- **Noise Rate**: 2%
- **Loss Rate**: 30%+
- **Key Length**: 50,000 qubits
- **Use Case**: Extended QKD networks

## Output and Results

### Console Output Example

```
===== BB84 PROTOCOL STATISTICS =====
Trials completed: 10
Total qubits transmitted: 10000
Average sifted key length: 2487.3
Key rate: 0.2487
Average QBER: 0.009875
Maximum QBER: 0.012341
Depolarization rate: 0.01
=====================================
```

### Results Structure

```json
{
  "statistics": {
    "num_trials": 10,
    "qber": {
      "mean": 0.009875,
      "std": 0.002145,
      "min": 0.005234,
      "max": 0.012341
    },
    "sifted_key": {
      "mean": 2487,
      "std": 45,
      "min": 2412,
      "max": 2589
    },
    "key_rate": {
      "mean": 0.2487,
      "std": 0.0045
    }
  },
  "results": [
    { "trial": 1, "qber": 0.009875, "sifted_key_length": 2500, ... },
    ...
  ]
}
```

## Performance Analysis

### Key Generation Rate Formula

$$R_{key} = \text{sifted\_key\_length} \times [1 - 2H(QBER)]$$

where $H(x) = -x\log_2(x) - (1-x)\log_2(1-x)$ is binary entropy.

### Theoretical QBER

For depolarizing channel: $QBER_{theory} = \frac{\text{depol\_rate}}{2}$

### Channel Capacity

$$C = 1 - H(\text{noise\_rate})$$

## Comparison: NetSquid vs QuNetSim

| Aspect | NetSquid | QuNetSim |
|--------|----------|----------|
| **Simulation Type** | Discrete-event | High-level framework |
| **Complexity** | Higher (detailed) | Lower (simplified) |
| **Noise Models** | Comprehensive | Basic |
| **Performance** | Slower (more accurate) | Faster |
| **Learning Curve** | Steeper | Gentler |
| **Use Case** | Research | Prototyping & Education |

## Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Verify installations
pip list | grep -E "netsquid|qunetsim|numpy"

# Reinstall if needed
pip install --upgrade netsquid qunetsim numpy
```

**2. Low Key Generation Rate**
- Check if noise_rate is too high
- Increase num_qubits for better statistics
- Verify QBER is below threshold

**3. Memory Issues**
- Reduce num_qubits parameter
- Use streaming output instead of storing all results
- Run simulations in separate processes

**4. QBER Anomalies**
- Verify depolarization_rate matches channel conditions
- Check if eavesdropping detection is working
- Increase num_trials for statistical significance

## Advanced Usage

### Batch Simulations

```python
import numpy as np
from config import ConfigManager
from netsquid.bb84_simulation import BB84Simulation

noise_rates = np.linspace(0, 0.1, 11)
results = {}

for noise in noise_rates:
    sim = BB84Simulation(depolarization_rate=noise, num_trials=20)
    sim.run_all_trials()
    results[f"noise_{noise:.2f}"] = sim.get_summary()
```

### Scenario Comparison

```python
from config import ConfigManager, IDEAL_SCENARIO, REALISTIC_SCENARIO, NOISY_SCENARIO
from analysis import ComparativeAnalysis

analyzer = ComparativeAnalysis()

for scenario_name, scenario_config in [
    ('Ideal', IDEAL_SCENARIO),
    ('Realistic', REALISTIC_SCENARIO),
    ('Noisy', NOISY_SCENARIO)
]:
    # Run simulation...
    analyzer.add_scenario(scenario_name, results)

print(analyzer.generate_comparison_report())
```

## References

1. **Bennett & Brassard (1984)** - Original BB84 protocol: "Quantum cryptography: Public key distribution and coin tossing"
2. **GLLP (1995)** - Security proof: "Generalized privacy amplification"
3. **NetSquid Documentation** - https://netsquid.org
4. **QuNetSim Documentation** - https://github.com/tsileo/qunetsim

## Related Documents

- Phase 3 Overall Report: See `/` directory
- QKD Theory: `02-qkd/qkd-overview.tex`
- BB84 Theory: `02-qkd/bb84/bb84-theory.tex`
- BB84 Theory (LaTeX): `02-qkd/bb84/bb84-simulation.tex`
- Security Analysis: `08-security-analysis/security-analysis.tex`

## Contact and Support

For issues or questions:
1. Check simulation logs in console output
2. Review troubleshooting section above
3. Consult NetSquid/QuNetSim documentation
4. Refer to Phase 3 main report for context

## License

Part of EGQCC Phase 3 Quantum Communication Project

---

**Last Updated**: January 19, 2026
**Version**: 1.0
**Status**: Complete
