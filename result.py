from qiskit import Aer, QuantumCircuit, transpile, assemble
import matplotlib.pyplot as plt
from qiskit.tools.visualization import plot_histogram

def get_answer(qc:QuantumCircuit):
    # 측정하는 부분을 추가
    qc.measure_all()
    # 양자 회로 그림을 저장
    qc.draw('mpl', fold = -1).savefig('result/circuit/circuit.png')

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
    key_with_max_value = max(counts, key=counts.get)
    print(key_with_max_value)
    # 그림의 크기 설정
    plt.figure(figsize=(10,10))
    # 결과의 histogram을 그리고 저장한다.
    plot_histogram(counts, figsize=(10,10)).savefig('result/histogram/hist.png')
    

    return result
























