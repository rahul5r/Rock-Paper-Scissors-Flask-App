from flask import Flask, render_template, request
import random

app = Flask(__name__)

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif ((user_choice == 1 and computer_choice == 3) or
          (user_choice == 2 and computer_choice == 1) or
          (user_choice == 3 and computer_choice == 2)):
        return "User"
    else:
        return "Computer"

def get_choice(n):
    choices = {1: "rock", 2: "paper", 3: "scissor"}
    return choices.get(n, "Invalid")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def game():
    user_choice = int(request.form.get('button'))
    computer_choice = random.randint(1, 3)
    winner = check_winner(user_choice, computer_choice)
    return render_template('index.html',
                           user_choice=get_choice(user_choice),
                           computer_choice=get_choice(computer_choice),
                           winner=winner)

if __name__ == '__main__':
    app.run(debug=True)
