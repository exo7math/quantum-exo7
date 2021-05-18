
### Partie A. Préparation

simulator = q.Aer.get_backend('statevector_simulator')

### Partie B. Construction du circuit

circuit = q.QuantumCircuit(1)

# Initialisation à la main : écriture algébrique
alpha0 = 3+1j
beta0 = 1-2j
norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2)
alpha, beta = alpha0/norme, beta0/norme
etat_initial = [alpha,beta]
qubit_initial = q.extensions.Initialize(etat_initial)
circuit.append(qubit_initial, [0])

# Circuit : une porte X
circuit.x(0)

# Partie C. Exécution 

job = q.execute(circuit, simulator)

# Partie D. Résultats

result = job.result()

coefficients = result.get_statevector()
print("Coefficient alpha:", coefficients[0])
print("Coefficient beta :", coefficients[1])

