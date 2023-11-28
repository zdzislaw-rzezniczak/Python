import smtplib
from email.mime.text import MIMEText

from flask import Flask, render_template, request
from post import Post
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

password = "###########"
recipients = ["zdzichrz@gmail.com"]
sender = "zdzichrz@gmail.com"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


@app.route('/')
def get_all_posts():
    print(posts)
    return render_template("index.html", posts=post_objects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)




@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        body = f"""
        From: {name};
        email: {email};
        phone number: {phone};
        message: {message};
        """
        send_email(subject=data['name'], body=body, sender=sender, recipients=recipients,
                   password=password)
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
