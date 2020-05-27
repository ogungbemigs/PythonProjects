#number guessing game
import random

true_number = random.randint(1, 49)

print ("Welcome to Number Guessing Game!!!!")
print ("A number will be generated randomly by the system, we will like you to guess what the number is! ")

print ("....................................................")

guess_number = int(input("Enter a number between 1 and 49: "))

while True:
    if guess_number == true_number:
        print ("You are right! Good Job!!!")
        break
    elif guess_number < true_number:
        print ("Your guess is low, Try Again")
        guess_number = int(input("Enter a number between 1 and 49: "))

    elif guess_number > true_number:
        print("Your guess is high, try again")
        guess_number = int(input("Enter a number between 1 and 49: "))
