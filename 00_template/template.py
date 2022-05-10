import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Tests(unittest.TestCase):
    def setUp(self):
        """Add print to setup to improve logs readability."""
        print()

    def test_a(self):
        self.assertTrue(True)
        log.info("log format")

if __name__ == "__main__":
    unittest.main(verbosity=2)
