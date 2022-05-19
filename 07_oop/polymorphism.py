import logging
import unittest
from functools import singledispatch, singledispatchmethod
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Tests(unittest.TestCase):
    def setUp(self):
        """Add print to setup to improve logs readability."""
        print()

    def test_singledispatch(self):
        @singledispatch
        def accumulate(values):
            log.info("default function")
            return sum(values)

        @accumulate.register
        def acc_dict(entries: dict):
            log.info("function for dictionary")
            return sum(entries.values())

        @accumulate.register(int)
        @accumulate.register(float)
        def acc_single_val(value: Union[int, float]):
            log.info("function for single value")
            return value

        with self.assertLogs(log, logging.INFO) as logs:
            self.assertEqual(accumulate([1, 2, 3, 4]), 10)
            self.assertIn("INFO:root:default function", logs.output)

        with self.assertLogs(log, logging.INFO) as logs:
            self.assertEqual(accumulate({1: 10, 2: 20, 3: 30}), 60)
            self.assertIn("INFO:root:function for dictionary", logs.output)

        with self.assertLogs(log, logging.INFO) as logs:
            self.assertEqual(accumulate(7), 7)
            self.assertIn("INFO:root:function for single value", logs.output)

    def test_singledispatch_method(self):
        class Accumulator:
            def __init__(self):
                self.acc = 0

            @singledispatchmethod
            def add(self, values):
                log.info("default method")
                self.acc += sum(values)

            @add.register
            def add_dict(self, entries: dict):
                log.info("method for dictionary")
                self.acc += sum(entries.values())

            @add.register(int)
            @add.register(float)
            def add_single_val(self, value: Union[int, float]):
                log.info("method for single value")
                self.acc += value

        acc = Accumulator()

        with self.assertLogs(log, logging.INFO) as logs:
            acc.add([1, 2, 3, 4])
            self.assertIn("INFO:root:default method", logs.output)

        self.assertEqual(acc.acc, 10)

        with self.assertLogs(log, logging.INFO) as logs:
            acc.add({1: 10, 2: 20, 3: 30})
            self.assertIn("INFO:root:method for dictionary", logs.output)

        self.assertEqual(acc.acc, 70)

        with self.assertLogs(log, logging.INFO) as logs:
            acc.add(7)
            self.assertIn("INFO:root:method for single value", logs.output)

        self.assertEqual(acc.acc, 77)


if __name__ == "__main__":
    unittest.main(verbosity=2)
