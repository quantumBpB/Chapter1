# 1. Create the quantum circuit
qc = QuantumCircuit(5, 1)  # 3 data qubits + 2 ancillas for syndrome detection

# Label: qubit 0 = original qubit
#        qubits 1 & 2 = encoding qubits
#        qubits 3 & 4 = ancilla qubits for error detection

# 2. Encode |+⟩ state into 3 qubits
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)

# 3. Introduce a bit-flip (X) error on one qubit (simulate noise)
qc.x(1)  # Try changing this to 0, 1, or 2

# 4. Syndrome measurement using ancilla qubits
qc.cx(0, 3)
qc.cx(1, 3)
qc.cx(1, 4)
qc.cx(2, 4)

# 5. Measure ancilla qubits (optional if just correcting)
qc.measure_all()

# 6. Run the simulation
sim = Aer.get_backend('aer_simulator')
qc = qc.decompose()  # Optional: show details
result = execute(qc, sim, shots=1024).result()
counts = result.get_counts()

# 7. Show the results
plot_histogram(counts)
qc.draw('mpl')
