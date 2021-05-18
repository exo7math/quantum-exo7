
import numpy as np
import matplotlib.pyplot as plt



##########################################
# Exemple du cours
# La transformée de Fourier (fonction)






# Visualisation

def affichage_convolution():

    # Exemple 1
	a, b = 0, 8*np.pi   # intervalle
	N = 300             # nb de points
	X = np.linspace(a,b,N)
	f1 = 2 + np.sin(X)
	f2 = 0.5+0.2*np.sin(3*X+np.pi/2)
	f3 = -0.2+0.4*np.sin(4*X+np.pi/3)

	F = [f1,f2,f3]   # toutes les fonctions
	# f = f1+f2+f3     # fonction à étudier

    # Exemple 2
	a, b = 0, 2*np.pi   # intervalle
	N = 300             # nb de points
	X = np.linspace(a,b,N)
	f1 = 1 + np.cos(3*X)
	f2 = 0.5 + 0.5*np.cos(5*X)

	F = [f1,f2]   # toutes les fonctions
	# f = f1+f2+f3     # fonction à étudier


	f = sum(F)
	ax = plt.subplot(2,1,1)
	ax.set_title("Fonction f")
	plt.plot(X,f)

	# ax = plt.subplot(3,1,2)
	# ax.set_title("fonction g")
	# plt.plot(g,color='orange')

	ax = plt.subplot(2,1,2)
	ax.set_title("Composantes")
	for fi in F:
	    plt.plot(X,fi,color='red')

	plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.95, hspace=1.0,wspace=0.5)
	plt.tight_layout()
	# plt.savefig('fourier-8bis.png')
	plt.show()
	return


affichage_convolution()