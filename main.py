from choiceQuestion import ChoiceQuestion


def main():

    score = ChoiceQuestion()

    first = ChoiceQuestion()
    first.setQuestion("5x5")
    first.addChoice("25", True)
    first.addChoice("55", False)
    first.addChoice("10", False)
    first.addChoice("0", False)

    second = ChoiceQuestion()
    second.setQuestion("What is 3 squared?")
    second.addChoice("6", False)
    second.addChoice("9", True)
    second.addChoice("33", False)
    second.addChoice("32", False)

    third = ChoiceQuestion()
    third.setQuestion("10x5")
    third.addChoice("105", False)
    third.addChoice("15", False)
    third.addChoice("25", False)
    third.addChoice("50", True)

    fourth = ChoiceQuestion()
    fourth.setQuestion("3x6")
    fourth.addChoice("36", False)
    fourth.addChoice("30", False)
    fourth.addChoice("18", True)
    fourth.addChoice("9", False)

    presentQuestion(first, score)
    presentQuestion(second, score)
    presentQuestion(third, score)
    presentQuestion(fourth, score)

    print("Your Score is", score.displayScore())
    if score.displayScore() == 4:
        print("You got perfect!")

def presentQuestion(q, s):
    q.display()
    answer = input("Your Answer: ")
    print(q.checkAnswer(answer))
    if q.checkAnswer(answer):
        s.addScore()

main()