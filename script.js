// script.js
function updateClock() {
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    document.getElementById('clock').textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    document.getElementById('date').textContent = now.toLocaleDateString(undefined, options);
}

setInterval(updateClock, 1000);
updateClock();

let timer;
let timeLeft = 25 * 60; // 25 minutes in seconds
let timerRunning = false;

document.getElementById('start-button').addEventListener('click', startTimer);
document.getElementById('stop-button').addEventListener('click', stopTimer);

function startTimer() {
    if (!timerRunning) {
        timerRunning = true;
        countdown();
    }
}

function stopTimer() {
    timerRunning = false;
    clearInterval(timer);
}

function countdown() {
    timer = setInterval(() => {
        if (timeLeft <= 0) {
            clearInterval(timer);
            alert("Time's up! Take a short break!");
            timeLeft = 25 * 60; // Reset timer
            timerRunning = false;
            document.getElementById('timer-display').textContent = "25:00";
            return;
        }
        timeLeft--;
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        document.getElementById('timer-display').textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }, 1000);
}

// Task Checklist Functionality
document.getElementById('add-task-button').addEventListener('click', addTask);

function addTask() {
    const taskInput = document.getElementById('task-input');
    const taskText = taskInput.value.trim();
    if (taskText) {
        const checklist = document.getElementById('checklist');
        const taskItem = document.createElement('div');
        taskItem.innerHTML = `<input type="checkbox"> ${taskText}`;
        checklist.appendChild(taskItem);
        taskInput.value = ''; // Clear input
    }
}

// Focus Session Button Functionality
document.getElementById('focus-button').addEventListener('click', () => {
    alert("Focus session started! Use the Windows Clock app to manage your focus time.");
});