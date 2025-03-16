# first understrand, if we have a binary value [0011] then:
# it has four digits then the value is (0.2^3) + (0.2^2) + (1.2^1) + (1.2^0) 
#  = 0.8 + 0.4 + 1.2 + 1.1 = 0+0+2+1 = 3 (here . is multiply symbol)
# so decimal 3 is equal to binary 0011

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram, circuit_drawer
from qiskit_aer import AerSimulator

# Function to set number in quantum register

# qc: Your QuantumCircuit object.
# register: a (a QuantumRegister with 3 qubits: a[0], a[1], a[2]).
# number: 2 (from a_input = 2). this will keep changing with user input.
# num_qubits: 3 (since a has 3 qubits).

def set_number(qc, register, number, num_qubits):
    binary = bin(number)[2:].zfill(num_qubits)  #binary of 2(e.g.) is ob10, where ob just tells its binary and 10 is the binary value for 10, this here we get rid of prefix 0b ~ [2:] removes '0b' prefix and zfill(4) pads it to 4 digits with leading zeros: "0010"
    for i in range(num_qubits):
        if binary[num_qubits - 1 - i] == '1': # Reverse order for qubit indexing
            qc.x(register[i])

# Get user input
try:
    a_input = int(input("Enter the first number (0–4): "))
    b_input = int(input("Enter the second number (0–4): "))
    if not (0 <= a_input <= 4 and 0 <= b_input <= 4):
        raise ValueError("Numbers must be between 0 and 4.")
except ValueError as e:
    print(f"Invalid input: {e}. Please enter integers between 0 and 4.")
    exit()

# Classical Bits
# A classical bit is the smallest unit of information in a regular computer. It can be either 0 or 1.
# With multiple bits, you can represent larger numbers in binary. For example:
# 1 bit: 0 or 1 (2 possible values).
# 2 bits: 00, 01, 10, 11 (4 possible values, 0–3 in decimal).
# 3 bits: 000, 001, 010, 011, 100, 101, 110, 111 (8 values, 0–7).
# 4 bits: 0000 to 1111 (16 values, 0–15).

# Define quantum and classical registers
# The QuantumRegister class in Qiskit can accept up to 3 arguments, but typically you’ll see 1 or 2 in practice. Here’s the full signature from Qiskit’s documentation (as of my knowledge up to March 2025):
# syntax: QuantumRegister(size, name=None, bits=None)

a = QuantumRegister(3, 'a')  # Input A (3 qubits, max 7, using 0–4) # 3 qubits: 2^3=8 values (0 to 7, i.e., 000 to 111).
b = QuantumRegister(3, 'b')  # Input B (3 qubits, max 7, using 0–4)
s = QuantumRegister(3, 's')  # Sum (3 qubits, max 7, fits 0–8)
c = ClassicalRegister(3, 'c')  # Classical register for sum

# Create the quantum circuit
# The QuantumCircuit class is highly flexible and can accept various combinations of arguments. Its full signature (based on Qiskit documentation up to March 2025) is:
# QuantumCircuit(*regs, name=None, global_phase=0, metadata=None)

qc = QuantumCircuit(a, b, s, c)

# Set user inputs
set_number(qc, a, a_input, 3)
set_number(qc, b, b_input, 3)

# Simplified quantum adder (no carry beyond 3 bits)
for i in range(3):
    qc.cx(a[i], s[i])  # Add A to S
    qc.cx(b[i], s[i])  # Add B to S
    if i < 2:  # Carry only up to s[2]
        qc.ccx(a[i], b[i], s[i+1])  # Carry to next bit

# Measure the sum
qc.measure(s, c)

# Visualize the circuit
print("Quantum Circuit Diagram:")
print(qc.draw(output='text'))

# Simulate the circuit
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

# Convert to decimal
decimal_result = int(list(counts.keys())[0], 2)

print("\nMeasurement Results (Binary):")
print(counts)
print(f"Decimal Result: {decimal_result}")