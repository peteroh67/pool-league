// change url to the previous month when previous-month button is clicked
document.getElementById('prev-month').addEventListener('click', () => {



});

// used to filter the games depending on inout from user
const playerSelect1 = document.getElementById('player-select-1');
const playerSelect2 = document.getElementById('player-select-2');
const filterButton = document.getElementById('filter-button');

filterButton.addEventListener('click', () => {
    const p1 = playerSelect1.value;
    const p2 = playerSelect2.value;
    filterTable(p1, p2);
});

// filter games table
function filterTable(selectedPlayer1, selectedPlayer2) {
    const tableRows = document.querySelectorAll('#game-table table tbody tr');
    tableRows.forEach(row => {
        const gamePlayer1 = row.cells[0].innerText;
        const gamePlayer2 = row.cells[1].innerText;

        // if the selected players don't match the rows players, hide the row
        if (!(matchesPlayers(gamePlayer1, gamePlayer2, selectedPlayer1, selectedPlayer2))) {
            row.style.display = 'none';
        }
    });
}

// Returns true if the selected players match the rows players.
function matchesPlayers(gamePlayer1, gamePlayer2, selectedPlayer1, selectedPlayer2) {
    if (selectedPlayer1 && selectedPlayer2) {
        // Both players are selected
        return (gamePlayer1 === selectedPlayer1 && gamePlayer2 === selectedPlayer2) ||
               (gamePlayer1 === selectedPlayer2 && gamePlayer2 === selectedPlayer1);
    } else if (selectedPlayer1 && !selectedPlayer2) {
        // Only player 1 is selected
        return gamePlayer1 === selectedPlayer1 || gamePlayer2 === selectedPlayer1;
    } else if (!selectedPlayer1 && selectedPlayer2) {
        // Only player 2 is selected
        return gamePlayer1 === selectedPlayer2 || gamePlayer2 === selectedPlayer2;
    } else {
        // No players are selected
        return false;
    }
}
