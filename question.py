class Question:
    def __int__(self):
        self._text = ""
        self._answer = ""

    def setQuestion(self, text):
        self._text = text

    def setAnswer(self, answerText):
        self._answer = answerText

    def checkAnswer(self, input):
        return input == self._answer

    def display(self):
        print(self._text)
