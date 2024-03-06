def convertir(tab:list)->int:
    a= 0
    b=tab[::-1]
    for i in range(len(tab)):
        if b[i] == 1:
            a = a + 2**i
    return a
print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))