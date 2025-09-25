import random
a=['r','p','s']
while True:
    computer_choice=a[random.randint(0,2)]
    user_choice=input("rock , paper or scissors(r , p , s)")
    print("computer choose-->",computer_choice)
    print("you chose-->",user_choice)
    if computer_choice=='r' and user_choice=='s' :
        print("you  lost")
    elif computer_choice=='p' and user_choice=='r':
        print("you  lost")
    elif  computer_choice=='s' and user_choice=='p':
        print("you  lost")
    elif computer_choice=='r' and user_choice=='p':
        print("you  won")
    elif computer_choice=='p' and user_choice=='s':
        print("you  won")
    elif computer_choice=='s' and computer_choice=='r':
        print("you  won")
    elif computer_choice==computer_choice:
        print('its a tie!')
    else:
        print("invalid input")
    q=input("continue?(y,n)")
    if q=='y':
        pass
    elif q=="n":
        print("thanks for playing!")
        break
    else:
        print("invaild responce!")
        break