import logging
import time
import unittest
from typing import Generator

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_counter_generator(self):
        def counter():
            cnt = 0
            while True:
                yield cnt
                cnt += 1

        gen = counter()

        # Function that incorporates yield keyword returns generator object not the value
        self.assertIsInstance(gen, Generator)

        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)

    def test_finite_counter(self):
        finite_counter = (x for x in range(50))

        for i, cnt in enumerate(finite_counter):
            self.assertEqual(i, cnt)

        finite_counter_2 = (x for x in range(1, 3))
        self.assertEqual(1, next(finite_counter_2))
        self.assertEqual(2, next(finite_counter_2))
        with self.assertRaises(StopIteration):
            next(finite_counter_2)

    def test_my_range_generator(self):
        def my_range(start=0, stop=10, step=1):
            cnt = start
            while cnt < stop:
                yield cnt
                cnt += step

        range_gen = iter(range(4, 100, 3))

        for x in my_range(4, 100, 3):
            self.assertEqual(x, next(range_gen))

    def test_fibonacci(self):
        def fibonacci(n: int = 20):
            """
            Fibonacci generator.

            F(0) = 0
            F(1) = 1

            F(n) = F(n-1) + F(n-2)

            Args:
                n (int): Quantity of generated values.

            Yield:
                int: Sequence value.
            """
            fn: int = 0
            fm: int = 1

            yield fn
            yield fm

            for _ in range(2, n):
                fm, fn = fn + fm, fm
                yield fm

        gen = fibonacci(100)

        fibo = list(gen)
        self.assertEqual(fibo[-1], fibo[-2] + fibo[-3])

    # def test_interactive_gen(self):
    #     def interactive_gen() -> float:
    #         x = 1.0
    #         y = yield x
    #         for _ in range(4):
    #             x = x + y
    #             y = yield x
    #
    #     g = interactive_gen()
    #     self.assertIsInstance(g, Generator)
    #
    #     # When we don't want to use for loop, we can
    #     # iterate through generator with next function
    #     y = next(g)
    #     log.info(f"{y=}")
    #     # next is equivalent to g.send(None)
    #     # in first call we cannot send anything because first
    #     # we need to return something
    #     while True:
    #         try:
    #             y = g.send(float(input("x=")))
    #             log.info(f"{y=}")
    #         except StopIteration:
    #             # Once we iterate with "next" function we need to handle
    #             # StopInteration exception
    #             break

    def test_primes(self):
        def primes_gen(end=1000):
            def check_if_even(x: int) -> bool:
                return not bool(x % 2)

            def check_if_divided_by_3(x: int) -> bool:
                sum_of_digits = 0
                for digit in str(x):
                    sum_of_digits += int(digit)
                return not bool(sum_of_digits % 3)

            def check_if_divided_by_5(x: int) -> bool:
                return str(x)[-1] in ("0", "5")

            def check_if_prime(x: int) -> bool:
                if check_if_even(x) or check_if_divided_by_3(x) or check_if_divided_by_5(x):
                    return False
                for i in primes:
                    if i > x // i:
                        break
                    if not x % i:
                        return False
                return True

            primes = list()

            yield 2
            yield 3
            yield 5
            x = 7
            while True:
                while not check_if_prime(x):
                    x += 1
                    if x >= end:
                        return
                primes.append(x)
                yield x
                x += 1

        start = time.time()
        for index, prime in enumerate(primes_gen(25), 1):
            log.debug(f"{index}. {prime}")
        log.info(f"duration = {time.time()-start:.8}s")

    def test_exercise_my_enumerate_generator(self,):
        """Write your own generator that behaves like 'enumerate' function.

        https://docs.python.org/3/library/functions.html#enumerate

        Add tests.
        """
        def enumerate_gen(it,start=0):
            index = start
            for item in it:
                yield index,item
                index +=1
        l = ["wedwed","dwedwa","wedwe"]
        self.assertEqual(list(enumerate(l)), list(enumerate_gen(l)))
        enum_fun = enumerate_gen(l)
        self.assertEqual(next(enum_fun), (0, "wedwed"))
        self.assertEqual(next(enum_fun), (1, "dwedwa"))
        self.assertEqual(next(enum_fun), (2, "wedwe"))
        self.assertRaises(StopIteration,next,enum_fun)

    def test_exercise_tic_tac_toe(self):
        """Write generator that infinitely returns first tic, then tac, then toe."""
        def tic_tac_toe():
            i = 0
            while True:
                if i % 3 == 0:
                    i += 1
                    yield "tic"
                if i % 3 == 1:
                    i += 1
                    yield "tac"
                if i % 3 == 2:
                    i += 1
                    yield "toe"
        gen = tic_tac_toe()
        t1 = time.time()
        for i in range(100):
            self.assertEqual(next(gen), "tic")
            self.assertEqual(next(gen), "tac")
            self.assertEqual(next(gen), "toe")
        t2 = time.time()
        self.assertLess(t2-t1, 0.0009)
if __name__ == "__main__":
    unittest.main(verbosity=2)
