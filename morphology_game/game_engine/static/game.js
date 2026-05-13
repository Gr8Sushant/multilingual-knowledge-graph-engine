let currentCorrectAnswer = "";
let currentTargetRoot = "";

// Helper function to see which language is selected
function getSelectedLanguage() {
    return document.querySelector('input[name="language"]:checked').value;
}

async function loadQuestion() {
    document.getElementById('options-container').innerHTML = "";
    document.getElementById('feedback-box').classList.add('hidden');
    document.getElementById('prompt-text').innerText = "Loading...";

    const lang = getSelectedLanguage(); // GET LANGUAGE

    try {
        // SEND LANGUAGE TO SERVER
        const response = await fetch(`/api/get_question?lang=${lang}`);
        const data = await response.json();
        
        currentCorrectAnswer = data.correct_answer;
        currentTargetRoot = data.root;
        
        document.getElementById('prompt-text').innerText = `${data.pronoun} + ${data.root}`;

        const container = document.getElementById('options-container');
        data.options.forEach(optionText => {
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.innerText = optionText;
            btn.onclick = () => checkAnswer(btn, optionText);
            container.appendChild(btn);
        });
    } catch (error) {
        console.error("Error loading question:", error);
    }
}
// Handle the user's click and talk to the SRS
async function checkAnswer(clickedButton, selectedText) {
    const allButtons = document.querySelectorAll('.option-btn');
    const feedbackBox = document.getElementById('feedback-box');
    const feedbackTitle = document.getElementById('feedback-title');

    allButtons.forEach(btn => btn.disabled = true);

    // 1. Check if they were right
    const isCorrect = (selectedText === currentCorrectAnswer);

    if (isCorrect) {
        clickedButton.classList.add('correct');
        feedbackTitle.innerText = "🎉 Correct!";
        feedbackBox.style.backgroundColor = "#e8f5e9";
    } else {
        clickedButton.classList.add('wrong');
        feedbackTitle.innerText = `❌ Oops! The correct answer was: ${currentCorrectAnswer}`;
        feedbackBox.style.backgroundColor = "#ffebee";
        
        allButtons.forEach(btn => {
            if (btn.innerText === currentCorrectAnswer) btn.classList.add('correct');
        });
    }

    // 2. Tell the Python Server to update the student's Spaced Repetition profile
    await fetch('/api/update_srs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            lang: getSelectedLanguage(),  // ADD THIS LINE
            root: currentTargetRoot,
            correct: (selectedText === currentCorrectAnswer)
        })
    });
    document.getElementById('feedback-box').classList.remove('hidden');
}

// Listen for the slider changing, and load a new question immediately!
document.querySelectorAll('input[name="language"]').forEach(radio => {
    radio.addEventListener('change', loadQuestion);
});

document.getElementById('next-btn').addEventListener('click', loadQuestion);
window.onload = loadQuestion;