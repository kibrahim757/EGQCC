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

QBER quantifies quantum channel quality:

```
QBER = (E / n) × 100%
```

Typical QBER values:
- Ideal system: 0%
- Short-distance lab: 1-3%
- Metropolitan networks (100 km): 3-5%
- Satellite systems (clear weather): 5-10%
- Maximum for secure QSDC: ~11%

### Secure Key Rate

Secure key rate is the speed at which secure information can be extracted:

Typical values:
- Lab conditions (short range): 10-100 kbps
- Metropolitan networks (50-100 km): 1-10 kbps
- Long-range networks (200+ km): < 1 kbps
- Satellite links: Highly variable (10 bps - 100 kbps)
