from question import Question


class ChoiceQuestion(Question):

    def __init__(self):
        super().__init__()
        self._choices = []


    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)


    def display(self):
        super().display()
        for i in range(len(self._choices)):
            choiceNumber = i + 1
            print("%d: %s" %(choiceNumber, self._choices[i]))


