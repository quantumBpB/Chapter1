# Import libraries
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a single-qubit quantum circuit
qc = QuantumCircuit(1, 1)

# Step 1: Start in |0⟩
# Step 2: Apply Hadamard gate to create superposition
qc.h(0)

# Optional: Add measurement to see probabilities
qc.measure(0, 0)

# Use simulator
simulator = AerSimulator()

# Execute circuit
job = simulator.run(qc, shots=1024)
result = job.result()

# Get measurement counts
counts = result.get_counts(qc)
print("Measurement counts:", counts)

# Plot histogram
hist = plot_histogram(counts)
hist.savefig("3.1.png")
circuit_diagram = qc.draw('mpl')
circuit_diagram.savefig("3.2.png")
