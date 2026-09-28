# Lab 1
# Group #: 10
# Author: Paul Shin
# Date: September 29, 2026

from guessing import guessing_game

from rps import rock_paper_scissors
def choose_game():
    """
    Asks the user which game they want to play.
    Keeps asking until the user enters 1, 2, or 3.
    Returns the choice as a string.

    Author: Paul Shin
    """

    while True:
        choice = input("\nWhich game do you want to play? "
                       "1. Guessing Game, 2. Rock-paper-scissors, 3. Quit: ")

        if choice in ("1", "2", "3"):
            return choice

        print("Invalid choice. Please enter 1, 2, or 3.")


def play_game(choice):
    """
    Calls the game function that matches the user's choice.

    Author: Paul Shin
    """

    if choice == "1":
        guessing_game()
    elif choice == "2":
        rock_paper_scissors()


def main():
    """
    Main program. Lets the user play multiple games, multiple times.
    After each game, the user can play again, switch games, or quit.

    Author: Paul Shin
    """

    print("Welcome to the Game Center!")
    choice = choose_game()

    while choice != "3":
        play_game(choice)

        next_step = input("\nPlay again (A), switch games (S), or quit (Q)? ").upper()

        if next_step == "S":
            choice = choose_game()
        elif next_step == "Q":
            choice = "3"
        elif next_step != "A":
            print("Invalid choice. Playing the same game again.")

    print("Thanks for playing. Goodbye!")


if __name__ == "__main__":
    main()
