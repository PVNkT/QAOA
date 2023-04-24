from make_graph import network_graph
from Hamiltonian import Hamiltonian
from variational_circuit import variational_circuit
from calc_exp import expectation
from optimization import opimization
from result import get_answer
import numpy as np


def main():
    nodes = [0, 1, 2, 3, 4]
    edges = [(0,1), (1,2), (2,3), (3,4), (1,0), (2,3)]
    gammas = np.array([1.9])
    betas = np.array([0.2])  
    init_para = np.concatenate([gammas, betas])
    
    graph = network_graph(nodes, edges).graph
    H = Hamiltonian(graph).H
    psi = variational_circuit(graph)
    state = psi.state
    exp = expectation(H, state).calc_exp
    opt_result = opimization(exp, init_para).scipy_min('COBYLA')
    # Print the optimization results
    opt_para = opt_result.x
    print(opt_para)
    print("Optimized objective function value:", opt_result.fun)
    circuit = psi.get_circuit(opt_para)
    circuit.draw('mpl').savefig('result/circuit/circuit.png')
    result = get_answer(circuit)
    return result











if __name__ == '__main__':
    main()


