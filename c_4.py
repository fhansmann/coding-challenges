values=input("Please enter numbers:" )

l=values.split(",")
t=tuple(l)

#tuple() method can convert list to tuple 
#remember: method is a function that is available for a given object because of the object's type.

print(l)
print(t)

#Output:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')