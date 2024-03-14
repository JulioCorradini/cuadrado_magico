document.addEventListener("DOMContentLoaded", function() {
    const numbers = [10, 11, 12, 4, 5, 6, 7, 8, 9]; // Array hardcodeado
    const board = document.getElementById('board');
    const numberList = document.getElementById('numbers');

    // Generar el tablero y los números
    generateBoard(board);
    generateNumberList(numbers, numberList);

    // Agregar event listener para los números
    numberList.addEventListener('click', function(event) {
        const target = event.target;
        if (target.tagName === 'LI') {
            const selectedNumber = parseInt(target.textContent);
            if (!isNaN(selectedNumber)) {
                target.classList.add('selected');
            }
        }
    });

    // Agregar event listener para las celdas del tablero
    board.addEventListener('click', function(event) {
        const target = event.target;
        if (target.classList.contains('cell') && !target.textContent) {
            const selectedNumber = numberList.querySelector('.selected');
            if (selectedNumber) {
                target.textContent = selectedNumber.textContent;
                selectedNumber.classList.remove('selected');
                selectedNumber.classList.add('disabled');
            }
        }
    });

    // Función para generar el tablero
    function generateBoard(board) {
        for (let i = 0; i < 9; i++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            board.appendChild(cell);
        }
    }

    // Función para generar la lista de números
    function generateNumberList(numbers, numberList) {
        numbers.forEach(number => {
            const li = document.createElement('li');
            li.textContent = number;
            numberList.appendChild(li);
        });
    }
});
