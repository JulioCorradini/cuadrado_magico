

// Función que genera la lista de números aleatórios.
function generateRandomNumbers() {
    const min_value = Math.floor(Math.random() * 1000) + 1;
    const gap_value = Math.floor(Math.random() * 5) * 2 + 1;
    const values = [];
    for (let i = 0; i < 9; i++) {
      values.push(min_value + i * gap_value);
    }

    // Encontrar la mediana
    const median = Math.floor(values.length / 2);

    // Reordenar la lista según las reglas del juego
    let aux_var = 0;
    // Los dos números impares anteriores se intercalan desde la segunda posición anterior (3° y 1°)
    aux_var = values[median - 1];
    values[median - 1] = values[median - 2];
    values[median - 2] = aux_var;

    aux_var = values[median - 3];
    values[median - 3] = values[median - 4];
    values[median - 4] = aux_var;

    // Los dos números impares posteriores se intercalan desde la segunda siguiente posición (7° y 9°)
    aux_var = values[median + 1];
    values[median + 1] = values[median + 2];
    values[median + 2] = aux_var;

    aux_var = values[median + 3];
    values[median + 3] = values[median + 4];
    values[median + 4] = aux_var;

    // Los dos números pares anteriores se ordenan de forma descendente desde la posición posterior (6° y 8°)
    // Los dos números pares posteriores se ordenan de forma ascendente desde la posición anterior (4° y 2°)
    aux_var = values[median - 1];
    values[median - 1] = values[median + 1];
    values[median + 1] = aux_var;

    aux_var = values[median + 3];
    values[median + 3] = values[median - 3];
    values[median - 3] = aux_var;

    return values;
  }

// Función para mezclar de forma aleatoria una lista
function shuffleList(list) {
    const shuffledList = [...list];
    for (let i = shuffledList.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffledList[i], shuffledList[j]] = [shuffledList[j], shuffledList[i]];
    }
    return shuffledList;
  }

function createHelpNumbers(orderedNumbers) {
    const helpNumbers = Array.from({ length: 3 }, () => Array(3).fill(null));
    const occupiedPositions = [];
  
    for (let i = 0; i < 3; i++) {
      while (true) {
        const position = Math.floor(Math.random() * (9)) + 1;
  
        if (!occupiedPositions.includes(position)) {
          occupiedPositions.push(position);
          const row = Math.floor((position) / 3);
          const col = (position) % 3;
          helpNumbers[row][col] = orderedNumbers[position];
          break;
        }
      }
    }
    
    return helpNumbers;
}

document.addEventListener('DOMContentLoaded', function() {
    const numbersList = document.getElementById('numbers');
    const board = document.getElementById('board');
  
    const selectedNumbers = [];
    const orderedNumbers = generateRandomNumbers();
    const availableNumbers = shuffleList(orderedNumbers);
    const helpNumbers = createHelpNumbers(orderedNumbers);

    
    // Rellenar la lista de números con los números generados aleatoriamente
    availableNumbers.forEach(number => {
        const listItem = document.createElement('li');
        listItem.innerText = number;
        numbersList.appendChild(listItem);
    });
    
    // Event listener for number selection
    numbersList.addEventListener('click', function(event) {
      const selectedNumber = event.target.innerText;
      if (!selectedNumbers.includes(selectedNumber)) {
        selectedNumbers.push(selectedNumber);
        event.target.classList.add('selected');
      }
    });
  
    // Event listener for board cell selection
    board.addEventListener('click', function(event) {
      const selectedCell = event.target;
      if (!selectedCell.classList.contains('selected') && selectedNumbers.length > 0) {
        const number = selectedNumbers.shift();
        selectedCell.innerText = number;
        selectedCell.classList.add('selected');
      }
    });
  
    // Create the board with random preset numbers
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.row = i;
        cell.dataset.col = j;
        board.appendChild(cell);
      }
    }

    // ESTON CONSOLE LOG NO VAN
    console.log(orderedNumbers);
    console.log(availableNumbers);
    console.log(helpNumbers);
  });
  