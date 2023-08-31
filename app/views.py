# di sini tempat import common library
import random

# di sini tempat import library yang khusus untuk project ini
from flask import render_template
from app import app

#############################################
import random

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/testingrandom")
def testingrandom():
    dice = [1, 2, 3, 4, 5, 6]
    randomchoice = random.choice(dice)
    randomchoice = str(randomchoice)
    return randomchoice
    

#############################################
if __name__ == "__main__":
    app.run()