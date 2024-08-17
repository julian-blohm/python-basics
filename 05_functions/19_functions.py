# defining function with return value
def input_number():
    return int(input("Enter a number 1: "))
# function has to be defined before invoked
input1 = input_number()
print(input1)
print("")

# arguments for functions
def input_other_number(num):
    return int(input("Enter a number 2: ")) * num

input2 = input_other_number(10)
print(input2)
print("")


# function with multiple parameter
def input_multiple_numbers(num1, num2):
    return int(input("Enter a number 3: ")) * num1 - num2

input3 = input_multiple_numbers(10, 10)
print(input3)
print("")

# also possible to define which value is for which parameter 
input4 = input_multiple_numbers(num2=10, num1=20)
print(input4)
print("")

# default values also possible, parameter is optional then
def input_number_default(num = 10):
    return int(input("Enter number 5: ")) * num

print(input_number_default())
print("")
print(input_number_default(5))
print("")

# functions don't need to return a value but return can also be used to end a function early

def print_mysum(num1, num2):
    mysum = num1 + num2 # vars declared inside a function, cannot be used outside of it
    if(mysum == 0):
        return
    print("The mysum is: " + mysum)

print_mysum(1, 1)
print_mysum(-1, 1)


# scope, if we want to use a var defined within also outside of it use globasl 
def input_mynum():
    global own_num
    own_num = 50
    result = int(input("Enter a Number: ")) * own_num
    return result

input_mynum()

print(own_num)