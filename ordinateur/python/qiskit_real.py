import qiskit as q

from qiskit_ibm_provider import IBMProvider
# from qiskit.tools.monitor import job_monitor
import matplotlib.pyplot as plt

### Partie A. Préparation

# Clé à donner une fois seulement, ensuite commenter cette ligne
# IBMProvider.save_account(token='804787a1d87195e221738e2e3e9fc1290bc4bcd92c2f5ace24b0e2f41d11d0b6df7fe908470d1342088ed831c7c30c25104678021fa032f1c7c5b9d6d7e04da7')

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
print(counts)

# Diagramme en barres
q.visualization.plot_histogram(counts)
plt.savefig('fig-resultats.png')
plt.show()