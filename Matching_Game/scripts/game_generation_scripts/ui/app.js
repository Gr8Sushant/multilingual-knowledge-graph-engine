// Global game state
let currentItems = [];
let currentIndex = 0;
let score = 0;
let isAudioPlaying = false;
let userXP = parseInt(localStorage.getItem('userXP') || '0', 10);

// DOM Elements
const menuScreen = document.getElementById('menu-screen');
const gameScreen = document.getElementById('game-screen');
const resultScreen = document.getElementById('result-screen');

const langSelect = document.getElementById('language-select');
const modeSelect = document.getElementById('mode-select');
const startBtn = document.getElementById('start-btn');
const errorMsg = document.getElementById('error-message');
const xpDisplay = document.getElementById('xp-display');
const xpBtn = document.getElementById('xp-btn');
const backBtn = document.getElementById('back-btn');

const promptDisplay = document.getElementById('prompt-display');
const optionsGrid = document.getElementById('options-grid');
const feedbackMessage = document.getElementById('feedback-message');
const nextBtn = document.getElementById('next-btn');
const audioBtn = document.getElementById('audio-btn');

const progressBar = document.getElementById('progress-bar');
const scoreDisplay = document.getElementById('score-display');
const questionCount = document.getElementById('question-count');

const finalScoreText = document.getElementById('final-score-text');
const homeBtn = document.getElementById('home-btn');

/**
 * Cleans up metadata from labels.
 * e.g. "grapheme:np:अ" -> "अ"
 * "lemma:eng:acquiring" -> "acquiring"
 * "abugida_roman:np:a" -> "a"
 */
function cleanLabel(text) {
    if (!text) return "";
    const parts = text.split(':');
    return parts[parts.length - 1];
}

// Initialize application
function init() {
    if (typeof gameData === 'undefined' || !gameData || gameData.length === 0) {
        errorMsg.textContent = "Error: Game data not found. Please run the generation script first.";
        startBtn.disabled = true;
        return;
    }

    // Populate languages
    const languages = [...new Set(gameData.map(item => item.language))].filter(Boolean).sort();
    
    languages.forEach(lang => {
        const option = document.createElement('option');
        option.value = lang;
        // Map common codes to full names if desired, or just show code
        const langNames = { "np": "Nepalese", "vn": "Vietnamese", "ur": "Urdu", "dr": "Darija" };
        option.textContent = langNames[lang] || lang.toUpperCase();
        langSelect.appendChild(option);
    });

    updateXPDisplay();

    // Event Listeners
    startBtn.addEventListener('click', startSession);
    nextBtn.addEventListener('click', renderNextQuestion);
    homeBtn.addEventListener('click', showMenu);
    audioBtn.addEventListener('click', playAudio);
    
    backBtn.addEventListener('click', () => {
        if(confirm('Are you sure you want to quit this session?')) {
            showMenu();
        }
    });

    xpBtn.addEventListener('click', () => {
        if(confirm('Do you want to reset your User XP to 0?')) {
            userXP = 0;
            saveXP();
        }
    });
}

function updateXPDisplay() {
    if (xpDisplay) {
        xpDisplay.textContent = userXP;
    }
}

function saveXP() {
    localStorage.setItem('userXP', userXP.toString());
    updateXPDisplay();
}

function startSession() {
    const selectedLang = langSelect.value;
    const selectedMode = parseInt(modeSelect.value, 10);

    errorMsg.textContent = "";
    currentIndex = 0;
    
    // Determine difficulty based on userXP
    let targetDifficulty = "easy";
    if (userXP >= 500) {
        targetDifficulty = "hard";
    } else if (userXP >= 100) {
        targetDifficulty = "medium";
    }
    
    // Filter questions by difficulty
    let filteredItems = gameData.filter(item => 
        item.language === selectedLang && 
        item.mode === selectedMode && 
        item.difficulty === targetDifficulty
    );
    
    // Fallback: If not enough items for that difficulty, use all available items
    if (filteredItems.length < 10) {
        filteredItems = gameData.filter(item => 
            item.language === selectedLang && 
            item.mode === selectedMode
        );
    }
    
    if (filteredItems.length === 0) {
        errorMsg.textContent = "No items found for the selected language and mode.";
        return;
    }

    currentItems = [...filteredItems];
    
    // Shuffle and pick 10 questions
    currentItems.sort(() => Math.random() - 0.5);
    currentItems = currentItems.slice(0, 10);

    currentIndex = 0;
    score = 0;
    
    showScreen(gameScreen);
    renderQuestion();
}

