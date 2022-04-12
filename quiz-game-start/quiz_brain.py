import self as self


class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (true/false) :").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, currect_answer):
        if user_answer == currect_answer:
            print("You are right")
            self.score +=1
        else:
            print("You are wrong")
        print(f"the correct answer is {currect_answer}")
        print(f"your current score is {self.score}/{self.question_no}")