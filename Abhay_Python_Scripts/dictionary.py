# Dictionary ---> key-Value pairs, unordered, Mutable

mydict={"Name":"Abhay","Company":"ZS"}
print(mydict)

mydict_2=dict(name="Aditya",Company="ZS")
print(mydict_2)

mydict["gmail"]="abhaytrekk@gmail.com"

print(mydict)

mydict["gmail"]="abhayrock@gmail.com"
print(mydict)


if "gmail" in mydict:
    print(mydict["gmail"])

try:
    print(mydict["name"])
except:
    print("Error")

for key in mydict.keys():
    print(key,end= " ")
print()

for key,value in mydict.items():
    print(key,end=" ")
    print(value,end=" ")
print()


mydict.pop("gmail")
print(mydict)

del mydict['Company']
print(mydict)


my_dict={3:9,4:12,5:15}
value=my_dict[3]
print(value)

mytuple=(8,7)
my_dict_2={mytuple}



