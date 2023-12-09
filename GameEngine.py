#Name: Pranav Parekh, Shachee SB
#Date: 12/01/2023
#Description: Working on the GameEngine class to provide functionality to the game

import os
import pickle
# Importing random for random number generation, and pickle for file storgae
import random
import csv

# Importing the classes and subclasses from the other files
from Captain import Captain, Creature
from Rabbit import Rabbit, Creature
from Veggie import Veggie, FieldInhabitant

#For the bonus question
from Snake import Snake


class GameEngine:
    # Initialization of the Private constants
    _NUMBEROFVEGGIES = 30
    _NUMBEROFRABBITS = 5
    _HIGHSCOREFILE = "highscore.data"

    #Constructor for the introduction of the variables
    def __init__(self):
        # Member variables
        self.field = []  # List representing the field
        self.rabbits = []  # List representing the rabbits in the field
        self.captain = None  # Variable representing the captain object
        self.vegetables = []  # List representing all possible vegetables in the game
        self.score = 0  # Variable representing the score

        #For the Bonus
        #self.snake = None

    #Loading the veggie file and performing initialization
    def initVeggies(self):

        # Prompt the user for the name of the veggie file
        filename = input("Enter the name of the veggie file: ")

        # Check if the file exists, and prompt for a new file name until a valid one is provided
        while not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            filename = input("Enter a valid veggie file name: ")

        try:
            with open(filename, 'r', newline='') as csvfile:
                csvreader = csv.reader(csvfile)

                # Read the first line to initialize the field size
                first_line = next(csvreader)
                field_size = (int(first_line[1]), int(first_line[2]))
                self.field = [[None] * field_size[1] for _ in range(field_size[0])]

                # Read the remaining lines to create and place Veggie objects

                for row in csvreader:
                    veggie_name, veggie_symbol, veggie_points = row
                    veggie = Veggie(veggie_name, veggie_symbol, int(veggie_points))
                    self.vegetables.append(veggie)
                    #print(self.vegetables)

                # Place the desired number of Veggie objects in the field
                for _ in range(self._NUMBEROFVEGGIES):
                    if len(self.vegetables) <= self._NUMBEROFVEGGIES:
                        veggie = random.choice(self.vegetables)
                        #veggies.remove(veggie)
                        self.placeVeggieRandomly(veggie)



        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")
        finally:
            csvfile.close()

    def placeVeggieRandomly(self, veggie):
        #Randomly select places to place our veggies
        while True:
            row = random.randint(0, len(self.field) - 1)
            col = random.randint(0, len(self.field[0]) - 1)

            # Check if the location is empty
            if self.field[row][col] is None:
                # Place the Veggie object in the field
                self.field[row][col] = veggie
                break

    # Function for Initialization of the Captain Object location
    def initCaptain(self):
        # Choose a random location for the Captain object
        row, col = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)

        # Check if the chosen location is occupied
        while self.field[row][col] is not None:
            row, col = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)

        # Create a new Captain object
        captain = Captain(row, col)

        # Set the initial position of the Captain
        captain.set_y(row)
        captain.set_x(col)

        # Add the Captain object to the list of captains
        self.captain = captain

        # Place the Captain object in the chosen location on the field
        self.field[row][col] = captain


    #Function for the initialization of the rabbit objects
    def initRabbits(self):

        # Place the initial Rabbit object in the field
        initial_rabbit = Rabbit()
        self.rabbits.append(initial_rabbit)

        # Find an empty location for the initial rabbit
        while True:
            row = random.randint(0, len(self.field) - 1)
            col = random.randint(0, len(self.field[0]) - 1)

            # Check if the location is empty and not occupied by Captain or Veggie
            if self.field[row][col] is None and not isinstance(self.field[row][col], (Captain, Veggie)):
                # Place the Rabbit object in the field
                self.field[row][col] = initial_rabbit
                initial_rabbit.set_y(row)
                initial_rabbit.set_x(col)
                break

        # Place the remaining Rabbit objects in the field
        for _ in range(self._NUMBEROFRABBITS - 1):
            self.placeRabbitRandomly()

    #We separate out the place rabbit function separately to avoid the creation of extra rabbits
    def placeRabbitRandomly(self):
        rabbit = Rabbit()

        # Find an empty location for the rabbit
        while True:
            row = random.randint(0, len(self.field) - 1)
            col = random.randint(0, len(self.field[0]) - 1)

            # Check if the location is empty and not occupied by Captain, Veggie, or another Rabbit
            if self.field[row][col] is None and not isinstance(self.field[row][col], (Captain, Veggie, Rabbit)):
                # Place the Rabbit object in the field
                self.field[row][col] = rabbit
                rabbit.set_y(row)
                rabbit.set_x(col)
                self.rabbits.append(rabbit)
                break

    #A function to initialize the Game
    def initializeGame(self):
        # Calling the initVeggies() method
        self.initVeggies()

        # Calling the initCaptain() method
        self.initCaptain()

        # Calling the initRabbits() method
        self.initRabbits()

        #For the bonus question: Calling the initSnake() method
        #self.initSnake()

    #Calculates the number of veggies remaining
    def remainingVeggies(self):
        # Count the number of non-empty slots in each row and sum them up
        #total_non_empty_slots = sum(row.count(obj) for row in self.field for obj in row if obj is not None)
        #/ Simplifying the code/ Count will not work
        total_non_empty_slots = 0
        for row in self.field:
            for obj in row:
                if obj is not None:
                    total_non_empty_slots += 1

        # Subtract the number of rabbits and the Captain present on the field
        #total_non_empty_slots -= 6

        #If we include the Snake as per our bonus question, we should subtract 7 instead of 6
        total_non_empty_slots -= 7

        return total_non_empty_slots

    #Introduction of the game to the user
    def intro(self):
        print("Welcome to Captain Veggie!")
        print("=========================================")
        print("In this game, you play as Captain Veggie,")
        print("a fearless character on a mission to collect")
        print("delicious vegetables while avoiding pesky rabbits.")
        print("Your goal is to achieve the highest score possible.")
        print("=========================================")

        # Display the list of possible vegetables with symbols, names, and point values
        print("List of Vegetables:")
        for veggie in self.vegetables:
            print(f"{veggie.get_symbol()} - {veggie.get_name()}: {veggie.get_points()} points")

        # Display Captain Veggie and Rabbit symbols
        print("=========================================")
        print(f"Captain Veggie Symbol: {self.captain.get_symbol()}")
        #print(f"Rabbit Symbol: {self.rabbits.get_symbol()}")
        print(f"Rabbit Symbol: R")
        print("=========================================")
        print("Get ready to embark on your veggie adventure!")

    #Printing function
    def printField(self):
        print("Field:")
        print("############################################")
        for row in self.field:
            print(" | ".join(str(cell) if cell is not None else " " for cell in row))

        print("############################################")

    # Function to get the score value
    def getScore(self):
        return self.score

    # A function that moves the rabbit object in the game
    def moveRabbits(self):
        for rabbit in self.rabbits:
            # Since row represents vertical movement, we represent it as the y coordinate
            # and col represents horizontal movement, we represent it as x coordinate
            current_row, current_col = rabbit.get_y(), rabbit.get_x()

            # Choose a random direction (up, down, left, right, diagonal, or no move)
            move_direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (0, 0)])

            # Calculate the new location
            new_row, new_col = current_row + move_direction[0], current_col + move_direction[1]

            # Check if the new location is within the boundaries of the field
            if 0 <= new_row < len(self.field) and 0 <= new_col < len(self.field[0]):
                # Check if the new location is not occupied by another Rabbit, Captain, or Veggie
                target_object = self.field[new_row][new_col]
                if target_object is None or isinstance(target_object, Veggie):
                    if not isinstance(target_object, Rabbit):
                        # Move the Rabbit to the new location
                        self.field[current_row][current_col] = None
                        self.field[new_row][new_col] = rabbit

                        # Update Rabbit's member variables with the new location
                        rabbit.set_y(new_row)
                        rabbit.set_x(new_col)

                        # If Rabbit moved, set its previous location to None
                        if current_row != new_row or current_col != new_col:
                            self.field[current_row][current_col] = None

    #Part 3: For the movement of the captain
    def moveCptVertical(self, vertical_movement):
        # Get the current position of the Captain
        current_row, current_col = self.captain.get_y(), self.captain.get_x()

        # Calculate the new location based on the vertical movement
        new_row, new_col = current_row + vertical_movement, current_col

        # Check if the new location is within the boundaries of the field
        if 0 <= new_row < len(self.field):
            target_object = self.field[new_row][new_col]

            # If the new location is an empty slot
            if target_object is None:
                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.set_y(new_row)
                self.captain.set_x(new_col)

            # If the new location is occupied by a Veggie
            elif isinstance(target_object, Veggie):
                veggie_name = target_object.get_name()
                veggie_points = target_object.get_points()

                print(f"A delicious vegetable ({veggie_name}) has been found!")
                self.captain.add_veggie(target_object)
                self.score += veggie_points

                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.set_y(new_row)
                self.captain.set_x(new_col)

            # If the new location is occupied by a Rabbit
            elif isinstance(target_object, Rabbit):
                print("Oops! You should not step on the rabbits.")
                return
                # Do not move the Captain object

            # If the Captain moved, set its previous location to None
            if current_row != new_row or current_col != new_col:
                self.field[current_row][current_col] = None

    def moveCptHorizontal(self, horizontal_movement):
        # Get the current position of the Captain
        current_row, current_col = self.captain.get_y(), self.captain.get_x()

        # Calculate the new location based on the horizontal movement
        new_row, new_col = current_row, current_col + horizontal_movement

        # Check if the new location is within the boundaries of the field
        if 0 <= new_col < len(self.field[0]):
            target_object = self.field[new_row][new_col]

            # If the new location is an empty slot

            if target_object is None:
                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.set_y(new_row)
                self.captain.set_x(new_col)

            # If the new location is occupied by a Veggie
            elif isinstance(target_object, Veggie):
                veggie_name = target_object.get_name()
                veggie_points = target_object.get_points()

                print(f"A delicious vegetable ({veggie_name}) has been found!")
                self.captain.add_veggie(target_object)
                self.score += veggie_points

                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.set_y(new_row)
                self.captain.set_x(new_col)

            # If the new location is occupied by a Rabbit
            elif isinstance(target_object, Rabbit):
                print("Oops! You should not step on the rabbits.")
                return
                # Do not move the Captain object

            # If the Captain moved, set its previous location to None
            #We use the current position for movement because we do not want to duplicate our captain by mistake
            if current_row != new_row or current_col != new_col:
                self.field[current_row][current_col] = None

    def moveCaptain(self):
        valid_directions = ['w', 's', 'a', 'd', 'W', 'S', 'A', 'D']

        # Prompt the user for direction input
        direction = input("Enter the direction to move the Captain (Up: W, Down: S, Left: A, Right: D): ")

        # Check if the input is a valid direction
        if direction in valid_directions:
            # Check the user's input and call the appropriate movement function
            if direction == 'w' or direction == 'W':
                self.moveCptVertical(-1)  # Move up
            elif direction == 's' or direction == 'S':
                self.moveCptVertical(1)  # Move down
            elif direction == 'a' or direction == 'A':
                self.moveCptHorizontal(-1)  # Move left
            elif direction == 'd' or direction == 'D':
                self.moveCptHorizontal(1)  # Move right
        else:
            print("Invalid direction. Please enter a valid direction (W, S, A, D).")

