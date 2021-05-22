import random
print("Number Guessing Game")
print("Guess the number between 1 and 9")
# A.I statements required in this project
guessNumber = random.randint(1,9)
guessChances = 5
userGuess = input("Enter your Guess : ")
# conditional statements required in this project
if (guessChances <= 5):
    print(userGuess)

    
if (userGuess == guessNumber & guessChances <= 5):
    print("Congrats you answered it Right !!!")
else:
    print("You were Wrong , try again later ")
