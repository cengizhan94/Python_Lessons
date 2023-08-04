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
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')
        for q in question.choices:
            print('-'+q)
        answer = input('answer: ')
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showScore(self):
        print('score:', self.score)
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex +1
        
        if questionNumber > totalQuestion:
            print('Quiz end')
        else:
            print(f'Question{questionNumber} of {totalQuestion}'.center(100,"*"))
        
question1 =Question("Best Languege: ", ["C#","Python","JavaScript","C++"],"Python") 
question2 = Question("Most Popular Languege: ", ["C#","Python","JavaScript","C++"],"Python")
question3 = Question("Most Profitable Languege: ", ["C#","Python","JavaScript","C++"],"Python")
question4 = Question("Most lovely Languege: ", ["C#","Python","JavaScript","C++"],"Python")
question5 = Question("Most easy Languege: ", ["C#","Python","JavaScript","C++"],"Python")


questions = [question1,question2,question3,question4,question5]

quiz = Quiz(questions)
quiz.loadQuestion()