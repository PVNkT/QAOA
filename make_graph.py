import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class network_graph:
    def __init__(self, nodes, edges) -> None:
        self.nodes = nodes
        self.edges = edges
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        self.graph = G
    
    def draw_graph(self):
        # Generate plot of the Graph
        # node를 빨간색으로 설정
        colors = ['r' for node in self.nodes()]
        # 상자 태두리 설정
        default_axes = plt.axes(frameon=True)
        # layout 설정
        pos = nx.spring_layout(self.graph)
        #그래프 그리기
        nx.draw_networkx(self.graph, node_color=colors, node_size=600, alpha=1, ax=default_axes, pos=pos)
                


if __name__ == '__main__':
    graph = network_graph([0,1,2,3],[(0,1), (1,2), (2,3), (3,0)]).graph
    print(graph.nodes)
    print(graph.edges)










