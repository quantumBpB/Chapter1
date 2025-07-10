from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create the circuit
qc = QuantumCircuit(5, 5)

qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.x(1)

qc.cx(0, 3)
qc.cx(1, 3)
qc.cx(1, 4)
qc.cx(2, 4)

qc.measure(range(5), range(5))

# Run simulation
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

# Plot histogram and circuit diagram
hist = plot_histogram(counts)

# This makes the histogram visible in Jupyter
hist
hist.savefig("histogram.png")
print("hist created")
# Draw the circuit as the last cell output
circuit_diagram = qc.draw('mpl')
circuit_diagram.savefig("circuit_diagram.png")
print("circuit created")