from qiskit import *
from qiskit.quantum_info import Operator, Statevector
import numpy as np
import matplotlib.pyplot as plt

# //ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
ARRAY_Z = np.array([[1,0],
                    [0,-1]])
ARRAY_I = np.array([[1,0],
                   [0,1]])

# //ーーーーーーーーーーーーーーーーーーーーー
def get_observable_magnetization(num_qubits):
    obs = np.zeros((2**num_qubits, 2**num_qubits))
    for i in range(num_qubits):
        operators = [ARRAY_I] * num_qubits
        operators[i] = ARRAY_Z
        # テンソル積を計算
        term = operators[0]
        for op in operators[1:]:
            term = np.kron(term, op)
        obs += term
    obs /= num_qubits
    return obs