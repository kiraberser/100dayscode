from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question


THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = 0
        self.label = Label()
        self.label.config(text=f"Score: {self.score}", padx=20, pady=20, bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        
        right = PhotoImage(file="images/true.png")
        self.button_true = Button(image=right, highlightthickness=0, command=self.is_true)
        self.button_true.grid(column=0, row=3)
        
        false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false, highlightthickness=0, command=self.is_false)
        self.button_false.grid(column=1, row=3)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            
    def is_true(self):
        
        self.give_feedback(self.quiz.check_answer("True"))
        
    def is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
        
        