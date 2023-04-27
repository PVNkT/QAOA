import qiskit
from qiskit import QuantumCircuit
from qiskit.opflow import CircuitStateFn
import numpy as np

class variational_circuit():

    def __init__(self, graph) -> None:
        # graph로 부터 node와 edge의 정보를 저장
        self.graph = graph.graph
        self.nodes = list(self.graph.nodes)
        self.edges = list(self.graph.edges)

    def state(self, parameter):
        # 만든 회로를 CircuitStateFn 형태로 바꿈
        # qiskit의 expectation 계산을 위해 형태를 바꿈
        qc = self.get_circuit(parameter)       
        return CircuitStateFn(qc)

    def get_circuit(self, parameter):
        # parameter들을 gamma와 beta로 다시 나눔
        gammas = parameter[:len(parameter)//2]
        betas = parameter[len(parameter)//2:]
        # 회로를 반복할 횟수
        p = len(gammas)
        # 주어진 크기의 양자 회로를 만듬
        qc = QuantumCircuit(len(self.nodes))
        # 모든 qubit에 Hadamard gate를 걸어 중첩 상태를 만든다.
        qc.h(range(len(self.nodes)))
        qc.barrier()
        # 반복 횟수만큼 지정된 형태의 unitary들을 적용함
        for i in range(p):
            for edge in self.edges:
                # 각 edge들에 대해서 problem Hamiltonian에 해당되는 unitary를 적용
                qc = self.problem_part(qc, edge, self.get_weight(edge)*gammas[i])
            qc.barrier()
            for node in self.nodes:
                # 각 node들에 대해서 mixing Hamiltonian에 해당되는 unitary를 적용
                qc = self.mixing_part(qc, node, betas[i])
        return qc

    def problem_part(self, qc:QuantumCircuit, qubits:tuple, gamma:float):
        # problem Hamiltonian에 대응하는 unitary를 주어진 qubit에 적용
        qc.cx(*qubits)
        qc.rz(gamma, qubits[1])
        qc.cx(*qubits)
        qc.barrier(*qubits)
        return qc

    def mixing_part(self, qc:QuantumCircuit, qubit, beta:float):
        # mixing Hamiltonian에 대응되는 unitary를 주어진 qubit에 적용
        qc.rx(beta, qubit)
        return qc

    def get_weight(self, edge):
        edge_weight = self.graph.get_edge_data(*edge)['weight']
        return edge_weight


















