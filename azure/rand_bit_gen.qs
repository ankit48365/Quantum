// operation Main(): Unit{  // To define an operation that does not return a value, use the Unit type.

//     use q = Qubit();
//     H(q);
//     let result = M(q);
// }

operation Main(): Result{ // To define an operation that returns a measurement result, use the operation keyword followed by the operation name and return type.

    use q = Qubit(); // To allocate a qubit, use the Qubit operation and store the qubit in the q variable.
    H(q); // To set the qubit in superposition, apply a Hadamard transformation. hadamard gate is used to create superposition.
    let result = M(q); // To measure the qubit value, use the M operation and store the measurement value in the result variable.
    Reset(q); // To reset the qubit, use the Reset operation.
    return result; // To return the measurement result, use the return statement.
}