"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
import random


TESTS = {
    "Score": [

    ]
}

N = 20
SIZE = 10


def generate_formula(prob_x=0.3, prob_bracket=0.2):
    formula = "x"
    for _ in range(15):
        operation = random.choice(["+", "-", "*", "/"])
        formula += operation
        if random.random() < prob_x:
            formula += "x"
        else:
            formula += str(round(random.random() * 10, 3))
        if random.random() < prob_bracket:
            formula = "(" + formula + ")"
    return formula


for dummy in range(N):
    formula_x = generate_formula()
    formula_y = generate_formula()
    points = []
    for x in range(1, 12):
        try:
            print(eval(formula_x))
            i = round(eval(formula_x) % 10, 3)
            j = round(eval(formula_y) % 10, 3)
            points.append([i, j])
        except OverflowError:
            dummy -= 1
            break
    else:
        TESTS["Score"].append({"input": points[:-1], "answer": points[-1]})
