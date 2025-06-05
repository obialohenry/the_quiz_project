from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =  []

for question in question_data:
    # print(f"a question: {question["text"]}")
    a_question_and_answer = Question(question=question["text"], answer=question["answer"])
    question_bank.append(a_question_and_answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    print(quiz.next_question())
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")