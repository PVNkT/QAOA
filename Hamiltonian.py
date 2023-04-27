from qiskit import QuantumCircuit
from qiskit.opflow import Z, I

class Hamiltonian:
    
    def __init__(self,graph):
        # graph에서 node와 edge의 정보를 저장
        self.graph = graph.graph
        nodes = list(self.graph.nodes)
        edges = list(self.graph.edges)
        
        # qubit의 수(=node의 수)를 저장
        self.qubit = len(nodes)
        # 모든 qubit에 identity operator를 적용하는 operator list
        self.I_op = self.list_to_op([I for _ in range(self.qubit)])
        # 첫번째 edge에 대한 Hamiltonian w*(I-Z_1Z_2)/2를 계산 
        Hamiltonian = 0.5*self.get_weight(edges[0])*(self.I_op - self.list_to_op(self.get_z_list(edges[0])))
        # 두번째 이후의 dege들에 대해서도 Hamiltonian을 계산하고 더해줌
        for edge in edges[1:]:
            Hamiltonian += 0.5*self.get_weight(edge)*(self.I_op - self.list_to_op(self.get_z_list(edge)))
        print(Hamiltonian)
        # scipy에서 minimize만을 지원하기 때문에 -를 붙여서 Hamiltonian을 최대화한다. 
        self.H = -Hamiltonian

    def get_z_list(self, edge):
        # 특정 edge에 대해서만 z operator가 가해지고 나머지는 I operator가 가해지게 하는 operator list를 만든다. 
        # 모든 qubit에 I operator가 적용되게 함
        z_list = [I for _ in range(self.qubit)] 
        # edge에 해당되는 qubit은 z operator가 적용되게 함
        z_list[edge[0]] = Z
        z_list[edge[1]] = Z
        return z_list


    def list_to_op(self, list):
        # operator list를 qiskit에서 지원하는 형태의 opertor로 변경
        # 첫번째 operator
        ops = list[0]
        # 각 opertor들을 합쳐서 하나의 operator로 표현 (tensor product)
        for op in list[1:]:
            ops = ops^op
        return ops
    
    def get_weight(self, edge):
        edge_weight = self.graph.get_edge_data(*edge)['weight']
        return edge_weight












if __name__ == '__main__':
    li = [1 for _ in range(10)]
    li[(3)] = 0
    print(li)







