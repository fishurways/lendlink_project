from app import app
from app import User, db

# di sini tempat import built-in library
import random

# di sini tempat import library yang khusus untuk project ini
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    '''This is for login page.'''
    username = request.form["username"]
    password = request.form["password"]

    print(username)
    print(password)

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        # Login sukses
        flash("Login sukses!", "success")
        return redirect(url_for("welcome"))
    else:
        # Login gagal
        flash("Login gagal. Periksa kembali username dan password Anda.", "danger")
        return redirect(url_for("index"))

@app.route("/welcome")
def welcome():
    return "Selamat datang! Anda berhasil login."


    
@app.route("/register", methods=["GET", "POST"])
def register():
    '''This is for register page.'''
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username sudah digunakan. Silakan pilih username lain.", "danger")
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Registrasi sukses! Silakan login dengan akun baru Anda.", "success")
            return redirect(url_for("index"))
    return render_template("register.html")
                            

@app.route("/testingrandom")
def testingrandom():
    dice = [1, 2, 3, 4, 5, 6]
    randomchoice = random.choice(dice)
    randomchoice = str(randomchoice)
    return randomchoice
    

#############################################
if __name__ == "__main__":
    app.run()
