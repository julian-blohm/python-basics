# lists are mutable and can be modified
# a tuple is immutable and can't be modified
# append or other modifier methods are not allowed als tuples are immutable
tuple1 = (1, 2, 3)
print(tuple1)

# can be used similarly as lists
for item in tuple1:
    print(item)

print(tuple[0:1])

# tuples can contain any type of data like numbers, strings, boolerans, other variables
tuple_var = 3
tuple2 = (1, "one", True, (1, 3), tuple_var)

# tuple with one element also alowed, make sure to write a comma at the end of it
tuple3 = (1,)
tuple4 = 1,