from qiskit import QuantumCircuit
from qiskit.opflow import Z, I

class Hamiltonian:
    
    def __init__(self,graph):
        nodes = list(graph.nodes)
        edges = list(graph.edges)
        
        self.qubit = len(nodes)
        
        I_op = self.list_to_op([I for _ in range(self.qubit)])
        Hamiltonian = 0.5*(I_op - self.list_to_op(self.get_z_list(edges[0])))
        for edge in edges[1:]:
            Hamiltonian += 0.5*(I_op - self.list_to_op(self.get_z_list(edge)))
        print(Hamiltonian)
        self.H = -Hamiltonian

    def get_z_list(self, edge):
        z_list = [I for _ in range(self.qubit)]
        z_list[edge[0]] = Z
        z_list[edge[1]] = Z
        return z_list


    def list_to_op(self, list):
        ops = list[0]
        for op in list[1:]:
            ops = ops^op
        return ops











if __name__ == '__main__':
    li = [1 for _ in range(10)]
    li[(3)] = 0
    print(li)







