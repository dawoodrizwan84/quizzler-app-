from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250, bg= "white")
        self.question_text = self.canvas.create_text(150,125, width=250,
                                                     text="Questions",
                                                   fill=THEME_COLOR, font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image,highlightthickness=0,
                                   command=self.correct_answer)
        self.cross_button.grid(row=2, column=1)

        check_image = PhotoImage(file="images/true.png")
        self.check_button= Button(image=check_image, highlightthickness=0,
                                  command=self.wrong_answer)
        self.check_button.grid(row=2, column=0)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")
    def correct_answer(self):
        # is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)






