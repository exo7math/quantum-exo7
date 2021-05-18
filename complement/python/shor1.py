from cmath import *    # complex numbers
import matplotlib.pyplot as plt

# Algorithme de Schor
# cas où l'ordre n'est pas une puissance de 2

N = 21  # entier à factoriser
a = 2   # entier premier avec N
r = 6   # ordre de a modulo N

n = 9   # N**2 <= 2**n < 2*N**2

# vérification prélables
test_ordre = (a**r)%N == 1 
print("Ordre ok ?",test_ordre)

test_registre = N**2 <= 2**n < 2*N**2
print("Taille registre ok ?",test_registre)

# quel ordre du second registre on mesure ?
k = 2

# combien de termes m dans la somme pour le premier registre correspondant ?
quotient = 2**n // r
reste = 2**n % r

if k < reste:
    m = quotient + 1
else:
    m = quotient

print(quotient,reste,m)

# Pour un j, calcul du coefficient
def exp_coeff(j,a):
    return exp(-2*pi*1j*r*j*a/2**n)

def coeff(j):
    sous_liste_coeff_j = [exp_coeff(j,a) for a in range(m)]
    somme_sous_liste_coeff_j = sum(sous_liste_coeff_j)
    coeff_j = 1/sqrt(2**n)*1/sqrt(m)*somme_sous_liste_coeff_j*exp(-2*pi*1j*j/2**n)
    return coeff_j

def proba(j):
    return abs(coeff(j))**2


liste_proba = [proba(j) for j in range(2**n)]
plt.plot(liste_proba,color="red")
plt.grid()
plt.savefig('schor.png')
plt.show()
#

for j in range(427-5,427+5):
    print("j =",j,"proba(j) = ",proba(j))



# Fractions continues
def cf(n, d):
    res = []
    q, r = divmod(n, d)
    while r != 0:
        res = res + [q]
        q, r = divmod(d, r)
        d = (d-r)//q
    return res + [q]


# test avec pi
print(cf(314159265,100000000))

j = 427
print(cf(j,2**n))