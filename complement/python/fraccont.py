from math import *

def reel_vers_frac(x,n=10):
    y = x
    myfrac = []
    for k in range(n):
        a = floor(y)        # Partie entiere
        if a<100000:
            myfrac.append(a)
        else: 
            break
        if y != a:
            y = 1/(y-a)     # Formule de recurrence
        else:
            break           # Stop car y entier
    return myfrac

def frac_vers_rationnel(myfrac,n):
    p_k_2 = 0
    q_k_2 = 1
    p_k_1 = 1
    q_k_1 = 0
    for a in myfrac[0:n]:
        p_k = a*p_k_1 + p_k_2
        q_k = a*q_k_1 + q_k_2 
        p_k_2, q_k_2 =  p_k_1, q_k_1
        p_k_1, q_k_1 =  p_k, q_k
    return p_k,q_k

# Test avec pi

x = pi
print("x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(1,len(frac)):
    print(frac_vers_rationnel(frac,n))

# Test avec 314/100

x = 314/100
print("x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))

 # Test avec 31415/10000

x = 314159/100000
print("x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))   

# Test avec 35/24

x = 75/14
print("x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))    


# Test avec 85/512

x = 85/512
print("1. x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))

# Test avec 171/512

x = 171/512
print("2. x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))   


# Test avec 256/512

x = 256/512
print("3. x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))  

# Test avec 341/512

x = 341/512
print("4. x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))  

# Test avec 427/512

x = 427/512
print("5. x =",x)
frac = reel_vers_frac(x)
print(frac)

for n in range(len(frac)):
    print(frac_vers_rationnel(frac,n+1))#
