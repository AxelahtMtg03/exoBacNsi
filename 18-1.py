def max_et_indice(tab:list)->tuple:
    maxi=tab[0]
    ind=0
    for i in range(len(tab)):
        if maxi<tab[i]:
            maxi=tab[i]
            ind=i
    return(maxi,ind)
print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))