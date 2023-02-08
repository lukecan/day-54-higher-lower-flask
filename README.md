# HIGHER LOWER GAME WITH FLASK
A simple Flask web application that allows the user to guess a number between 0 and 9. The application generates a random number and checks if the user's input matches the random number. If the number is correct, it returns a "You Found Me!" message and a celebratory gif. If the user's input is too low, it returns a "Too Low!" message and a disappointed gif. If the user's input is too high, it returns a "Too High!" message and a disappointed gif.

## Requirements

- Flask
- random

## Usage
To run the application either run it through and IDE or execute the following command in terminal:
`export FLASK_APP = server.py`
`flask run`
Open your web browser and go to http://localhost:5000/. The main page will display a "Guess a number between 0 and 9!" message and a fun gif. You can make a guess by entering a number in the URL, for example, http://localhost:5000/5.

## How It Works

The application generates a random number between 0 and 9 when it starts. The user can make a guess by entering a number in the URL. The number function in the guess_the_number.py file checks if the user's input matches the random number. If the number is correct, it returns a "You Found Me!" message and a celebratory gif. If the user's input is too low, it returns a "Too Low!" message and a disappointed gif. If the user's input is too high, it returns a "Too High!" message and a disappointed gif.

## Conclusion

This is a simple Flask application that demonstrates the basic functionality of Flask and serves as a good starting point for more complex Flask projects.