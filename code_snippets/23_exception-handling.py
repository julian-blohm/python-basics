# exceptions and errors can be handled
def claculate_input():
    try:
        x = int(input("Enter a number:"))
        y = 1 / x
        print(y)
    except ZeroDivisionError: # you could also list more errors here
        print("You cannot divide by zero")
    except ValueError:
        print("Please provide a number")
    except:
        print("Something else went wrong")

    print("all done")
    return None
claculate_input()


# errors can be handled inside or outside functions
def calculate_input2():
    x = int(input("Enter a number:"))
    y = 1 / x
    print(y)

    return None

try:
    calculate_input2()
except (ZeroDivisionError, ValueError):
    print("Input not possible")
except:
    print("something else wrong")
    raise # raises the error
