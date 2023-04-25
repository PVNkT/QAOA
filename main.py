from make_graph import network_graph
from Hamiltonian import Hamiltonian
from variational_circuit import variational_circuit
from calc_exp import expectation
from optimization import opimization
from result import get_answer
import numpy as np


def main():
    # graph의 node를 설정
    nodes = [0, 1, 2, 3, 4]
    # graph의 edge를 설정
    edges = [(0,1,1.0),(0,2,1.0),(1,2,1.0),(3,2,1.0),(3,4,1.0),(4,2,1.0)]
    # 초기 parameter를 설정, 값들의 길이가 반복 횟수 p에 해당된다.
    gammas = np.array([1.9, 1])
    betas = np.array([0.2, 0])  
    init_para = np.concatenate([gammas, betas])
    
    # node와 edge를 기반으로 graph를 만든다.
    graph = network_graph(nodes, edges).graph
    # 그래프를 기반으로 대응되는 Hamiltonian을 계산
    H = Hamiltonian(graph).H
    # 그래프를 기반으로 대응되는 parameter로 표현된 양자 상태의 회로를 만든다.
    psi = variational_circuit(graph)
    state = psi.state
    # Hamiltonian과 variational state를 기반으로 기댓값을 계산한다.
    # parameter가 주어지면 그에 대응되는 expectation을 주는 함수
    exp = expectation(H, state).calc_exp
    # 주어진 optimizing 방법을 통해서 optimizing을 진행
    opt_result = opimization(exp, init_para).scipy_min('COBYLA')
    # Print the optimization results
    # 최적화된 parameter를 불러온다.
    opt_para = opt_result.x
    print('Optimal parameter:', opt_para)
    print("Optimized objective function value:", opt_result.fun)
    # 최적화된 parameter에 해당되는 양자 상태를 얻는다.
    circuit = psi.get_circuit(opt_para)
    #양자 상태를 측정하여 최적의 결과를 계산한다.
    result = get_answer(circuit)
    return result











if __name__ == '__main__':
    main()


