from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np


def quantum():
    qr = QuantumRegister(2, 'qbit')
    cr = ClassicalRegister(2, 'cbit')
    qc = QuantumCircuit(qr, cr)

    qc.h(0)
    qc.cx(0,1)
    qc.h(0)

    qc.measure(range(2), range(2))
    backend = AerSimulator()
    job = backend.run(qc, shots=1)
    result = job.result().get_counts()
    if '01' in result or '11' in result:
        return True
    return False

print(quantum())
