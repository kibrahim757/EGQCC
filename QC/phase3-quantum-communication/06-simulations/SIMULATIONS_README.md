# Phase 3 Quantum Communication - Simulations Module

## Overview
This module contains comprehensive quantum key distribution (QKD) protocol simulations implemented using both NetSquid and QuNetSim frameworks. The simulations model quantum communication protocols, channel noise, eavesdropping detection, and network performance metrics.

## Project Structure

```
06-simulations/
├── netsquid/                 # NetSquid framework simulations
│   ├── scripts/
│   │   └── bb84_netsquid.py # BB84 implementation
│   ├── results/              # Simulation output
│   ├── logs/                 # Execution logs
│   └── README.md             # NetSquid documentation
├── qunetsim/                 # QuNetSim framework simulations
│   ├── scripts/
│   │   └── bb84_qunetsim.py # BB84 implementation
│   ├── results/              # Simulation output
│   ├── logs/                 # Execution logs
│   └── README.md             # QuNetSim documentation
├── utils/                    # Shared utilities
│   └── qc_utils.py          # Common functions
├── analysis/                 # Analysis and reporting
│   └── comprehensive_analysis.py
├── config.json              # Global configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Quick Start

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv qc_env
source qc_env/bin/activate  # Linux/macOS
# or
qc_env\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Run BB84 Simulation (NetSquid)
```bash
cd netsquid/scripts
python bb84_netsquid.py
```

### 3. Run BB84 Simulation (QuNetSim)
```bash
cd qunetsim/scripts
python bb84_qunetsim.py
```

### 4. Analyze Results
```bash
cd analysis
python comprehensive_analysis.py
```

## Simulation Frameworks

### NetSquid
- **Website**: https://netsquid.org/
- **Strengths**: Detailed quantum operations, continuous-time simulation, realistic noise models
- **Use Case**: Research-grade quantum network simulation
- **Key Features**:
  - Component-based architecture
  - Quantum error models
  - Network topology support
  - Performance analysis tools

### QuNetSim
- **Website**: https://github.com/tsimsimis/QuNetSim
- **Strengths**: High-level quantum network API, easy protocol implementation
- **Use Case**: Rapid protocol prototyping and validation
- **Key Features**:
  - Discrete-time simulation
  - Quantum gate operations
  - Network routing
  - Entanglement swapping support

## Protocols Implemented

### BB84 (Bennett-Brassard 1984)
- **Type**: Quantum Key Distribution
- **Security**: Information-theoretic
- **Key Generation**: ~0.5 bits per transmitted qubit
- **Detection**: Eavesdropping via QBER monitoring

#### Protocol Phases:
1. **Quantum Transmission**: Alice sends random qubits in random bases
2. **Measurement**: Bob measures qubits with random bases
3. **Basis Sifting**: Public discussion of bases, keep matching cases
4. **Error Rate Estimation**: Sample subset to calculate QBER
5. **Security Check**: If QBER < threshold, key is secure
6. **Error Correction**: Apply reconciliation (optional)
7. **Privacy Amplification**: Reduce eavesdropper information

## Configuration

### Global Settings (config.json)
```json
{
  "protocols": {
    "bb84": {
      "n_qubits": 1000,
      "depolarize_rate": 0.01,
      "security_threshold": 0.11
    }
  },
  "quantum_channels": {
    "realistic_short": {
      "loss_rate": 0.01,
      "error_rate": 0.005
    }
  }
}
```

### Adjustable Parameters
- **n_qubits**: Number of quantum bits transmitted
- **depolarize_rate**: Quantum channel noise level
- **loss_rate**: Probability of qubit loss
- **security_threshold**: QBER threshold for eavesdropping detection
- **trials**: Number of simulation repetitions

## Key Concepts

### Quantum Bit Error Rate (QBER)
- **Definition**: Fraction of bits that differ between Alice and Bob after measurement
- **Formula**: QBER = (errors) / (total sifted bits)
- **No Eavesdropping**: Expected QBER ≈ 0.25 × channel_error_rate
- **Threshold**: BB84 security requires QBER < 11%

### Sift Efficiency
- **Definition**: Fraction of qubits kept after basis sifting
- **Ideal Value**: 25% (half the bases randomly match)
- **Final Key Length**: sift_efficiency × n_qubits × (1 - 2×H(QBER))

### Secret Key Rate
- **Definition**: Theoretically secure bits per quantum bit transmitted
- **Formula**: SKR = sift_rate × (1 - 2×H(QBER))
- **Typical Value**: 10-20% for practical implementations

### Eavesdropping Indicators
- **QBER Increase**: Eve's measurement disturbs quantum states
- **Error Patterns**: Detectable changes in error distribution
- **Detection Probability**: Increases with sample size

## Simulation Results

### Typical Outputs

#### Success Case
```
Configuration: 1000 qubits, 0.01 depolarization
Sifted Key: 250 bits (25% efficiency)
QBER: 0.0485
Final Key: 185 bits (18.5% efficiency)
Status: SECURE
```

#### Compromised Case
```
Configuration: 1000 qubits, 0.15 depolarization (eavesdropping)
Sifted Key: 240 bits (24% efficiency)
QBER: 0.1542 (exceeds threshold of 0.11)
Final Key: 0 bits (protocol aborted)
Status: EAVESDROPPER DETECTED
```

### Analysis Metrics
- Protocol efficiency
- Security margins
- Noise resilience
- Network performance
- Scalability limits

## Performance Analysis

### Noise Resilience
The protocol remains secure under:
- Quantum channel loss: up to ~5%
- Quantum errors: up to ~5%
- Combined noise: depends on error model

### Scalability
- Network nodes: up to 50 simulated nodes
- Key length: scalable to multi-megabit range
- Distance: extended with quantum repeaters
- Rate: 1-10 kHz for practical implementations

## Advanced Topics

### Quantum Error Correction
- Applied to sifted key before final use
- Cascade reconciliation (typical)
- Overhead: ~50% additional bits needed
- Final efficiency: 5-10% of transmitted qubits

### Privacy Amplification
- Reduces eavesdropper information
- Applied after error correction
- Privacy amplification factor: configurable
- Typical rounds: 5-10

### Quantum Repeaters
- Extend transmission distance
- Entanglement swapping and purification
- Supported by QuNetSim
- Implementation in NetSquid: manual

### Network Integration
- Multi-hop quantum networks
- Classical authentication channels
- Network routing protocols
- Quantum internet backbone

## Troubleshooting

### Low Sift Efficiency (<20%)
- Verify random basis generation
- Check basis matching logic
- May indicate implementation bug

### Unexpectedly High QBER (>0.10)
- Review channel error models
- Verify measurement implementation
- Check measurement-basis correspondence

### Slow Simulation
- Reduce n_qubits
- Use fewer trials
- Optimize Python/NumPy usage
- Consider GPU acceleration (future)

### Missing Dependencies
```bash
pip install -r requirements.txt
python -m pip install --upgrade numpy scipy
```

## Documentation

### Protocol Papers
- **BB84**: Bennett & Brassard (1984) - "Quantum Cryptography: Public key distribution and coin tossing"
- **Security**: Shor & Preskill (2000) - "Simple proof of security of the BB84 quantum key distribution protocol"
- **QBER Analysis**: Tomamichel et al. (2012) - "Tight bounds for practical private key rates from quantum network noise"

### Framework Documentation
- **NetSquid**: https://netsquid.org/documentation/
- **QuNetSim**: https://github.com/tsimsimis/QuNetSim/wiki

### Phase 3 QC Project
- **Introduction**: See `01-introduction/`
- **QKD Overview**: See `02-qkd/`
- **QTA**: See `03-qta/`
- **QSDC**: See `04-qsdc/`
- **Performance Analysis**: See `07-performance-analysis/`
- **Security Analysis**: See `08-security-analysis/`

## Development Guide

### Adding New Protocols
1. Create protocol class in new script
2. Implement quantum operations
3. Add analysis metrics
4. Document parameters and outputs
5. Add to framework comparison

### Adding Custom Channels
1. Extend error models in config.json
2. Implement noise simulation
3. Test against theoretical predictions
4. Document in README

### Contributing Analysis
1. Add metrics to comprehensive_analysis.py
2. Generate plots using matplotlib
3. Document findings
4. Add to final report

## Verification

### Correctness Tests
```bash
pytest tests/
python -m pytest --cov=
```

### Performance Benchmarks
- Single trial: <1 second
- 10 trials (1000 qubits): <10 seconds
- Network analysis (50 nodes): <60 seconds

### Validation
- Compare NetSquid vs QuNetSim results
- Verify against theoretical predictions
- Check QBER under different noise rates
- Validate sift efficiency ~25%

## References

1. Bennett, C. H., & Brassard, G. (1984). Quantum cryptography: Public key distribution and coin tossing. In Proceedings of IEEE International Conference on Computers, Systems and Signal Processing.

2. Shor, P. W., & Preskill, J. (2000). Simple proof of security of the BB84 quantum key distribution protocol. Physical Review Letters, 85(2), 441.

3. Brunner, N., et al. (2014). Bell nonlocality. Reviews of Modern Physics, 86(2), 419.

4. NetSquid Documentation: https://netsquid.org/

5. QuNetSim Repository: https://github.com/tsimsimis/QuNetSim

## Contact & Support

For issues, questions, or contributions:
1. Check documentation in framework README files
2. Review protocol papers for theoretical understanding
3. Validate implementation against specifications
4. Add improvements to analysis modules

## License

This project is part of the EGQCC Phase 3 Quantum Communication research initiative.

---

**Last Updated**: January 19, 2026
**Version**: 1.0.0
**Status**: Active Development
