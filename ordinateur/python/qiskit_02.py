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
alpha0 = 3+1j
beta0 = 1-2j
norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2)
alpha, beta = alpha0/norme, beta0/norme
etat_initial = [alpha,beta]
qubit_initial = circuit.initialize(etat_initial, [0])


# [[à reporter]]
# ## Initialisation à la main : sphère de Bloch 
# theta, phi = np.pi/3, np.pi/2
# circuit.u3(theta,phi,0,0)

# Une porte X
circuit.x(0)

# Sauvegarder l'état du qubit
circuit.save_statevector()

print(circuit.draw(output='text'))


### Partie C. Exécution 

tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit)


### Partie D. Résultats

result = job.result()

coefficients = result.get_statevector()
print("Coefficient alpha:", coefficients[0])
print("Coefficient beta :", coefficients[1])

