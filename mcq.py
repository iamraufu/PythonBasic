from Question import Question

questions_prompts = [
    "Who developed the Python language?\n(a) Zim Den\n(b) Guido van Rossum\n(c) Niene Stom\n(d) Wick van Rossum\n\n",
    "What is the maximum possible length of an identifier?\n(a) 16\n(b) 32\n(c) 64\n(d) None of these\n\n",
    "In which year was the Python language developed?\n(a) 1995\n(b) 1972\n(c) 1981\n(d) 1989\n\n",
    "In which language is Python written?\n(a) English\n(b) PHP\n(c) C\n(d) All of the above\n\n",
    "In which year was the Python 3.0 version developed?\n(a) 2008\n(b) 2000\n(c) 2010\n(d) 2005\n\n"
]

questions = [
    Question(questions_prompts[0], "d"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "d"),
    Question(questions_prompts[3], "c"),
    Question(questions_prompts[4], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)