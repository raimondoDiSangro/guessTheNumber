# A simple "Guess the number" Game that imports and uses the random Module
import random

tries = 0
print('Welcome to the Guess the number game, what is your name?')
name = input()

number = random.randint(1, 1000)
print('Hi ' + name + ' guess what number I picked between 1 and 1000, you have 10 guesses')

for tries in range(10):
    print('Take a guess.')
    guess = input()
    guess = int(guess)  # casting to int whatever we input?!

    if guess < number:
        print('Too low!')

    if guess > number:
        print('Too high!')

    if guess == number:
        break

if guess == number:
    tries = str(tries + 1)
    print('You guessed right, ' + name + 'you needed ' + tries + 'guesses to win')

if guess != number:
    number = str(number)
    print('Sorry ' + name + ' you lost. The number I was thinking of was ' + number)
