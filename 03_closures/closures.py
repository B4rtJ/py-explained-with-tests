import logging
import unittest
from typing import List, Tuple

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_closure(self):
        def function(number : int, string : str):

            local_variable = 5
    
            def _closure():
                 log.debug(f"{type(string)} object at {hex(id(string))}, {string=}")
                 log.debug(f"{type(number)} object at {hex(id(number))}, {number=}")
                 log.debug(f"{type(local_variable)} object at {hex(id(local_variable))}, {local_variable=}")
                 return (string, number, local_variable)

            self.assertEqual(_closure(), (string, number, local_variable))

            self.assertIs(local_variable, _closure.__closure__[0].cell_contents)
            self.assertIs(number, _closure.__closure__[1].cell_contents)
            self.assertIs(string, _closure.__closure__[2].cell_contents)

            return _closure

        closure = function(123, "abc")
        for cell in closure.__closure__:
            log.debug(f"{cell}, {cell.cell_contents}")

    def test_lambda_modulo_addition(self):

        modulus = 4
        lambda_add = lambda a, b, /: (a + b) % modulus
        self.assertEqual(lambda_add(123, 456), (123 + 456) % 4)


    def test_lambda_average(self):
        lambda_average = lambda *args : sum(args)/len(args)
        self.assertEqual(lambda_average(1,2,3,4,5,6), sum([1,2,3,4,5,6])/6)

    def test_lambda_weighted_average(self):
        weighted_average_args : Tuple[Tuple[int, float]] = ((1,2), (4,5), (4, 1.6), (5, 2))

        def weighted_average(*args):
            _sum = 0
            _len = 0
            for t in args:
                _sum += t[0] * t[1]
                _len += t[1]
            return _sum / _len

        lambda_weighted_average = lambda *args : sum(map(lambda t: t[0] * t[1], args)) / sum(map(lambda t: t[1], args))
        self.assertEqual(weighted_average(*weighted_average_args), lambda_weighted_average(*weighted_average_args))

    def test_exercise(self):
        def function(s:str):
            def closure():
                s2 = s.upper()
                return "_".join(s2)
            return closure
        lam = lambda s: "_".join(s.upper())
        self.assertEqual(lam("wdwqede"),function("wdwqede")())
        """Define closure and lambda.
            Both of them should change given string to uppercase
            and add underscore at the beginning.
            Add some tests.
        """

if __name__ == "__main__":
    unittest.main(verbosity=2)
