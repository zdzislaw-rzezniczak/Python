from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        res = function()
        modified = f'<b>{res}</b>'
        return modified
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        res = function()
        modified = f'<i>{res}</i>'
        return modified
    return wrapper_function

@app.route("/")
@make_bold
@make_italic
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
