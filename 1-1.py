def verifie(l:list)->bool:
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
print(verifie([0, 5, 8, 8, 9]))