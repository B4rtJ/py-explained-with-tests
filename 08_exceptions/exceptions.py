import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s [%(filename)13s:%(lineno)4d] %(message)s",
)

logger = logging.getLogger()


class MyOwnException(Exception):
    """My own exception"""


def division(x, y):
    result = None
    try:
        result = x / y
    except ZeroDivisionError as err:
        logger.exception(err)
        result = float("NaN")
        logger.warning("falling back to %f", result)
    except Exception as err:
        logger.error("Unhandled exception")
        raise err
    else:
        logger.debug("no exception")
    finally:
        logger.debug("result is %s", result)
    return result


"""
Different ways of raising an exception.

raise exc from from_exc

This lambda will raise exception `exc` from exception `from_exc`
Traceback will say that `from_exc` was the cause of `exc`.

Previous exceptions could be masked by setting `from_exc`
to `None`. This way traceback will only contain `exc` information.

Example:
    raise MyException("Some message") from exc
    raise exc from None

If no `from` statement is present. `exc` information will be
printed out and if previous exception existed those will be
printed out as well with information - during handling exception
another occurred.

Example:
    raise exc
"""


class Tests(unittest.TestCase):
    def setUp(self):
        print("\n" + 50 * "-")

    def test_unexpected_exception(self):
        self.assertRaises(Exception, division, 5, "123")

    def test_division_by_zero(self):
        self.assertIsNotNone(division(5, 0))

    def test_no_exception(self):
        self.assertEqual(division(5, 2), 2.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
