# you can slice a list by defining start and end of a list mylist[start:end]
# start would be included, end not
letters = ['A', 'B', 'C', 'D', 'E']
firstTwo = letters[0:2]
print(firstTwo)
print('')

# if only start, will be sliced from there
print(letters[1:])
print('')

# if only end, will sliced until the end
print(letters[:3])
print('')

# negative indices also possible e.g. to cut first and last element (sometimes you dont know the length)
print(letters[1:-1])
print('')

# also possible without specifying indices, basically copys the list into a new list in memory
print(letters[:])
print('')

# if using del, original list will be modified
del letters[1:3]
print(letters)
print('')

# with del also all letters can be deleted from list
del letters[:]
print(letters)
print('')