# dictionaries consist of a list of keys and values 
usernames ={
    "hello": "bye",
    "name": "j",
    "mail": "mymail", 
}

# to get something from a dictionary, we just use the key to get the value
print(usernames["hello"])
print("")

# there are some built in methods that can be used to read the data
# dictionary.keys() - get the keys as a list that we can use to iterate over it
print(usernames.keys())
print("")

for key in usernames.keys():
    print(key + " - " + usernames[key])

print("")

# dictionary.values() - get the values as a list
print(usernames.values())
print("")

# dictionary.items() - get keys and values, returns a list of tuples with the key value pairs
print(usernames.items())
print("")


# how to modify dictionary
# change specific value for key
usernames["name"] = "b"
print(usernames["name"])

print("")

# add new data to dictionary
usernames.update({"groot": "groot123"})
print(usernames)
print("")

# remove data from dicitonary
del usernames["name"]
print(usernames)
print("")

# to remove the last item in the dictionary
usernames.popitem()
print(usernames)
print("")

# copy dictionary
usernames_copy = usernames.copy()
print(usernames_copy)
print("")

# remove all items from dictionary
usernames_copy.clear()
print(usernames_copy)
print("")