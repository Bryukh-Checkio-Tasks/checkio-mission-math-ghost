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

N = 30
SIZE = 10

import math

def generate_formula(prob_x=0.5, prob_bracket=0.2, prob_trig=0.25):
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
        if random.random() < prob_trig:
            formula = "math." + random.choice(["sin", "cos"]) + "(" + formula + ")"
    return formula

dummy = 0
while dummy < N:
    formula_x = generate_formula()
    # formula_y = generate_formula()
    values = []
    for x in range(1, 12):
        try:
            i = round(eval(formula_x), 3)
            values.append(i)
        except (OverflowError, ZeroDivisionError):
            break
    else:
        if abs(max(values) - min(values)) >= 1:
            TESTS["Score"].append({"input": values[:-1],
                                   "answer": values,
                                   "real_point": values[-1]})
            dummy += 1