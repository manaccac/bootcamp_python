import sys
from random import randint

print("This is an interactive guessing game!\n"
      "You have to enter a number between 1 and 99 to find out"
      "the secret number.\n"
      "Type 'exit' to end the game.\n"
      "Good luck!\n")

guess = randint(1, 99)
player_guess = input("What's your guess between 1 and 99?\n")
nb_guess = 1

while (player_guess != guess):
    while(not player_guess.isdigit()):
        if (player_guess == "exit"):
            print("Goodbye!")
            exit()
        else:
            print("That's not a number.")
            nb_guess += 1
            player_guess = input("What's your guess between 1 and 99?\n")
    player_guess = int(player_guess)
    if(player_guess > guess):
        print("Too high!")
    elif(player_guess < guess):
        print("Too low!")
    else:
        break
    nb_guess += 1
    player_guess = input("What's your guess between 1 and 99?\n")

if (nb_guess == 1 and guess == 42):
    print("The answer to the ultimate question of"
          "life, the universe and everything is 42.")
    print("Congratulations! You got it on your first try!")
    exit()
print("Congratulations, you've got it!")
print("You won in %d attempts!" % nb_guess)
