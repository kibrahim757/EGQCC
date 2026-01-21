# The BB84 Quantum Key Distribution Protocol

**Author**: Engineer Mohamed Helmy  
**GitHub**: https://github.com/7elmie  
**LinkedIn**: https://www.linkedin.com/in/7elmie/

**Focus**: Prepare and Measure mechanics, QBER monitoring, Privacy Amplification

---

The BB84 protocol (Bennett & Brassard, 1984) is the foundational quantum key distribution protocol enabling secure key generation through quantum mechanics. BB84 implements three critical security mechanisms for Phase 3:

1. **Prepare and Measure Mechanics**: Quantum state preparation and measurement-based key generation
2. **QBER Monitoring**: Real-time quantum bit error rate measurement for intrusion detection
3. **Privacy Amplification**: Post-processing techniques to clean the shared key

BB84 demonstrates how quantum mechanics prevents eavesdropping through the no-cloning theorem and measurement uncertainty, establishing keys with information-theoretic security (unconditional against quantum computers).

## Prepare and Measure Mechanics

BB84 uses the prepare-and-measure paradigm: Alice prepares quantum states, transmits them over an insecure quantum channel, and Bob measures them using randomly chosen bases. This asymmetry provides security.

### Quantum State Encoding

In BB84, information is encoded using two mutually unbiased bases (MUBs). For photon polarization implementations, these bases are typically:

- **Rectilinear Basis (Z)**: {|0⟩, |1⟩}
- **Diagonal Basis (X)**: {|+⟩, |-⟩}

Where:
```
|+⟩ = (1/√2)(|0⟩ + |1⟩)
|-⟩ = (1/√2)(|0⟩ - |1⟩)
```

The non-orthogonality between bases ensures that measurements performed in the wrong basis yield random outcomes.

## Protocol Description

The BB84 protocol proceeds as follows:

1. Alice randomly selects a bit string and a sequence of encoding bases.
2. Alice prepares quantum states accordingly and transmits them to Bob.
3. Bob randomly selects measurement bases and measures incoming states.
4. Alice and Bob publicly compare bases over the classical channel.
5. Bits corresponding to matching bases are retained (sifting).

At this stage, Alice and Bob share a raw key that may contain errors due to noise or eavesdropping.

## Eavesdropping Detection and QBER Monitoring

The BB84 protocol detects eavesdropping through Quantum Bit Error Rate (QBER) analysis. After sifting, Alice and Bob publicly compare a random subset of their raw key bits. If an eavesdropper (Eve) has been monitoring the channel:

- Eve must measure each quantum state in a randomly chosen basis
- Eve will measure in the wrong basis roughly 50% of the time
- Wrong measurements produce random outcomes with 50% error rate
- Alice and Bob will observe QBER significantly above the quantum noise floor

The theoretical QBER threshold is:

```
Q_threshold = 11% (accounting for quantum noise in real systems)
```

If measured QBER exceeds this threshold, eavesdropping is detected and the protocol is aborted.

## Privacy Amplification

Even with no detected eavesdropping, the raw key may contain information leaked to Eve through:

- Quantum channel losses that are correlated with measurement outcomes
- Partial information gained through beam-splitting attacks
- Side-channel leakage from measurement apparatus

Privacy amplification removes this residual information through post-processing:

### Parity-Check Codes

The sifted key is divided into blocks. New key bits are generated as:

```
k'_i = k_{i,1} ⊕ k_{i,2} ⊕ ... ⊕ k_{i,m}
```

Where ⊕ denotes XOR operation and m is the block size. This reduces Eve's knowledge exponentially with the block size.

### Toeplitz Matrices

Alternatively, random Toeplitz matrices are applied to the raw key:

```
k'_final = T · k_sifted (mod 2)
```

This provides provably secure privacy amplification with exponential information removal.

## Security Intuition

An eavesdropper attempting to intercept and resend quantum states must perform measurements. Due to basis mismatch, this introduces errors that manifest as an increased Quantum Bit Error Rate (QBER).

By publicly comparing a subset of their raw key, Alice and Bob can estimate the QBER. If the observed error rate exceeds a predefined threshold, the protocol is aborted.

The security of BB84 relies on the fundamental impossibility of simultaneously measuring non-commuting observables without disturbance. Any attempt by an adversary to gain information about the key inevitably introduces detectable errors.

Security proofs of BB84 show that, below a certain QBER threshold, Alice and Bob can apply error correction and privacy amplification to distill a secret key that is statistically independent of the adversary's information.

## Assumptions and Limitations

The theoretical security of BB84 assumes:

- Ideal single-photon sources
- Perfect detectors
- Authenticated classical communication

Real-world implementations relax these assumptions, leading to practical attack vectors such as photon-number-splitting attacks. Addressing these issues requires enhanced protocols and implementation-aware security analysis.

This theoretical foundation provides the basis for simulation, performance evaluation, and physical-layer analysis presented in subsequent sections.
