import qiskit as q

from qiskit_ibm_provider import IBMProvider
import matplotlib.pyplot as plt

### Partie A. Préparation

# Clé à donner une fois seulement, ensuite commenter cette ligne
IBMProvider.save_account(token='ce5a6210bb21...')

provider = IBMProvider()

print(provider.backends()) # Affiche les ordinateurs disponibles

backend = provider.get_backend('ibm_kyoto') # Choix d'un ordinateur disponible

### Partie B. Construction du circuit

circuit = q.QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0,1], [0,1])

### Partie C. Exécution 

tcircuit = q.transpile(circuit, backend)
job = backend.run(tcircuit, shots=1000)

### Partie D. Résultats et visualisation

result = job.result()
counts = result.get_counts(tcircuit)
print("Nombre de '00', '01', '10' et de '11' :", counts)

q.visualization.plot_histogram(counts)
plt.show()