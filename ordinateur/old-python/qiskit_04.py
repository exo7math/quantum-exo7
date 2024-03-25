import qiskit as q
import matplotlib.pyplot as plt

### Partie A. Préparation

# On simule un ordinateur quantique
simulator = q.Aer.get_backend('qasm_simulator')

### Partie B. Construction du circuit

# Circuit quantique avec 2 qubits et 2 mesures
circuit = q.QuantumCircuit(2, 2)

circuit.h(0)  # Porte de Hadamard sur le premier qubit
circuit.x(1)  # Porte X sur le second qubit
circuit.cx(0, 1) # CNOT
# circuit.h(1)
circuit.measure([0,1], [0,1]) # Mesure


# print(circuit.draw(output='text'))

import PIL
# img_circuit = circuit.draw(output='latex',filename='fig-circuit-latex.png')
img_circuit = circuit.draw(output='latex')
img_circuit.show()


# print(circuit.draw(output='latex_source'))

### Partie C. Exécution 

# Lancer de 1000 simulations
job = q.execute(circuit, simulator, shots=1000)

### Partie D. Résultats et visualisation

result = job.result()

# Comptage
counts = result.get_counts(circuit)
print("Nombre de '00', '01', '10' et de '11':",counts)

# # Diagramme en barres
q.visualization.plot_histogram(counts)
# plt.savefig('fig-qiskit-04.png')
plt.show()
