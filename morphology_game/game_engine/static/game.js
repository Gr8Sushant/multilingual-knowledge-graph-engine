let currentCorrectAnswer = "";
let currentTargetRoot = "";
let currentTargetPronoun = "";

// Helper function to see which language is selected
function getSelectedLanguage() {
    return document.querySelector('input[name="language"]:checked').value;
}

function getSelectedDifficulty() {
    return document.querySelector('input[name="difficulty"]:checked').value;
}

async function loadQuestion() {
    document.getElementById('options-container').innerHTML = "";
    document.getElementById('feedback-box').classList.add('hidden');
    document.getElementById('prompt-text').innerText = "Loading...";

    const lang = getSelectedLanguage(); 
    const diff = getSelectedDifficulty();

    try {
        const response = await fetch(`/api/get_question?lang=${lang}&difficulty=${diff}`);
        const data = await response.json();
        
        currentCorrectAnswer = data.correct_answer;
        currentTargetRoot = data.root;
        currentTargetPronoun = data.pronoun;
        
        document.getElementById('prompt-text').innerHTML = 
        `${data.english_pronoun} + ${data.english_translation} <br> <span style="font-size: 0.7em; color: #666;">(${data.pronoun} + ${data.root})</span>`;        
        
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
        document.getElementById('prompt-text').innerText = "Failed to load question.";
    }
}

// Handle the user's click and talk to the SRS
async function checkAnswer(clickedButton, selectedText) {
    const allButtons = document.querySelectorAll('.option-btn');
    const feedbackBox = document.getElementById('feedback-box');
    const feedbackTitle = document.getElementById('feedback-title');

    allButtons.forEach(btn => btn.disabled = true);

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

    // Inform the backend server using the targeted grammatical pronoun token
    try {
        await fetch('/api/update_srs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                lang: getSelectedLanguage(),  
                pronoun: currentTargetPronoun, 
                correct: isCorrect
            })
        });
    } catch (error) {
        console.error("Error updating SRS:", error);
    }

    document.getElementById('feedback-box').classList.remove('hidden');
} // <--- THIS WAS THE MISSING CLOSING BRACKET THAT CRASHED YOUR CODE!

// Listen for the UI switches and load fresh questions immediately
document.querySelectorAll('input[name="language"]').forEach(radio => {
    radio.addEventListener('change', loadQuestion);
});

document.querySelectorAll('input[name="difficulty"]').forEach(radio => {
    radio.addEventListener('change', loadQuestion);
});

document.getElementById('next-btn').addEventListener('click', loadQuestion);
window.onload = loadQuestion;