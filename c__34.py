def Dict_print():
    d = dict()
    
    for i in range(1,21):
        d[i] = i ** 2
        
    for (k,v) in d.items():	
        print(v)
    
Dict_print()
