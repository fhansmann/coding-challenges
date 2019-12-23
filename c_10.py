x = input()
words = [word for word in x.split(" ")]
print(" ".join(sorted(list(set(words)))))
