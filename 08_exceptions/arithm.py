import ast
import logging
from typing import Union
import unittest
extensions = ['sphinx.ext.napoleon']
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

logger = logging.getLogger()


class Numeric:
    class NotANumber(ArithmeticError):
        """

        """


    def __init__(self, x : Union[float, int, bytes]):
        try:
            self.__val = float(x)
        except ValueError:
            self.__val = Numeric.from_ast(x)

    @staticmethod
    def from_ast(x):
        result = None
        try:
            result = ast.literal_eval(x)
        except ValueError as err:
            raise Numeric.NotANumber("type conversion error") from err
        else:
            try:
                assert isinstance(result, (float, int))
            except AssertionError as err:
                raise Numeric.NotANumber("bad type error") from err

        return result

    def __truediv__(self, x):
        result = None
        try:
            result = self.__val / float(x)
        except ZeroDivisionError as err:
            logger.error(err)
            result = float('NaN')
            logger.warning("falling back to %f", result)
        except Exception as err:
            logger.exception("Unhandled exception")
            raise err
        else:
            logger.debug("no exception")
        finally:
            logger.debug("result is %s", result)
        return result

    def __lt__(self, x):
        return self.__val < float(x)

    def __eq__(self, x):
        return float(self.__val) == float(x)

    def __int__(self):
        return int(self.__val)

    def __float__(self):
        return float(self.__val)

    def __pow__(self, x):
        """
        Todo:
            Add `OverflowError` exception handler.
            
            Return `+inf` once overflowed value is positive
            `-inf` otherwise`. Fix tests.
        """
        try:
            return self.__val ** float(x)
        except OverflowError as err:
            if self.__val < 0:
                return "-inf"
            if self.__val > 0:
                return "inf"

    def __repr__(self):
        return str(self.__val)


class Tests(unittest.TestCase):
    def setUp(self):
        print("\n" + 50 * "-")

    def test_division_by_zero(self):
        self.assertIsNotNone(Numeric(5) / Numeric(0))

    def test_overflow_exception(self):
        self.assertEqual(Numeric(5) ** Numeric(1000), "inf")
        self.assertEqual(Numeric(-5) ** Numeric(999), "-inf")
        self.assertEqual(Numeric(2) ** Numeric(2), 4)

    def test_cant_cast_from_string(self):
        self.assertRaises(Numeric.NotANumber, Numeric, "abc")


if __name__ == "__main__":
    unittest.main(verbosity=2)
