import qiskit as q
from qiskit.tools.monitor import job_monitor
import matplotlib.pyplot as plt

### Partie A. Préparation

# Clé à donner une fois seulement, ensuite commenter la ligne
# q.IBMQ.save_account('ce5a6210bb21...')

q.IBMQ.load_account()

# print(q.IBMQ.providers())

provider = q.IBMQ.get_provider(group='open')

# print(provider.backends())

backend = provider.get_backend('ibmq_5_yorktown')

### Partie B. Construction du circuit
### Partie C. Execution 

# La construction du circuit et son lancement on été fait dans 'qiskit_job_execute'
# On a retenu l'identifiant de la la tâche à entrer ci-dessous.

# Partie D. Résultats et visualisation
my_job_id = '608966546edbf75164d08991'

job_exp = backend.retrieve_job(my_job_id)
result_exp = job_exp.result()
counts_exp = result_exp.get_counts()
print(counts_exp)

q.visualization.plot_histogram(counts_exp)
# plt.savefig('fig-qiskit-real.png')
plt.show()