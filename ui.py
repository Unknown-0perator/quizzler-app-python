from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Arial', 16, 'bold'))
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Hello',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_btn_image = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_btn_image, highlightthickness=0)
        self.true_btn.grid(column=0, row=2)
        false_btn_image = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_btn_image, highlightthickness=0)
        self.false_btn.grid(column=1, row=2)
        self.window.mainloop()
