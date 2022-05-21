# LIST --> ordered,duplicate,mutable
mylist =["abhay","pratap","singh"]
print(mylist)

for x in mylist:
    print(x)

if 'abhay' in mylist:
    print("abhay is resent in list")

mylist.append("aditya")
print(mylist)

mylist.insert(2,"khushboo")
print(mylist)

print(mylist.pop())
print(mylist)

item=mylist.remove("khushboo")
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist=[0]*5
print(mylist)

mylist2=[1,2,3,4,5]
new_list=mylist2+mylist
print(new_list)

mylist=[1,2,3,4,5,6,7,8,9]

a=mylist[1:5]
print(a)

a=mylist[::-1]
print(a)


list_1=["acp","dcp","jcp"]
list_cpy=list_1
list_cpy.append("commisssioner")

print(list_1)
print(list_cpy)

# VS


list_1=["acp","dcp","jcp"]
list_cpy=list(list_1)
list_cpy.append("commisssioner")

print(list_1)
print(list_cpy)


mylist=[1,2,3,4,5]
b=[x*x for x in mylist]

print(mylist)
print(b)
