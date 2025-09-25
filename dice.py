import random
while True:
    a=input("do you want to roll(y/n)")
    if a=='y' or "Y":
        print('(',random.randint(1,6),",",random.randint(1,6),')')
    elif a=='n' or "N":
        print("thanks for playing")
        break
    else:
        print("invalid input")