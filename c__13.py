s = input()
d = {"digits":0, "letters":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass

print("Letters", d["letters"])
print("Digits", d["digits"])
