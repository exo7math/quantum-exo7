import qiskit as q
from qiskit.tools.monitor import job_monitor
import matplotlib.pyplot as plt

### Partie A. Préparation

# Clé à donner une fois seulement, ensuite commenter la ligne
# q.IBMQ.save_account('ce5a6210bb21...')

q.IBMQ.load_account()

# print(q.IBMQ.providers())

provider = q.IBMQ.get_provider(group='open')

# print(provider.backends())

backend = provider.get_backend('ibmq_essex')

### Partie B. Construction du circuit

circuit = q.QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0,1], [0,1])

print(circuit.draw(output='text'))

### Partie C. Execution 

job_exp = q.execute(circuit, backend=backend, shots=1000)
job_monitor(job_exp)


# Partie D. Résultats et visualisation
result_exp = job_exp.result()
counts_exp = result_exp.get_counts(circuit)
print(counts_exp)

q.visualization.plot_histogram(counts_exp)
# plt.savefig('fig-qiskit-real.png')
plt.show()