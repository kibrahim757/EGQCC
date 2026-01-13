# Quantum Key Distribution 

# 📡 Quantum Key Distribution (QKD) Deep-Dive
**Lead: Muhamed HelmY**

This section focuses on the physical layer of quantum security, ensuring unconditional security through the laws of physics.

---

## 1. BB84 Protocol: "Prepare and Measure" Mechanics
The BB84 protocol is the foundation of our simulation. It utilizes the non-orthogonal states of photons to exchange cryptographic keys.

### The Process:
1. **Preparation:** Alice sends photons in random bases: Rectilinear $(+)$ or Diagonal $(\times)$.
2. **Measurement:** Bob measures in random bases.
3. **Sifting:** They announce their bases over a classical channel and keep bits where bases matched.

## 2. Quantum Bit Error Rate (QBER)
QBER is our primary diagnostic tool for detecting eavesdropping (Eve). In an ideal noiseless channel, QBER should be $0$.

### Detection Logic:
- If Eve intercepts, she must measure and resend, which introduces an error rate of at least $25\%$.
- The threshold for a secure key is typically $QBER < 11\%$.
- **Formula:** $$QBER = \frac{n_{wrong}}{n_{total}}$$
where $n_{wrong}$ is the number of mismatched bits between Alice and Bob after sifting.

## 3. Privacy Amplification (PA)
Even if QBER is low, Eve might have gained partial information. Privacy Amplification is the post-processing stage that "cleans" the key.

### Technique:
We use **Universal Hash Functions** (like Toeplitz Matrices) to compress the sifted key into a shorter, highly secure final key.
- **Goal:** Reduce Eve’s maximum information $\epsilon$ to a negligible value.
- **Result:** A final key where Eve has zero usable knowledge.

---
*Check `bb84_simulation.py` for a practical implementation of these concepts.*
*Last updated on: (13-01-2026)..*