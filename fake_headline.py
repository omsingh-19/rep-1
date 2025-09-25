import random
names= ["Shahrukh Khan ", "Virat Kohli ", "Nirmala Sitharaman ", "A Mumbai Cat ", "A Group of Monkeys "]
actions=["launches ", "cancels ", "dances with ", "eats ", "declares war on "]
places=["at Red Fort ", "in Mumbai local train ", "a plate of samosas ", "inside Parliament ", "at Ganga ghat "]
while True:
    a=input("Do you want a news headline(y/n)")
    if a=='y' or a=='Y':
        print(random.choice(names)+random.choice(actions)+random.choice(places))
    elif a=='n' or a=='N':
        print("Have a nice day!")
        break
    else:
        print('Invalid input !')