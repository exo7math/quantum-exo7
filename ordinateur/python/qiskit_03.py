import qiskit as q
from qiskit_aer import AerSimulator
import numpy as np

### Partie A. Préparation

# On simule un ordinateur quantique
simulator = AerSimulator(method="statevector")


### Partie B. Construction du circuit

# Circuit quantique avec un q-bit 
circuit = q.QuantumCircuit(1)


# Initialisation à la main : écriture algébrique
alpha = np.sqrt(3)/2 
beta = 1/(2*np.sqrt(2))*(1-1j)
etat_initial = [alpha,beta]
qubit_initial = circuit.initialize(etat_initial, [0])

circuit.h(0) # Une porte de Hadamard
circuit.x(0) # Porte X
circuit.y(0) # Porte Y
# circuit.h(0) # Une porte de Hadamard

# Un porte quantique défini par matrice
# theta, phi, mylambda = np.pi/3, -np.pi/6, np.pi/4
# circuit.u3(theta,phi,mylambda,0)

# Sauvegarder l'état du qubit
circuit.save_statevector()

print(circuit.draw(output='text'))

img_circuit = circuit.draw(output='mpl', style="iqp", filename='fig-circuit.png')
img_circuit.show()

### Partie C. Execution 

tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit)


### Partie D. Résultats

result = job.result()

coefficients = result.get_statevector()
print("Coefficicient alpha:", coefficients[0])
print("Coefficicient beta :", coefficients[1])

