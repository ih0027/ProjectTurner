import random
import time
import os

# Configuration
chanceOfStartAlive = 0.5
xDim, yDim = 40, 20  # Smaller for console visibility

# Initialize board
board = [[random.random() < chanceOfStartAlive for _ in range(xDim)] for _ in range(yDim)]

def count_neighbors(b, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue # Skip the cell itself
            
            # Use modulo (%) to create a "toroidal" (wrapping) grid
            if b[(y + j) % yDim][(x + i) % xDim]:
                count += 1
    return count

while True:
    # Clear console (optional, for animation)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 1. Print current state
    for row in board:
        print("".join(["#" if cell else " " for cell in row]))
    
    # 2. Calculate next generation
    next_board = [[False for _ in range(xDim)] for _ in range(yDim)]
    
    for y in range(yDim):
        for x in range(xDim):
            neighbors = count_neighbors(board, x, y)
            
            if board[y][x]:
                # Survival: 2 or 3 neighbors
                next_board[y][x] = neighbors in [2, 3]
            else:
                # Birth: exactly 3 neighbors
                next_board[y][x] = neighbors == 3
                
    # 3. Update board for next iteration
    board = next_board
    time.sleep(0.1)