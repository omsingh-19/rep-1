while True:
    print("press 1--> addition")
    print("press 2--> subtractin")
    print("press 3--> multiplication")
    print("press 4--> dvision")
    a=int(input("press 5--> exit"))
    if a==5:
        break
    b=int(input("enter the first number"))
    c=int(input("enter the second number"))
    if a==1:
        print(b,'+',c,'= ',b+c)
    elif a==2:
        print(b,'-',c,'= ',b-c)
    elif a==3:
        print(b,'*',c,'= ',b*c)
    elif a==4:
        if c!=0:
            print(b,'/',c,'= ',b/c)
        else:
            print('cannot divide by 0!!')
    else:
        print('invalid input!!')
print('Have a nice day!')

    