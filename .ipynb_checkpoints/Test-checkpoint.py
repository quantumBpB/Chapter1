from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, DensityMatrix, partial_trace
from qiskit.visualization.bloch import Bloch
import matplotlib.pyplot as plt
import numpy as np

# Helper: Calculate Bloch vector from 2x2 density matrix
def get_bloch_vector(dm):
    x = 2 * np.real(dm[0, 1])
    y = 2 * np.imag(dm[1, 0])
    z = np.real(dm[0, 0] - dm[1, 1])
    return [x, y, z]

# Helper: Plot 1 Bloch sphere per figure (older Qiskit compatibility)
def plot_bloch_spheres(state, title_prefix):
    for i in range(4):
        reduced_dm = partial_trace(DensityMatrix(state), [j for j in range(4) if j != i]).data
        bloch_vec = get_bloch_vector(reduced_dm)
        b = Bloch()
        b.add_vectors(bloch_vec)
        b.title = f"{title_prefix} Qubit {i}"
        b.render()
        b.save("ERR.jpg")

# Step 1: Initial state (|0000>)
qc = QuantumCircuit(4)
initial_sv = Statevector.from_instruction(qc)

# Step 2: Bloch before Hadamard
plot_bloch_spheres(initial_sv, "Before")

# Step 3: Apply Hadamard to all qubits
for i in range(4):
    qc.h(i)

# Step 4: Final state
final_sv = Statevector.from_instruction(qc)

# Step 5: Bloch after Hadamard
plot_bloch_spheres(final_sv, "After")

