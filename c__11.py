value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p)
    if intp%5 == 0: #"if not intp%5" -> cleaner
        value.append(p)

print(','.join(value)) #joing = string method! (does not work for dictionaries, as he join() method tries to concatenate the key (not value) of the dictionary to the string. )

