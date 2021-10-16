sentence = input("Please enter the sentence:\n")

tup = ()
for c in sentence:
    if c not in tup:
        tup += (c.upper())

