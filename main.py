#Name: Pranav Parekh, Shachee SB
#Date; 12/08/2023
#Description: The main function that implements the methods of the Game Engine

from GameEngine import GameEngine

def main():
    """
    Main function to run the vegetable harvest game.
    """
    # Instantiate and store a GameEngine object
    game = GameEngine()

    # Initialize the game
    game.initializeGame()

    # Display the game's introduction
    game.intro()

    # Variable to store the number of remaining vegetables in the game
    remaining_vegetables = game.remainingVeggies()

    # While there are still vegetables left in the game
    while remaining_vegetables > 0:
        # Output the number of remaining vegetables and the player's score
        print(f"\nRemaining Vegetables: {remaining_vegetables}")
        print(f"Player's Score: {game.getScore()}")

        # Print out the field
        game.printField()

        # Move the rabbits
        game.moveRabbits()

        # Move the captain
        game.moveCaptain()

        #Moving the Snake: Bonus
        #game.moveSnake()

        # Determine the new number of remaining vegetables
        remaining_vegetables = game.remainingVeggies()

    # Display the Game Over information
    game.gameOver()

    # Handle the High Score functionality
    game.highScore()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
