#Mexxen
#TODO: Veranderen in blind mexxen (bestaat nog niet als app).

import random

score = []
sheet = {'low':None, 'advise':None}



def turn():

    def scoring():
        print("\nYour final throw is " + str(first) + " and " + str(second) + ". Next player may now roll.\n\n")
        score.append(first+second)
        sheet.update({'low':min(score)})
        print(str(sheet['low']) + " is the lowest roll.\n")

    n = 1

    first = random.randint(1, 6)
    second = random.randint(1, 6)
    print(first, second)

    if (first == 1 and second == 2) or (first == 2 and second == 1):
        print("MEXX in " + str(n) + "!!! Next player may now roll.\n\n")
        scoring()
        x = False

    elif (first == 1 and second == 3) or (first == 3 and second == 1):
        print("Adtje aanwijzen! \n")

    elif (first == 2 and second == 3) or (first == 3 and second == 2):
        print("Laaaaageeeeeeer kan niet! \n")

    x = True
    
    while x:

        choice = int(input("Choose: (1) Keep ["+str(first)+"], (2) Keep ["+str(second)+"], (3) Reroll both, (4) End turn (5) Pass with advise \n"))

        if choice == 1:
            second = random.randint(1, 6)
            print(first, second)
            
        elif choice == 2:
            first = random.randint(1, 6)
            print(first, second)

        elif choice == 3:
            first = random.randint(1, 6)
            second = random.randint(1, 6)
            print(first, second)

        elif choice == 4:
            scoring()
            x = False

        elif choice == 5:
            advise = str(input("Type your advise and pass to the next player.\n" ))
            x = False    


        if (first == 1 and second == 2) or (first == 2 and second == 1):
            print("MEXX in " + str(n) + "!!! Next player may now roll.\n\n")
            x = False

        elif (first == 1 and second == 3) or (first == 3 and second == 1):
            print("Adtje aanwijzen! \n")

        elif (first == 2 and second == 3) or (first == 3 and second == 2):
            print("Laaaaageeeeeeer kan niet! \n")
            
        n += 1

        if n == 3:
            scoring()
            x = False
    
play = True

while play:
    turn()   
