
### Partie A. Préparation
simulator = q.Aer.get_backend('qasm_simulator')

### Partie B. Construction du circuit
circuit = q.QuantumCircuit(2, 2)  # 2 qubits et 2 mesures

circuit.h(0)  # Porte de Hadamard sur le premier qubit
circuit.x(1)  # Porte X sur le second qubit
circuit.cx(0, 1) # CNOT
circuit.h(1)  # Porte de Hadamard sur le second qubit
circuit.measure([0,1], [0,1]) # Mesure (q0->c0,q1->c1)

# Affichage graphique du circuit
import PIL
img_circuit = circuit.draw(output='latex')
img_circuit.show()


### Partie C. Exécution 
job = q.execute(circuit, simulator, shots=1000)

### Partie D. Résultats et visualisation
result = job.result()
counts = result.get_counts(circuit)
print("Nombre de '00', '01', '10' et de '11':",counts)

# Diagramme en barres
q.visualization.plot_histogram(counts)
plt.show()
