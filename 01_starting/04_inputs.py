# prompts user to input some data from the console
# accepts optional parameter that can be used to write a message to the user before input
# always returns string
# input function asks user for input from console
input("How are you?")

print("/nTry again and store in variable ")

favorite_color = input("What is your favorite Color?")
print("Your favorite color is " + favorite_color)

# value of input is always a string
# we can use type casting to change type of data int(), float()

age = input("How old?")

print(int(age) - 10)
print(float(age) - 10)

# also possible to be used for input function
age_again = int(input("how old?"))

print(age_again)
