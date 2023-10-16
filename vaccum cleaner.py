class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.row = 0
        self.col = 0

    def clean(self):
        while True:
            self.clean_current_cell()
            if not self.move_to_next_cell():
                break

    def clean_current_cell(self):
        if self.grid[self.row][self.col] == 1:
            print(f"Cleaning cell at row {self.row}, col {self.col}")
            self.grid[self.row][self.col] = 0

    def move_to_next_cell(self):
        if self.row < self.rows - 1:
            self.row += 1
        elif self.col < self.cols - 1:
            self.row = 0
            self.col += 1
        else:
            return False
        return True

if __name__ == "__main__":
    # Define a grid where 1 represents a dirty cell
    grid = [[1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]]

    # Create a vacuum cleaner agent and start cleaning
    #vacuum = VacuumCleaner(grid)
    #vacuum.clean()

#The code you’ve written defines a simple vacuum cleaner agent for a grid environment. The vacuum cleaner starts at the top-left cell of the grid and moves down each column from top to bottom, then moves to the next column from left to right. If a cell is dirty (represented by 1), the vacuum cleaner cleans it and updates the cell to be clean (represented by 0). The cleaning process continues until all cells have been visited.

#Here’s a step-by-step explanation of the code:

#The VacuumCleaner class is defined with methods to initialize the vacuum cleaner (__init__), clean the grid (clean), clean the current cell (clean_current_cell), and move to the next cell (move_to_next_cell).
#In the __init__ method, the vacuum cleaner is initialized with a grid and starting position (top-left cell).
#The clean method starts the cleaning process. It continues cleaning and moving to the next cell until all cells have been visited.
#The clean_current_cell method cleans the current cell if it’s dirty.
#The move_to_next_cell method moves the vacuum cleaner to the next cell in the grid. It returns False if all cells have been visited, otherwise it returns True.
#In the main part of the code, a grid is defined, a VacuumCleaner object is created with this grid, and the clean method is called to start the cleaning process.
#This is a simple model of a vacuum cleaner agent and its environment. In a more complex model, you might include obstacles in the environment, allow the agent to perceive its surroundings, or use a more sophisticated strategy for navigating through the grid
