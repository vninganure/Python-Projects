THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizeInterface:

    def __init__(self, QuizBrain: QuizBrain):
        self.quize = QuizBrain

        self.window = Tk()
        self.window.title("Quizeller")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvass = self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Hi, Vijay", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text=f"score:{self.quize.score}", bg=THEME_COLOR, fg="white", font=("Arial",16, "bold"))
        self.score_label.grid(row=0, column=1)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quize.still_has_questions():
            self.score_label.config(text=f"score:{self.quize.score}")
            q_text = self.quize.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached of end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quize.check_answer(user_answer="True"))

    def false_pressed(self):
        is_right = self.quize.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)