#A test run
#game = GameEngine()
#game.moveCaptain()

#Part 4: Ending the game and including the high score
    def gameOver(self):
        print("Game Over!")
        harvested_veggies = [veggie.get_name() for veggie in self.captain.get_collected_veggies()]
        print("You harvested the following vegetables:", ', '.join(harvested_veggies))
        print("Your score:", self.score)

    def highScore(self):
        high_scores = []

        # Check if the highscore.data file exists
        if os.path.exists(self._HIGHSCOREFILE):
            # Open the highscore.data file for binary reading
            with open(self._HIGHSCOREFILE, 'rb') as file:
                # Unpickle the file into the List of high scores
                high_scores = pickle.load(file)

        # Prompt the user for their initials and extract the first 3 characters
        player_initials = input("Enter your initials: ")[:3].upper()

        # Create a Tuple with the player's initials and score
        player_score_tuple = (player_initials, self.score)

        # If there are no high scores yet recorded, add the Tuple to the List
        if not high_scores:
            high_scores.append(player_score_tuple)
        else:
            # Add the Tuple to the correct position in the List
            inserted = False

            for i, (initials, score) in enumerate(high_scores):
                if self.score > score:
                    high_scores.insert(i, player_score_tuple)
                    inserted = True
                    break

            # If the score is not higher than any existing scores, append it to the end
            if not inserted:
                high_scores.append(player_score_tuple)

        # Output the high scores
        print("\nHigh Scores:")
        for i, (initials, score) in enumerate(high_scores, start=1):
            print(f"{i}. {initials}: {score}")

        # Open the highscore.data file for binary writing
        with open(self._HIGHSCOREFILE, 'wb') as file:
            # Pickle the List of high scores to the file
            pickle.dump(high_scores, file)


