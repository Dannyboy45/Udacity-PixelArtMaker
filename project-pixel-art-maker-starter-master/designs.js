
window.addEventListener('load', function() {
    const form = document.getElementById('sizePicker');

    form.addEventListener('submit', event => {
        event.preventDefault();
        makeGrid();
    });
})

function makeGrid() {    
    
    const tableGrid = document.getElementById('pixelCanvas');
    tableGrid.innerHTML = '';

    const numOfRows = parseInt(document.getElementById('inputHeight').value);
    const numOfColumns = parseInt(document.getElementById('inputWidth').value);    

    for(let i = 0; i < numOfRows; i++){
        const row = document.createElement('tr');

        for(let j = 0; j < numOfColumns; j++){
            const cell = document.createElement('td');

            cell.addEventListener('click', event => {
                const colorPicker = document.getElementById('colorPicker');
                event.target.style.backgroundColor = colorPicker.value;
            });

            row.appendChild(cell);
        }

        tableGrid.appendChild(row);
    }
}
