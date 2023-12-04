#Name: Pranav Parekh, Sachee
#Date: 12/01/2023
#Description: Working on the GameEngine class to provide functionality to the game

#Importing random for random number generation
import random

class GameEngine:
    # Private constants
    _NUMBEROFVEGGIES = 30
    _NUMBEROFRABBITS = 5
    _HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        # Member variables
        self.field = []  # List representing the field
        self.rabbits = []  # List representing the rabbits in the field
        self.captain = None  # Variable representing the captain object
        self.vegetables = []  # List representing all possible vegetables in the game
        self.score = 0  # Variable representing the score

    def initVeggies(self):
        # Prompt user for the veggie file
        veggie_file_name = input("Enter the name of the veggie file: ")

        # Repeatedly prompt until a file that exists appears
        while not os.path.exists(veggie_file_name):
            print("File not found. Please enter a valid file name.")
            veggie_file_name = input("Enter the name of the veggie file: ")

        # Reading the veggie file and initializing the field and possible vegetables
        with open(veggie_file_name, 'r') as file:
            # Read the first line to initialize the field to None
            dimensions = file.readline().split()
            rows, cols = int(dimensions[0]), int(dimensions[1])
            self.field = [[None for _ in range(cols)] for _ in range(rows)]

            # Reading the remaining lines to create Veggie objects
            for line in file:
                veggie_data = line.strip().split()
                veggie_name = veggie_data[0]
                veggie_points = int(veggie_data[1])
                self.vegetables.append(Veggie(veggie_name, veggie_points))

            # Populate the field with NUMBEROFVEGGIES Veggie objects
            for _ in range(self._NUMBEROFVEGGIES):
                veggie = random.choice(self.vegetables)
                row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

                # Check if the chosen location is occupied
                while self.field[row][col] is not None:
                    row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

                # Place the Veggie object in the chosen location
                self.field[row][col] = veggie

    def initCaptain(self):
        rows, cols = len(self.field), len(self.field[0])

        # Choose a random location for the Captain object
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

        # Check if the chosen location is occupied
        while self.field[row][col] is not None:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

        # Create a new Captain object and store it in the appropriate member variable
        self.captain = Captain(row, col)

        # Place the Captain object in the chosen location on the field
        self.field[row][col] = self.captain

    def initRabbits(self):
        rows, cols = len(self.field), len(self.field[0])

        for _ in range(self._NUMBEROFRABBITS):
            # Choose a random location for the Rabbit object
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

            # Check if the chosen location is occupied
            while self.field[row][col] is not None:
                row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

            # Create a new Rabbit object
            rabbit = Rabbit(row, col)  # Replace with your Rabbit class and constructor

            # Add the Rabbit object to the List of rabbits
            self.rabbits.append(rabbit)

            # Place the Rabbit object in the chosen location on the field
            self.field[row][col] = rabbit

    def initializeGame(self):
        # Calling the initVeggies() method
        self.initVeggies()

        # Calling the initCaptain() method
        self.initCaptain()

        # Calling the initRabbits() method
        self.initRabbits()

    #Calculation of the remaining veggies
    def remainingVeggies(self):
        remaining_veggies = sum(row.count(None) for row in self.field)
        return remaining_veggies

    #Introduction of the game to the user
    def intro(self):
        print("Welcome to the Vegetable Harvest Game!")
        print("In this game, you will play as Captain Veggie and your goal is to harvest as many vegetables as possible.")
        print("Be careful of the rabbits roaming in the field, as they may eat the vegetables!")
        print("\nList of Possible Vegetables:")
        for veggie in self.vegetables:
            veggie.printInfo()  # Replace with the appropriate method in your Veggie class
        print(f"\nCaptain Veggie Symbol: {self.captain.getSymbol()}")  # Replace with the appropriate method in your Captain class
        print("Rabbit Symbol: R")

    #Printing function
    def printField(self):
        print("Field:")
        for row in self.field:
            print(" | ".join(str(cell) if cell is not None else " " for cell in row))
            print("-" * (4 * len(row) - 1))

    # Function to get the score value
    def getScore(self):
        return self.score

    # A function that moves the rabbit object in the game
    def moveRabbits(self):
        for rabbit in self.rabbits:
            # Store the current location of the Rabbit
            current_row, current_col = rabbit.getRow(), rabbit.getCol()

            # Choose a random direction (up, down, left, right, diagonal, or no move)
            move_direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (0, 0)])

            # Calculate the new location
            new_row, new_col = current_row + move_direction[0], current_col + move_direction[1]

            # Check if the new location is within the boundaries of the field
            if 0 <= new_row < len(self.field) and 0 <= new_col < len(self.field[0]):
                # Check if the new location is not occupied by another Rabbit or Captain
                if self.field[new_row][new_col] is None or isinstance(self.field[new_row][new_col], Veggie):
                    # Move the Rabbit to the new location
                    self.field[current_row][current_col] = None
                    self.field[new_row][new_col] = rabbit

                    # Update Rabbit's member variables with the new location
                    rabbit.setRow(new_row)
                    rabbit.setCol(new_col)

                    # If Rabbit moved into a space occupied by Veggie, remove the Veggie from the field
                    if isinstance(self.field[new_row][new_col], Veggie):
                        self.score += self.field[new_row][new_col].getPoints()
                        self.field[new_row][new_col] = rabbit

                    # If Rabbit moved, set its previous location to None
                    if current_row != new_row or current_col != new_col:
                        self.field[current_row][current_col] = None
                        
