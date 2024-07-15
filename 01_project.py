import random
# snake water gun or rock paper scissors

def gamewin(Comp, you):
    if Comp == you:
        return None
    elif Comp == 'S':
        if you == 'W':
            return False
        elif you=='g':
            return True
        elif Comp == 'W':
            if you == 'g':
                return False
        elif you=='S':
            return True
    elif Comp == 'g':
        if you == 'S':
            return False
        elif you=='W':
            return True

a = input("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    Comp = 'S'
elif randNo == 2:
        Comp = 'W'
elif randNo == 3:
            Comp = 'g'

you= input("Your Turn: Snake(s) Water(w) or Gun(g)?")

a = gamewin(Comp, you)
if a == None:
    print("The game is a tie!")
elif  a :
    print("You win")
else:
    print("You  Lose!")