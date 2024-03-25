import qiskit as q
from qiskit_aer import QasmSimulator

### Partie A. Préparation

simulator = QasmSimulator()

### Partie B. Construction du circuit

circuit = q.QuantumCircuit(2, 2)

## B.1 Préparation de l'état de Bell
circuit.h(0)  # Porte de Hadamard
circuit.cx(0, 1) # CNOT

message_alice = '01'  # choix entre '00', '01', '10', '11'

## B.2 Porte d'Alice selon message à transmettre
if message_alice == '00':
	circuit.iden(0)  # identité
elif message_alice == '01':
	circuit.z(0)     # porte Z
elif message_alice == '10':
	circuit.x(0)     # porte X
elif message_alice == '11':
	circuit.x(0)     # porte X
	circuit.z(0)     # suivi de porte Z	

## B.3 Décodage
circuit.cx(0, 1) # CNOT
circuit.h(0)  # Porte de Hadamard

## B.4 Mesures
circuit.measure([0,1], [0,1]) # Mesures

print(circuit.draw(output='text'))

### Partie C. Exécution 

# Lancer de 1000 simulations
tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit, shots=1000)

# Partie D. Résultats

result = job.result()

# Comptage
counts = result.get_counts(tcircuit)
print("Nombre de '00', '01', '10' '11' :", counts)

