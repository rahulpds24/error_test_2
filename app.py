const quizData = [
    {
        question: 'What is the correct form of the verb in this sentence: She ___ to the store every Saturday.',
        a: 'go',
        b: 'goes',
        c: 'gone',
        d: 'going',
        correct: 'b'
    },
    {
        question: 'Which sentence is grammatically correct?',
        a: 'He don\'t like pizza.',
        b: 'He doesn\'t likes pizza.',
        c: 'He doesn\'t like pizza.',
        d: 'He not like pizza.',
        correct: 'c'
    },
    {
        question: 'Choose the correct word: Each of the students ___ their homework.',
        a: 'have done',
        b: 'has done',
        c: 'were done',
        d: 'done',
        correct: 'b'
    },
    {
        question: 'Identify the error: She go to the gym every day.',
        a: 'She',
        b: 'go',
        c: 'to',
        d: 'the',
        correct: 'b'
    }
];

const quizContainer = document.getElementById('quiz');
const submitButton = document.getElementById('submit');

function loadQuiz() {
    const currentQuizData = quizData[quizIndex];
    quizContainer.innerHTML = `
        <h2>${currentQuizData.question}</h2>
        <label>
            <input type='radio' name='answer' value='a'> ${currentQuizData.a}
        </label>
        <label>
            <input type='radio' name='answer' value='b'> ${currentQuizData.b}
        </label>
        <label>
            <input type='radio' name='answer' value='c'> ${currentQuizData.c}
        </label>
        <label>
            <input type='radio' name='answer' value='d'> ${currentQuizData.d}
        </label>
    `;
}

let score = 0;
let quizIndex = 0;
loadQuiz();

submitButton.addEventListener('click', () => {
    const answerEls = document.querySelectorAll('input[name=answer]');
    let selectedAnswer;
    answerEls.forEach((answerEl) => {
        if (answerEl.checked) {
            selectedAnswer = answerEl.value;
        }
    });
    if (selectedAnswer === quizData[quizIndex].correct) {
        score++;
    }
    quizIndex++;
    if (quizIndex < quizData.length) {
        loadQuiz();
    } else {
        quizContainer.innerHTML = `<h2>You scored ${score} out of ${quizData.length}</h2>`;
    }
});