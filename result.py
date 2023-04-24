from qiskit import Aer, QuantumCircuit, transpile, assemble
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_histogram

def get_answer(qc:QuantumCircuit):
    qc.measure_all()
    #양자 회로를 transpile, assemble하는 코드
    simulator = Aer.get_backend('aer_simulator')
    t_qc = transpile(qc, simulator)
    qobj = assemble(
        t_qc,
        shots=1000,
        )
    #시뮬레이션을 시행
    job = simulator.run(qobj)
    #결과를 받는다.
    
    result = job.result()
    counts = result.get_counts(qc)
    plt.figure(figsize=(10,10))
    plot_histogram(counts, figsize=(10,10)).savefig('result/histogram/hist.png')
    return result
























