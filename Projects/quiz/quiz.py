import random
import json

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self. score = 0
    
    def set_questions(self,questions):
        self.questions = questions
        

    def start(self):
        print("Welcome to Quiz Game! If you want to quit now, press 'q' and quit. Each question is 1 point.")
        random.shuffle(self.questions)
        for question in self.questions:
            print(question["question"])
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == question["answer"].lower():
                print("Correct Answer!")
                self.score += 1
            elif user_answer.lower() =="q":
                print("Game Over!")
                break
            else:
                print(f"Wrong Answer. Correct answer is: {question['answer']}")
        print(f"Game Over! Your score: {self.score}/{len(self.questions)}")
def read_questions_from_file(file_path):
    questions=[]
    with open(file_path, "r") as file:
        questions = json.load(file)
        return questions
questions = read_questions_from_file("Projects\quiz\questions.json")

quiz = QuizGame(questions)
quiz.start()
        