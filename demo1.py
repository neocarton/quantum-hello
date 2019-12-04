# https://qiskit.org/documentation/getting_started.html

from qiskit import (QuantumRegister, ClassicalRegister, QuantumCircuit)
from qcomp import (qexec)

# Task: Qubit |0>
qr = QuantumRegister(1) # Initailly = |0>
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Qubit |1>
qr = QuantumRegister(1) # Initailly = |0>
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr) # Not(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Qubit |01>
qr = QuantumRegister(2) # Initailly = |0>
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[0]) # Not(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Qubit |10>
qr = QuantumRegister(2) # Initailly = |0>
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[1]) # Not(qr)
circuit.measure(qr, cr)
qexec(circuit)