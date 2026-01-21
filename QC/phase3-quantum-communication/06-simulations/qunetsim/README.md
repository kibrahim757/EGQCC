# QuNetSim Simulations

## Overview
QuNetSim (Quantum Network Simulator) provides an alternative simulation framework for quantum network protocols, including BB84 QKD, quantum repeaters, and quantum internet applications.

## Objectives
- Simulate quantum protocols with discrete time steps
- Validate BB84 protocol implementation
- Model quantum network routing and entanglement swapping
- Compare with NetSquid for cross-validation

## Framework Features
- Discrete-time quantum network simulation
- Built-in quantum gate operations
- Network topology configuration
- Integration with classical computing

## Tools
- QuNetSim Framework
- Python 3.8+

## Installation

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment

### Setup Steps
1. Create virtual environment:
   ```bash
   python -m venv qunetsim_env
   source qunetsim_env/bin/activate  # Linux/macOS
   ```

2. Install QuNetSim:
   ```bash
   pip install qunetsim
   ```

3. Verify installation:
   ```bash
   python -c "import qunetsim; print('QuNetSim installed')"
   ```

## Protocol Implementations

### BB84 Protocol
- Two-basis quantum key distribution
- Random basis selection for both Alice and Bob
- Basis reconciliation and sifting phase
- Eavesdropping detection through QBER analysis

## Directory Structure
```
qunetsim/
├── scripts/
│   ├── bb84_qunetsim.py        # BB84 protocol implementation
│   └── network_analysis.py      # Network performance analysis
├── results/
│   ├── simulation_output.json   # Raw simulation results
│   ├── analysis_report.txt      # Performance analysis
│   └── figures/                 # Generated visualizations
├── logs/
│   └── simulation_*.log         # Execution logs
├── config.json                  # QuNetSim configuration
└── README.md                    # This file
```

## Usage

### Running BB84 Simulation
```bash
cd scripts
python bb84_qunetsim.py --qubits 1000 --trials 10 --loss 0.01
```

### Parameters
- `--qubits`: Number of quantum bits to transmit (default: 1000)
- `--trials`: Number of simulation trials (default: 10)
- `--loss`: Quantum channel loss rate (default: 0.01)
- `--error`: Quantum error rate (default: 0.005)
- `--output`: Output file for results (default: results/output.json)

### Network Performance Analysis
```bash
python network_analysis.py --topology mesh --nodes 5
```

## Simulation Results

### Output Files
- `simulation_output.json`: Raw simulation results in JSON format
- `analysis_report.txt`: Formatted analysis report with metrics
- `protocol_log.txt`: Detailed protocol execution log

### Key Metrics
- **Sift Efficiency**: Fraction of qubits kept after basis sifting (~25%)
- **QBER**: Quantum Bit Error Rate (measure of channel quality)
- **Final Key Length**: Usable key bits after error correction
- **Eavesdropper Detection**: Whether eve was detected through QBER analysis

## Performance Benchmarks

### Typical Results (Ideal Channel)
```
Transmitted Qubits:    1000
Sifted Key Length:     250-260
Sift Efficiency:       25%
QBER:                  0.0-0.02
Final Key Length:      150-200 bits
Protocol Secure:       YES
```

### With Noise (1% Loss)
```
Transmitted Qubits:    1000
Sifted Key Length:     240-250
Sift Efficiency:       24-25%
QBER:                  0.03-0.05
Final Key Length:      130-180 bits
Protocol Secure:       YES
```

## Quantum Network Features

### Node Types
- **Alice**: Quantum key originator
- **Bob**: Quantum key receiver
- **Eve**: Eavesdropper (optional, for security testing)
- **Repeater**: Quantum repeater for long-distance links

### Channel Types
- **Quantum Channel**: Transmits quantum states
- **Classical Channel**: Announces bases and compares sifted keys
- **Authenticated Channel**: For secure public discussion

## Advanced Topics

### Eavesdropping Detection
The protocol includes eavesdropping detection based on QBER:
- **Threshold**: 11% for BB84
- **Detection Principle**: Eve's measurement increases errors
- **Error Patterns**: Detectable changes in bit agreement rates

### Network Routing
- Point-to-point: Direct Alice-Bob connection
- Linear: Sequential repeater chain
- Mesh: Multi-hop quantum network

### Error Correction Integration
- Cascade error correction (typical)
- Privacy amplification with parity check
- Reconciliation efficiency: 80-95%

## Troubleshooting

### Common Issues
1. **ImportError: No module named 'qunetsim'**
   - Solution: pip install qunetsim

2. **QBER suspiciously high (>0.15)**
   - Check channel loss rate
   - Verify quantum gate fidelities
   - Look for implementation bugs in measurement logic

3. **Sift efficiency too low (<0.20)**
   - Verify random basis selection
   - Check basis matching logic
   - Review basis comparison implementation

## Advanced Configuration

See `config.json` for detailed simulation parameters:
- Quantum error models
- Channel loss characteristics
- Protocol thresholds
- Eavesdropping detection settings

