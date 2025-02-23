// https://learn.microsoft.com/en-us/training/modules/explore-entanglement/3-create-entanglement-qsharp
import Microsoft.Quantum.Diagnostics.*; // Aka Std.Diagnostics.*;


// Create the Bell state {|phi+⟩}

// operation Main() : (Result, Result) {
//     use (q1, q2) = (Qubit(), Qubit()); 

//     H(q1); 
//     CNOT(q1, q2); // Entangle qubits q1 and q2 

//     DumpMachine();

//     let (m1, m2) = (M(q1), M(q2));
//     Reset(q1);
//     Reset(q2);

//     return (m1, m2);
// }

// Create the Bell state {|phi-⟩}

// operation Main() : (Result, Result) {
//     use (q1, q2) = (Qubit(), Qubit());

//     H(q1);
//     Z(q1); // Apply the Pauli Z operation to the control qubit
//     CNOT(q1, q2);

//     DumpMachine();

//     let (m1, m2) = (M(q1), M(q2));
//     Reset(q1);
//     Reset(q2);

//     return (m1, m2);
// }

// Create the Bell state {|psi+⟩}

// operation Main() : (Result, Result) {
//     use (q1, q2) = (Qubit(), Qubit());
//     H(q1);
//     Z(q1); // Apply the Pauli Z operation to the control qubit
//     CNOT(q1, q2);
//     X(q1); // Apply the Pauli X operation to the control qubit

//     DumpMachine();

//     let (m1, m2) = (M(q1), M(q2));
//     Reset(q1);
//     Reset(q2);

//     return (m1, m2);
// }


// Create the Bell state {|psi-⟩}

operation Main() : (Result, Result) {
    use (q1, q2) = (Qubit(), Qubit());
    H(q1);
    Z(q1); // Apply the Pauli Z operation to the control qubit
    CNOT(q1, q2);
    X(q1); // Apply the Pauli X operation to the control qubit
    Z(q1); // Apply the Pauli Z operation to the control qubit

    DumpMachine();

    let (m1, m2) = (M(q1), M(q2));
    Reset(q1);
    Reset(q2);

    return (m1, m2);
}