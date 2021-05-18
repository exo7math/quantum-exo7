
import numpy as np
import matplotlib.pyplot as plt



##########################################
# La transformée de Fourier discrète
##########################################


def enrouler(t,X):
    n = len(X)
    S = np.linspace(0,t,n,endpoint=False)
    E = np.exp(-2j*np.pi*S)
    return X * E

def centre(t,X):
    n = len(X)
    S = np.linspace(0,t,n,endpoint=False)
    E = np.exp(-2j*np.pi*S)
    Z = X *  E    
    return sum(Z)/n


# Exemple 1
X = np.array([1.5,4,2,3])
Z = enrouler(1,X)
# print("Z =",Z)
# print("Centre =",centre(1,X))

# Exemple 2
# T = np.linspace(np.pi/2,3/2*np.pi,10)
# X = 2+np.cos(T)
# Z = enrouler(1,X)
# print("Z =",Z)
# print("Centre =",centre(1,X))

# Exemple 3
# a, b = 0, 2*np.pi
# n = 200
# T = np.linspace(a,b,n)
# X = 1 + np.cos(3*T)

# Exemple 0
# a, b = 0, 2*np.pi
# n = 100
# T = np.linspace(a,b,n)
# f1 = 1 + np.sin(4*T)
# f2 = 0.2*np.sin(4*3*T + np.pi/2)
# f3 = 0.4*np.sin(4*5*T + np.pi/3)
# X = f1 + f2 + f3

# Exemple 4
a, b = 0, 2*np.pi
n = 1000
T = np.linspace(a,b,n)
f1 = 1 + np.cos(3*T)
f2 = 0.5 + 0.5*np.cos(5*T)
X = f1 + f2



# Visualisation

def affichage(t,X):
    # 1. Affichage linéaire
    ax = plt.subplot(1,1,1)
    # ax.set_title("Graphe linéaire")
    # ax.plot(X,color='red')
    # ax.set_xticks([])
    # ax.axhline(0)

    # Point avec segments verticaux
    # for i in range(len(X)):
    #     ax.scatter(i,X[i],color='red')
    #     ax.plot((i,i),(0,X[i]),color='gray')
    # ax.xaxis.set_ticks(range(len(X)))


    # 2. Affichage circulaire

    # Cercle unité
    # ax = plt.subplot(1,2,2)
    # ax.set_title("Graphe circulaire")

    # # Cercle unité
    ax.scatter(0,0,color='black')
    T = np.linspace(0,2*np.pi,100)
    ax.plot(np.cos(T),np.sin(T))

    # # # Points
    Z = enrouler(t,X)
    # ax.scatter(Z.real,Z.imag,color='red')

    # # # Segments depuis l'origine
    # for z in Z:
    #     ax.plot((0,z.real),(0,z.imag),color='gray')

    # relier les points
    ax.plot(Z.real,Z.imag,color='red')   

    # # Centre de gravité
    G = centre(t,X)
    ax.scatter(G.real,G.imag,color='orange',marker = 'x')
    ax.axis('off')
    ax.set_aspect('equal')
    # plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.95, hspace=1.0,wspace=0.5)
    plt.tight_layout()
    # plt.savefig('fourier-9-1.png')
    plt.show()
    return  

affichage(1.005,X)

# affichage(1.01,X)
# affichage(4,X)
# affichage(5,X)


def affichage_centres(X):
    # Centre de gravité en fonction du paramètre t
    tmin, tmax = 1, 10
    N = 200
    T = np.linspace(tmin,tmax,N)
    GG = np.zeros(N,dtype=complex)
    for i in range(N):
        t = T[i]
        GG[i] = centre(t,X)

    plt.axhline(0)
    plt.xticks(range(tmin,tmax))
    plt.plot(T,GG.real,color='blue')
    plt.tight_layout()
    # plt.savefig('fourier-10.png')

    plt.show()

    return

# affichage_centres(X)