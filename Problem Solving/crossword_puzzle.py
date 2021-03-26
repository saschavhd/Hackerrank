# Init

n = 10  # Grid size

# Functions

def crosswordPuzzle(grid, word_list):
    while word_list:
        word = word_list[0]
        wl = len(word_list[0])
        for i in range(n-wl):
            for j in range(i+wl, n):
                if ''.join(grid[i:j]) == word:



# Main

if __name__ == '__main__':
    grid = []
    for _ in range(n):
        grid.append(list(input))
    word_list = input.split(';')
    result = crosswordPuzzle(grid, word_list)
