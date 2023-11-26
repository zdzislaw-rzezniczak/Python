from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)
AGIFY_API_URL = "https://api.agify.io"
GENDERIZE_API_URL = "https://api.genderize.io/"


@app.route("/")
def hello_world():
    year = dt.datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def guess_age_gender(name):
    name_capitlize = name.title()
    query = {"name": name}
    response_agify = requests.get(AGIFY_API_URL, params=query)
    age = response_agify.json()['age']
    response_gender = requests.get(GENDERIZE_API_URL, params=query)
    print(response_gender.json())
    gender = response_gender.json()['gender']
    return render_template("guess.html", name=name_capitlize, age=age, gender=gender)



@app.route("/blog/<num>")
def get_blog(num):

    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
