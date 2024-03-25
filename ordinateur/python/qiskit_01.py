import qiskit as q
from qiskit_aer import QasmSimulator
import matplotlib.pyplot as plt

### Partie A. Préparation

# On simule un ordinateur quantique
simulator = QasmSimulator()


### Partie B. Construction du circuit

# Circuit quantique avec un qubit et une mesure
circuit = q.QuantumCircuit(1, 1)

# Une porte de Hadamard
circuit.h(0)

# Mesure du qubit (donne un bit classique)
circuit.measure(0, 0)

# Affichage du circuit
print(circuit.draw(output='text'))  

# circuit.draw(output='mpl', style="iqp")
# plt.show()

### Partie C. Exécution 

# Lancer de 1000 simulations
tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit, shots=1000)

### Partie D. Résultats et visualisation

result = job.result()

# Comptage
counts = result.get_counts(tcircuit)
print("Nombre de '0' et de '1' :", counts)

# Diagramme en barres
q.visualization.plot_histogram(counts)
# plt.savefig('fig-qiskit-01.png')
plt.show()