# Lab 1
# Group #: 10
# Author: Mark Demot
# Date: September 29, 2026

import random

def rock_paper_scissors():
    """
    Plays a Rock, Paper, Scissors Game
    The player enters one of the options
    The computer chooses its own options
    Final score is shown after the game is over
    
    Author: Mark Demot
    """
    
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    print("===============================")
    print("🎮 WELCOME TO ROCK, PAPER, SCISSORS! 🎮")
    print("Type 'exit' at any time to quit.")
    print("===============================\n")
    to_play = input('Do you want to play(Y/N)?:').lower().strip()
    if to_play !='y':
        print('Okay, maybe next time')
        return
    while True:
        player_choice = input('Please enter your choice(type exit to end game):').lower().strip()
        if player_choice == 'scissor':
            player_choice = 'scissors'
        computer_choice = random.choice(choices)
        if player_choice == 'exit':
            print('Thanks for playing!')
            break

        if player_choice not in choices:
            print('Invalid choice or typo, try again')
            continue

        if player_choice == 'rock' and computer_choice == 'scissors':
            print('Computer chose scissors. You win!')
            player_score += 1
        elif player_choice == 'scissors' and computer_choice == 'paper':
            print('Computer chose paper. You win!')
            player_score += 1
        elif player_choice == 'paper' and computer_choice == 'rock':
            print('Computer chose rock. You win!')
            player_score += 1
        elif computer_choice == 'rock' and player_choice == 'scissors':
            print('Computer chose rock. You lose!')
            computer_score += 1
        elif computer_choice == 'scissors' and player_choice == 'paper':
            print('Computer chose scissors. You lose!')
            computer_score += 1
        elif computer_choice == 'paper' and player_choice == 'rock':
            print('Computer chose paper. You lose!')
            computer_score += 1
        elif player_choice == computer_choice:
            print("It's a draw!")
    print('GAME OVER')
    print(f'Final score -> You: {player_score} - Computer: {computer_score}')
    if player_score > computer_score:
        print('You win!')
    elif player_score == computer_score:
        print("It was a tie game")
    else:
        print('You lose!')

if __name__ == '__main__':
    rock_paper_scissors()