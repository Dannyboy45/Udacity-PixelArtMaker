function makeGrid() {       

    const numOfRows = parseInt(document.getElementById('inputHeight').value);
    const numOfColumns = parseInt(document.getElementById('inputWidth').value);

    const tableGrid = document.getElementById('pixelCanvas');

    for(let i = 0; i < numOfRows; i++){
        const row = document.createElement('tr');

        for(let j = 0; j < numOfColumns; j++){
            const cell = document.createElement('td', 'blah');

            cell.addEventListener('click', event => {
                event.target.style.backgroundColor = "blue";
            });

            row.appendChild(cell);
        }

        tableGrid.appendChild(row);
    }
}
