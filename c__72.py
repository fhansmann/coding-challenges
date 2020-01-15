def remove_dup (L1, L2):
    L1_copy = L1[:]
    for i in L1_copy:
        if i in L2:
            L1.remove(i)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

remove_dup(L1, L2)
print(L1)

# Note that you should not modify a list as your are iterating over it; Python is not updating the list as you change the list; make a copy first!
