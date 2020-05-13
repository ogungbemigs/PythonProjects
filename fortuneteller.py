#paper Fortune teller game
import random

answer = 'y'
print("Welcome to Fortune Teller game")
print("You will Select a color and a number and i will tell you what the future holds for you")

while answer == 'y':
    color = input ("Select a color [Yellow, Green, Blue, Red]:b ")
    if color == 'Yellow' or color == 'Green':
        number = int(input("Select a number [1, 2, 5, 6]: "))
        if number == 1:
            print ("Dont worry, be happy")
            elif number == 2:
            print ("Dont worry, be happy")
            elif number == 5:
            print ("Dont worry, be happy")
            elif number == 6:
            print ("Dont worry, be happy")
            else:
            print("Number 1, 2, 5, 6 are the only numbers allowed")
    elif color == 'Blue' or color == 'Red':
        number = int(input("Select a number [3, 4, 7, 8]: "))
        if number == 3:
            print ("Dont worry, be happy")
        elif number == 4:
            print ("Dont worry, be happy")
        elif number == 7:
            print ("Dont worry, be happy")
        elif number == 8:
            print ("Dont worry, be happy")
        else:
            print("Number 3, 4, 7, 8 are the only numbers allowed")
    else:
        print("Colors Yellow, Green, Blue and Red are the only Colors allowed")

    answer = input("play again! insert 'y' for YES and 'n' for NO. ")
