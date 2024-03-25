import qiskit as q
import numpy as np

### Partie A. Préparation

# On simule un ordinateur quantique
simulator = q.Aer.get_backend('statevector_simulator')

### Partie B. Construction du circuit

# Circuit quantique avec un q-bit 
circuit = q.QuantumCircuit(1)

# Initialisation à la main : écriture algébrique
alpha0 = 3+1j
beta0 = 1-2j
norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2)
alpha, beta = alpha0/norme, beta0/norme
etat_initial = [alpha,beta]
qubit_initial = q.extensions.Initialize(etat_initial)
circuit.append(qubit_initial, [0])


# [[à reporter]]
# ## Initialisation à la main : sphère de Bloch 
# theta, phi = np.pi/3, np.pi/2
# circuit.u3(theta,phi,0,0)

# Une porte X
circuit.x(0)

print(circuit.draw(output='text'))


# Partie C. Exécution 

job = q.execute(circuit, simulator)


# Partie D. Résultats

result = job.result()

coefficients = result.get_statevector()
print("Coefficient alpha:", coefficients[0])
print("Coefficient beta :", coefficients[1])

