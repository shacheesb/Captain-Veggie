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