function renderQuestion() {
    if (currentIndex >= currentItems.length) {
        endSession();
        return;
    }

    const item = currentItems[currentIndex];
    const mode = item.mode;
    
    // Update UI Stats
    updateProgress();
    scoreDisplay.textContent = `Score: ${score} / ${currentIndex}`;
    questionCount.textContent = `Q: ${currentIndex + 1} / ${currentItems.length}`;
    
    // Reset states
    feedbackMessage.innerHTML = "";
    optionsGrid.innerHTML = "";
    nextBtn.classList.add('hidden');
    audioBtn.classList.add('hidden');

    // Display Prompt
    if (mode === 1) {
        promptDisplay.textContent = cleanLabel(item.transliteration);
        if (item.audio_path || item.audio_placeholder) {
            audioBtn.classList.remove('hidden');
        }
    } else {
        promptDisplay.textContent = cleanLabel(item.english_prompt);
    }

    // Render Options
    item.options.forEach(opt => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        
        let optText = opt;
        let optTrans = null;
        
        if (typeof opt === 'object' && opt !== null) {
            optText = opt.text;
            optTrans = opt.transliteration;
        }
        
        const mainSpan = document.createElement('span');
        mainSpan.className = 'main-text';
        mainSpan.textContent = cleanLabel(optText);
        btn.appendChild(mainSpan);
        
        if (optTrans) {
            const hint = document.createElement('div');
            hint.className = 'transliteration-hint';
            hint.textContent = cleanLabel(optTrans);
            btn.appendChild(hint);
        }
        
        btn.addEventListener('click', () => handleAnswer(optText, btn));
        optionsGrid.appendChild(btn);
    });
}

function handleAnswer(selectedRaw, btnElement) {
    const item = currentItems[currentIndex];
    const correctRaw = item.correct_grapheme || item.correct_nepali; // key name might be correct_nepali generically
    const isCorrect = selectedRaw === correctRaw;
    
    // Disable all buttons
    const allBtns = optionsGrid.querySelectorAll('.option-btn');
    allBtns.forEach(btn => {
        btn.disabled = true;
        // Highlight the correct one regardless
        const mainSpan = btn.querySelector('.main-text');
        const btnText = mainSpan ? mainSpan.textContent : btn.textContent;
        if (btnText === cleanLabel(correctRaw)) {
            btn.classList.add('correct');
        }
    });

    if (isCorrect) {
        score++;
        userXP += 10; // Award 10 XP for correct answer
        saveXP();
        btnElement.classList.add('correct');
        feedbackMessage.innerHTML = `<span class="success">Correct! +10 XP</span>`;
    } else {
        btnElement.classList.add('incorrect');
        feedbackMessage.innerHTML = `<span class="error">Incorrect. Correct answer is ${cleanLabel(correctRaw)}</span>`;
    }

    // Add transliteration sub-text if mode 2
    if (item.mode === 2 && item.correct_transliteration) {
        feedbackMessage.innerHTML += `<span class="sub-text">Pronounced: ${cleanLabel(item.correct_transliteration)}</span>`;
    }

    scoreDisplay.textContent = `Score: ${score} / ${currentIndex + 1}`;
    nextBtn.classList.remove('hidden');
}

function updateProgress() {
    const percent = (currentIndex / currentItems.length) * 100;
    progressBar.style.width = `${percent}%`;
}

function renderNextQuestion() {
    currentIndex++;
    renderQuestion();
}

function endSession() {
    progressBar.style.width = `100%`;
    finalScoreText.textContent = `${score} / ${currentItems.length}`;
    showScreen(resultScreen);
}

function showMenu() {
    showScreen(menuScreen);
}

function showScreen(screenElement) {
    [menuScreen, gameScreen, resultScreen].forEach(el => el.classList.remove('active'));
    screenElement.classList.add('active');
}

function playAudio() {
    if (isAudioPlaying) return;
    isAudioPlaying = true;
    
    const originalText = audioBtn.innerHTML;
    audioBtn.innerHTML = `🔊 Playing...`;
    
    // Simulate audio playing delay
    setTimeout(() => {
        audioBtn.innerHTML = originalText;
        isAudioPlaying = false;
    }, 1500);
}

// Start
document.addEventListener('DOMContentLoaded', init);
