from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Arial', 16, 'bold'))
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Hello',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_btn_image = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_btn_image, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)
        false_btn_image = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_btn_image, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f'Score:{self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of Quizz')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
