import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

#failed attempt :

#number = random.randrange(1,10)
#guess = input("Guess a number from 1 to 10: ")
#guess = int(guess)
#if guess == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
#    if guess == number:
#        print("Great job! You got it!")
#    if guess != number:
#         print("Sorry, better luck next time.")
#         print("The number was " + str(number))
#else:
#    print("Hey! I said a number!")

number = random.randrange(1,10)
guess = input("Guess a number from 1 to 10: ")
guess = int(guess)
if guess == number:
    print("Great job! You got it!")
else:
    print("Sorry, better luck next time.")
    print("The number was " + str(number))