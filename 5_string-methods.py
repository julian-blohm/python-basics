# operators can also be used for text
# e.g. to concatenate strings
print("hello" + " " + "there")

# also the multiplier can be used to repeat the string
print("ha" * 10)
print("ha" * 2)
print("ha" * 0)
print("ha" * -1)

# to cast ints etc. to strings, following can be done
print(str(22)) # this is now a string

# example
apple_prize = 2
apple_amount = input("Howe many apples do you want? ")
total_sum = apple_prize * int(apple_amount)

# to print it, we now need it as a string
print("You have to pay: " + str(total_sum))