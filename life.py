

# the program works now
# finish the take_input() function
# and implement it to the game so one can change the starting setup.
#
# maybe turn it into a CLI so it can be played directly from the command line.


def reset_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = 0

def get_cell(grid, x, y):
    return grid[x][y]

def set_cell(grid, x, y, state):
    grid[x][y] = state

def find_neighbours(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            count += grid[x + i][y + j]
    count -= grid[x][y]
    return count

def print_grid(grid):
    for row in range(len(grid)):
        print(grid[row])
    print("\n")

def take_input(grid):
    print("welcome to the game of life \n")
    print("this is the starting board \n")
    print_grid(grid)

        
def main(cols, rows, generations):
    grid = [[0 for i in range(cols)] for j in range(rows)]
    gen = 1
    
    #       starting grid 
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    set_cell(grid, 2, 2, 1)
    set_cell(grid, 3, 2, 1)
    set_cell(grid, 4, 2, 1)
    
    print("starting grid")
    print_grid(grid)

    while gen <= generations:
        new_grid = [[0 for i in range(cols)] for j in range(rows)]
        for x in range(0, cols - 1):
            for y in range(0, rows - 1):
                neibours = find_neighbours(grid, x, y)
                #edges
                if y == 0 or y == cols - 1 or x == 0 or x == rows - 1:
                    new_grid[x][y] = grid[x][y]

                state = grid[x][y]
                #rules
                if state == 0 and neibours == 3:
                    new_grid[x][y] = 1
                elif state == 1 and (neibours < 2 or neibours > 3):
                    new_grid[x][y] = 0
                else:
                    new_grid[x][y] = grid[x][y]

        
        print(f"generation: {gen}")
        print_grid(new_grid)
        grid = new_grid

        gen += 1
        
        

main(10, 10, 5)