from random import randint

def lancer(n:int)->list:
    a=[]
    for i in range(n):
        a.append(randint(0,6))
    return a

def paire6(a):
    b=0
    for k in a:
        if k == 6:
            b+=1
    print(a)
    return b == 2
print(paire6(lancer(5)))