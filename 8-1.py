def maxDico(dico:dict)->tuple:
    max = 0
    reverseDico = {dico[i]: i for i in dico}
    for element in dico.values():
        if element> max:
            max=element
    return (reverseDico[max],max)

print(maxDico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(maxDico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))
