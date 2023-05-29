import json
from flask import Flask, request
from quiz import QuizStore


app = Flask(__name__)
quiz_store_path = "./backend/db/quizzes.json"
quiz_store = QuizStore(quiz_store_path)


@app.get("/quiz")
def get_quiz_names_and_ids():
    quiz_names_and_ids = quiz_store.get_quiz_names()
    return json.dumps(quiz_names_and_ids)


@app.get("/quiz/<idx>")
def get_quiz(idx):
    quiz = quiz_store.get_quiz(int(idx))
    return json.dumps(quiz)


@app.post("/quiz")
def add_quiz():
    quiz_name = request.form["name"]
    author = request.form["author"]
    qns = json.loads(request.form["qns"])
    raw_quiz = {
        "metadata": {
            "name": quiz_name,
            "author": author,
        },
        "qns": qns
    }
    quiz_store.add_quiz(raw_quiz)
    return "True"


@app.delete("/quiz/<idx>")
def delete_quiz(idx):
    quiz_store.delete_quiz(int(idx))
    return "True"
