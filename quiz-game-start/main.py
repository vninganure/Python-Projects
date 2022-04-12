from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_q = Question(question_text,question_ans)
    question_bank.append(new_q)
c_quest = QuizBrain(question_bank)

while c_quest.still_has_question():
    c_quest.next_question()
