import random

# Tamaño del cuadrado.
square_size = 3

# Función para generar un cuadrado vacío con tres números aleatóreamente posicionados.
def generate_empty_square(square_size, positions):
  """
  Genera un cuadrado vacío con tres números aleatorios ya ubicados.

  Args:
    square_size: Tamaño del cuadrado.
    positions: Diccionario que mapea las posiciones del cuadrado a los valores.

  Returns:
    Un cuadrado vacío con tres números aleatorios ya ubicados.
  """

  # Creo el cuadrado vacío.
  empty_square = [[None for _ in range(square_size)] for _ in range(square_size)]

  # Lista para almacenar las posiciones ya ocupadas.
  occupied_positions = []

  # Ubico tres números aleatorios en el cuadrado.
  for _ in range(3):
    while True:
      # Genero una posición aleatoria.
      position = random.randint(1, square_size * square_size)

      # Si la posición no está ocupada, la ubico.
      if position not in occupied_positions:
        occupied_positions.append(position)
        empty_square[(position - 1) // square_size][(position - 1) % square_size] = positions[position]
        break

  return empty_square, occupied_positions


# Función para generar el cuadrado guía con los núemros posicionados correctamente.
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

    # Creo un valor mínimo aleatorio a partir del cual crear el resto de los números.
    min_value = random.randint(1, 1000)
    # Creao un valor de salto aleatorio para que la serie de números tenga una separación entre ellos.
    gap_value = random.randrange(1, 11, 2)
    # Creo una lista para guardar la serie de números.
    values= []
    # Creo una serie de núeros a partir del valor mínimo y los agrego a la lista.
    for i in range(square_size * square_size):
       i += 1
       values.append(min_value)
       min_value += gap_value
   
    #Imprimo el array desordenado
    print(values)
   
   # ALGORITTMO QUE REORDENA LOS ELEMENTOS DEL ARRAY DE FORMA QUE RESPETE LAS REGLAS DEL JUEGO.
    # PRIMERO DEBO ENCONTRAR LA MEDIANA
    median = int(len(values) / 2) 
    # CREO UNA VARIABLE AUXILIAR.
    aux_var = 0
    # LOS DOS NÚEMROS IMPARES ANTERIORES SE UBICAN DESDE LA SEGUNDA POSICIÓN ANTERIOR DE FORMA INTERCALADA (3° Y 1°)
    aux_var = values[median - 1]
    values[median - 1] = values[median - 2]
    values[median - 2] = aux_var

    aux_var = values[median - 3]
    values[median - 3] = values[median - 4]
    values[median - 4] = aux_var
    # LOS DOS NÚMEMRO IMPARES POSTERIORES SE UBICAN DESDE LA SEGUNDA SIGUIENTE POSICIÓN DE FORMA INTERCALADA (7° Y 9°)
    aux_var = values[median + 1]
    values[median + 1] = values[median + 2]
    values[median + 2] = aux_var

    aux_var = values[median + 3]
    values[median + 3] = values[median + 4]
    values[median + 4] = aux_var
    # LOS DOS NÚMEROS PARES ANTERIORES SE UBICAN DE FORMA DESCENDENTE DESDE LA POSICIÓN POSTERIOR DE FORMA INTERCALDA ( 6° Y 8°)
    # LOS DOS NÚMEROS PARES POSTERIORES SE UBICAN DE FORMA ASCENDENTE DESDE LA POSICIÓN ANTERIOR DE FORMA INTERCALADA (4° Y 2°)
    aux_var = values[median - 1]
    values[median - 1] = values[median + 1]
    values[median + 1] = aux_var

    aux_var = values[median + 3]
    values[median + 3] = values[median - 3]
    values[median - 3] = aux_var

    #Imprimo el array ordenado
    print(values)

   # Pueblo el diccionario con la serie de núemeros.
    indice = 0
    for position in positions:
       positions[position] = values[indice]
       indice += 1
    
    # Imprimo el diccionario.
    print(positions)
    
    # Pintando el cuadrado con los valores del diccionario.
    for row in range(square_size):
       for column in range(square_size):
          square[row][column] = positions[(row * square_size + column) + 1]
    
    # Imprimimos el cuadrado.
    for row in square:
       print(row)
   
    # Genero el cuadrado vacío y obtengo las posiciones ocupadas.
    empty_square, occupied_positions = generate_empty_square(square_size, positions)

    # Imprimimos el cuadrado vacío.
    for row in empty_square:
     print(row)
     
     # Obtener los números disponibles que no están inicialmente ocupados.
    available_numbers = [v for k, v in positions.items() if k not in occupied_positions]

    # Solicitar al usuario ingresar números en el cuadrado vacío.
    print("\nIngrese los números disponibles en las posiciones libres del cuadrado vacío:")

    for i in range(square_size):
        for j in range(square_size):
            if empty_square[i][j] is None:
                print(f"Números disponibles: {available_numbers}")
                while True:
                    user_number = int(input(f"Ingrese un número para la posición [{i+1}][{j+1}]: "))
                    if user_number in available_numbers:
                        empty_square[i][j] = user_number
                        available_numbers.remove(user_number)
                        break
                    else:
                        print("El número ingresado no es válido. Intente de nuevo.")
            else:
                print(f"La posición [{i+1}][{j+1}] ya está ocupada.")

    # Imprimir el cuadrado vacío con los números ingresados por el usuario.
    print("\nCuadrado con números ingresados por el usuario:")
    for row in empty_square:
        print(row)

    # Verificar si todos los números coinciden con los del cuadrado generado.
    is_identical = True
    for i in range(square_size):
        for j in range(square_size):
            if empty_square[i][j] != square[i][j]:
                is_identical = False
                break
        if not is_identical:
            break

    if is_identical:
        print("\n¡Los números ingresados coinciden con los del cuadrado generado!")
    else:
        print("\nLos números ingresados no coinciden con los del cuadrado generado.")

create_square(square_size)