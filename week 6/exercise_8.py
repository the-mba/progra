sentence = input("Please enter the sentence:\n")

tup = ()
for c in sentence:
    c = c.upper()
    if c not in tup:
        tup += (c,)

print(tup)