import json


class QuizStore:
    def __init__(self, quiz_store_path):
        self.quiz_store_path = quiz_store_path
        self.quizzes = self._read_quiz_store()
        self.max_quiz_id = self._get_max_quiz_id()

    def _read_quiz_store(self):
        with open(self.quiz_store_path) as f:
            try:
                quizzes = json.load(f)
            except json.decoder.JSONDecodeError as e:
                quizzes = list()
        return quizzes

    def _get_max_quiz_id(self):
        if len(self.quizzes) == 0:
            max_quiz_id = -1
        else:
            max_quiz_id = max([quiz["metadata"]["id"] for quiz in self.quizzes])
        return max_quiz_id

    def _save_quizzes(self):
        with open(self.quiz_store_path, 'w') as f:
            json.dump(self.quizzes, f)

    def _index_quiz(self, quiz):
        self.max_quiz_id += 1
        quiz["metadata"]["id"] = self.max_quiz_id
        idx = 0
        for level in ("easy", "medium", "advanced"):
            for qn in quiz["qns"][level]:
                qn["index"] = idx
                idx += 1

    def get_quiz(self, quiz_id):
        for quiz in self.quizzes:
            if quiz["metadata"]["id"] == quiz_id:
                return quiz

    def get_quiz_names(self):
        quiz_names_and_ids = [[quiz["metadata"]["name"], quiz["metadata"]["id"]] for quiz in self.quizzes]
        return quiz_names_and_ids

    def add_quiz(self, quiz):
        assert quiz["metadata"]["name"] is not None
        self._index_quiz(quiz)
        self.quizzes.append(quiz)
        self._save_quizzes()

    def delete_quiz(self, idx):
        for i, quiz in enumerate(self.quizzes):
            if quiz["metadata"]["id"] == idx:
                quiz_idx = i
                break
        else:
            quiz_idx = None
        if quiz_idx is not None:
            del self.quizzes[quiz_idx]
            self._save_quizzes()


if __name__ == "__main__":
    # create sample quiz
    quiz = {
        "metadata": {
            "name": "Math Quiz 2",
            "author": "Bryan Leong"
        },
        "qns": {
            "easy": [
                {
                    "qn": "What is 1-1?",
                    "choices": ["0", "1", "2", "3"],
                    "answer": 0
                },
                {
                    "qn": "What is 10+5?",
                    "choices": ["0", "15", "2", "3"],
                    "answer": 1
                },
                {
                    "qn": "What is 7+100?",
                    "choices": ["0", "1", "107", "3"],
                    "answer": 2
                }
            ],
            "medium": [
                {
                    "qn": "What is 2*10?",
                    "choices": ["0", "4", "1", "20"],
                    "answer": 3
                },
                {
                    "qn": "What is 10*90?",
                    "choices": ["100", "900", "600", "30"],
                    "answer": 1
                },
                {
                    "qn": "What is 10/5?",
                    "choices": ["0", "2", "17", "5"],
                    "answer": 1
                }
            ],
            "advanced": [
                {
                    "qn": "What is 2*2+5?",
                    "choices": ["0", "4", "9", "5"],
                    "answer": 2
                },
                {
                    "qn": "What is (10*5)/2?",
                    "choices": ["100", "1", "25", "30"],
                    "answer": 2
                },
                {
                    "qn": "Why did uNivUS crash on 29/5?",
                    "choices": ["Because someone forgot to enable load balancing! :(", "1", "17", "5"],
                    "answer": 0
                }
            ],
        },
    }

    quiz_store = QuizStore("./backend/db/quizzes.json")
    # quiz_store.add_quiz(quiz)
    print(quiz_store.get_quiz_names())
    print(quiz_store.get_quiz(0))
