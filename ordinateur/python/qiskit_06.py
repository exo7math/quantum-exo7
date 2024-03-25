import qiskit as q
from qiskit_aer import QasmSimulator
import matplotlib.pyplot as plt

# Partie A. Préparation

# On simule un ordinateur quantique
simulator = QasmSimulator()

# Partie B. Construction du circuit

# Circuit quantique avec 3 qbit et 3 mesures
circuit = q.QuantumCircuit(3, 3)
circuit.h(0)  # Porte de Hadamard
circuit.h(2)  # Porte de Hadamard
circuit.cx(0, 1) # CNOT
circuit.h(1)  # Porte de Hadamard
circuit.cx(1, 2) # CNOT
circuit.measure([0,1,2], [0,1,2]) # Mesures


print(circuit.draw(output='text'))

# Partie C. Execution 

# Lancer de 1000 simulations
tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit, shots=1000)

# Partie D. Résultats et visualisation

result = job.result()

# Comptage
counts = result.get_counts(tcircuit)
print("Nombre de '000', '001', ... '111':", counts)

# Plot a histogram
q.visualization.plot_histogram(counts)
# plt.savefig('fig-qiskit-06.png')
plt.show()
