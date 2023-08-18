from flask import Flask
app = Flask(__name__)
#############################################
import random

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/testingrandom")
def testingrandom():
    import random
    dice = [1, 2, 3, 4, 5, 6]
    randomchoice = random.choice(dice)
    randomchoice = str(randomchoice)
    return randomchoice
    

#############################################
if __name__ == "__main__":
    app.run()