from flask import Flask
from flask import render_template

app = Flask("jobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


app.run()
