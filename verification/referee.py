"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"

checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.

checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.

"""

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers
from prediction import CheckioRefereePrediction

from tests import TESTS

from math import hypot

MAX_DIST = 3

def ext_checker(answer, user_result):
    if (not isinstance(user_result, (list, tuple)) or len(user_result) != 2 or
            not isinstance(user_result[0], (int, float)) or
            not isinstance(user_result[0], (int, float))):
        return False, "The result should be a list/tuple of the numbers.", 0
    if (not 0 <= user_result[0] < 10 or not 0 <= user_result[1] < 10):
        return False, "The prediction coordinates should be from 0 to 10.", 0
    distance = hypot(answer[0] - user_result[0], answer[1] - user_result[1])
    score = 0 if distance >= 1 else round(100 * distance / MAX_DIST)
    return True, "Next", score

cover = """def cover(f, data):
    return f(tuple(tuple(d) for d in data))
"""


api.add_listener(
    ON_CONNECT,
    CheckioRefereePrediction(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        },
        checker=ext_checker,  # checkers.float.comparison(2)
        function_name="predict_ghost"
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
