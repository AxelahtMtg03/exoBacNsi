def recherche(elt:int,tab:list)->int:
    for i in range(len(tab)):
        if tab[i]==elt:
            return i
    return -1
print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
print(recherche(50, []))
print(recherche(4, [2, 4, 4, 3, 4]))