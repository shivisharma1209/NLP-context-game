// website/static/home.js

document.addEventListener('DOMContentLoaded', function() {
    const previousGuessesList = document.getElementById('previous-guesses-list');

    previousGuesses.forEach(guess => {
        const listItem = document.createElement('li');
        const wordSpan = document.createElement('span');
        wordSpan.textContent = `${guess.word} - Rank: ${guess.rank}`;
        
        const progressBarContainer = document.createElement('div');
        progressBarContainer.className = 'progress-bar-container';
        
        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        progressBar.style.width = `${guess.progress_percentage}%`;
        
        progressBarContainer.appendChild(progressBar);
        listItem.appendChild(wordSpan);
        listItem.appendChild(progressBarContainer);
        previousGuessesList.appendChild(listItem);
    });
});