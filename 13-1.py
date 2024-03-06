def recherche(a:float,tab:list)->int:
    b=0
    for i in range(len(tab)):
        if tab[i]==a:
            b+=1
    return b
print(recherche(5, []))
print(recherche(5, [-2, 3, 4, 8]))
print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5, [-2, 5, 3, 5, 4, 5]))