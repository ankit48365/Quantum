namespace QuantumAdder {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation HalfAdder(a : Qubit, b : Qubit, sum : Qubit, carry : Qubit) : Unit {
        body (...) {
            CNOT(a, sum);
            CNOT(b, sum);
            CCNOT(a, b, carry);
        }
    }

    @EntryPoint()
    operation Main() : Unit {
        using (register = Qubit[4]) {
            let a = register[0];
            let b = register[1];
            let sum = register[2];
            let carry = register[3];

            // Prepare the initial state (set a and b to 1 for testing)
            X(a);
            X(b);

            // Perform the half-adder operation
            HalfAdder(a, b, sum, carry);

            // Measure the sum and carry
            let resultSum = M(sum);
            let resultCarry = M(carry);

            Message($"The sum is {resultSum}");
            Message($"The carry is {resultCarry}");

            // Reset the qubits
            if (resultSum == One) {
                X(sum);
            }
            if (resultCarry == One) {
                X(carry);
            }
        }
    }
}
