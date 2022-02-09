"""Refactor this script in a way that executes steps in right sequence.

Steps should be called from 1 to 5. Use context manager."""

import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Abc:
    def __init__(self):
        log.info("1. creating object")

    def dummy_print(self):
        log.info("2. dummy print")
    
    def cleanup(self):
        log.info("3. cleaning object")

    def __del__(self):
        self.cleanup()


class Tests(unittest.TestCase):
    def setUp(self):
        print("\n" + 50 * "-")

    def test_cleanup(self):
        try:
            a = Abc()
            a.dummy_print()
            log.info(hehe) # this line should stay :)
        except:
            log.info("4. exception")
    
        log.info("5. this should be called after object cleanup")

if __name__ == "__main__":
    unittest.main(verbosity=2)
