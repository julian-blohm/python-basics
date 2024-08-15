# logical operators “and” “not” and “or” return boolean values based on the passed values
age1 = 24
age2 = 16

if (age1 >= 18 and age2 >= 18):
    print("Both are adults")
elif (age1 >= 18 or age2 >= 18):
    print("One of you is an adult")
else:
    print("Both of you are minors")

is_hungry = False
if (not is_hungry):
    print("you are not hungry")