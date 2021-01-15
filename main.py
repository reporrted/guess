# This is a guess the number game.
import random
print('Hello, what is your name.')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 10.')
secretNumber = random.randint(1, 10)

# Ask the player to guess 6 times.
for guesses in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # This is the correct guess.

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guesses) + ' guesses.')
else:
    print('No, the number I was thinking of was ' + str(secretNumber) + '.')
