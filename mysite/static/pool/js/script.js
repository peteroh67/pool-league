// change to previous or next month when the associated button is pressed. works for both games and league table
function changeMonth(direction, view) {
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

    let baseUrl = '/pool/';
    let newUrl = '';

    if (view === 'games') {
        newUrl = `${baseUrl}games/${newMonth}/`;
    } else if (view === 'leaguetable') {
        newUrl = `${baseUrl}leaguetable/${newMonth}/`;
    }
    window.location.href = newUrl;
};

prevMonthGames = document.getElementById('prev-month-games');

if (prevMonthGames) {
    prevMonthGames.addEventListener('click', () => {
        changeMonth('prev', 'games');
    });
}

nextMonthGames = document.getElementById('next-month-games');

if (nextMonthGames) {
    nextMonthGames.addEventListener('click', () => {
        changeMonth('next', 'games');
    });
}

prevMonthLeague = document.getElementById('prev-month-league-table')

if (prevMonthLeague) {
    prevMonthLeague.addEventListener('click', () => {
        changeMonth('prev', 'leaguetable');
    });
}

nextMonthLeague = document.getElementById('next-month-league-table');

if (nextMonthLeague) {
    nextMonthLeague.addEventListener('click', () => {
        changeMonth('next', 'leaguetable');
    });
}

// filter games table
function filterTable(selectedPlayer1, selectedPlayer2) {

    console.log("Filter table");
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

// Returns true if the selected player(s) match the rows players.
function matchesPlayers(gamePlayer1, gamePlayer2, selectedPlayer1, selectedPlayer2) {
    console.log("match player to games");
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
        console.log(playerSelect1);
        console.log(playerSelect1.value);

        const p1 = playerSelect1.value;
        const p2 = playerSelect2.value;
        console.log("event listener filter");
        filterTable(p1, p2);
    });
}


