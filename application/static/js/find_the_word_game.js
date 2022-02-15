// (1) Skapa en Array med ord
// (2) Skapa en function som slumpar ett ord ur arrayen.
// (3) Shuffla ordet, så att tex popcorn blir ocrnpop
// (4) skicka den shufflade strängen till random word elementet
// (5) gör dom shufflade bokstäverna klickbara, så att den bokstaven man klickat på
//     hamnar i den blå boxen.
// (6) När man fått ett ord, skall man trycka på kontroll knappen, för att jämföra
//     om ordet man valt är detsamma som det slumpade ordet. Om det är det skall man få
//     poäng, annars skall ett nytt ord slumpas fram och shufflas.
// (7) och när man fått ett ord och det är kontrollerat skall nästa knappen lysa upp.


// Punkt 1
    let Wordarray = ['python', 'fåtölj', 'popcorn', 'apelsin', 'sjuksköterska', 'kalender', 'svenska', 'danska', 'hund'
        , 'katt', 'gais', 'köttbullar', 'spagetti', 'blomma', 'zebra', 'måne', 'solen', 'torsk', 'lax', 'lejon',
        'tröja', 'byxor', 'dator', 'giraff', 'hårtork', 'tavla','sköldpadda', 'piano', 'ljusstake',
        'mugg', 'mobiltelefon', 'påse', 'tofflor', 'hörlurar', 'ros', 'skål', 'godis', 'kaka',
        'glass', 'tulpan', 'blåbär', 'jordgubbe', 'tält', 'träd', 'skola', 'bio', 'tv', 'glasögon', 'papper',
        'lägenhet', 'dagis', 'ryggsäck', 'fröken', 'lärare', 'penna', 'stol', 'huvud', 'näsa', 'öron', 'axlar', 'knä'
        , 'tår'];
    let get_my_element = document.getElementById('la_word');
    let chosenLetters = document.querySelector('.input_letters');
    let score = '';
    let points = 0;
    let sortedArray = [];
    let rnd_letters = document.querySelector('.random_word');

    let selected_word = ""
    let button = document. querySelector('.next_btn')
    let index = 0;
    let num_of_elements = Wordarray.length
    let turn_counter = 0;
        chosenLetters.value = ""
    let score2 = document.getElementById('txt2');
    let score_box = 0;

    function start_from_button(){

            let one_letter = document.querySelectorAll('h1');
            one_letter.forEach(function (one_letter) {
                rnd_letters.removeChild(one_letter);
            })
        shuffla_shuffla();



    }

    shuffla_shuffla();


// Punkt 2
    function shuffla_shuffla() {

    button.disabled = true;
    selected_word = Wordarray[Math.floor(Math.random() * Wordarray.length)];
    console.log(selected_word);

// punkt 3
    let splitted_letters = selected_word.split('');
    sortedArray = splitted_letters.sort((a,b) => 0.5 - Math.random());
    displayLetters();
     }

//


    function displayLetters(){

        for (let i = 0; i < sortedArray.length; i++) {
            let letters = document.createElement('h1');
            letters.innerHTML = sortedArray[i];
            rnd_letters.appendChild(letters);

         }
        remove_letters_from_screen()
}




    function remove_letters_from_screen() {

        let one_letter = document.querySelectorAll('h1');
        one_letter.forEach(function (one_letter) {
            one_letter.addEventListener('click', () => {

                chosenLetters.value += one_letter.innerText;
                rnd_letters.removeChild(one_letter);
                let user_word = chosenLetters.value;
                chosenLetters.innerText = user_word;
                /*if (uppercased.includes(user_word)) {

                }*/
            })
        })
    }
    function checkWord(){
        let is_it_right_word = chosenLetters.value;

       if(is_it_right_word === selected_word)
       {
                score = document.querySelector('.score');
                score2 = document.querySelector('#txt2');
                    points ++;
                score.innerText = points.toString() + " Poäng";
                index = Wordarray.indexOf(selected_word)
                Wordarray.splice(index,1);
                console.log(Wordarray);
                button.disabled = false;
                chosenLetters.value="Rätt Ord!"


       }else {
                index = Wordarray.indexOf(selected_word)
                Wordarray.splice(index,1);
                console.log(Wordarray);
                button.disabled = false;
                chosenLetters.value="Fel Ord!"



       }

    }
        function NextWord(){

            chosenLetters.value=""

            turn_counter ++;
            let one_letter = document.querySelectorAll('h1');
            one_letter.forEach(function (one_letter) {
                rnd_letters.removeChild(one_letter);
            })

            if(turn_counter === num_of_elements)
            {
              let the_end = document.querySelector('.text_end_game');
               the_end.innerText ="Spelet är slut."
                send();
                turn_counter = 0;
             }



            shuffla_shuffla()

        }

         function send() {
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