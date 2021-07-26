// Select color input
// Select size input

// When size is submitted by the user, call makeGrid()

function makeGrid() {



// Your code goes here!
       

    const numOfRows = parseInt(document.getElementById('inputHeight').value);
    const numOfColumns = parseInt(document.getElementById('inputWidth').value);

    //alert('table or rows and columns: ' + numOfRows + ' ' + numOfColumns); 

    const tableGrid = document.getElementById('pixelCanvas');

    for(let i = 0; i < numOfRows; i++){
        const row = document.createElement('tr');

        for(let j = 0; j < numOfColumns; j++){
            const cell = document.createElement('td', 'blah');

            cell.addEventListener('click', event => {
                event.target.style.backgroundColor = "blue";
                //console.log(event.target);
            });

            row.appendChild(cell);
        }

        tableGrid.appendChild(row);
    }



}
