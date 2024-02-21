const playerSelect = document.getElementById('player-select');
const filterButton = document.getElementById('filter-button');

filterButton.addEventListener('click', () => {
    const selectedPlayer = playerSelect.value;
    filterTable(selectedPlayer);
});

function filterTable(player) {
    const tableRows = document.querySelectorAll('#game-table table tbody tr');
    console.log(tableRows)
    tableRows.forEach(row => {
        const player1 = row.cells[0].innerText;
        const player2 = row.cells[1].innerText;
        if (player1 === player || player2 === player) {
            row.style.display = ''; // Show the row
        } else {
            row.style.display = 'none'; // Hide the row
        }
    });
}
