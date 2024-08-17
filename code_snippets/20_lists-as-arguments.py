# lists can be also passed to functions
def multiply_values(list):
   
   # create empty list
    multiplied_values = [] 
   
    # iterate over list and copy each value to our list multiplied by 2
    for item in list:
        multiplied_values.append(item * 2) 
    return multiplied_values

print(multiply_values([1,2,3])) # if a list is not provieded, python would throw an error