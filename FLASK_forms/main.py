from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    imie = None
    haslo = None
    if request.method == 'POST':
        imie = request.form['username']
        haslo = request.form['password']
    return f"<h1>imie {imie}, haslo {haslo}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
