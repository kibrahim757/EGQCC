import numpy as np

def simulate_bb84(num_bits=100, eavesdropped=False):
    print(f"--- Starting BB84 Simulation ({'With' if eavesdropped else 'Without'} Eve) ---")
    
    # 1. Alice generates random bits and random bases
    alice_bits = np.random.randint(2, size=num_bits)
    alice_bases = np.random.randint(2, size=num_bits) # 0: Rectilinear (+), 1: Diagonal (x)
    
    # 2. Transmission (Eve's interference)
    bob_bases = np.random.randint(2, size=num_bits)
    if eavesdropped:
        eve_bases = np.random.randint(2, size=num_bits)
        # Eve measures the qubits, changing their states
        intercepted_bits = []
        for i in range(num_bits):
            # If Eve chooses the same basis as Alice, she gets the right bit
            # If not, she randomizes the bit for Bob
            if eve_bases[i] == alice_bases[i]:
                intercepted_bits.append(alice_bits[i])
            else:
                intercepted_bits.append(np.random.randint(2))
        transmitted_bits = intercepted_bits
    else:
        transmitted_bits = alice_bits

    # 3. Bob measures the received bits
    bob_bits = []
    for i in range(num_bits):
        if bob_bases[i] == alice_bases[i]:
            bob_bits.append(transmitted_bits[i])
        else:
            bob_bits.append(np.random.randint(2))

    # 4. Sifting Phase (Alice and Bob compare bases)
    sifted_key_alice = []
    sifted_key_bob = []
    for i in range(num_bits):
        if alice_bases[i] == bob_bases[i]:
            sifted_key_alice.append(alice_bits[i])
            sifted_key_bob.append(bob_bits[i])

    # 5. Error Rate Calculation (QBER)
    errors = sum(a != b for a, b in zip(sifted_key_alice, sifted_key_bob))
    qber = (errors / len(sifted_key_alice)) * 100 if len(sifted_key_alice) > 0 else 0

    print(f"Sifted Key Length: {len(sifted_key_alice)}")
    print(f"Quantum Bit Error Rate (QBER): {qber:.2f}%")
    
    if qber > 11.0: # Standard threshold for detecting an eavesdropper
        print("ALERT: High QBER detected! Potential eavesdropper (Eve) present.")
    else:
        print("SECURE: Low QBER. Key is safe to use.")
    
    return sifted_key_bob

# Run simulation twice to show the difference
if __name__ == "__main__":
    # Case 1: Secure Channel
    simulate_bb84(num_bits=100, eavesdropped=False)
    print("\n" + "="*40 + "\n")
    # Case 2: Eavesdropped Channel
    simulate_bb84(num_bits=100, eavesdropped=True)