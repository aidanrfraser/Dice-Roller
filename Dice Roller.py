import random
def add(x,y):
    return x+y
def Roller():
    d1=random.randint(1,6)
    print(d1)
    d2=random.randint(1,6)
    print(d2)
    print("The sum of the dice is ", add(d1,d2))
    if d1==d2:
        print("You got doubles!")
    yess = input("Type y to roll again! ")
    if yess == 'y':
        Roller()
    else:
        print("Goodbye!")
def DiceRoll():
    yess = input("Roll the dice? (y/n) ")
    if yess == 'y':
        Roller()
    else:
        print("Ok, type y to roll if you change your mind!")
        yess = input("")
        if yess == 'y':
            Roller()
        else:
            print("Ok, bye!")
run = input("Would you like to play a game? ")
if run == 'yes':
    DiceRoll()
elif run == 'y':
    DiceRoll()
elif run == 'ye':
    DiceRoll()
elif run == 'yeah':
    DiceRoll()
elif run == "sure":
    DiceRoll()
