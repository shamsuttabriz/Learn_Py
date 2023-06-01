#This is a Guess the number Game:
import random
secretNumber = random.randint(1, 20)

print("I am thinking of number between 1 and 20")


#Ask the player to guess 6 times:
for guessTaken in range(0, 6):
    print('Take a guess of Number: ')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess no is too high. Please guess the low no.')
    elif guess < secretNumber:
        print('Your guess no is too low. Please guess the high no.')
    else :
        break

if (guess == secretNumber):
    print("Great! Your guessed my number is " + str(guessTaken+1) + " guesses")
else:
    print("Sorry! The number I was thinking of was " + str(secretNumber))