from flask import Flask, render_template, request, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Jane Doe',
        'title': 'Blog Post content',
        'content': 'Second post content',
        'data_posted': 'April 21, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post content',
        'content': 'Second post content',
        'data_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title= "About")
