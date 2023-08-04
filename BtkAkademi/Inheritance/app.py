class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

question1 =Question("Best Languege: ", ["C#","Python","JavaScript","C++"],"Python") 
question2 = Question("Most Popular Languege: ", ["C#","Python","JavaScript","C++"],"Python")
question3 = Question("Most Profitable Languege: ", ["C#","Python","JavaScript","C++"],"Python")

questions = [question1,question2,question3]

quiz = Quiz[questions]