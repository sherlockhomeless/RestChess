from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "is running"


@app.route("/game")
def return_current_gamestate():
    pass


@app.route("/move", methods=["POST"])
def make_move(move):
    assert request.method == "POST"
    pass


@app.route("/log")
def return_log():
    pass


@app.route("/init", methods=["POST"])
def init_board():
    pass

