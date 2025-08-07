import random

def create_grid(rows, cols):
    """Create a grid with random treasure location."""
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    treasure_row = random.randint(0, rows - 1)
    treasure_col = random.randint(0, cols - 1)
    grid[treasure_row][treasure_col] = 'T'
    return grid, (treasure_row, treasure_col)

def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(' '.join(row))

def get_guess(rows, cols):
    """Get user's guess for treasure location."""
    while True:
        try:
            row = int(input(f"Guess row (0 to {rows - 1}): "))
            col = int(input(f"Guess column (0 to {cols - 1}): "))
            if 0 <= row < rows and 0 <= col < cols:
                return row, col
            else:
                print("Invalid input. Row and column must be within the grid.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_distance(guess, treasure):
    """Calculate the distance between user's guess and treasure."""
    return abs(guess[0] - treasure[0]) + abs(guess[1] - treasure[1])

def main():
    rows, cols = 5, 5
    grid, treasure_location = create_grid(rows, cols)
    print("Welcome to the Treasure Hunt Game!")
    print("Find the treasure by guessing the correct row and column.")

    guesses = 0
    while True:
        print_grid(grid)
        guess = get_guess(rows, cols)
        guesses += 1
        if guess == treasure_location:
            print(f"Congratulations! You found the treasure in {guesses} guesses.")
            break
        else:
            distance = calculate_distance(guess, treasure_location)
            print(f"Oops! You didn't find the treasure. The treasure is {distance} cells away from your guess.")

if __name__ == "__main__":
    main()
