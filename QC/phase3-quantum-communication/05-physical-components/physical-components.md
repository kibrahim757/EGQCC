# Physical Layer Components

**Author**: Engineer Mohamed Helmy  
**GitHub**: https://github.com/7elmie  
**LinkedIn**: https://www.linkedin.com/in/7elmie/

---

## Single-Photon Sources

Single-photon sources are the foundation of quantum communication systems, generating individual photons with well-defined quantum properties. These sources must satisfy strict requirements for wavelength stability, timing precision, and quantum state purity.

### Spontaneous Parametric Down-Conversion (SPDC)

SPDC is the most widely used method for generating entangled photon pairs in laboratory settings:

- **Physical Principle**: A high-energy pump photon interacts with a nonlinear crystal, producing two lower-energy signal and idler photons.
- **Type I vs Type II Phase Matching**: Type I uses collinear phase matching, while Type II uses non-collinear geometry.
- **Advantages**: Produces genuine quantum states, high purity, proven scalability.
- **Disadvantages**: Multiple pair generation limits rates, requires high-power pump lasers.
- **Typical Performance**: 
  - Pair generation rate: 10^6 - 10^8 pairs/second
  - Visibility (for entangled states): > 95%
  - Multi-pair suppression: g^(2)(0) ≈ 0.5 - 0.7

### Quantum Dot Single-Photon Sources

Semiconductor quantum dots provide on-demand single-photon generation:

- **Operating Principle**: Electron-hole recombination in confined quantum states produces single photons.
- **Key Specifications**:
  - Emission wavelength: 500 nm - 1550 nm (tunable by dot size)
  - Single-photon purity: g^(2)(0) < 0.1 (near-ideal)
  - Repetition rate: GHz (up to 80 GHz demonstrated)
  - Collection efficiency: 40-60%
- **Advantages**: On-demand operation, high repetition rates, excellent purity.
- **Disadvantages**: Temperature sensitivity, spectral wandering, limited scalability.

### SPDC vs Quantum Dots

| Property | SPDC | Quantum Dot |
|----------|------|------------|
| Photon Generation | Probabilistic | On-demand |
| Single-Photon Quality | Good | Excellent |
| Repetition Rate | 100 kHz - 1 MHz | Up to 80 GHz |
| Entanglement Capability | Native | Requires engineering |
| Temperature Stability | Excellent | Requires cooling |
| Cost per system | $50k-200k | $100k-300k |

## Quantum Communication Channels

The communication channel is the critical link through which quantum states are transmitted. Channel characteristics directly determine protocol feasibility and achievable transmission distances.

### Optical Fiber Links

Fiber-based quantum communication offers metropolitan-range coverage:

#### Single-Mode Fiber (SMF) Characteristics

- **Standard Specifications (SMF-28)**:
  - Core diameter: 8-10 μm
  - Attenuation: 0.17-0.20 dB/km at 1550 nm (C-band)
- **Quantum Effects**:
  - Chromatic Dispersion: ~17 ps/(nm·km)
  - Polarization Mode Dispersion (PMD): < 0.05 ps/√km
  - Birefringence: Creates time-varying polarization rotation
- **Practical Range**: Up to 100 km without quantum repeaters
- **Advantages**: Established infrastructure, low-cost, mature technology
- **Disadvantages**: Requires polarization compensation, acoustic noise sensitivity

#### Wavelength Selection

| Band | Wavelength | Attenuation | Primary Use |
|------|-----------|-------------|------------|
| O-band | 1260-1360 nm | 0.15 dB/km | Long-distance |
| E-band | 1360-1460 nm | 0.35 dB/km | Water absorption peak |
| S-band | 1460-1530 nm | 0.25 dB/km | Long-distance repeaters |
| C-band | 1530-1565 nm | 0.17 dB/km | Standard telecom |
| L-band | 1565-1625 nm | 0.20 dB/km | Extended range |

### Free-Space Quantum Links

Free-space communication enables ground-to-satellite and atmospheric quantum communication:

#### Advantages and Limitations

**Advantages**:
- No fiber loss accumulation
- Line-of-sight enables global coverage
- No polarization drift
- Higher data rates possible

**Challenges**:
- Atmospheric absorption and scattering
- Turbulence-induced beam wandering
- Phase noise from index fluctuations
- Daylight background count rates
- Pointing and tracking requirements

#### Atmospheric Transmission

Typical values:
- Clear weather: 80-90%
- Cloudy conditions: 10-30%
- Night conditions: 1-5%
- Maximum practical range: 500 km ground-to-ground, 1200 km satellite

