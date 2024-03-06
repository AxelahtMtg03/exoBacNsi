def mult(n1:int,n2:int)->int:
    add = n1
    if n2 == 0:
        return 0
    for i in range(1,abs(n2)):
        add+=n1
    if n1<0 and n2<0:
        return abs(add)
    elif (n1>0 and n2<0) or (n1<0 and n2>0):
        return -abs(add)
    else:
        return add
print(mult(3,5))
print(mult(-4,-8))
print(mult(-2,6))
print(mult(-2,0))