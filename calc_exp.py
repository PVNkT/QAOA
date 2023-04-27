from qiskit.opflow.expectations import PauliExpectation
from qiskit.opflow.state_fns import StateFn
from qiskit.opflow.converters import CircuitSampler
from qiskit import QuantumCircuit, Aer
from qiskit.opflow import CircuitOp, CircuitStateFn

class expectation:
    def __init__(self, op, circuit_state) -> None:
        # 주어진 operator와 양자 상태를 저장
        self.op = op
        self.circuit_state = circuit_state
        
    def calc_exp(self, parameter):
        # 양자 상태에 parameter를 적용하여 값을 얻음 
        circuit_state = self.circuit_state(parameter)
        # qiskit에서 expectation을 계산하는 형태로 전환    
        measureable_expression = StateFn(self.op, is_measurement=True).compose(circuit_state)
        expectation = PauliExpectation().convert(measureable_expression)
        # 계산에 사용할 simulator
        simulator = Aer.get_backend('aer_simulator')
        # expectation에 대한 sampling을 진행
        sampler = CircuitSampler(simulator).convert(expectation)
        # 계산된 expectation 값에서 실수 값만을 반환 (Hamiltonian은 Hermition이기 때문에 허수부는 0이 된다.)
        return sampler.eval().real








if __name__ == '__main__':
    circuit = QuantumCircuit(2)
    circuit.z(0)
    circuit.z(1)
    op = CircuitOp(circuit)
    psi = QuantumCircuit(2)
    psi.x(0)
    psi.x(1)
    psi = CircuitStateFn(psi)
    




