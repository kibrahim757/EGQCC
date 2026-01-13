# Post-Quantum Cryptography 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![liboqs](https://img.shields.io/badge/liboqs-latest-green.svg)](https://github.com/open-quantum-safe/liboqs)

A comprehensive research and educational repository demonstrating post-quantum cryptography implementations using liboqs, along with quantum computing simulations using Cirq and Qiskit.

## 📋 Table of Contents

- [Overview](#overview)
- [Why Post-Quantum Cryptography?](#why-post-quantum-cryptography)
- [Mathematical Foundations](#mathematical-foundations)
- [Use Cases & Applications](#use-cases--applications)
- [History of PQC](#history-of-pqc)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Demonstrations](#demonstrations)
- [Algorithms Available](#algorithms-available)
- [Performance Benchmarks](#performance-benchmarks)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)
- [Author](#author)

## 🎯 Overview

**Post-Quantum Cryptography (PQC)** encompasses cryptographic algorithms specifically designed to remain secure against attacks from both classical computers and future quantum computers. This repository provides comprehensive research, demonstrations, and practical implementations.

### What This Repository Covers:

1. **Post-Quantum Cryptography (PQC)** using liboqs
   - Key Encapsulation Mechanisms (KEMs)
   - Digital Signature Schemes
   - NIST-approved standards (ML-KEM, ML-DSA, SLH-DSA, Falcon)

2. **Quantum Computing Simulations**
   - Google's Cirq framework
   - IBM's Qiskit framework
   - Quantum algorithms (Bell states, Grover's algorithm, quantum teleportation)

3. **Threat Model Analysis**
   - Classical vs quantum cryptography security
   - Migration strategies and timelines
   - Real-world use cases and applications

4. **Research Analysis**
   - NIST standardization process
   - Performance optimization studies (OptHQC)
   - Industry adoption and readiness assessments

## 🔐 Why Post-Quantum Cryptography?

### The Quantum Threat

#### 1. Shor's Algorithm (1994)
- Breaks RSA factorization in polynomial time O(n³)
- Breaks ECC via discrete logarithm problem
- Impact: 2048-bit RSA breakable in hours on a quantum computer
- Result: Current public-key infrastructure becomes obsolete

#### 2. Grover's Algorithm (1996)
- Quadratic speedup for unstructured search
- Reduces symmetric key security by half
- AES-128 becomes 64-bit security
- Solution: Use AES-256 (128-bit quantum security)

#### 3. Current Quantum State (2025)
- NISQ Era: 50-1000 noisy qubits
- IBM: 1,121 qubit processor
- Google: Willow chip with error correction
- Timeline: Cryptographically Relevant Quantum Computers (CRQCs) in 10-20 years

### Security Comparison

| Algorithm | Classical Computer | Quantum Computer |
|-----------|-------------------|------------------|
| RSA-2048  | ✅ SECURE (~300 trillion years) | ❌ BROKEN (~few hours) |
| ECC-256   | ✅ SECURE (billions of years) | ❌ BROKEN (~few hours) |
| AES-128   | ✅ SECURE | ⚠️ WEAKENED (64-bit security) |
| AES-256   | ✅ SECURE | ✅ SECURE (128-bit security) |
| Kyber768  | ✅ SECURE | ✅ SECURE |
| Dilithium3| ✅ SECURE | ✅ SECURE |

### Why Migrate NOW?

#### 1. "Harvest Now, Decrypt Later" Attacks
This threat is REAL and happening TODAY:
- Adversaries ARE collecting encrypted data now
- NSA and CISA have issued official warnings
- Threat exists BEFORE quantum computers arrive

Timeline Example:
- 2025: Data encrypted with RSA-2048
- 2035: Quantum computer breaks it
- 2035: Your 2025 data is exposed

Who's at Risk?
- Government documents (25-75 year classification)
- Medical records (50+ year retention)
- Financial data (7-10+ year retention)
- Trade secrets and intellectual property
- Personal communications

#### 2. Long-Term Data Protection Requirements

| Data Type | Protection Needed | RSA/ECC Lifetime |
|-----------|------------------|------------------|
| Credit Cards | 3-5 years | ❌ Broken ~2035 |
| Medical Records | 50+ years | ❌ Broken ~2035 |
| TOP SECRET | 75 years | ❌ Broken ~2035 |
| Nuclear Waste Data | 10,000 years | ❌ Broken ~2035 |

Regulatory Requirements:
- GDPR: Indefinite for sensitive data
- HIPAA: 6 years to lifetime
- SEC: 7 years minimum
- Government TOP SECRET: Up to 75 years

The Gap: We need cryptography that outlasts the data!

#### 3. Critical Infrastructure Lifecycle

Replacement Cycles:
- Power grid: 30-50 years
- Railway systems: 20-40 years
- Buildings: 25-30 years
- Industrial control: 15-25 years

The Problem:
- Systems deployed TODAY will operate past 2050
- Quantum computers likely by 2035-2040
- Retrofit is extremely expensive

The Solution:
- Deploy PQC NOW in new systems
- Build crypto-agility into infrastructure
- Use hybrid mode during transition

#### 4. Consequences of Inaction

A) Mass Decryption Event
- Decades of communications exposed
- State secrets compromised
- Corporate espionage at scale

B) PKI Infrastructure Collapse
- Digital signatures become forgeable
- Cannot authenticate software updates
- Loss of digital trust

C) Financial System Vulnerability
- Transaction forgery
- Cryptocurrency theft
- Market manipulation

D) National Security Crisis
- Military communications compromised
- Intelligence operations exposed
- Critical infrastructure vulnerable

E) Loss of Digital Trust
- E-commerce collapse
- Digital transformation reversed
- Economic disruption

#### 5. Benefits of Early Adoption

Future-Proof Security:
- Protection against both classical and quantum threats
- Long-term confidentiality guaranteed
- Regulatory compliance

Crypto-Agility:
- Quick algorithm switching capability
- Modular architecture
- Reduced future migration costs

Competitive Advantage:
- Market trust and confidence
- Compliance leadership
- Customer data protection

#### 6. The Window is Closing

Critical Timeline:
- 2024-2025: Standards published ✅
- 2025-2027: Development phase (NOW)
- 2027-2030: Mass deployment
- 2030-2035: Complete migration
- 2035+: Quantum threat becomes real

⚠️ URGENT: 10-15 year migration needed. Must start NOW!

## 🔬 Mathematical Foundations

Post-Quantum Cryptography is built on five main mathematical families, each with different hardness assumptions:

### 1. Lattice-Based Cryptography ⭐ (Most Promising)

Mathematical Foundation:
- Learning With Errors (LWE)
- Ring-LWE and Module-LWE variants
- Shortest Vector Problem (SVP)

Advantages:
- Excellent performance
- Strong security proofs
- Supports both encryption and signatures
- Most versatile family

Examples:
- CRYSTALS-Kyber (ML-KEM) - NIST winner
- CRYSTALS-Dilithium (ML-DSA) - NIST winner
- Falcon - NIST winner

### 2. Hash-Based Signatures

Mathematical Foundation:
- Cryptographic hash functions
- Merkle tree structures
- One-time signatures

Advantages:
- Minimal security assumptions
- Simple and well-understood
- Conservative security choice
- Proven security based on hash functions

Examples:
- SPHINCS+ (SLH-DSA) - NIST winner
- XMSS, LMS

### 3. Code-Based Cryptography

Mathematical Foundation:
- Syndrome decoding problem (NP-complete)
- Error-correcting codes
- 40+ years of confidence

Advantages:
- Fast encryption/decryption
- Longest track record (McEliece since 1978)
- Cryptographic diversity
- No known quantum algorithm

Examples:
- Classic McEliece - NIST Round 4
- HQC - NIST Round 4
- BIKE - NIST Round 4

### 4. Multivariate Cryptography

Mathematical Foundation:
- Multivariate polynomial equations over finite fields

Status:
- Rainbow (broken in 2022)
- Research continues with new variants

### 5. Isogeny-Based Cryptography

Mathematical Foundation:
- Elliptic curve isogenies

Status:
- SIKE (broken in 2022)
- Smallest keys but security concerns
- Active research for new constructions

## 🌐 Use Cases & Applications

### Critical Infrastructure

#### 1. Power Grid and Energy Systems
Applications:
- SCADA system security
- Smart grid communications
- Nuclear facility controls
- Oil and gas pipeline management

Requirements:
- 30-50 year operational lifetime
- Real-time constraints
- Legacy system integration

#### 2. Water Treatment Facilities
- Control system authentication
- Chemical dosing security
- Distribution network monitoring
- **Threat**: Past communications reveal vulnerabilities

#### 3. Transportation Networks
**Sectors:**
- Air Traffic Control systems
- Railway signaling
- Maritime navigation
- Autonomous vehicles (V2V, V2I)

**Applications:**
- Secure command and control
- Certificate authentication
- Firmware integrity verification

#### 4. Telecommunications
- 5G/6G core networks
- Fiber management systems
- Satellite communications
- Submarine cable control

### Financial & Digital Economy

#### 1. Banking and Payments
- Wire transfers and ACH
- ATM network security
- Credit card processing
- Mobile payment systems

**Urgency**: 7-10 year data retention already vulnerable

#### 2. Blockchain and Cryptocurrency
- Bitcoin/Ethereum security
- Smart contracts
- Digital asset custody

**Quantum Threat:**
- ECDSA signatures vulnerable
- Need quantum-resistant addresses

#### 3. Stock Exchanges
- High-frequency trading systems
- Market data integrity
- Settlement systems

#### 4. Digital Identity
- eSignature services
- Document authentication
- Certificate authorities
- PKI infrastructure

### Government & Healthcare

#### 1. Government and Defense
- Classified communications (TOP SECRET)
- Diplomatic cables
- Intelligence operations
- Military command and control

**Requirement**: 25-75 year protection needed NOW

#### 2. Healthcare Systems
- Electronic Health Records (EHR)
- Medical imaging (PACS)
- Telemedicine platforms
- Medical device security

**Regulation**: HIPAA + 50-year retention requirements

### Emerging Technologies

#### 1. Internet of Things (IoT)
- Smart home devices
- Industrial IoT sensors
- Wearables
- Smart city infrastructure

**Challenges:**
- Limited CPU, memory, battery
- Need lightweight implementations

#### 2. Cloud Computing
- TLS/SSL connections
- VM isolation
- Database encryption
- Backup security

#### 3. Satellite Communications
- GPS/GNSS security
- Satellite control systems
- Earth observation
- Deep space missions

## 📜 History of PQC

### Early Foundations (1978-1996)

**1978 - McEliece Cryptosystem**
- First code-based cryptosystem
- Still unbroken after 45+ years
- Large keys (~1 MB)

**1989 - Merkle Signatures**
- Hash-based signatures
- Foundation for SPHINCS+

**1994 - Shor's Algorithm** 🚨 **BREAKTHROUGH**
- Peter Shor proves quantum computers can break RSA
- Catalyst for PQC research

**1996 - Three Major Events:**
- NTRU Cryptosystem (first practical lattice-based)
- Grover's Algorithm (quadratic search speedup)
- First PQC workshops established

### Development Era (2000-2015)

**2001** - NIST AES Selection (AES-256 sufficient for quantum resistance)

**2005-2008** - Academic Growth
- PQCrypto conferences established
- NSA begins PQC assessment

**2011** - NTRU Revisited with Ring-LWE improvements

### NIST Standardization (2016-2022)

**2016** - NIST Announces PQC Standardization
- December 20: Call for proposals
- Goal: Standardize quantum-resistant algorithms

**2017 - Round 1**: 69 Submissions from 25+ countries

**2019 - Round 2**: 26 Candidates (17 KEMs, 9 signatures)

**2020 - Round 3**: 7 Finalists + 8 Alternates

**2022 - Winners Announced** (July 5)

**Primary Standards:**
- CRYSTALS-Kyber (ML-KEM)
- CRYSTALS-Dilithium (ML-DSA)
- Falcon
- SPHINCS+ (SLH-DSA)

**Round 4 Continues:**
- Classic McEliece
- BIKE
- HQC

### Current Era (2023-2025)

**2023** - Standards Development
- Draft FIPS published
- Industry pilots begin

**2024** - **OFFICIAL STANDARDS RELEASED** (August 13) 🎉

**NIST FIPS Published:**
- **FIPS 203**: Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM / Kyber)
- **FIPS 204**: Module-Lattice-Based Digital Signature Standard (ML-DSA / Dilithium)
- **FIPS 205**: Stateless Hash-Based Digital Signature Standard (SLH-DSA / SPHINCS+)

**Industry Response:**
- Apple: PQC in iMessage
- Google: Chrome experiments
- Cloudflare: Edge deployment

**2025** - Current State (December)
- NISTIR 8545: Round 4 status
- Industry adoption accelerating
- TLS 1.3 PQC cipher suites
- VPN providers adding support
- HSM manufacturers ready

**Challenges:**
- Legacy system migration
- IoT performance constraints
- Certificate Authority infrastructure updates

**Future (2026-2030):**
- Round 4 completion
- Widespread production deployment
- International harmonization

- 🔑 **Key Encapsulation Mechanisms**: Kyber (ML-KEM) implementations with multiple security levels
- ✍️ **Digital Signatures**: Dilithium (ML-DSA), Falcon, and SPHINCS+ implementations
- ⚡ **High Performance**: All operations complete in milliseconds
- 🧪 **Comprehensive Testing**: Benchmarking and performance analysis tools
- 🔬 **Quantum Simulations**: Bell states, Grover's algorithm, quantum teleportation
- 📊 **Educational Examples**: Step-by-step explanations with visual outputs
- 🌐 **Production Ready**: Built on liboqs, the industry-standard PQC library

## ✨ Features

### Prerequisites

- Python 3.8 or higher
- GCC/G++ compiler
- CMake
- Git

### Method 1: From Source (Linux/macOS)

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y cmake gcc g++ ninja-build libssl-dev git

# Clone and build liboqs
git clone --depth=1 https://github.com/open-quantum-safe/liboqs.git
cd liboqs
mkdir build && cd build
cmake -GNinja -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_SHARED_LIBS=ON ..
ninja
sudo ninja install
sudo ldconfig
```

### Method 2: Package Managers

**Ubuntu/Debian:**
```bash
sudo apt-get install liboqs-dev
```

**macOS (Homebrew):**
```bash
brew install liboqs
```

**Windows (vcpkg):**
```bash
vcpkg install liboqs
```

### Method 3: Docker

```bash
docker pull openquantumsafe/liboqs
docker run -it openquantumsafe/liboqs
```

### Method 4: Python Bindings

```bash
# Install liboqs-python
pip install liboqs-python

# Install quantum computing frameworks
pip install cirq qiskit qiskit-aer
```

### Build Options

Configure liboqs with additional flags:

```bash
cmake -GNinja \
  -DCMAKE_INSTALL_PREFIX=/usr/local \
  -DBUILD_SHARED_LIBS=ON \
  -DOQS_USE_OPENSSL=ON \
  -DOQS_DIST_BUILD=ON \
  ..
```

### Google Colab Setup

For a zero-installation experience, use our [interactive Colab notebook](https://colab.research.google.com/drive/1OGYULoYvtzcmPWfe7MaBbqfmCN6Mtl8A?usp=sharing):

1. Open the notebook
2. Run Cell 1 (installation - takes 5-10 minutes)
3. Restart runtime
4. Run remaining cells sequentially

## 🚀 Installation

### Kyber Key Encapsulation

```python
import oqs

# Initialize Kyber768
kem = oqs.KeyEncapsulation("Kyber768")

# Alice generates keypair
public_key = kem.generate_keypair()

# Bob encapsulates shared secret
ciphertext, bob_shared_secret = kem.encap_secret(public_key)

# Alice decapsulates to recover shared secret
alice_shared_secret = kem.decap_secret(ciphertext)

# Verify secrets match
assert alice_shared_secret == bob_shared_secret
print("✅ Shared secret established!")
```

### Dilithium Digital Signatures

```python
import oqs

# Initialize Dilithium
sig = oqs.Signature("Dilithium3")

# Generate signing keypair
public_key = sig.generate_keypair()

# Sign message
message = b"Hello, Post-Quantum World!"
signature = sig.sign(message)

# Verify signature
is_valid = sig.verify(message, signature, public_key)
print(f"✅ Signature valid: {is_valid}")
```

## 🧪 Demonstrations

### 1. Post-Quantum Cryptography with liboqs

#### Kyber (ML-KEM) - Key Encapsulation
- **Security Levels**: Kyber512, Kyber768, Kyber1024
- **Use Case**: Secure key exchange resistant to quantum attacks
- **Performance**: Sub-millisecond operations
- **Status**: NIST-approved standard (ML-KEM)

#### Dilithium (ML-DSA) - Digital Signatures
- **Security Levels**: Dilithium2, Dilithium3, Dilithium5
- **Use Case**: Authentication and integrity verification
- **Performance**: 1-3 milliseconds per operation
- **Status**: NIST-approved standard (ML-DSA)

### 2. Quantum Computing with Cirq (Google)

#### Bell State - Quantum Entanglement
Demonstrates quantum entanglement where measuring one qubit instantly determines the other's state. Results show only |00⟩ and |11⟩ states, proving quantum correlation.

#### Grover's Search Algorithm
Demonstrates quantum search speedup: finds a marked item with ~85% success rate compared to 25% classical random chance, showing quadratic speedup.

### 3. Quantum Computing with Qiskit (IBM)

#### Bell State Verification
Confirms entanglement using IBM's framework, demonstrating framework-independent quantum phenomena.

#### Quantum Teleportation
Demonstrates transferring quantum states using entanglement and classical communication, a foundational technology for quantum networks.

## 📚 Algorithms Available

### Key Encapsulation Mechanisms (30+ algorithms)

**NIST Standards:**
- **ML-KEM** (FIPS 203): ML-KEM-512, ML-KEM-768, ML-KEM-1024
- **CRYSTALS-Kyber**: Kyber512, Kyber768, Kyber1024

**Other Lattice-Based:**
- **NTRU**: NTRU-HPS-2048-509, NTRU-HPS-2048-677, NTRU-HRSS-701, NTRU-HRSS-1024
- **Saber**: LightSaber, Saber, FireSaber

**Code-Based:**
- **BIKE**: BIKE-L1, BIKE-L3, BIKE-L5
- **Classic McEliece**: Multiple parameter sets
- **HQC**: HQC-128, HQC-192, HQC-256

### Digital Signature Schemes (15+ algorithms)

**NIST Standards:**
- **ML-DSA** (FIPS 204): ML-DSA-44, ML-DSA-65, ML-DSA-87
- **CRYSTALS-Dilithium**: Dilithium2, Dilithium3, Dilithium5
- **SLH-DSA** (FIPS 205): SPHINCS+ variants (SHA2, SHAKE)
- **Falcon**: Falcon-512, Falcon-1024

**Other:**
- **SPHINCS+**: Multiple parameter sets (simple, robust)
- **Picnic**: Various security levels
- **Rainbow**: Multiple security levels

## ⚡ Performance Benchmarks

### Key Encapsulation Mechanisms (50 iterations average)

| Algorithm   | KeyGen (ms) | Encap (ms) | Decap (ms) |
|------------|-------------|------------|------------|
| Kyber512   | 0.04        | 0.05       | 0.06       |
| Kyber768   | 0.06        | 0.07       | 0.08       |
| Kyber1024  | 0.08        | 0.09       | 0.10       |

### Digital Signatures (50 iterations average)

| Algorithm   | KeyGen (ms) | Sign (ms)  | Verify (ms)|
|------------|-------------|------------|------------|
| Dilithium2 | 0.08        | 1.2        | 0.5        |
| Dilithium3 | 0.12        | 2.1        | 0.7        |

**Key Observations:**
- All KEM operations complete in under 0.1 milliseconds
- Signature operations complete in 1-3 milliseconds
- Performance is practical for real-world applications
- Higher security levels have slightly longer operation times

## 📁 Project Structure

```
EGQCC/PQC/
├── README.md                    # This file
├── notebooks/
│   └── LIBOQS.ipynb            # Comprehensive Google Colab demo
├── presentations/
│   ├── main_presentation.pdf    # Overview and concepts
│   └── tools_presentation.pdf   # Technical implementation
├── examples/
│   ├── kyber_demo.py           # Kyber KEM examples
│   ├── dilithium_demo.py       # Dilithium signature examples
│   └── benchmarks.py           # Performance testing
├── quantum/
│   ├── cirq_examples.py        # Cirq demonstrations
│   └── qiskit_examples.py      # Qiskit demonstrations
└── docs/
    ├── installation.md         # Detailed setup guide
    ├── algorithms.md           # Algorithm documentation
    └── threat_model.md         # Security analysis
```

## 🏛️ Research Groups & Universities

### Open Quantum Safe (OQS) Project - liboqs

**Website**: [openquantumsafe.org](https://openquantumsafe.org)
**GitHub**: [github.com/open-quantum-safe/liboqs](https://github.com/open-quantum-safe/liboqs)
**Founded**: 2016

**Project Leader:**
- **Douglas Stebila** (Co-founder, Project Leader)
  - Position: Associate Professor, University of Waterloo
  - Department: Combinatorics & Optimization, Faculty of Mathematics
  - Website: [douglas.stebila.ca](https://www.douglas.stebila.ca)

**Funding Sources:**
1. **Natural Sciences and Engineering Research Council of Canada (NSERC)**
   - Discovery Grant RGPIN-2016-05146
   - Discovery Accelerator Supplement ($120,000, 2016-2019)
   - Focus: Quantum-safe cryptography for the Internet

2. **Canadian Centre for Cyber Security**
   - Ongoing support for OQS development

3. **NGI Assure Fund (European Union)**
   - Support for oqs-provider development
   - Administered by NLnet foundation

### NIST Post-Quantum Cryptography Project

**Organization**: National Institute of Standards and Technology (NIST)
**Website**: [csrc.nist.gov/projects/post-quantum-cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
**Started**: December 2016
**Status**: Standards published August 2024

**Project Leadership:**
- **Dustin Moody** (Project Lead) - NIST Computer Security Division
- **Lily Chen** (Manager) - NIST Cryptographic Technology Group Manager

**Funding:**
- US Federal Government Budget
- NIST budget allocation: $10-15 million (2016-2024)
- International collaboration funding

### University of Waterloo - Institute for Quantum Computing (IQC)

**Website**: [uwaterloo.ca/institute-for-quantum-computing](https://uwaterloo.ca/institute-for-quantum-computing/)
**Location**: Waterloo, Ontario, Canada
**Founded**: 2002

**Key Researchers in PQC:**

1. **Michele Mosca** (Executive Director)
   - Professor, Department of Combinatorics & Optimization
   - Co-founder: evolutionQ, Open Quantum Safe
   - Focus: Quantum threat assessment, PQC migration
   - Website: [iqc.uwaterloo.ca/people/profile/mmosca](https://services.iqc.uwaterloo.ca/people/profile/mmosca/)

2. **Douglas Stebila**
   - Associate Professor
   - Co-founder: Open Quantum Safe
   - Focus: Internet protocols, key exchange
   - Website: [douglas.stebila.ca](https://www.douglas.stebila.ca)

**Funding Sources:**
- Government of Canada
- Province of Ontario
- Industry partnerships (50+ companies)
- Research grants (NSERC, CFI)
- Mike & Ophelia Lazaridis donation ($100 million)

**Major Projects:**
- Open Quantum Safe (OQS)

### MIT - Massachusetts Institute of Technology

**Website**: [csail.mit.edu](https://www.csail.mit.edu/)
**Department**: Computer Science and Artificial Intelligence Lab (CSAIL)

**Key Researchers:**

1. **Vinod Vaikuntanathan**
   - Professor of Computer Science
   - Focus: Lattice-based cryptography, Fully Homomorphic Encryption (FHE)
   - Website: [people.csail.mit.edu/vinodv](https://people.csail.mit.edu/vinodv/)
   - Key work: LWE-based cryptosystems, homomorphic encryption

2. **Shafi Goldwasser**
   - Professor (MIT / UC Berkeley / Weizmann)
   - Turing Award winner (2012)
   - Focus: Complexity theory, cryptography

**Funding:**
- NSF (National Science Foundation)
- DARPA (Defense Advanced Research Projects Agency)
- ONR (Office of Naval Research)
- Simons Foundation
- MIT endowment
- Typical grant: $500K-$2M per project

### Other Leading Labs & Companies

**Industry:**
- Amazon Web Services (AWS)
- Cloudflare
- Google
- Microsoft Research
- IBM Research

**Academia:**
- ENS Paris/Lyon (France)
- TU Eindhoven (Netherlands)
- KU Leuven (Belgium) - COSIC Group
- Stanford University

## 📰 Conferences & Journals

### Top-Tier Cryptography Conferences

**Tier 1 - Cryptography:**
- **CRYPTO** (Santa Barbara, Annual)
- **EUROCRYPT** (Europe, Annual)
- **ASIACRYPT** (Asia, Annual)
- Acceptance Rate: ~15%

**PQC-Specific:**
- **PQCrypto** (Rotating, Annual)
  - Focus: Exclusively Post-Quantum Cryptography
  - Attendance: 200-400 researchers

**Implementation Focused:**
- **CHES** (Cryptographic Hardware and Embedded Systems)
- **TCHES** (Transactions on CHES - Journal with presentation)

**Security Conferences:**
- **IEEE S&P** (Oakland)
- **USENIX Security**
- **ACM CCS**
- **NDSS**

### Leading Journals

**Tier 1:**
- **Journal of Cryptology** (Springer/IACR)
- **TCHES** (IACR, Open Access)
- **IEEE TIFS** (Impact Factor: 6.8)
- **IEEE TDSC** (Impact Factor: 7.3)

**Open Access:**
- **MDPI Cryptography**
- **MDPI Applied Sciences**

**Preprints:**
- **IACR ePrint** ([eprint.iacr.org](https://eprint.iacr.org))
- **arXiv.org** (FREE, immediate publication)

## 🔮 Future Directions

### Research Directions

#### 1. Algorithm Innovation
- Hybrid cryptography standardization
- New mathematical foundations
- Efficiency improvements
- Post-quantum homomorphic encryption

#### 2. Implementation Research
- Hardware acceleration (CPU instructions)
- Lightweight PQC for IoT
- Side-channel resistance
- Formal verification

#### 3. New Applications
- Post-quantum zero-knowledge proofs
- PQ multi-party computation
- PQ blockchain protocols
- PQ IoT security protocols

#### 4. Cryptanalysis
- Continued security analysis
- Quantum algorithm research
- Classical attack improvements
- Long-term evaluation

### Standardization Roadmap

**Long-Term (2030-2035):**
- Full ecosystem support
- Classical crypto phase-out begins
- Quantum computers arrive
- PQC proves its value

### Deployment Challenges

**Technical:**
- Performance impact (15-50% latency increase)
- Large keys/signatures (10-50x larger)
- Legacy system integration
- Side-channel vulnerabilities

**Organizational:**
- Lack of awareness
- High migration costs ($1M-$10M+ for enterprises)
- Expertise shortage
- Risk aversion

**Regulatory:**
- Compliance uncertainty
- International coordination
- Certification delays

### Opportunities

**For Researchers:**
- Many open problems
- High-impact publications
- Funding availability
- Real-world impact

**For Industry:**
- Early-mover advantage
- New products/services
- Market differentiation

**For Organizations:**
- Future-proof security
- Regulatory compliance
- Competitive advantage

## 📢 Call to Action

### For Organizations

1. **Start NOW** - Don't wait for quantum computers
2. **Cryptographic inventory** - Identify what needs protection
3. **Risk assessment** - Evaluate data sensitivity and lifetime
4. **Develop migration plan** - Create realistic timeline
5. **Allocate budget** - $1M-$10M+ for large enterprises
6. **Train staff** - Build internal expertise
7. **Pilot in new systems** - Hybrid mode deployment

### For Researchers

1. Work on practical challenges
2. Optimize implementations
3. Develop lightweight variants
4. Contribute to open-source projects

### For Policymakers

1. Mandate PQC for critical infrastructure
2. Provide funding for migration
3. Accelerate standards development
4. Raise public awareness

## 📝 Summary

### Key Takeaways

1. **QUANTUM THREAT IS REAL**
   - Shor's algorithm breaks RSA/ECC
   - 10-20 years away
   - "Harvest now, decrypt later" happening TODAY

2. **STANDARDS ARE HERE**
   - NIST FIPS 203, 204, 205 (August 2024)
   - Mandatory for federal systems
   - Industry following suit

3. **PERFORMANCE IS ACCEPTABLE**
   - Kyber competitive with ECDH
   - Dilithium 2-3x slower but acceptable
   - OptHQC shows 3.6x improvement

4. **APPLICATIONS ARE WIDESPREAD**
   - Critical infrastructure
   - Finance, healthcare, IoT
   - 5G/6G networks

5. **TOOLS ARE AVAILABLE**
   - liboqs is production-ready
   - Easy integration
   - Active community support

6. **READINESS IS LOW**
   - Only 23% have migration plans
   - Expertise shortage
   - Funding gaps

### Critical Message

**The quantum threat is coming. We have the tools. The question is WHEN, not IF.**

**The answer must be: NOW.**

*"The time to repair the roof is when the sun is shining."*

---

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution

- Additional algorithm implementations
- Performance optimization
- Documentation improvements
- Educational examples
- Real-world use cases
- Integration guides

## 🤝 Contributing

### Official Support Channels

**GitHub:**
- Issues: [github.com/open-quantum-safe/liboqs/issues](https://github.com/open-quantum-safe/liboqs/issues)
- Discussions: [github.com/open-quantum-safe/liboqs/discussions](https://github.com/open-quantum-safe/liboqs/discussions)
- Pull Requests: Active community contributions
- Response Time: Usually within 24-48 hours

**Documentation:**
- Main Docs: [openquantumsafe.org](https://openquantumsafe.org/)
- API Reference: [openquantumsafe.org/liboqs](https://openquantumsafe.org/liboqs/)
- Wiki: Comprehensive guides and tutorials

**Stack Overflow:**
- Tags: `[post-quantum-cryptography]`, `[liboqs]`
- Community: Growing PQC community
- Questions: 100+ related questions

### Community Statistics

- **Contributors**: 50+ active contributors
- **GitHub Stars**: 1,800+ (Top PQC library)
- **Monthly Downloads**: 50,000+
- **Academic Citations**: 200+ papers
- **Project Integrations**: 30+ projects using liboqs
- **Global Presence**: Worldwide developer community

## 👥 Community & Support

### Cloud Providers
- **Cloudflare**: Uses OQS for HTTPS experiments
- **AWS**: Testing PQC integration
- **Microsoft Azure**: Experiments with PQC

### Software Companies
- **Mozilla Firefox**: PQC testing
- **Google Chrome**: CECPQ experiments
- **Apple**: iOS/macOS security research

### Security Companies
- **Cisco**: Network equipment PQC
- **Fortinet**: Firewall PQC support
- **Palo Alto Networks**: Security appliances

### Academia
**Leading Universities:**
- MIT, Stanford, UC Berkeley
- KU Leuven, TU Eindhoven
- University of Waterloo (Institute for Quantum Computing)
- Used in research and teaching worldwide

### Government & Standards
- **NIST**: Reference implementation for PQC standardization
- **NSA**: Evaluation and testing
- **European Commission**: PQCRYPTO project
- Various national cybersecurity agencies

## 🏢 Industry Adoption

### vs. PQClean
- **liboqs**: More comprehensive, production-ready, optimized for performance
- **PQClean**: Focus on clean, portable, reference code
- **Use Case**: liboqs for deployment, PQClean for reference implementations

### vs. Bouncy Castle PQC
- **liboqs**: C library, performance-focused, native integration
- **Bouncy Castle**: Java/C#, easier JVM integration
- **Use Case**: Depends on language preference and ecosystem

### vs. OpenSSL PQC Fork
- **liboqs**: Standalone library, algorithm-focused, flexible
- **OpenSSL**: Full SSL/TLS stack integration
- **Use Case**: liboqs for flexibility, OpenSSL fork for protocol integration

### vs. libsodium
- **liboqs**: Post-quantum cryptography focused
- **libsodium**: Classical cryptography, extremely easy to use
- **Use Case**: Different purposes (PQC vs classical crypto)

### Industry Status
✅ **LEADING OPEN-SOURCE PQC LIBRARY**
- Most widely deployed open-source PQC library
- Industry standard for PQC research and integration
- Active development and maintenance
- Strong community support and contributions
- Used by Fortune 500 companies and government agencies

## 🔬 Comparison with Similar Tools

### liboqs Project
- **Website**: [openquantumsafe.org](https://openquantumsafe.org/)
- **GitHub**: [github.com/open-quantum-safe/liboqs](https://github.com/open-quantum-safe/liboqs)
- **Documentation**: [openquantumsafe.org/liboqs](https://openquantumsafe.org/liboqs/)
- **Wiki**: [github.com/open-quantum-safe/liboqs/wiki](https://github.com/open-quantum-safe/liboqs/wiki)

### Related OQS Projects
- **oqs-openssl**: OpenSSL with PQC support
- **oqs-openssh**: SSH with PQC support
- **oqs-provider**: OpenSSL 3.0 provider for PQC
- **oqs-demos**: Example applications and demonstrations

### Quantum Computing Frameworks
- **Cirq**: [quantumai.google/cirq](https://quantumai.google/cirq) - Google's quantum computing framework
- **Qiskit**: [qiskit.org](https://qiskit.org) - IBM's quantum computing framework

### Standards and Research
- **NIST PQC Project**: [csrc.nist.gov/projects/post-quantum-cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- **NIST Standards (2024)**:
  - **FIPS 203**: Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM / Kyber)
  - **FIPS 204**: Module-Lattice-Based Digital Signature Standard (ML-DSA / Dilithium)
  - **FIPS 205**: Stateless Hash-Based Digital Signature Standard (SLH-DSA / SPHINCS+)

### Academic Papers
- **Kyber**: Bos et al., "CRYSTALS-Kyber: A CCA-secure module-lattice-based KEM" (2018)
- **Dilithium**: Ducas et al., "CRYSTALS-Dilithium: Digital Signatures from Module Lattices" (2018)
- **SPHINCS+**: Bernstein et al., "SPHINCS+: Stateless Hash-Based Signatures" (2019)
- **Falcon**: Fouque et al., "Falcon: Fast-Fourier Lattice-based Compact Signatures" (2018)
- **Shor's Algorithm**: Peter Shor, "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer" (1994)

### Tutorials & Guides
- Getting Started Guide
- API Reference (Doxygen)
- Integration Examples
- Performance Tuning Guide
- Security Best Practices

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### License Features
- ✅ **Commercial Use**: Allowed
- ✅ **Modification**: Allowed  
- ✅ **Distribution**: Allowed
- ✅ **Private Use**: Allowed
- ✅ **No Cost**: Completely free to use

liboqs itself is also under the MIT License, making it suitable for both academic research and commercial deployment.

## 👤 Author

**Raghade Nawar**

- GitHub: [@7elmie](https://github.com/7elmie)
- Project: [EGQCC/PQC](https://github.com/7elmie/EGQCC)

## 🙏 Acknowledgments

- **Open Quantum Safe (OQS)** team for creating and maintaining liboqs
- **NIST** for Post-Quantum Cryptography standardization and competition
- **Google Quantum AI** team for Cirq framework
- **IBM Quantum** team for Qiskit framework
- **Dr. Mohamed Shahin** for supervision and guidance
- The global cryptography research community
- All contributors and users of this repository

## 📊 Project Statistics

- **Repository Stars**: 1,800+ (liboqs)
- **Contributors**: 50+ active developers
- **Monthly Downloads**: 50,000+
- **Academic Citations**: 200+ research papers
- **Supported Algorithms**: 45+ PQC algorithms
- **Industry Adoption**: Used by major tech companies and government agencies

## 📚 Current Research & Selected Papers

### Overview of Research Landscape

This repository tracks and analyzes cutting-edge PQC research across six key areas:

### Paper 1: NIST FIPS 203, 204, 205 (August 2024)

**Organization**: National Institute of Standards and Technology (NIST)

**Type**: Official Federal Standards

**Content:**
- FIPS 203: ML-KEM (Kyber)
- FIPS 204: ML-DSA (Dilithium)
- FIPS 205: SLH-DSA (SPHINCS+)

**Impact**: Mandatory for US government systems, sets global standards

**Applications**: Database encryption, backup security, secure communications

### Paper 2: Performance Benchmarks (MDPI, May 2025)

**Title**: "Practical Performance Benchmark Across Heterogeneous Environments"

**Type**: Empirical study

**Coverage**: All NIST winners + Round 4 candidates

**Platforms Tested**: x86-64, ARM, RISC-V, embedded systems

**Impact**: Provides real-world deployment data for practitioners

### Paper 3: Critical Infrastructure (IEEE IoT, June 2024)

**Title**: "Cybersecurity in Critical Infrastructures: PQC Perspective"

**Focus**: SCADA, power grid, water systems, transportation

**Content**: Real-time constraints, deployment case studies

**Impact**: Policy-shaping research for infrastructure security

### Paper 4: OpenRAN (arXiv, January 2025)

**Title**: "Introducing Post-Quantum Algorithms in OpenRAN Interfaces"

**Focus**: 5G/6G telecommunications

**Content**: Performance in real-time networks

**Impact**: Guidance for telecom industry deployment

### Paper 5: OptHQC (arXiv, December 2025) ⭐ Featured

**Title**: "OptHQC: Optimize HQC for High-Performance Post-Quantum Cryptography"

**Type**: Algorithm optimization research

**Achievement**: 3.6x speedup for HQC

**Significance**: Makes code-based crypto competitive with lattice-based schemes

[See detailed analysis below](#opthqc-detailed-analysis)

### Paper 6: Enterprise Readiness (arXiv, September 2025)

**Title**: "Are Enterprises Ready for Quantum-Safe Cybersecurity?"

**Type**: Survey of 500+ organizations

**Finding**: Only 23% have migration plans

**Impact**: Wake-up call for industry adoption

---

## 🔍 OptHQC: Detailed Analysis

### Paper Information

**Title**: OptHQC: Optimize HQC for High-Performance Post-Quantum Cryptography

**Source**: arXiv Preprint

**Publication Date**: December 15, 2025

**Type**: Algorithm Optimization

### Background: What is HQC?

**HQC** = Hamming Quasi-Cyclic Code
- Code-based Key Encapsulation Mechanism (KEM)
- NIST Round 4 candidate (still under evaluation)
- Based on error-correcting codes
- Alternative to lattice-based schemes

### Why Code-Based Cryptography Matters

#### 1. Mathematical Diversity
- **NOT** based on lattices (unlike Kyber, Dilithium)
- Different security assumptions
- Hedge against algorithm-specific attacks
- **"Don't put all eggs in one basket"**

#### 2. Historical Confidence
- McEliece (1978) – unbroken for 45+ years
- Decades of cryptanalysis
- Well-understood security
- Conservative choice for long-term protection

#### 3. Security Foundation
- Syndrome Decoding Problem (NP-complete)
- No known quantum algorithm
- Solid mathematical basis

### The Problem Before OptHQC

#### HQC Advantages:
- Smaller keys than Classic McEliece
- Quasi-cyclic structure = efficiency
- Moderate key/ciphertext sizes
- IND-CCA2 secure

#### HQC Problems:
- **MUCH slower** than Kyber
- Performance bottleneck
- Not competitive
- Limited real-world adoption

### Performance Gap - Original HQC vs Kyber

| Operation | Original HQC | Kyber-768 | Gap |
|-----------|-------------|-----------|-----|
| Key Generation | 245 μs | 68 μs | **3.6x slower** |
| Encapsulation | 189 μs | 70 μs | **2.7x slower** |
| Decapsulation | 298 μs | 98 μs | **3.0x slower** |

**Why This Matters:**
- Organizations choosing Kyber by default
- Code-based crypto seen as "too slow"
- Lack of cryptographic diversity
- **Risk**: All systems using same math (lattices)

### Specific Performance Bottlenecks

#### 1. Polynomial Multiplication
- Most expensive operation in HQC
- Naive approach: O(n²) complexity
- Takes 60-70% of total time
- n = 17,669 for HQC-128 (large!)

#### 2. Poor Memory Access Patterns
- Random memory access
- Cache misses
- Poor locality
- Memory bottleneck

#### 3. No SIMD Utilization
- Original: Scalar operations only
- Modern CPUs: AVX2 (256-bit), AVX-512 (512-bit)
- Not using available hardware
- Wasted potential

#### 4. Inefficient Data Structures
- Suboptimal polynomial representation
- Redundant conversions
- Extra memory copies
- Overhead

**Research Question**: Can we make HQC competitive with lattice-based schemes while maintaining code-based security and NIST compatibility?

### The Solution: OptHQC Optimization Framework

#### 1. Advanced Polynomial Multiplication

**Solution A - Adapted NTT:**
- Number Theoretic Transform adapted for HQC
- Custom prime selection
- Optimized butterfly operations
- Complexity: O(n log n) vs O(n²)
- **Result: 2.1x speedup**

**Solution B - Karatsuba Multiplication:**
- Divide-and-conquer approach
- O(n^1.585) complexity
- Better for some HQC parameters
- **Result: 1.8x speedup**

**Hybrid Strategy:**
- Karatsuba for smaller polynomials
- NTT for larger operations
- Automatic selection based on size
- Best of both worlds

#### 2. SIMD Vectorization

**AVX2 Implementation (256-bit):**
- Process 32 bytes in parallel
- Vectorized polynomial operations
- Bit-packing optimizations
- **Result: 2.8x speedup**

**AVX-512 Implementation (512-bit):**
- Process 64 bytes in parallel
- More parallelism
- Intel/AMD new CPUs
- **Result: 3.4x speedup**

**ARM NEON Implementation:**
- 128-bit SIMD for ARM
- Mobile/embedded optimization
- **Result: 2.2x speedup**

#### 3. Memory Optimization

**Cache-Friendly Layout:**
- Restructure polynomial storage
- Improve spatial locality
- Reduce cache misses by 60%
- **Result: 1.4x speedup**

**In-Place Operations:**
- Eliminate temporary buffers
- Reduce memory allocations
- Lower footprint 35-40%
- **Result: 1.3x speedup + memory savings**

**Prefetching:**
- Software prefetch instructions
- Anticipate memory patterns
- Hide memory latency
- **Result: 1.2x additional speedup**

#### 4. Algorithmic Improvements

**Reed-Solomon Decoding:**
- Key operation in decapsulation
- Optimized Berlekamp-Massey
- Fast polynomial evaluation
- **Result: 1.6x speedup**

**Sparse Polynomial Handling:**
- Many HQC polynomials are sparse
- Specialized multiplication
- Skip zero coefficients
- **Result: 1.5x speedup**

#### 5. Low-Level Optimizations

**Assembly Kernels:**
- Hand-optimized critical loops
- Perfect register allocation
- Minimal instructions
- **Result: 1.3x additional speedup**

**Compiler Optimizations:**
- -O3 optimization level
- Loop unrolling
- Function inlining
- Auto-vectorization hints

### Results & Achievements

#### Main Performance Improvement (Intel CPU)

**Original HQC-128**: 189 μs encapsulation
**OptHQC-128**: 52 μs encapsulation

🎉 **SPEEDUP: 3.6x FASTER!**

#### Key Comparison

| Algorithm | Speed (μs) | Ranking |
|-----------|-----------|---------|
| Kyber-512 | 45 | 🥇 Fastest |
| **OptHQC-128** | 52 | 🥈 **COMPETITIVE!** |
| Kyber-768 | 70 | 🥉 3rd |
| Original HQC-128 | 189 | ❌ Too slow |

**BREAKTHROUGH**: OptHQC now competitive with Kyber!

#### Cross-Platform Results

- **AMD CPUs**: OptHQC **FASTER** than Kyber! (49 vs 68 μs)
- **Intel AVX-512**: OptHQC **FASTER** than Kyber! (38 vs 42 μs)
- **ARM**: Acceptable (580 vs 450 μs)

#### Memory Savings

- **Original**: 42 KB peak memory
- **OptHQC**: 27 KB peak memory
- **Reduction**: 36% less memory

#### Optimization Breakdown

1. NTT polynomial multiplication → 2.1x speedup
2. SIMD vectorization (AVX2/AVX-512) → 2.8-3.4x speedup
3. Cache optimization → 1.4x speedup
4. Algorithm improvements → 1.6x speedup

**Combined**: **3.6x total speedup**

### Key Achievements

✅ **1. CODE-BASED CRYPTO IS NOW FAST ENOUGH**
- OptHQC competitive with Kyber
- No longer "too slow" excuse
- Ready for real-world deployment

✅ **2. CRYPTOGRAPHIC DIVERSITY IS POSSIBLE**
- Deploy Kyber (lattice) + OptHQC (code-based)
- Protection if one family breaks
- Different math = better security

⚡ **3. BEST ON AMD/INTEL AVX-512**
- Actually FASTER than Kyber on some platforms
- Platform-specific optimization matters

💾 **4. MEMORY EFFICIENT**
- 36% less memory
- Better for embedded systems

### When to Use Each Algorithm

#### Use OptHQC When:
✓ AMD or Intel AVX-512 systems
✓ Need cryptographic diversity
✓ Can handle 2-4 KB keys
✓ Want code-based security

#### Use Kyber When:
✓ Smallest keys needed
✓ Already NIST standard
✓ Limited memory devices

#### Use Classic McEliece When:
✓ Ultra-conservative security
✓ 45+ years confidence
✓ Can tolerate 1+ MB keys
✓ Maximum security priority

### Impact on NIST Round 4

- Strengthens case for code-based standard
- Shows performance parity is achievable
- Diversification now practical

**CONCLUSION**: Code-based crypto is NO LONGER slow. Time to diversify!

### Future Work

**Potential Improvements:**
- Hardware acceleration (FPGA, ASIC)
- GPU implementation (parallel)
- Quantum instruction sets (future CPUs)
- Algorithm-specific hardware

**Research Directions:**
- Apply to other code-based (BIKE, McEliece)
- Hybrid multiplication strategies
- CPU-specific microarchitecture tuning
- Memory-hard variants

### Tools & Data Used

**Tools:**
- SUPERCOP benchmarking framework
- GCC/Clang compilers with optimizations
- Intel VTune for profiling
- Valgrind for memory analysis
- Custom benchmarking suite

**Data Details:**
- Testing platforms: 10+ different CPUs
- Test runs: 10,000+ iterations per measurement
- Statistical analysis: Mean + standard deviation
- Reproducibility: Code available on GitHub

**Analysis Techniques:**
- Polynomial multiplication timing breakdown
- Cache miss rate analysis
- SIMD instruction utilization
- Memory bandwidth measurements
- Power consumption profiling

**Key Quote**: "OptHQC demonstrates that code-based cryptography can achieve performance comparable to lattice-based schemes through systematic optimization. This opens the door for practical deployment of cryptographically diverse post-quantum systems."

**FINAL RECOMMENDATION**: Organizations should deploy BOTH lattice-based (Kyber) and code-based (OptHQC) algorithms to maximize security against unknown future attacks. Code-based crypto is NO LONGER too slow. It's time to diversify!

---

## 📞 Support

If you have questions or need help:

1. Check the [documentation](docs/)
2. Open an [issue](https://github.com/7elmie/EGQCC/issues)
3. Review existing [discussions](https://github.com/7elmie/EGQCC/discussions)

---

**⚠️ Important Note**: This repository is for research and educational purposes. For production deployments, ensure proper security audits and follow your organization's security policies.

**🔮 The Future is Post-Quantum**: Start your migration today. The quantum threat is real, and the tools are ready.

---

*Last Updated: January 2026*
