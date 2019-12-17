list=[]
for i in range(2000, 2300):
	if (i%7==0) and (i%5 !=0):
	  list.append(str(i)) #join() works with strings only

print (", ".join(list))
