# python offers some methods specifically for lists like list.append() and list.insert()

countries = ["GER", "FRA", "GB"]
# append - add item to the end of the list

countries.append("SPA")
print(countries)
print('')

# insert - add data at a specific index
countries.insert(2, "ITA")
print(countries)
print('')

# to swap values in the list, a temporary variable would be needed
temp_country = countries[0]
countries[0] = countries[1]
countries[1] = temp_country
print(countries)
print('')

# easier way is the following:
countries[0], countries[1] = countries[1], countries[0]
print(countries)
print('')

# sort - sorts values by default ascending starting with lowest number
ages = [55, 10, 20, 72]
ages.sort()
print(ages)
print('')

# reverse - reverses all elements in list
ages.reverse()
print(ages)
print('')