"""
    #Bonus Question: Snake functions
    #Performing initialization of the snake in the same manner as that of the captain
    def initSnake(self):
        if self.snake is None:
            # Choose a random location for the Snake object
            row, col = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)

            # Check if the chosen location is occupied
            while self.field[row][col] is not None:
                row, col = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)

            # Create a new Snake object
            snake = Snake(row, col)

            # Set the initial position of the Snake
            snake.set_y(row)
            snake.set_x(col)

            # Add the Snake object to the list of snakes
            #self.snake = snake

            # Place the Snake object in the chosen location on the field
            self.field[row][col] = snake

    def moveSnake(self):
        # Check if the snake object exists
        if self.snake is not None:
            # Get the current position of the captain
            captain_pos_x, captain_pos_y = self.captain.get_x(), self.captain.get_y()

            # Calculate the direction from the snake towards the captain
            direction_x, direction_y = self.calculateSnakeDirection(captain_pos_x, captain_pos_y)

            # Calculate the new position for the snake
            new_row, new_col = self.snake.get_y() + direction_y, self.snake.get_x() + direction_x

            # Check if the new position is within the boundaries of the field
            if 0 <= new_row < len(self.field) and 0 <= new_col < len(self.field[0]):
                target_object = self.field[new_row][new_col]

                # Check if the new location is not occupied by a vegetable or rabbit
                if target_object is None or target_object.get_symbol() == 'V':
                    # Move the snake to the new location
                    self.field[self.snake.get_y()][self.snake.get_x()] = None
                    self.field[new_row][new_col] = self.snake
                    self.snake.y, self.snake.x = new_row, new_col

                    # If the snake moved into a space occupied by Captain, deduct vegetables
                    if target_object is not None and target_object.get_symbol() == 'V':
                        self.deductVegetablesFromCaptain(5)
                        self.resetSnakePosition()
                else:
                    # If the new location is occupied by a vegetable or rabbit, reset the snake position
                    self.resetSnakePosition()
            else:
                # If the new location is outside the field, reset the snake position
                self.resetSnakePosition()

    def calculateSnakeDirection(self, captain_pos_x, captain_pos_y):
        # Calculate the direction from the snake towards the captain
        row_diff = captain_pos_y - self.snake.get_y()
        col_diff = captain_pos_x - self.snake.get_x()

        # Determine the direction to move
        if abs(row_diff) > abs(col_diff):
            return (1 if row_diff > 0 else -1, 0)
        else:
            return (0, 1 if col_diff > 0 else -1)

    def deductVegetablesFromCaptain(self, amount):
        # Deduct vegetables from the captain's basket
        if amount > 0:
            captain = self.field[self.snake.get_y()][self.snake.get_x()]
            captain.deductVegetables(amount)

    #We want to reset the snake position after the snake has discovered the captain
    def resetSnakePosition(self):
        if self.snake is not None:
            # Reset the snake to a new random, unoccupied position on the field
            empty_positions = [(r, c) for r in range(len(self.field)) for c in range(len(self.field[0])) if
                               self.field[r][c] is None]
            if empty_positions:
                new_pos_x, new_pos_y = random.choice(empty_positions)
                self.field[self.snake.get_y()][self.snake.get_x()] = None
                self.field[new_pos_x][new_pos_y] = self.snake
                self.snake.y, self.snake.x = new_pos_y, new_pos_x

"""
