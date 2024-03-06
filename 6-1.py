def recherche(tab:list,nb:int)->int:
    a=0
    b=0
    for i in range(len(tab)):
        if tab[i] == nb:
            a=i
            b=1
    if b == 0:
        return len(tab)
    else:
        return a

