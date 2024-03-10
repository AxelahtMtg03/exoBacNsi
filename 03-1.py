def moyenne(l:list)->float:
    a = 0
    b=0
    for i in range(len(l)):
        a += l[i][0] *l[i][1]
        b += l[i][1]
    if b==0:
        return None
    return a/b           
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))