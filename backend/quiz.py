from typing import List
import json


class Question:
    def __init__(self, qn: str, choices: List, answer: int):
        """
        Question class
        :param qn: Question to ask.
        :param choices: MCQ choices in a list.
        :param answer: index of the correct answer in the choices list.
        """
        self.qn = qn
        self.choices = choices
        self.answer = answer

    def get_qn(self):
        return self.qn

    def get_choices(self):
        return self.choices

    def get_answer(self):
        return self.answer

    def send_qn(self):
        payload = {"qn": self.get_qn, "choices": self.choices}
        return json.dumps(payload)

    def check_answer(self, choice):
        """
        Check if the given answer is correct.
        :param choice: Index of the chosen answer from the student.
        :return: boolean if given choice is correct.
        """
        return choice == self.get_answer()


class Quiz:
    def __init__(self, level):
        self.level = level
        self.qns = self.read_qns()

    def read_qns(self):
        qns_path = f"./db/questions/{self.level}.json"
        with open(qns_path) as f:
            qns = [Question(qn["qn"], qn["choices"], qn["answer"]) for qn in json.load(f)]
            return qns


if __name__ == "__main__":
    ...
