from math import gcd
# Calculs d'ordre/période pour l'algorithme de Schor

def ordre(a,N):
    """ 
    Calcul de l'ordre a modulo N 
    """
    k = 1
    while ((a ** k) % N) != 1 :
        k = k+1
    return k

# Test
# print(ordre(2,15))

def facteurs(N):
    print("Entier à factoriser N =",N)
    for a in range(2,N):
        print("")
        d = gcd(a,N)
        if d != 1:
            print("a = ",a,"  d = pgcd(a,N) > 1")
            print("    facteur d  =", d)

        else:
            r = ordre(a,N)
            if r%2 == 0:  # r pair ?
                x = a ** (r//2) - 1
                y = x + 2 

                print("a = ",a,"  ordre r =",r,"pair")
                if y%N == 0:
                    print("    N divise a^(r/2) + 1, ECHEC")
                else: 
                    d = gcd(x,N)
                    dd = gcd(y,N)
                    print("    facteur d  =",d)
                    print("    facteur d' =",dd)


            else:

                print("a = ",a," ordre r =",r,"impair, ECHEC")

    return

# Test
facteurs(103)
