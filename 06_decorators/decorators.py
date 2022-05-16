import logging
import unittest
import sys
import os
import time
import functools
import random

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()

# decorators are wrappers that can be applied on functions and class __call__ methods
# decorators can by applied with @ sign and name of function that implements decorator

class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_simplest_decorator(self):

        def simplest_decorator(fun):
            log.debug("Decorate function")
            return fun

        @simplest_decorator
        def simple_function():
            log.debug("Simple function")
            return True

        self.assertTrue(simple_function())
        self.assertTrue(simple_function())

    def test_decorator_wit_closure(self):

        def decorator_with_closure(fun):
            def wrapper(*args, **kwargs):
                log.debug("Decorated function")
                return fun(*args, **kwargs)
            return wrapper

        @decorator_with_closure
        def simple_function():
            log.debug("Simple function")
            return True

        self.assertTrue(simple_function())
        self.assertTrue(simple_function())

    def test_decorator_to_upper(self):

        def to_upper(fun):
            def wrapper(*args, **kwargs):
                result : str = fun(*args, **kwargs)
                return result.upper()
            return wrapper

        def get_string():
            return "python"

        self.assertEqual(get_string(), "python")
        self.assertEqual(to_upper(get_string)(), "PYTHON")

    def test_parametrized_decorator(self):

        def repeat(num : int = 4):
            def _decor(fun):
                @functools.wraps(fun)
                def _wrapper(*args, **kwargs):
                    results = []
                    for _ in range(num):
                        results.append(fun(*args, **kwargs))
                    return results
                return _wrapper
            return _decor

        @repeat(2)
        def get_time():
            time_now = time.time()
            log.debug(f"Float timestamp is {time_now}")
            return time.time()

        results = get_time()

        # self.assertEqual(get_time.__name__, "get_time")
        # self.assertGreater(results.pop(), results.pop())

        randoms = repeat(2)(random.random)()
        self.assertNotEqual(randoms.pop(), randoms.pop())

    def test_exercise(self):
        """Define retry decorator, that runs
        decorated function until successfull (result evaluated to True)
        or until maximum number of retries has been reached"""

        def retry(num=5):
            def _decor(fun):
                @functools.wraps(fun)
                def _wrapper(*args, **kwargs):
                    for _ in range(num):
                        if fun(*args, **kwargs):
                            return True
                return _wrapper
            return _decor

        results = (result for result in [False, False, True, False, True])
        @retry()
        def retried_function():
            try:
                return next(results)
            except StopIteration:
                return False
        f = retried_function()
        self.assertTrue(f)
 
if __name__ == "__main__":
    unittest.main(verbosity=2)
