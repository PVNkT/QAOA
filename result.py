from qiskit import Aer, QuantumCircuit, transpile, assemble
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_histogram
from utils import savefig


def get_answer(qc:QuantumCircuit, graph_name:str = "default_graph"):
    # 측정하는 부분을 추가
    qc.measure_all()
    # 양자 회로 그림을 그림
    qc.draw('mpl', fold = -1)
    # 회로의 재목 설정
    plt.title(graph_name+' variational circuit')
    # 회로 내부의 빈공간 설정
    plt.margins(0.01,0.1)
    # 회로 밖에 여유공간 설정
    plt.tight_layout(pad=0.1)
    # 그림을 저장
    with savefig('result/'+graph_name+'/', graph_name + '_circuit.png') as sf:
        sf
    plt.clf()
    #양자 회로를 transpile, assemble하는 코드
    simulator = Aer.get_backend('aer_simulator')
    t_qc = transpile(qc, simulator)
    qobj = assemble(
        t_qc,
        shots=100*2**qc.num_qubits,
        )
    #시뮬레이션을 시행
    job = simulator.run(qobj)
    #결과를 받는다.
    result = job.result()
    counts = result.get_counts(qc)
    # 가장 많이 나온 값을 찾고 그 값을 출력한다.
    key_with_max_value = max(counts, key=counts.get)
    print(key_with_max_value)
    
    # 결과의 histogram을 그리고 저장한다.
    plot_histogram(counts, figsize=(2**(qc.num_qubits-2),10), title=graph_name+' result histogram')
    # 그래프 내부의 빈공간 설정
    plt.tight_layout(pad=0.3)
    # 그래프 밖에 여유공간 설정
    plt.margins(0.001,0.1)
    # 그래프 저장
    with savefig('result/'+graph_name+'/', graph_name + '_hist.png') as sf:
        sf
    
    return result
























