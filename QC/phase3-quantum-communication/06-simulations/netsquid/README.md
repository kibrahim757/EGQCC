# NetSquid Simulations

## Objectives
- Simulate BB84 protocol with discrete-event simulation
- Model noisy quantum channels comprehensively
- Evaluate key generation rate under realistic conditions
- Analyze protocol performance across noise scenarios

## Tools
- NetSquid: Discrete-event quantum network simulator
- Python 3.8+
- NumPy, SciPy for numerical analysis
- Matplotlib for visualization

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)
- NetSquid installation (may require academic license)

### Steps
1. Create a virtual environment:
   ```bash
   python -m venv netsquid_env
   ```

2. Activate the virtual environment:
   - On Windows: `netsquid_env\Scripts\activate`
   - On Linux/macOS: `source netsquid_env/bin/activate`

3. Install NetSquid and dependencies:
   ```bash
   pip install netsquid numpy matplotlib scipy
   ```

4. Verify installation:
   ```bash
   python -c "import netsquid; print(netsquid.__version__)"
   ```

## Usage

### Running BB84 Protocol Simulation

1. Navigate to the netsquid directory
2. Execute the BB84 simulation script:
   ```bash
   python bb84_simulation.py
   ```

3. View results in console output or results directory

### Simulation Architecture

The simulation comprises these key components:

**Quantum Nodes:**
- Alice: State preparation and transmission
- Bob: State measurement and result recording
- Quantum Memory: Storage for quantum states

**Quantum Channel:**
- Configurable loss and noise models
- Depolarization, amplitude damping, phase damping options
- Distance-dependent attenuation

**Classical Channel:**
- Authenticated communication for basis comparison
- Sifting protocol implementation
- QBER estimation and eavesdropping detection

### Configuration Parameters

Edit `bb84_simulation.py` to customize:

```python
# Simulation setup
num_qubits = 10000          # Total quantum bits transmitted
depolarization_rate = 0.01  # 1% error per qubit
num_trials = 10             # Independent trial runs

# Channel parameters
loss_rate = 0.0             # Photon loss probability
channel_length_km = 0.0     # For attenuation calculation

# Protocol thresholds
qber_threshold = 0.11       # Eavesdropping detection threshold
```

### Output Files

Simulation generates:

- **Console Output**: Real-time trial progress and statistics
- **Results Directory**: 
  - `trial_results.csv`: Individual trial metrics
  - `statistics.json`: Aggregated statistics
  - `performance_plots.png`: Visualization of results

### Advanced Features

**Noise Models:**
```python
# Depolarizing noise
from netsquid.components.models import DepolarNoiseModel
noise = DepolarNoiseModel(depol_rate=0.01)

# Amplitude damping
from netsquid.components.models import AmplitudeDampingModel
noise = AmplitudeDampingModel(gamma=0.05)
```

**Quantum Memory:**
- Define qubit storage capacity
- Configure read/write fidelity
- Set decoherence parameters

**Message Scheduling:**
- Control quantum state transmission timing
- Model realistic communication delays
- Synchronize Alice and Bob operations

## Results

### Performance Metrics

The simulation computes:

- **Quantum Bit Error Rate (QBER)**
  - Measured on subset of sifted key
  - Compared against theoretical prediction
  - Used for eavesdropping detection

- **Key Generation Rate**
  - Final secure bits per transmitted qubit
  - Theoretical vs. practical comparison
  - Scalability analysis

- **Sift Efficiency**
  - Percentage of qubits retained after basis reconciliation
  - Expected: ~25% for random basis selection
  - Actual variation due to noise

- **Secure Key Length**
  - After privacy amplification
  - Bits truly secure from eavesdropper
  - Distance-dependent degradation

### Example Results Output

```
=== BB84 Protocol Statistics ===
Trials completed: 10
Total qubits transmitted: 10000
Average sifted key length: 2487.3
Key rate: 0.2487
Average QBER: 0.009875
Maximum QBER: 0.012341
Depolarization rate: 0.01
================================
```

## Configuration

### Predefined Scenarios

**Ideal Channel:**
```python
BB84Simulation(num_qubits=10000, depolarization_rate=0.0, num_trials=10)
```

**Realistic Channel:**
```python
BB84Simulation(num_qubits=10000, depolarization_rate=0.01, num_trials=10)
```

**Long-Distance (100 km):**
```python
BB84Simulation(num_qubits=50000, depolarization_rate=0.05, num_trials=20)
```

### Custom Configuration

Modify `config.py` for centralized parameter management:

```python
from config import ConfigManager, NOISY_SCENARIO

manager = ConfigManager(NOISY_SCENARIO)
manager.set_scenario('long_distance')
```

## Analysis and Visualization

### Using Analysis Tools

```python
from analysis import SimulationAnalyzer, PerformanceMetrics

analyzer = SimulationAnalyzer()
# Add trial results...
stats = analyzer.compute_statistics()
print(analyzer.performance_summary())
```

### Generating Plots

```python
# Compare scenarios
import matplotlib.pyplot as plt

plt.plot(noise_rates, key_rates, 'o-', label='Key Rate')
plt.xlabel('Depolarization Rate')
plt.ylabel('Key Rate (bits/qubit)')
plt.show()
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| NetSquid import error | Verify installation: `pip list \| grep netsquid` |
| Memory overflow | Reduce `num_qubits` parameter |
| Low key generation rate | Check noise_rate; may be too high |
| QBER exceeds threshold | Indicates excessive channel noise or eavesdropping |

## Performance Optimization

- **Parallel Trials**: Run independent trials in separate processes
- **Large-Scale Simulations**: Use batch processing with reduced key_length
- **Memory Optimization**: Stream results to file instead of storing in memory

## References

- NetSquid Framework: [Official Documentation]
- BB84 Protocol: Bennett & Brassard (1984)
- Quantum Channel Models: GLLP (1995)
- Phase 3 Report: See `references/phase3-references.bib`

## Related Simulations

- QuNetSim BB84 Implementation: `../qunetsim/bb84_simulation.py`
- Shared Configuration: `../config.py`
- Analysis Utilities: `../analysis.py`

## Notes

NetSquid provides:
- Discrete-event simulation for accurate timing
- Comprehensive quantum channel models
- Scalable network simulations
- Performance analysis tools

This implementation focuses on protocol-level simulation. For physical layer analysis, see the main Phase 3 report.

