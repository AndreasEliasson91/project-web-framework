# Learning By Games

## Description
A learning plattform for kids. Created for a project in Web Development, in the course _Project In Web Framework_ at __Teknikhögskolan in Göteborg__. <br /><br />
The idea is for kids to develop their knowledge in reading and writing swedish and math, in a fun way using basic games. The four games we currently have is: <br />
- __Hitta ordet!__ - A find the word game, where the player has to guess a word in swedish from an anagram
- __Cute Memory__ - Basic memory game, with cute animal pictures
- __Ordgåtan__ - Swedish word game. The player draws a card with a random sentence and answers a question based on the cards statement
- __A-Maze-ing-Game__ - Math game. The player navigates through a maze by answer math questions<br /><br />

The projects run with a Flask framework and uses a MongoDB database.<br /><br />

## Dependencies
To install dependencies from the requirements-file:
```
pip install -r requirements.txt
```
<br />The project also requires a running __MongoDB__ (we're using a docker container to set that up) and a _.env_ with the following variables:
```
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT

SECRET_KEY= To encrypt and decrypt passwords
```
<br />It also needs a _config.cfg_ in the application package for mail services to work. I need to contain the following:
```
MAIL_SERVER
MAIL_USERNAME
MAIL_PASSWORD
MAIL_PORT
MAIL_USE_SSL
MAIL_USE_TLS
```

## Contributors
We're a team of four people who worked on this project:
- [Andreas](https://github.com/AndreasEliasson91)
- [Anna](https://github.com/S172258)
- [Lenny](https://github.com/lennyrydweissner)
- [Markus](https://github.com/Antonsen2)
<br /><br />
### Teknikhögskolan - Python Development, specializing in AI
_Handed in for evaluation 16/2 2022_
