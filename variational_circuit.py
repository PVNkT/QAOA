import qiskit
from qiskit import QuantumCircuit
from qiskit.opflow import CircuitStateFn
import numpy as np

class variational_circuit():

    def __init__(self, graph) -> None:
        self.nodes = list(graph.nodes)
        self.edges = list(graph.edges)

    def state(self, parameter):
        qc = self.get_circuit(parameter)       
        return CircuitStateFn(qc)

    def get_circuit(self, parameter):
        gammas = parameter[:len(parameter)//2]
        betas = parameter[len(parameter)//2:]
        p = len(gammas)
        qc = QuantumCircuit(len(self.nodes))
        qc.h(range(len(self.nodes)))
        qc.barrier()
        for i in range(p):
            for edge in self.edges:
                qc = self.problem_part(qc, edge[0:2], gammas[i])
        qc.barrier()
        for i in range(p):
            for node in self.nodes:
                qc = self.mixing_part(qc, node, betas[i])
        return qc

    def problem_part(self, qc:QuantumCircuit, qubits:tuple, gamma:float):
        qc.cx(*qubits)
        qc.rz(gamma, qubits[1])
        qc.cx(*qubits)
        return qc

    def mixing_part(self, qc:QuantumCircuit, qubit, beta:float):
        if type(qubit) == tuple:
            qubit = qubit[0]
        qc.rx(beta, qubit)
        return qc

















