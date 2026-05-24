let currentCorrectAnswer = "";
let currentTargetSitId = "";
let currentMetadata = {}; // New: We store the metadata here

function getSelectedLanguage() {
    return document.querySelector('input[name="language"]:checked').value;
}

async function loadQuestion() {
    document.getElementById('options-container').innerHTML = "";
    document.getElementById('feedback-box').classList.add('hidden');
    document.getElementById('prompt-text').innerText = "Loading...";

    const lang = getSelectedLanguage();

    try {
        const response = await fetch(`/api/get_question?lang=${lang}`);
        const data = await response.json();
        
        if (data.error) {
            document.getElementById('prompt-text').innerText = "Not enough data for this language yet.";
            return;
        }

        currentCorrectAnswer = data.correct_answer;
        currentTargetSitId = data.situation_id;
        currentMetadata = data.metadata; // Save the raw data for our feedback engine
        
        document.getElementById('prompt-text').innerText = data.situation_english;
        
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

async function checkAnswer(clickedButton, selectedText) {
    const allButtons = document.querySelectorAll('.option-btn');
    const feedbackBox = document.getElementById('feedback-box');
    const feedbackTitle = document.getElementById('feedback-title');
    const feedbackExplanation = document.getElementById('feedback-explanation');

    allButtons.forEach(btn => btn.disabled = true);

    const isCorrect = (selectedText === currentCorrectAnswer);
    let constructiveFeedback = "";

    if (isCorrect) {
        clickedButton.classList.add('correct');
        feedbackTitle.innerText = "🎉 Spot on!";
        feedbackBox.style.backgroundColor = "#e8f5e9"; // Light green background
        
        // Constructive reinforcement for a GOOD answer
        constructiveFeedback = `
            <strong>Why you are right:</strong> You correctly recognized this as a <em>${currentMetadata.category}</em> expression. 
            Because this action happens <em>${currentMetadata.timing}</em> the event, <strong>${currentCorrectAnswer}</strong> is the perfect choice.<br><br>
            <span style="color: #555; font-size: 0.9em;"><em>Literal translation: "${currentMetadata.literal}"</em></span>
        `;
    } else {
        clickedButton.classList.add('wrong');
        feedbackTitle.innerText = `❌ Not quite.`;
        feedbackBox.style.backgroundColor = "#ffebee"; // Light red background
        
        // Constructive redirection for a BAD answer
        constructiveFeedback = `
            <strong>Let's break it down:</strong> You selected <em>${selectedText}</em>, but the correct cultural expression here is <strong>${currentCorrectAnswer}</strong>.<br><br>
            This scenario falls under the <em>${currentMetadata.category}</em> category and must be said <em>${currentMetadata.timing}</em> the event occurs. Make sure to watch the timing!<br><br>
            <span style="color: #555; font-size: 0.9em;"><em>Literal translation: "${currentMetadata.literal}"</em></span>
        `;
        
        // Highlight the correct answer so they see what they missed
        allButtons.forEach(btn => {
            if (btn.innerText === currentCorrectAnswer) btn.classList.add('correct');
        });
    }

    // Inject the new smart feedback
    feedbackExplanation.innerHTML = constructiveFeedback;

    // Send the result to the Spaced Repetition System
    await fetch('/api/update_srs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            situation_id: currentTargetSitId,
            correct: isCorrect
        })
    });
    
    feedbackBox.classList.remove('hidden');
}

document.querySelectorAll('input[name="language"]').forEach(radio => {
    radio.addEventListener('change', loadQuestion);
});
document.getElementById('next-btn').addEventListener('click', loadQuestion);

window.onload = loadQuestion;