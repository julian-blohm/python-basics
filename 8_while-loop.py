# while loop
secret_number = 3

guess = int(input("What is the secret number?"))
while guess != secret_number:
    guess = int(input("Guess again:"))
else: #can also have an else block; not best practice this way
    print("Congrats you guessed right")


i = 1
x = 5
while True:
    if (i <= x):
        print("i <= x")
        i = i + 3 
    else:
        print("i > x")
        break
