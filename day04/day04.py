def create_hell_matrix(path):
    matrix=[]
    with open(path) as file:
        input = file.read().strip().split('\n')
        for line in input:
            row = list(line)
            row_with_border = ['*', '*', '*'] + row + ['*', '*', '*']  # Add borders
            matrix.append(row_with_border)

        # Create the top and bottom border lines
        row_length = len(matrix[0])  # Length of a row after adding borders
        border_row = ['*'] * row_length

        # Add 3 border rows to the top
        for _ in range(3):
            matrix.insert(0, border_row)

        # Add 3 border rows to the bottom
        for _ in range(3):
            matrix.append(border_row)

        # Print the matrix for verification
        for row in matrix:
            print(''.join(row))
    return matrix

def search_diag(matrix, x, y):
    count = 0
    if matrix[x+1][y+1] == 'M' and matrix[x+2][y+2] == 'A' and matrix[x+3][y+3]== 'S':
        count +=1
    if matrix[x-1][y-1] == 'M' and matrix[x-2][y-2] == 'A' and matrix[x-3][y-3] == 'S':
        count +=1
    if matrix[x+1][y-1] == 'M' and matrix[x+2][y-2] == 'A' and matrix[x+3][y-3] == 'S':
        count +=1
    if matrix[x-1][y+1] == 'M' and matrix[x-2][y+2] == 'A' and matrix[x-3][y+3] == 'S':
        count +=1
    return count

def search_horizontal(matrix, x, y):
    count = 0
    if matrix[x][y+1] == 'M' and matrix[x][y+2] == 'A' and matrix[x][y+3] == 'S':
        count +=1
    if matrix[x][y-1] == 'M' and matrix[x][y-2] == 'A' and matrix[x][y-3] == 'S':
        count +=1
    return count

def search_vertical(matrix, x, y):
    count = 0
    if matrix[x+1][y] == 'M' and matrix[x+2][y] == 'A' and matrix[x+3][y] == 'S':
        count +=1
    if matrix[x-1][y] == 'M' and matrix[x-2][y] == 'A' and matrix[x-3][y] == 'S':
        count +=1
    return count

def search_MAS(matrix, x, y):
    count = 0
    if matrix[x+1][y+1] == 'S' and matrix[x-1][y-1] == 'M' and matrix[x-1][y+1]== 'S' and matrix[x+1][y-1]== 'M':
        count +=1
    if matrix[x+1][y+1] == 'M' and matrix[x-1][y-1] == 'S' and matrix[x-1][y+1]== 'M' and matrix[x+1][y-1]== 'S':
        count +=1
    if matrix[x+1][y+1] == 'M' and matrix[x-1][y-1] == 'S' and matrix[x-1][y+1]== 'S' and matrix[x+1][y-1]== 'M':
        count +=1
    if matrix[x+1][y+1] == 'S' and matrix[x-1][y-1] == 'M' and matrix[x-1][y+1]== 'M' and matrix[x+1][y-1]== 'S':
        count +=1
    return count

def count_xmas(path):
    sum_xmas = 0
    matrix = create_hell_matrix(path)
    for line_num, line in enumerate(matrix):
        for char_num, char in enumerate(line):
            if char == "X":
                sum_xmas += search_horizontal(matrix, line_num, char_num)
                sum_xmas += search_vertical(matrix, line_num, char_num)
                sum_xmas += search_diag(matrix, line_num, char_num)
    return(sum_xmas)

def count_mas(path):
    sum_mas = 0
    matrix = create_hell_matrix(path)
    for line_num, line in enumerate(matrix):
        for char_num, char in enumerate(line):
            if char == "A":
                sum_mas += search_MAS(matrix, line_num, char_num)
    return(sum_mas)

if __name__ == "__main__":
    print("---Part One---")
    print("Total number of XMAS with test input: ", count_xmas('input-example-day04-part1.txt'))
    print("Total number of XMAS: ", count_xmas('input-day04.txt'))
    print("---Part Two---")
    print("Total number of MAS CROSS with test input: ", count_mas('input-example-day04-part1.txt'))
    print("Total number of MAS CROSS: ", count_mas('input-day04.txt'))
