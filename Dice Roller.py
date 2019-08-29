def DiceRoll():
    import random
    def add(x,y):
        return x+y
    min=1
    max=6
    yess = float(input("Roll the dice? 1=yes, 0=no "))
    if yess == 1:
        d1=random.randint(min,max)
        print(d1)
        d2=random.randint(min,max)
        print(d2)
        print("The sum of the dice is ", add(d1,d2))
        if d1==d2:
            print("You got doubles!")
        print("Type 1 to roll again!")
        del yess
        yess = float(input(""))
        if yess == 1:
            DiceRoll()
        else:
            print("Goodbye!")
    if yess == 0:
        print("Ok, type 1 to roll if you change your mind!")
        del yess
        yess = float(input(""))
        if yess == 1:
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
