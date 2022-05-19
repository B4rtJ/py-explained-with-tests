import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()

class DepA:
    pass

class DepB:
    pass

class CompositionNoInjection:
    def __init__(self):
        self.dep_a = DepA()
        self.dep_b = DepB()


c = CompositionNoInjection()
# c.dep_a.configure()


class CompositionInjection:
    def __init__(self, dep_a : DepA, dep_b : DepB):
        self.dep_a = dep_a
        self.dep_b = dep_b

dep_a = DepA()
dep_b = DepB()

c1 = CompositionInjection(dep_a, dep_b)



class CompositionCompromise:
    def __init__(self, dep_a : DepA = None, dep_b : DepB = None):
        if dep_a is None:
            self.dep_a = DepA()
        if dep_b is None:
            self.dep_b = DepB()

cc = CompositionCompromise()
c2 = CompositionCompromise(dep_a, dep_b)


class Tests(unittest.TestCase):
    def setUp(self):
        """Add print to setup to improve logs readability."""
        print()

    def test_a(self):
        self.assertTrue(True)
        log.info("log format")

if __name__ == "__main__":
    unittest.main(verbosity=2)
