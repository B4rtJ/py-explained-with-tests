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

    def test_class_access(self):

        class AttrAccess:
            def __init__(self):
                self.public = "public"
                self._protected = "protected"
                self.__private = "private"

        attr_access = AttrAccess()
        self.assertEqual(attr_access.public, "public")
        self.assertEqual(attr_access._protected, "protected")
        self.assertEqual(attr_access._AttrAccess__private, "private")

        private_getter = lambda obj, attr: getattr(obj, "_" + type(obj).__name__ + attr)
        self.assertEqual(private_getter(attr_access, "__private"), "private")


if __name__ == "__main__":
    unittest.main(verbosity=2)
