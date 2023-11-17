from flask import Flask
from random import randint

app = Flask(__name__)

number = randint(0,9)
print(number)

@app.route('/')
def home():  # put application's code here
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif'></img>"

@app.route('/<int:num>')
def check_guess(num):
    if num > number:
        return "<h1>Too High!</h1><img src='https://media.giphy.com/media/yoJC2Olx0ekMy2nX7W/giphy.gif'</img>"
    elif num < number:
        return "<h1>Too Low!</h1><img src='https://media.giphy.com/media/O3JyUHiKqsviE/giphy.gif'</img>"
    else:
        return "<h1>You found me!</h1><img src='https://media.giphy.com/media/S9i8jJxTvAKVHVMvvW/giphy.gif'</img>"


if __name__ == '__main__':
    app.run()
