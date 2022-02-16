from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Soroush Mehraban',
        'title': 'Blog post 1',
        'content': "First post content",
        "date_posted": "February 16, 2022"
    },
{
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': "Second post content",
        "date_posted": "February 16, 2022"
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
