import random

# Tamaño del cuadrado.
square_size = 6

def create_square(square_size):
    
    # Creo las variables necesarias.
    position = 0
    positions = {}
    value = 0

    # Creo el cuadrado.
    square = list(range(square_size))
    for row in square:
        square[row] = list(range(square_size))

    # Pueblo el diccionario con las claves que representan cada una de las posiciones del cuadrado y las inicializo a todas en 0.
    for column in square:
        for row in column:
           position += 1
           positions.setdefault(position, 0)
    
    # Pueblo cada clave con un valor aleatorio.
    for position in positions:
       value = random.randint(1, 10)
       positions[position] = value
    
    # Imprimo el diccionario.
    print(positions)
    
    # Pintando el cuadrado con los valores del diccionario.
    for row in range(square_size):
       for column in range(square_size):
          square[row][column] = positions[(row * square_size + column) + 1]
    
    # Imprimimos el cuadrado.
    for row in square:
       print(row)

create_square(square_size)