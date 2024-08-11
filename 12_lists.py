# lists
# each element has an index starting with 0 (no surprise)
countries = ["USA", "UK", "France", "Germany"]

# access values from lists using the index
print(countries[0])
print(countries[1])
print(countries[3])
print("")

# overwrite values
countries[0] = "India"
print(countries[0])
print("")

# get length of list
print(len(countries))
print("")

# delete item in list
print(countries[1])
del countries[1] # index 2 has now index 1 ...
print(countries[1])

print("")
# get "last" items from list with negative values
print(countries[-3]) # = india with index 0
