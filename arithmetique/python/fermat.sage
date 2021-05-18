# test de Fermat avec Sage
#oad("fermat.sage")  

N = 1000

def test_fermat(n,a):
    return pow(a,n-1,n) == 1

print("Test de Fermat pour a=2")
nb = 0
for n in range(2,N+1):
    if (not is_prime(n)) and test_fermat(n,2):
        print(n)
        nb +=1
print("Exceptions :",nb)

def test_fermat_2_3_5_7(n):
    return test_fermat(n,2) and test_fermat(n,3) and test_fermat(n,5) and test_fermat(n,7) 


N = 1000000

print("Test de Fermat pour a=2,3,5 et 7")
nb_exceptions = 0
nb_premiers = 0
for n in range(2,N+1):
    if is_prime(n):
        nb_premiers +=1
    elif test_fermat_2_3_5_7(n):
        print(n)
        nb_exceptions +=1

print("Exceptions :",nb_exceptions)
print("Nb de nb premiers :",nb_premiers)