## Photon Detectors

Photon detectors convert individual photons into electrical signals, directly impacting quantum communication performance.

### Avalanche Photodiodes (APDs)

APDs are the industry standard for single-photon detection:

- **Detection Efficiency**: 50-80% quantum efficiency
- **Timing Characteristics**:
  - Time resolution: 100-300 ps (FWHM)
  - Dead time: 100-500 ns
  - After-pulsing probability: 1-5%
- **Dark Count Rate**: 100-1000 Hz at room temperature
- **Temperature Dependence**: ~2× increase per 10°C rise

#### Limitations

- Blind time prevents detecting photons within ~500 ns
- After-pulsing reduces effective detection fidelity
- Temperature sensitive, requires cooling
- Limited wavelength coverage

### Superconducting Nanowire Single-Photon Detectors (SNSPDs)

SNSPDs represent state-of-the-art performance:

- **Key Performance**:
  - Detection efficiency: 85-95%
  - Dark count rate: 10-100 Hz
  - Time resolution: 50-100 ps
  - Dead time: 10-50 ns
  - Maximum count rate: > 100 MHz
- **Wavelength Independence**: Nearly wavelength-independent (400-1700 nm)

#### System Requirements

- Operating at 4K requires liquid helium (~$4000 per quart)
- System Cost: $100k-300k per detection channel
- Multi-pixel arrays available for multiplexed detection

### Detector Comparison

| Metric | APD | SNSPD |
|--------|-----|-------|
| Quantum Efficiency | 50-80% | 85-95% |
| Dark Count Rate | 100-1000 Hz | 10-100 Hz |
| Time Resolution | 100-300 ps | 50-100 ps |
| Dead Time | 100-500 ns | 10-50 ns |
| Max Count Rate | 1-2 MHz | > 100 MHz |
| Operating Temperature | 273-323 K | 4 K |
| System Cost | $5k-15k | $100k-300k |
| Maturity | Mature | Emerging |

## Noise and Loss Mechanisms

Noise and loss are the primary factors limiting quantum communication distance and secure key rates.

### Decoherence Mechanisms

Decoherence is the loss of quantum coherence through environmental interactions:

1. **Photon Loss (Amplitude Damping)**: 
   - Absorption in fiber with exponential decay
   - Useful transmission limited to ~100 km at 1550 nm

2. **Polarization Decoherence (Phase Damping)**:
   - Random birefringence variations in fiber
   - Decoherence time: T_2 ~ 1-10 μs

3. **Phase Decoherence**:
   - Chromatic dispersion causes frequency components to travel at different speeds
   - Coherence length: L_c = λ²/Δλ ~ 1-100 cm

### Attenuation and Loss

**Fiber Attenuation**:
- Rayleigh Scattering: Dominant at short wavelengths
- Infrared Absorption: Dominant at long wavelengths
- Practical values at 1550 nm: 0.17-0.20 dB/km

**Loss Budget for 100 km fiber link**:
- Fiber loss (100 km @ 1550 nm): 18 dB
- Coupling loss: 0.5-1 dB
- Component loss: 0.5-2 dB
- Connectors: 0.5-1 dB
- **Total**: ~20-22 dB (~0.6-0.8% transmission)

### Noise Sources

#### Detector Noise

- **Dark Counts**: Random thermal excitations (100-1000 Hz for APDs, 10-100 Hz for SNSPDs)
- **Afterpulsing**: Charge carrier trapping causing delayed false clicks (1-5% probability)

#### Environmental Noise

- **Background Light**: 1000-10000 photons/s in daylight
- **Acoustic Vibration**: 10 Hz - 10 kHz frequency range
- **Thermal Fluctuations**: ~0.01 nm/°C wavelength drift

## System Performance Metrics

### Quantum Bit Error Rate (QBER)

QBER quantifies quantum channel quality and is critical for security assessment:

```
QBER = (E / n) × 100%

Where:
- E = number of errors in sifted key
- n = total number of sifted key bits
```

**QBER Physics:**
```
Total QBER = QBER_noise + QBER_eavesdropping + QBER_implementation

Components:
1. QBER_noise: Environmental + detector sources (1-3%)
   - Thermal noise in detector
   - Spontaneous emission
   - Phase diffusion

2. QBER_eavesdropping: Active attack (0-25%)
   - 0% if no eavesdropping
   - 25% if complete intercept-resend attack

3. QBER_implementation: System imperfections (0-5%)
   - Calibration errors
   - Timing jitter
   - Birefringence drift
```

