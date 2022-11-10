print("Welcome to Guess the number !")
print("THe rules are simple.Iwill think of number,and you will try to guess it ")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight !=True:
    guess = input("Guess a number between 1 and 10:")
    if int(guess) ==number:
        print("You guessed {}. This is correct ! You win!".format(guess))
        isGuessRight =True
    else:
        print("You gussed {}. Sorry,that isnt it.try again.".format(guess))
        print("Count to 10!")