from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import circuit_drawer

# Define a quantum circuit with 4 qubits (including a carry qubit) and 4 classical bits
qc = QuantumCircuit(4, 4)

# Example: Adding binary numbers 1 (|01⟩) and 1 (|01⟩)

# Initialize the input qubits
qc.x(0)  # Set |01⟩ for the first number
qc.x(2)  # Set |01⟩ for the second number

# Apply CNOT gate for addition
qc.cx(0, 3)  # CNOT gate on qubit 0 with target qubit 3 (sum)
qc.cx(2, 3)  # CNOT gate on qubit 2 with target qubit 3 (sum)

# Apply Toffoli gate for carry
qc.ccx(0, 2, 1)  # Toffoli gate with control qubits 0, 2, and target qubit 1 (carry)

# Measure the result
qc.measure([3, 1], [0, 1])  # Measure sum and carry qubits into classical bits

# Visualize the circuit
qc.draw(output='mpl')

# Use the Aer simulator
simulator = Aer.get_backend('qasm_simulator')

# Transpile the circuit for the simulator
qc = transpile(qc, simulator)

# Assemble the circuit into a Qobj
qobj = assemble(qc)

# Execute the circuit
result = execute(qc, backend=simulator).result()

# Get the result counts
counts = result.get_counts(qc)
print(counts)

# Plot the result
plot_histogram(counts)


