import qiskit as q

### Partie A. Préparation

# On simule un ordinateur quantique
simulator = q.Aer.get_backend('qasm_simulator')

### Partie B. Construction du circuit

# Circuit quantique avec un qubit et une mesure
circuit = q.QuantumCircuit(1, 1)

# Une porte de Hadamard
circuit.h(0)

# Mesure du qubit (donne un bit classique)
circuit.measure(0, 0)

# Affichage du circuit
print(circuit.draw(output='text'))  

### Partie C. Exécution 

# Lancer de 1000 simulations
job = q.execute(circuit, simulator, shots=1000)

### Partie D. Résultats et visualisation

result = job.result()

# Comptage
counts = result.get_counts(circuit)
print("Nombre de '0' et de '1':",counts)

# Diagramme en barres
import matplotlib.pyplot as plt
q.visualization.plot_histogram(counts)
plt.show()
