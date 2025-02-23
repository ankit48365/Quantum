//  In this unit, you'll create quantum superposition and dive into probabilities with Q# by using the DumpMachine function. 
// The DumpMachine function dumps information about the current status of the quantum system at the point where it's called.

//  Below is  simple program that generates a random bit using a qubit in superposition. 
// You'll use the DumpMachine function to see the state of the qubit at different points in the program.
//  https://learn.microsoft.com/en-us/training/modules/explore-superposition/5-explore-superposition-qsharp

import Microsoft.Quantum.Diagnostics.*;

operation Main() : Result {
    use q = Qubit();
    Message("Initialized qubit:");
    DumpMachine(); // First dump
    Message(" ");
    H(q);
    Message("Qubit after applying H:");
    DumpMachine(); // Second dump
    Message(" ");
    let randomBit = M(q); // Measure the qubit
    Message("Qubit after the 1st measurement:");
    DumpMachine(); // Third dump
    Message(" ");

    // let randomBit = M(q); // Measure the qubit
    Message("Qubit after the 2nd measurement:");
    DumpMachine(); // Third dump
    Message(" ");

    let randomBit = M(q); // Measure the qubit
    Message("Qubit after the 3rd measurement:");
    DumpMachine(); // Third dump
    Message(" ");

    Reset(q);
    Message("Qubit after resetting:");
    DumpMachine(); // Fourth dump
    Message(" ");
    return randomBit;
}