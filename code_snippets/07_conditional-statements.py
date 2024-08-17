# conditions - if/else statements allow to run code conditionally
age = int(input("How old are you?"))

# colon ':' needed after if statement
if age >= 18:
    if age == 18:
        print("You are 18 years old")
    else:
        print("You are an adult")
elif age < 6:
    print("You are younger than 6")
else:
    print("You are a child")