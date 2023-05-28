import json
from flask import Flask, request


app = Flask(__name__)


@app.route("/questions/<level>")
def get_questions(level):
    qns_path = f"./db/questions/{level}.json"
    qns =
    return json.dumps(x)


@app.route("/test", methods=["POST"])
def test2():
    print(request.form["test"])
    return "HEY"
