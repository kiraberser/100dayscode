from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)
first_question = QuizBrain(question_bank)

while first_question.still_has_question(): 
    first_question.next_question()

print("You've completed the quiz")
print(f"Your final score was: {first_question.score}/{first_question.question_number}")

