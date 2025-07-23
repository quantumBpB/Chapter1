from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, Aer, execute

# Registers
q = QuantumRegister(3)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

# Step 1: Prepare |ψ⟩ on q[0]
qc.h(0)
qc.rz(1.0, 0)  # Arbitrary state

# Step 2: Create Bell pair between q[1] and q[2]
qc.h(1)
qc.cx(1, 2)

# Step 3: Entangle q[0] with Bell pair
qc.cx(0, 1)
qc.h(0)

# Step 4: Measure q[0] and q[1]
qc.measure(0, 0)
qc.measure(1, 1)

# Step 5: Conditional operations on q[2]
qc.x(2).c_if(c, 1)
qc.z(2).c_if(c, 2)
qc.x(2).c_if(c, 3)
qc.z(2).c_if(c, 3)

qc.draw('mpl')
