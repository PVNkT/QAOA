from qiskit.opflow.expectations import PauliExpectation
from qiskit.opflow.state_fns import StateFn
from qiskit.opflow.converters import CircuitSampler
from qiskit import QuantumCircuit, Aer
from qiskit.opflow import CircuitOp, CircuitStateFn

class expectation:
    def __init__(self, op, circuit_state) -> None:
        self.op = op
        self.circuit_state = circuit_state
        
    def calc_exp(self, parameter):
        circuit_state = self.circuit_state(parameter)    
        measureable_expression = StateFn(self.op, is_measurement=True).compose(circuit_state)
        expectation = PauliExpectation().convert(measureable_expression)
        simulator = Aer.get_backend('aer_simulator')
        sampler = CircuitSampler(simulator).convert(expectation)
        print(sampler.eval())
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
    