## References
- QuNetSim: https://github.com/tsimsimis/QuNetSim
- BB84 Protocol: Bennett & Brassard (1984)
- Quantum Network Simulation: Dahlberg et al. (2019)
- Sifting stage for key extraction
- QBER estimation and threshold checking

### Quantum Repeaters
- Entanglement distribution nodes
- Bell state measurement (BSM)
- Entanglement purification
- Extend communication distance beyond direct fiber links

## Simulation Parameters

Edit `config.json` to customize:
- Number of quantum states sent (typically 1000-100000)
- Quantum channel error rates
- Detector efficiency parameters
- Protocol-specific thresholds
- Network topology

## Running Simulations

```bash
# Basic BB84 simulation
python bb84_simulation.py --config config.json --output results/

# With custom parameters
python bb84_simulation.py --distance 100 --photons 50000 --qber_threshold 0.11
```

## Output Analysis

Simulation generates:
- Key rates (bits/second)
- QBER statistics
- Detection efficiency metrics
- Comparison with theoretical predictions

## Cross-Validation with NetSquid

Both QuNetSim and NetSquid implementations provide:
- Identical protocol specifications
- Same physical parameters
- Independent validation of results
- Benchmark comparison

## References
- QuNetSim Documentation: https://github.com/tsilifis/QuNetSim
- Simulation frameworks comparison in Phase 3 main report
- NumPy for numerical computations

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Steps
1. Create a virtual environment:
   ```bash
   python -m venv qunetsim_env
   ```

2. Activate the virtual environment:
   - On Windows: `qunetsim_env\Scripts\activate`
   - On Linux/macOS: `source qunetsim_env/bin/activate`

3. Install QuNetSim and dependencies:
   ```bash
   pip install qunetsim numpy scipy matplotlib
   ```

4. Verify installation:
   ```bash
   python -c "import qunetsim; print('QuNetSim ready')"
   ```

## Usage

### Running BB84 Protocol Simulation
1. Navigate to the qunetsim directory
2. Execute the BB84 simulation script:
   ```bash
   python bb84_simulation.py
   ```

### Protocol Execution Steps
The simulation follows these BB84 protocol steps:

**Step 1:** Alice prepares random bits and random bases (Rectilinear or Diagonal)
**Step 2:** Bob randomly selects measurement bases
**Step 3:** Bob measures received quantum states with his chosen bases
**Step 4:** Alice and Bob publicly compare bases (sifting phase)
**Step 5:** Eavesdropping check via QBER estimation using subset of sifted key

### Configurable Parameters
- **Key Length**: Number of quantum bits to transmit
- **Noise Rate**: Quantum channel depolarization rate (0.0 to 1.0)
- **QBER Threshold**: Detection threshold for eavesdropping
- **Number of Trials**: Repetitions for statistical analysis

### Output Files
- Console logs with protocol execution details
- QBER values and key generation statistics
- Trial-by-trial results logging
- Success rate and eavesdropping detection counts

## Results

### Key Performance Indicators
- **Success Rate**: Percentage of trials without eavesdropping detection
- **QBER (Quantum Bit Error Rate)**: Measure of channel quality
- **Sifted Key Length**: Number of bits retained after basis reconciliation
- **Final Key Length**: Secure key bits after privacy amplification
- **Key Generation Rate**: Final key bits per transmitted quantum bit

### Analysis Output
- Mean and standard deviation for all metrics
- Minimum and maximum observed values
- QBER threshold comparison
- Detection statistics for eavesdropping scenarios

## Configuration

Edit simulation parameters in `bb84_simulation.py`:

```python
# Simulation parameters
num_trials = 10
key_length = 10000
noise_rate = 0.01  # 1% depolarization
```

## Advanced Usage

### Scenario Testing
The framework supports testing multiple scenarios:

1. **Ideal Channel**: No noise or errors
   ```python
   protocol = BB84Protocol(key_length=10000, noise_rate=0.0)
   ```

2. **Realistic Channel**: With typical quantum channel noise
   ```python
   protocol = BB84Protocol(key_length=10000, noise_rate=0.01)
   ```

3. **Noisy Channel**: High loss and error rates
   ```python
   protocol = BB84Protocol(key_length=10000, noise_rate=0.05)
   ```

### Eavesdropping Simulation
The protocol automatically detects eavesdropping attempts through:
- QBER threshold violation detection
- Error rate analysis on test subsets
- Abort protocol on suspicious activity

## Troubleshooting

- **Import Errors**: Verify QuNetSim is correctly installed
- **Memory Issues**: Reduce `key_length` for large simulations
- **QBER Anomalies**: Check noise_rate parameter matches channel conditions
- **Low Key Rates**: Expected at high noise rates; verify threshold settings

## Performance Considerations

- **Simulation Time**: Scales linearly with num_trials * key_length
- **Memory Usage**: Proportional to key_length parameter
- **Accuracy**: Increases with num_trials (typically 10-20 sufficient)

## References

- BB84 Protocol: Bennett & Brassard (1984)
- QuNetSim Framework: [Official Documentation]
- Phase 3 Report: See `references/phase3-references.bib`

## Related Files

- NetSquid implementation: `../netsquid/bb84_simulation.py`
- Configuration: `../config.py`
- Analysis tools: `../analysis.py`
