import gc
import weakref
import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class ClassWithDestructor:
    def __del__(self):
        log.info("Destructor has been called")

class Tests(unittest.TestCase):
    def setUp(self):
        print("\n" + 50 * "-")

    def test_gc(self):
        global c0, c1, c2, w1
        c0 = ClassWithDestructor()
        c1 = c0
        c2 = c1
        w1 = weakref.ref(c2)

        self.assertIs(c1, c2)
        self.assertIs(c2, c0)
        self.assertIs(w1(), c2)

        gc.enable()

        self.assertIn("c1", gc.get_referrers(c0)[0])
        self.assertIn("c2", gc.get_referrers(c0)[0])
        self.assertIn("c0", gc.get_referrers(c0)[0])
        self.assertIn("w1", gc.get_referrers(c0)[0])

        del c1
        self.assertNotIn("c1", gc.get_referrers(c0)[0])

        del c2
        self.assertNotIn("c2", gc.get_referrers(c0)[0])

        self.assertIsInstance(w1(), ClassWithDestructor)
        del c0
        gc.collect()
        self.assertIsNone(w1())


if __name__ == "__main__":
    unittest.main(verbosity=2)
