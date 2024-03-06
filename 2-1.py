def indices_maxi(tab:list):
    nbmaxi = tab[0]
    indice =[]
    for element in tab:
        if element>nbmaxi:
            nbmaxi = element
    for i in range(len(tab)):
        if tab[i]==nbmaxi:
            indice.append(i)

    return (nbmaxi,indice)
print( indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))