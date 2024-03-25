from qiskit_aer import AerSimulator

### Partie A. Préparation

simulator = AerSimulator(method="statevector")

### Partie B. Construction du circuit

circuit = q.QuantumCircuit(1)

# Initialisation à la main : écriture algébrique
alpha0 = 3+1j
beta0 = 1-2j
norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2)
alpha, beta = alpha0/norme, beta0/norme
etat_initial = [alpha,beta]
qubit_initial = circuit.initialize(etat_initial, [0])

# Circuit : une porte X
circuit.x(0)

# Sauvegarder l'état du qubit
circuit.save_statevector()

### Partie C. Exécution 
tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit)

### Partie D. Résultats

result = job.result()

coefficients = result.get_statevector()
print("Coefficient alpha:", coefficients[0])
print("Coefficient beta :", coefficients[1])

