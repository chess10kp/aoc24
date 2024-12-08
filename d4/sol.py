output = ""
with open ("input.txt") as file:
    output = file.read()
    output = output.splitlines() 

total = 0 

def count_xmas(word_search):
    rows = len(word_search)
    cols = len(word_search[0])
    word = "XMAS"
    word_len = len(word)
    count = 0
    
    # Define all directions: horizontal, vertical, diagonal
    directions = [
        (0, 1),  # Right (horizontal)
        (0, -1), # Left (horizontal)
        (1, 0),  # Down (vertical)
        (-1, 0), # Up (vertical)
        (1, 1),  # Down-right diagonal
        (-1, -1),# Up-left diagonal
        (1, -1), # Down-left diagonal
        (-1, 1), # Up-right diagonal
    ]
    
    # Check all cells in the grid
    for r in range(rows):
        for c in range(cols):
            # For each direction, check if "XMAS" can fit starting at (r, c)
            for dr, dc in directions:
                if all(0 <= r + i * dr < rows and 0 <= c + i * dc < cols and word_search[r + i * dr][c + i * dc] == word[i] for i in range(word_len)):
                    count += 1
                    
    return count

def x_mas(output):
    total = 0
    for i in range(1, cols-1):
        for j in range(1, rows-1):
                if output[i][j] == "A":
                    if (sorted([output[i-1][j-1], output[i+1][j+1] ]) == ["M", "S"] ) and sorted([output[i-1][j+1], output[i+1][j-1]]) == ["M", "S"]:
                        total += 1  

    return total

x_mas(output)
