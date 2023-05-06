# Rock Paper Scissors Game Individual Assignment 
import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Initialize the user and computer scores
user_score = 0
computer_score = 0
draw_count = 0

# Start the game
while True:

    # Get the user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ")

    # Make the computer's choice
    computer_choice = random.choice(choices)

    # Compare the choices and determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
        draw_count += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock smashes scissors.")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper covers rock.")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors cuts paper.")
        user_score += 1
    else:
        print("The computer wins!")
        computer_score += 1

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ")

    # If the user doesn't want to play again, print the final scores and exit the game
    if play_again == "n":
        print("Final scores:")
        print("User:", user_score)
        print("Computer:", computer_score)
        print("Draws:", draw_count)
        break
