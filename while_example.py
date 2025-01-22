#you have 3 lives, you roll a dice, if you get a 6 you win.
#If you don't get a 6, you lose a life. #Let's code this shit using "while".
from random import randint

Lives = 3
while Lives > 0: #meaning that as long as i have more lives than 0
    #Roll the dice
    dice = randint (1, 6) #Never add the a and b, it is done on its own
    if dice == 6:
        print("You rolled a 6! You win Oh My God!")
        break
    Lives = Lives - 1
    print("You rolled a", dice, "you have", Lives, "left")

if Lives == 0:
    print ("You Lose Boy You Ass!")