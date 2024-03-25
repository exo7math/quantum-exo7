import qiskit as q

from qiskit_ibm_provider import IBMProvider
import matplotlib.pyplot as plt

### Partie A. Préparation

# Clé à donner une fois seulement, ensuite commenter cette ligne
IBMProvider.save_account(token='ce5a6210bb21...')

provider = IBMProvider()

# Afficher les simulateurs et ordinateurs disponibles
# print(provider.backends())

# Choix du simulateur ou de l'ordinateur
backend = provider.get_backend('ibmq_qasm_simulator')  # simulateur
# backend = provider.get_backend('ibm_kyoto') # vrai ordinateur quantique

### Partie B. Construction du circuit

circuit = q.QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0,1], [0,1])

print(circuit.draw(output='text'))
### Partie B. Construction du circuit

circuit.draw(output='mpl', style="iqp")
plt.show()

### Partie C. Exécution 

# Lancer de 1000 simulations
print("Démarrage des calculs...")

tcircuit = q.transpile(circuit, backend)
job = backend.run(tcircuit, shots=1000)
print(f"L'identifiant de cette session ('Job') est : {job.job_id()}")
print("Vous retrouverez les résultats sur https://quantum.ibm.com/jobs")

### Partie D. Résultats et visualisation

result = job.result()

print("Calculs terminés.")

# Comptage
counts = result.get_counts(tcircuit)
print("Nombre de '00', '01', '10' et de '11' :", counts)

# Diagramme en barres
q.visualization.plot_histogram(counts)
plt.savefig('fig-resultats.png')
plt.show()