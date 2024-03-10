def fusion(l1:list,l2:list)->list:
    l=[]
    for p in l1:
        l.append(p)
    for k in l2:
        l.append(k)
    for i in range(1,len(l)):
        cle = l[i]
        j=i-1
        while j>=0 and l[j]>cle:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=cle
    return l
print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))