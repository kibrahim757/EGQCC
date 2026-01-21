# Security Analysis of the BB84 Protocol

**Author**: Engineer Mohamed Helmy  
**GitHub**: https://github.com/7elmie  
**LinkedIn**: https://www.linkedin.com/in/7elmie/

---

The security of the BB84 protocol arises directly from the fundamental incompatibility of quantum measurements performed in non-commuting bases. This section provides an intuitive and analytical examination of the security mechanisms underlying BB84, with a particular focus on error rates and attack detection.

## Adversary Model

In the BB84 security model, the adversary (Eve) is assumed to have complete control over both the quantum and classical channels. Eve may perform arbitrary quantum operations, including intercept-resend, entangling attacks, and collective measurements.

The only limitation imposed on Eve is adherence to the laws of quantum mechanics. This adversary model ensures information-theoretic security.

## Intercept-Resend Attack

The simplest attack strategy against BB84 is the intercept-resend attack. Eve measures each transmitted quantum state in a randomly chosen basis and resends a new state to Bob based on her measurement outcome.

Due to random basis selection:

- Eve selects the correct basis with probability 0.5
- Incorrect basis measurements introduce random errors

This results in an expected Quantum Bit Error Rate (QBER) of approximately 25%, which is easily detectable by Alice and Bob.

## Quantum Bit Error Rate (QBER)

The Quantum Bit Error Rate is defined as:

```
QBER = (Number of erroneous bits) / (Total number of compared bits)
```

By publicly comparing a subset of the sifted key, Alice and Bob estimate the QBER. If the measured QBER exceeds a predefined threshold, the protocol is aborted.

## Security Thresholds

Security proofs show that BB84 remains secure as long as the QBER remains below a critical threshold (typically around 11% under ideal assumptions). Below this threshold, error correction and privacy amplification can be applied to distill a secret key that is statistically independent of Eve's information.

## Implications for Practical Systems

In practical systems, QBER may increase due to:

- Channel noise and loss
- Detector inefficiencies
- Source imperfections

Distinguishing between benign noise and malicious interference is therefore a central challenge in real-world QKD deployments.
