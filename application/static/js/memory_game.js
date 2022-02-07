class MixOrMatch {
    constructor(totalTime, cards) {
        this.cardsArray = cards;
        this.totalTime = totalTime;
        this.timeRemaining = totalTime;
        this.timer = document.getElementById('time-remaining');
        this.ticker = document.getElementById('flips');
        this.score = document.getElementById('score');
        this.score2 = document.getElementById('txt1');
    }

    startGame() {
        console.log('jag har startat spelet')
        document.querySelector('.game_end').innerHTML="";
        this.timeRemaining = this.totalTime;
        this.cardToCheck = null;
        this.matchedCards = [];
        this.busy = true;
        this.the_score = 0;
        this.score_box = 0;

        this.score_string = ''
        setTimeout(() => {
            this.shuffleCards(this.cardsArray);
            this.countdown = this.startCountdown();
            this.busy = false;
        }, 500)
        this.hideCards();
        this.timer.innerText = this.timeRemaining;

        this.score.innerText = this.the_score;
        this.score2.value = this.score_box;
    }

    startCountdown() {
        return setInterval(() => {
            this.timeRemaining--;
            this.timer.innerText = this.timeRemaining;
            if(this.timeRemaining === 0)
                this.gameOver();
        }, 1000);
    }

    startCountdown() {
        return setInterval(() => {
            this.timeRemaining--;
            this.timer.innerText = this.timeRemaining;
            if (this.timeRemaining === 0)
                this.gameOver();

        }, 1000);

    }

    send() {
        let button = document.getElementById('clickButton'),
            form = button.form;

        form.addEventListener('submit', function () {
            return false;
        })

        let times = 1;   //Here put the number of times you want to auto submit
        (function submit() {
            if (times == 0) return;
            form.submit();
            times--;
            setTimeout(submit, 1000);   //Each second
        })();

    }

    gameOver() {
        clearInterval(this.countdown);
       // document.getElementById('game_end').innerHTML('Spelet är slut');
        document.querySelector('.game_end').innerHTML="Spelet är slut, tryck starta knappen , om du vill spela igen.";
        this.send();
        this.the_score = 0;

    }

    victory() {
        clearInterval(this.countdown);
        document.getElementById('victory-text').classList.add('visible');
    }

    hideCards() {
        this.cardsArray.forEach(card => {
            card.classList.remove('visible');
            card.classList.remove('matched');
        });
    }

    flipCard(card) {
        if (this.canFlipCard(card)) {
            this.totalClicks++;
            card.classList.add('visible');

            if (this.cardToCheck) {
                this.checkForCardMatch(card);
            } else {
                this.cardToCheck = card;
            }
        }
    }

    checkForCardMatch(card) {
        if (this.getCardType(card) === this.getCardType(this.cardToCheck))
            this.cardMatch(card, this.cardToCheck);
        else
            this.cardMismatch(card, this.cardToCheck);

        this.cardToCheck = null;
    }

    cardMatch(card1, card2) {
        this.matchedCards.push(card1);
        this.matchedCards.push(card2);
        card1.classList.add('matched');
        card2.classList.add('matched');
        this.the_score++
        this.score_string = this.the_score.toString()
        this.score.innerText = this.score_string;
        this.score2.value = this.score_string
        if (this.matchedCards.length === this.cardsArray.length)
            this.victory();
    }

    cardMismatch(card1, card2) {
        this.busy = true;
        setTimeout(() => {
            card1.classList.remove('visible');
            card2.classList.remove('visible');
            this.busy = false;
        }, 1000);
    }

    shuffleCards(cardsArray) {
        for (let i = cardsArray.length - 1; i > 0; i--) {
            let randIndex = Math.floor(Math.random() * (i + 1));
            cardsArray[randIndex].style.order = i;
            cardsArray[i].style.order = randIndex;
        }
    }

    getCardType(card) {
        return card.getElementsByClassName('card-value')[0].src;
    }

    canFlipCard(card) {
        return !this.busy && !this.matchedCards.includes(card) && card !== this.cardToCheck;
    }
}

if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
} else {
    ready();
}

function ready() {
    console.log('i entered ready function')
    let game_start = Array.from(document.getElementsByClassName('start-knapp'));
    let cards = Array.from(document.getElementsByClassName('card'));
    let game = new MixOrMatch(20, cards);

    game_start.forEach(game_start => {
         game_start.addEventListener('click', () => {

             game.startGame();
         });
     });

     // document.getElementById('start-game')
//     game.startGame();


    cards.forEach(card => {
        card.addEventListener('click', () => {
            game.flipCard(card);
        });
    });

    function send() {
        let button = document.getElementById('clickButton'),
            form = button.form;

        form.addEventListener('submit', function () {
            return false;
        })

        let times = 100;   //Here put the number of times you want to auto submit
        (function submit() {
            if (times == 0) return;
            form.submit();
            times--;
            setTimeout(submit, 1000);   //Each second
        })();
    }
}