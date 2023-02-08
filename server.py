from flask import Flask
from random import randrange

# Generate random number for guessing game
rand_number = randrange(0, 9)

# Initialize Flask app
app = Flask(__name__)


# Route for the home page
@app.route("/")
def index():
    return "<h1 style=text-align:center>Guess a number between 0 and 9!</h1>" \
           "<img style='display:block; margin-left: auto; margin-right: auto;' " \
           "src='https://media.giphy.com/media/iGq09qqrDmbJ98wkZo/giphy.gif'>"


# Route for guessing the number
@app.route("/<number>")
def number(number):
    # Check if the guessed number is equal to the generated number
    if rand_number == int(number):
        return "<h1 style='color:green; text-align:center;'>You Found Me! </h1>" \
               "<img style='display:block; margin-left: auto; margin-right: auto;' " \
               "src='https://media.giphy.com/media/XxSFFgDxlg6cFsCDiZ/giphy.gif'>"
    # Check if the guessed number is less than the generated number
    elif int(number) < rand_number:
        return "<h1 style='color:red; text-align:center;'>Too Low!</h1>" \
               "<img style='display:block; margin-left: auto; margin-right: auto;' " \
               "src='https://media.giphy.com/media/BEob5qwFkSJ7G/giphy.gif'>"
    # If none of the above conditions are met, it means the guessed number is higher than the generated number
    else:
        return "<h1 style='color:red; text-align:center;'>Too High!</h1>" \
               "<img style='display:block; margin-left: auto; margin-right: auto;' " \
               "src='https://media.giphy.com/media/BEob5qwFkSJ7G/giphy.gif'>"


# Main function to run the app
if __name__ == "__main__":
    app.run(debug=True)