**Real-World QBER Values:**
```
| System Type | Distance | QBER | Notes |
|------------|----------|------|-------|
| Lab - Direct coupling | <1 m | 0.1-0.5% | Ideal conditions |
| Lab - Short fiber | 1 km | 0.5-1.5% | Good stability |
| Metropolitan | 10 km | 1-3% | Polarization control needed |
| Metropolitan | 50 km | 2-4% | Thermal compensation |
| Metro/Long | 100 km | 3-5% | Active stabilization |
| Long distance | 200 km | 5-8% | Repeaters needed |
| Satellite (day) | 500+ km | 5-15% | Weather dependent |
| Satellite (night) | 500+ km | 1-3% | Better conditions |
```

### Secure Key Rate Analysis

Secure key rate is the speed at which secure information can be extracted:

**BB84 Key Rate Formula:**
```
R_key = η_sys · f · (1/4) · (1 - 2Q)

Where:
- η_sys = system efficiency (transmission × detection)
- f = frame rate (Hz)
- 1/4 = sifting factor (50% basis match, ~50% survive)
- (1 - 2Q) = privacy amplification factor
- Q = QBER

Example calculation @ 100 km:
- η_sys = 0.0008 (fiber: -20 dB, detectors: -0.5 dB)
- f = 1 MHz
- 1/4 = 0.25 sifting efficiency
- Q = 0.04 (4% QBER)
- (1 - 2×0.04) = 0.92 (92% efficiency after privacy amplification)

R_key = 0.0008 × 1e6 × 0.25 × 0.92 = 184 kbps
```

**Measured Key Rates Across Distances:**
```
| Distance | Typical QBER | Frame Rate | Sifted Rate | Final Key Rate |
|----------|-------------|-----------|------------|-----------------|
| 10 km    | 1%          | 1 MHz     | 250 kHz    | 850 kbps        |
| 25 km    | 1.5%        | 1 MHz     | 245 kHz    | 825 kbps        |
| 50 km    | 2.5%        | 500 kHz   | 120 kHz    | 400 kbps        |
| 75 km    | 3.2%        | 100 kHz   | 24 kHz     | 80 kbps         |
| 100 km   | 4%          | 50 kHz    | 11 kHz     | 35 kbps         |
| 150 km   | 5.5%        | 10 kHz    | 2 kHz      | 3.5 kbps        |
| 200 km   | 6.2%        | 5 kHz     | 0.9 kHz    | 1.8 kbps        |
| 500 km   | 8%          | 500 Hz    | 60 bps     | 12 bps          |
```

### System Design Considerations

**Component Selection Trade-offs:**

```python
class QuantumSystemDesign:
    """Design trade-offs for quantum communication systems"""
    
    design_scenarios = {
        "Metro (10-100 km)": {
            "source": "SPDC - probabilistic",
            "detector": "APD (60-80% efficiency)",
            "fiber": "SMF-28 (standard telecom)",
            "distance_limited_by": "Fiber attenuation",
            "typical_qber": "2-4%",
            "key_rate_at_100km": "35 kbps",
            "cost": "$50k-200k"
        },
        
        "Enterprise (100-500 km)": {
            "source": "Quantum dot (high rate)",
            "detector": "SNSPD preferred, APD ok",
            "fiber": "Low-loss fiber + dispersion compensation",
            "distance_limited_by": "Quantum repeaters needed",
            "typical_qber": "4-8%",
            "key_rate_at_100km": "50-200 kbps",
            "cost": "$500k-2M"
        },
        
        "Satellite (Global)": {
            "source": "High-power SPDC + frequency up-conversion",
            "detector": "Ground: APD/SNSPD, Satellite: Avalanche",
            "medium": "Free-space vacuum",
            "distance_limited_by": "Atmospheric conditions",
            "typical_qber": "5-15%",
            "key_rate_varies": "1 bps (cloudy) - 100 kbps (clear night)",
            "cost": "$10M-50M"
        }
    }

# Selection guide
def select_components(distance_km, budget_dollars):
    """Select appropriate components for given parameters"""
    
    if distance_km <= 10:
        return "Lab: APD detector, SPDC source, any fiber"
    elif distance_km <= 100:
        if budget_dollars < 100000:
            return "Metro: APD detector, SPDC source, SMF"
        else:
            return "Metro: SNSPD detector, Quantum dot, SMF"
    elif distance_km <= 500:
        if budget_dollars < 1000000:
            return "Need repeaters! APD detector + quantum repeater"
        else:
            return "Advanced: SNSPD, quantum dot, low-loss fiber"
    else:
        return "Satellite: Custom design required"
```

---

