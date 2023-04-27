from qiskit import Aer, QuantumCircuit, transpile, assemble
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_histogram
from utils import savefig


class optimized_result:
    def __init__(self, qc:QuantumCircuit, graph) -> None:
        # 양자 상태를 만드는 회로
        self.qc = qc
        # 양자 상태의 adjoint (bra vector state)
        self.inv_qc = qc.inverse()
        # 그래프의 종류가 무엇인지 저장
        self.graph_name = graph.graph_name
        # graph에서 Hamiltonian을 이루는 z operator들을 확인하기 위해서 edge들을 불러온다.
        edges = graph.graph.edges
        # expectation을 계산하는데 사용되는 회로를 그리는 과정
        # Hamiltonian이 덧셈 형태로 더해져 있기 때문에 각 Pauli string에 대해서 expectation 계산을 각각 진행하여야 한다.
        # I로만 이루어진 경우에는 inv회로와 기존 회로가 모두 상쇄되기 때문에 표현하지 않았다. 
        for edge in edges:
            # 기존의 회로를 그대로 가져옴
            partial_qc = self.qc.copy()
            partial_qc.barrier()
            # 해당되는 edge에 z operator를 작용
            partial_qc.z(edge[0])
            partial_qc.z(edge[1])
            partial_qc.barrier()
            # 기존 회로의 반대를 추가함
            partial_qc = partial_qc.compose(self.inv_qc)
            partial_qc.measure_all()
            # 회로를 그리고 저장
            self.draw_circuit(partial_qc, added_name=f'{edge} partial expectation')
    
    def get_answer(self):
        qc = self.qc
        # 측정하는 부분을 추가
        qc.measure_all()
        self.draw_circuit(qc)
        #양자 회로를 transpile하는 코드
        simulator = Aer.get_backend('aer_simulator')
        t_qc = transpile(qc, simulator)
        #시뮬레이션을 시행
        job = simulator.run(t_qc, shots=100*2**qc.num_qubits)
        #결과를 받는다.
        result = job.result()
        counts = result.get_counts(qc)
        # 가장 많이 나온 값을 찾고 그 값을 출력한다.
        key_with_max_value = max(counts, key=counts.get)
        print(key_with_max_value)
        
        # 결과의 histogram을 그리고 저장한다.
        plot_histogram(counts, figsize=(2**(qc.num_qubits-2),10), title=self.graph_name+' result histogram')
        # 그래프 내부의 빈공간 설정
        plt.tight_layout(pad=0.3)
        # 그래프 밖에 여유공간 설정
        plt.margins(0.001,0.1)
        # 그래프 저장
        with savefig('result/'+self.graph_name+'/', self.graph_name + '_hist.png') as sf:
            sf
        
        return result
    
    def draw_circuit(self, qc, added_name:str = ''):
        # 양자 회로 그림을 그림
        qc.draw('mpl', fold = -1)
        # 회로의 재목 설정
        plt.title(self.graph_name+' variational circuit')
        # 회로 내부의 빈공간 설정
        plt.margins(0.01,0.1)
        # 회로 밖에 여유공간 설정
        plt.tight_layout(pad=0.1)
        # 그림을 저장
        with savefig('result/'+self.graph_name+'/', self.graph_name + added_name + '_circuit.png') as sf:
            sf
        plt.clf()
        return None























