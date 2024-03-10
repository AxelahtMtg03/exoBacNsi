def doublon(l:list)->bool:
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            return True
    return False
print(doublon([2, 5, 7, 7, 7, 9]))