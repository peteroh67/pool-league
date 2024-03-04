// change to previous or next month when the associated button is pressed. works for both games and league table
function changeMonth(direction) {
    let currentMonth = window.location.pathname.split("/")[3];
    let newMonth;

    if (direction === 'prev') {
        newMonth = (parseInt(currentMonth, 10) - 1).toString().padStart(2, '0');
        if (newMonth === '00') {
            newMonth = '12'; // December
        }
    } else if (direction === 'next') {
        newMonth = (parseInt(currentMonth, 10) + 1).toString().padStart(2, '0');
        if (newMonth === '13') {
            newMonth = '01'; // January
        }
    }

    let baseUrlTokens = window.location.pathname.split("/");
    let newUrl = `/${baseUrlTokens[1]}/${baseUrlTokens[2]}/${newMonth}/`

    window.location.href = newUrl;
};

prevMonth = document.getElementById('prev-month');

if (prevMonth) {
    prevMonth.addEventListener('click', () => {
        changeMonth('prev');
    });
}

nextMonth = document.getElementById('next-month');

if (nextMonth) {
    nextMonth.addEventListener('click', () => {
        changeMonth('next');
    });
}

// filter games table
function filterGamesTable(selectedPlayer1, selectedPlayer2) {

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

// Returns true if the selected player(s) match the rows players. Used by filterGamesTable()
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

// used to filter the games depending on input from user
const playerSelect1 = document.getElementById('player-select-1');
const playerSelect2 = document.getElementById('player-select-2');

filterButton = document.getElementById('filter-button');

if (filterButton) {
    filterButton.addEventListener('click', function() {

        const p1 = playerSelect1.value;
        const p2 = playerSelect2.value;
        filterGamesTable(p1, p2);
    });
}


