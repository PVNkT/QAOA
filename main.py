import numpy as np
from omegaconf import OmegaConf
from ast import literal_eval

from make_graph import network_graph
from Hamiltonian import Hamiltonian
from variational_circuit import variational_circuit
from calc_exp import expectation
from optimization import opimization
from result import get_answer


def main(cfg=OmegaConf.load('config.yaml'))->None:
    graphs = OmegaConf.load('graphs.yaml')
    cfg.merge_with(cfg, graphs)
    cfg.merge_with_cli()
    # graph의 node를 설정
    graph_name = cfg.graph
    nodes = [i for i in range(cfg[graph_name].node)]
    # graph의 edge를 설정
    edges = list(literal_eval(cfg[graph_name].edge))
    # 초기 parameter를 설정, 값들의 길이가 반복 횟수 p에 해당된다.
    gammas = np.array(cfg.init_para.gamma)
    betas = np.array(cfg.init_para.beta)  
    init_para = np.concatenate([gammas, betas])
    
    # node와 edge를 기반으로 graph를 만든다.
    graph = network_graph(nodes, edges, graph_name).graph
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
    # 계산된 최적화 값
    print("Optimized objective function value:", opt_result.fun)
    # 최적화된 parameter에 해당되는 양자 상태를 얻는다.
    circuit = psi.get_circuit(opt_para)
    #양자 상태를 측정하여 최적의 결과를 계산한다.
    result = get_answer(circuit, graph_name)











if __name__ == '__main__':
    main()