## Integration and System-Level Considerations

### Polarization Management

Fiber birefringence causes continuous polarization rotation:

**Problem:**
```
Alice sends: |H⟩ (horizontal polarization, Z basis)
Due to fiber birefringence:
After 1 km: rotated by ~10°
After 10 km: rotated by ~100° (unpredictable due to temperature)
After 100 km: Could be at any angle!

Bob receives: Unknown polarization state
Bob's measurement: 50% chance correct (if he guesses right basis)
Net result: QBER increases to 50%!
```

**Solutions:**
1. **Active Compensation:**
   - Measure polarization continuously
   - Apply real-time corrections with liquid-crystal retarders
   - Cost: $10k-50k per link
   - Maintenance: Continuous calibration needed

2. **Decoy State BB84:**
   - Use 3-4 different decoy state intensities
   - Eliminates photon-number-splitting attacks
   - Reduces sensitivity to polarization drift

3. **Polarization-Entangled QKD:**
   - Use entanglement in time-bin instead of polarization
   - Immune to polarization drift
   - Example: COW (Coherent One-Way) protocol

### Timing Synchronization

Timing accuracy is critical for QTA and synchronization:

**Requirements:**
```
| Protocol | Timing Requirement | Difficulty | Solution |
|----------|-------------------|-----------|----------|
| BB84     | Millisecond sync   | Easy      | NTP synchronization |
| QTA      | 100 ps accuracy    | Hard      | GPS + atomic clock |
| QSDC     | Microsecond sync   | Medium    | Cesium standard |
```

**GPS-Based Synchronization:**
```python
class GPSSynchronization:
    """GPS-based timing for QTA"""
    
    def __init__(self):
        self.gps_uncertainty = 10  # ns (typical 1PPS module)
        self.cable_delay_uncertainty = 2  # ns
        self.electronics_jitter = 50  # ps
        
    def total_timing_error(self):
        # Root sum of squares
        error = np.sqrt(
            self.gps_uncertainty**2 + 
            self.cable_delay_uncertainty**2 + 
            self.electronics_jitter**2
        )
        return error  # ~10 ns total
    
    def qta_feasibility(self, distance_km):
        """Check if QTA is feasible at given distance"""
        expected_toa = 2 * distance_km / 0.3  # microseconds
        toa_ns = expected_toa * 1000
        
        tolerance_ps = 100  # ±100 ps for QTA
        tolerance_ns = tolerance_ps / 1000
        
        timing_error = self.total_timing_error()
        
        feasible = timing_error < tolerance_ns
        margin = tolerance_ns / timing_error if timing_error > 0 else float('inf')
        
        return {
            'feasible': feasible,
            'margin': margin,
            'error_vs_tolerance': f"{timing_error:.1f} ns vs {tolerance_ns:.3f} ns"
        }
```

### Environmental Stability

**Temperature Effects:**
```
Temperature variation: ±5°C
↓
Fiber refractive index changes
↓
Polarization rotation: ~0.1°/°C in SMF-28
↓
QBER increase: ~0.5-1% per °C
↓
Example: Room fluctuations ±5°C → QBER changes by ±2.5-5%
```

**Solutions:**
- Climate-controlled facilities: ±1°C
- Thermal compensation in fiber: Heating jackets
- Active feedback loops: Monitor QBER, adjust parameters
- Vibration isolation: Optical benches on pneumatic insulators

---

## Cost Analysis and System Architecture

**Complete System Cost Breakdown (100 km metropolitan link):**

```
Basic Lab Setup ($100-150k):
├─ Quantum Source (SPDC): $50k
├─ Detector Module (2x APD): $10k
├─ Single-mode fiber (100 km): $5k
├─ Optical components: $10k
├─ Control electronics: $20k
└─ Software/integration: $5-15k

Enterprise Metropolitan System ($500k-1M):
├─ High-reliability source: $100k
├─ Detectors (4x SNSPDs): $300k
├─ Fiber + polarization control: $50k
├─ Electronics + DSP: $80k
├─ Software suite: $50k
└─ Installation + testing: $20k

Long-Distance Network ($5-10M):
├─ Multiple QKD nodes: $1.5M
├─ Quantum repeaters (per node): $2M
├─ Fiber infrastructure: $1M
├─ Network management: $500k
├─ Integration and validation: $500k
└─ Training + support: $500k

Satellite System ($20-50M):
├─ Space-qualified QKD payload: $5M
├─ Ground station (single): $3M
├─ Multiple ground stations (10x): $25M
├─ Network integration: $5M
└─ Launch + deployment: $5-10M
```
