def maxList(l:list)->float:
    max=l[0]
    for i in range(len(l)):
        if l[i]>max:
            max = l[i]
    return max
print(maxList([98, 12, 104, 23, 131, 9]))
print(maxList([-27, 24, -3, 15]))