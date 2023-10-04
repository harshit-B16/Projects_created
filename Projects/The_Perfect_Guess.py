import random
randNumber = random.randint(1,100)
# print(randNumber)
userGuess = None
guesses = 0
while userGuess != randNumber:
    userGuess = int(input("Enter your guess \n"))
    guesses += 1

    if (userGuess == randNumber):
        print("You guessed it right !!")

    else:
        if userGuess > randNumber:
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
        
print(f"You guess the number in {guesses} times")

with open("Highscore.txt", 'r') as f:
    Highscore = int(f.read())

if (guesses<Highscore):
    print("you have just broken the high score!")
    with open("Highscore.txt", 'w') as f:
        f.write(str(guesses))