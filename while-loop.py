#A while loop makes a section of code repeat until a certain condition is met.

import random   

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#generate a target number to guess
number=random.randint(1,10)
#declare a condition used for the while loop
isGuessRight=False

while isGuessRight!=True:
    guess=input("Guess a number between 1 and 10: ")
    #if the guess is right
    if int(guess)==number:
        print(f'You guessed {guess}. That is correct! You win!')
        #Stop the while loop
        isGuessRight=True
    else:
        #the loop keeps going
        print(f'You guessed {guess}. Sorry, that is not it. Try again.')

