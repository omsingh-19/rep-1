import random
computer_guess=random.randint(1,100)
while True:
    user_guess=int(input("guess a number between 1-100"))
    if user_guess<computer_guess:
        print("too low")
    elif user_guess>computer_guess:
        print("too high")
    else:
        print("you gussed the number!")
        break