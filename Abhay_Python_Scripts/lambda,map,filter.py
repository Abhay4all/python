
add_10=lambda x:x+5
print(add_10(5))

# def add_10(x):
#     print(x+5)

mult_2=lambda x,y:x*y
print(mult_2(5,6))


points=[(2,3),(5,9),(1,7),(0,19),(3,3),(1,0)]
print(points)
sorted_points=sorted(points,key=lambda x:x[1]) # sort according to y index
print(sorted_points)


# MAP function
# map(function,seq)

a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

c=[x*2 for x in a]
print(c)

# filter(func,seq)

a=[1,2,3,4,5,6]
b=filter(lambda x:x%2==0,a)
print(list(b))

d=[x for x in a if x%2==0]
print(d)