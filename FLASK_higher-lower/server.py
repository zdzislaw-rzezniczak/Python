from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home():
    return ("<h1> Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


random_number = random.randint(0, 9)
print(random_number)


@app.route('/<int:number>')
def guess_number(number):
    if number == random_number:
        return ("<h1> You win</h1>"
                 "<img src='https://media.giphy.com/media/26u4exk4zsAqPcq08/giphy.gif'>")
    elif number > random_number:
        return ("<h1> Try lower</h1>"
                 "<img src='https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif'>")

    else:
        return ("<h1> Try higher </h1>"
                 "<img src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)