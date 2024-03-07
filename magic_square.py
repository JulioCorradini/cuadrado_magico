import random

square_size = 3

def create_square(square_size):
    
    position = 0
    positions = {}
    value = 0

    # Creo las columnas del cuadrado.
    square = list(range(square_size))

    # Creo las filas del cuadrado.
    for row in square:
        square[row] = list(range(square_size))
    for row in square:
     print(row)

    # Pueblo el diccionario con las claves que representan cada una de las posiciones del cuadrado y las inicializo a todas en 0.
    for column in square:
        for row in column:
           position += 1
           positions.setdefault(position, 0)
    
    # Pueblo cada clave con un valor aleatorio.
    for position in positions:
       value = random.randint(1, 10)
       positions[position] = value
    
    # Pintando el cuadrado con los valores del diccionario.
    for cell in positions:
        
          

    print(positions)

create_square(square_size)