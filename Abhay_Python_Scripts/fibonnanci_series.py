# fibbonici series

a=0
b=1
print(a,end=" ")
print(b,end=" ")
while (b<50):
    c=a+b
    a=b
    b=c
    print(c,end=" ")