#For movement of the captian
    def moveCptVertical(self, vertical_movement):
        current_row, current_col = self.captain.getRow(), self.captain.getCol()

        # Calculate the new location based on the vertical movement
        new_row, new_col = current_row + vertical_movement, current_col

        # Check if the new location is within the boundaries of the field
        if 0 <= new_row < len(self.field):
            target_object = self.field[new_row][new_col]

            # If the new location is an empty slot
            if target_object is None:
                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.setRow(new_row)
                self.captain.setCol(new_col)

            # If the new location is occupied by a Veggie
            elif isinstance(target_object, Veggie):
                veggie_name = target_object.getName()
                veggie_points = target_object.getPoints()

                print(f"A delicious vegetable ({veggie_name}) has been found!")
                self.captain.addVeggie(target_object)
                self.score += veggie_points

                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.setRow(new_row)
                self.captain.setCol(new_col)

            # If the new location is occupied by a Rabbit
            elif isinstance(target_object, Rabbit):
                print("Oops! You should not step on the rabbits.")
                # Do not move the Captain object

            # If the Captain moved, set its previous location to None
            if current_row != new_row or current_col != new_col:
                self.field[current_row][current_col] = None

    def moveCptHorizontal(self, horizontal_movement):
        current_row, current_col = self.captain.getRow(), self.captain.getCol()

        # Calculate the new location based on the horizontal movement
        new_row, new_col = current_row, current_col + horizontal_movement

        # Check if the new location is within the boundaries of the field
        if 0 <= new_col < len(self.field[0]):
            target_object = self.field[new_row][new_col]

            # If the new location is an empty slot
            if target_object is None:
                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.setRow(new_row)
                self.captain.setCol(new_col)

            # If the new location is occupied by a Veggie
            elif isinstance(target_object, Veggie):
                veggie_name = target_object.getName()
                veggie_points = target_object.getPoints()

                print(f"A delicious vegetable ({veggie_name}) has been found!")
                self.captain.addVeggie(target_object)
                self.score += veggie_points

                self.field[current_row][current_col] = None
                self.field[new_row][new_col] = self.captain
                self.captain.setRow(new_row)
                self.captain.setCol(new_col)

            # If the new location is occupied by a Rabbit
            elif isinstance(target_object, Rabbit):
                print("Oops! You should not step on the rabbits.")
                # Do not move the Captain object

            # If the Captain moved, set its previous location to None
            if current_row != new_row or current_col != new_col:
                self.field[current_row][current_col] = None

    def moveCaptain(self):
        valid_directions = ['w', 's', 'a', 'd', 'W', 'S', 'A', 'D']

        # Prompt the user for direction input
        direction = input("Enter the direction to move the Captain (Up: W, Down: S, Left: A, Right: D): ").lower()

        # Check if the input is a valid direction
        if direction in valid_directions:
            # Check the user's input and call the appropriate movement function
            if direction == 'w':
                self.moveCptVertical(-1)  # Move up
            elif direction == 's':
                self.moveCptVertical(1)  # Move down
            elif direction == 'a':
                self.moveCptHorizontal(-1)  # Move left
            elif direction == 'd':
                self.moveCptHorizontal(1)  # Move right
        else:
            print("Invalid direction. Please enter a valid direction (W, S, A, D).")

#A test run
#game = GameEngine()
#game.moveCaptain()

