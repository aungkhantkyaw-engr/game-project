# Lab 1
# Group #: 10
# Author: Aung Khant Kyaw
# Date: September 28, 2026

import random

def guessing_game():
    """
    Plays a number guessing game.
    The computer generates a random number from 1 to 100.
    The user has five attempts to guess the number.
    
    Author: Aung Khant Kyaw
    """
    
    number = random.randint(1, 100)
    tries = 5
    
    print("\nI'm thinking of a number between 1 and 100.")
    
    while tries > 0:
        guess = int(input(f"Guess what it is. You have {tries} tries: "))
        
        if guess == number:
            print("You got it!")
            return
        
        tries = tries - 1
        
        if tries > 0:
            if guess < number:
                print(f"Nope! Too low. Try again ({tries} tries left).")
            else:
                print(f"Nope! too high. Try again ({tries} tries left).")
                
    print(f"Nope! You lost. The number was {number}.")
    
if __name__ == "__main__":
    play_again = "Y"

    while play_again.upper() == "Y":
        guessing_game()
        play_again = input("Do you want to play again? (Y/N): ")