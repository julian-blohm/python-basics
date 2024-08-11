# for ... in ...:
for i in range(10): # range function create an array with values from 0 to 9
    if (i == 2):
        continue # skips this execution
    if (i == 7):
        break # breaks out of loop
    print("i is in", i)