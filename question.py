class Question:
    def __init__(self):
        self.text = ""
        self.answer = ""
        self.score = 0

    def setQuestion(self, text):
        self.text = text

    def setAnswer(self, answerText):
        self.answer = answerText

    def addScore(self):
        self.score += 1

    def checkAnswer(self, input):
        return input == self.answer

    def display(self):
        print(self.text)

    def displayScore(self):
        return self.score

