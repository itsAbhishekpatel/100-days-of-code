from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# question bank which consist of a list of quesiton objects 
question_bank = []

# create n objects and store in a list 
for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()

