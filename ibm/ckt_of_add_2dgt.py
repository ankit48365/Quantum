# first understrand, if we have a binary value 0011 then:
# it has four digits then the value is (0.2^3) + (0.2^2) + (1.2^1) + (1.2^0) 
#  = 0.8 + 0.4 + 1.2 + 1.1 = 0+0+2+1 = 3 (here . is multiply symbol)
# so decimal 3 is equal to binary 0011

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram, circuit_drawer
from qiskit_aer import AerSimulator

# Function to convert decimal to binary and set qubits
def set_number(qc, register, number, num_qubits):
    # qc: Your QuantumCircuit object.
    # register: a (a QuantumRegister with 4 qubits: a[0], a[1], a[2], a[3]).
    # number: 2 (from a_input = 2).
    # num_qubits: 4 (since a has 4 qubits).
    
    # Convert number to binary string, padded to num_qubits length
    binary = bin(number)[2:].zfill(num_qubits)  #binary of 2(e.g.) is ob10, where ob just tells its binary and 10 is the binary value for 10, this here we get rid of prefix 0b ~ [2:] removes '0b' prefix and zfill(4) pads it to 4 digits with leading zeros: "0010"
    # Apply X gates based on binary representation
    for i in range(num_qubits):
        if binary[num_qubits - 1 - i] == '1':  # Reverse order for qubit indexing
            qc.x(register[i])

# Get user input
try:
    a_input = int(input("Enter the first number (0-9): "))
    b_input = int(input("Enter the second number (0-9): "))
    
    # Validate input (since we're using 4 qubits, max value is 15)
    if not (0 <= a_input <= 10 and 0 <= b_input <= 10):
        raise ValueError("Numbers must be between 0 and 10.")
except ValueError as e:
    print(f"Invalid input: {e}. Please enter integers between 0 and 10.")
    exit()


# Classical Bits
# A classical bit is the smallest unit of information in a regular computer. It can be either 0 or 1.
# With multiple bits, you can represent larger numbers in binary. For example:
# 1 bit: 0 or 1 (2 possible values).
# 2 bits: 00, 01, 10, 11 (4 possible values, 0–3 in decimal).
# 3 bits: 000, 001, 010, 011, 100, 101, 110, 111 (8 values, 0–7).
# 4 bits: 0000 to 1111 (16 values, 0–15).

# for our problem we have to only accept values between (0~9) , The number of possible values is 2^4 = 16, so you get 0 to 15.
# Define quantum and classical registers

a = QuantumRegister(4, 'a')  # Input A (4 qubits = max 15)
b = QuantumRegister(4, 'b')  # Input B (4 qubits = max 15)
s = QuantumRegister(5, 's')  # Sum (4 bits + 1 carry bit)
c = ClassicalRegister(5, 'c')  # Classical register to measure the sum

# Create the quantum circuit
qc = QuantumCircuit(a, b, s, c)

# Set user inputs into the quantum registers
set_number(qc, a, a_input, 4)  # Set A based on user input
set_number(qc, b, b_input, 4)  # Set B based on user input

# Quantum ripple-carry adder
for i in range(4):
    qc.ccx(a[i], b[i], s[i+1])  # Toffoli gate for carry
    qc.cx(a[i], s[i])           # CNOT for partial sum
    qc.cx(b[i], s[i])           # CNOT for partial sum

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