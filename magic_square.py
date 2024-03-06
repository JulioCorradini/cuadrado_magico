square_size = 3

def create_square(square_size):
    square = list(range(square_size))
    for row in square:
        square[row] = list(range(square_size))
    for row in square:
     print(row)

create_square(square_size)