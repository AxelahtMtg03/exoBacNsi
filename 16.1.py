def recherche_indices_classement(elt:int,tab:list)->tuple:
    l1,l2,l3 = [],[],[]
    for i in range(len(tab)):
        if tab[i]>elt:
            l3.append(i)
        elif tab[i]<elt:
            l1.append(i)
        else:
            l2.append(i)
    return (l1,l2,l3)
print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print( recherche_indices_classement(3, []))