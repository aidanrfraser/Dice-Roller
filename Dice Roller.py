def DiceRoll():
    import random
    def add(x,y):
        return x+y
    min=1
    max=6
    yess = input("Roll the dice? (y/n) ")
    if yess == 'y':
        d1=random.randint(min,max)
        print(d1)
        d2=random.randint(min,max)
        print(d2)
        print("The sum of the dice is ", add(d1,d2))
        if d1==d2:
            print("You got doubles!")
        print("Type y to roll again!")
        del yess
        yess = input("")
        if yess == 'y':
            DiceRoll()
        else:
            print("Goodbye!")
    if yess == 0:
        print("Ok, type y to roll if you change your mind!")
        del yess
        yess = float(input(""))
        if yess == 'y':
            DiceRoll()
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
