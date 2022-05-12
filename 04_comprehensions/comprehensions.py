import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_list_with_one_loop(self):
        def list_with_one_loop():
            lst = []
            for i in range(5):
                lst.append(i * 2)
            return lst

        list_comprehension = [i * 2 for i in range(5)]
        log.debug(f"{list_comprehension=}")
        self.assertEqual(list_with_one_loop(), list_comprehension)

    def test_list_with_two_loops(self):
        def list_with_two_loops():
            rows = []
            for i in range(11):
                col = []
                for j in range(11):
                    col.append(i * j)
                rows.append(col)
            return rows

        list_comprehension = [[i * j for i in range(11)] for j in range(11)]
        self.assertEqual(list_with_two_loops(), list_comprehension)

    def test_set_example(self):
        def set_example():
            modulo_7 = set()
            for i in range(4, 29, 2):
                modulo_7.add(i % 7)
            return modulo_7

        set_comprehension = {i % 7 for i in range(4, 29, 2)}
        log.debug(f"{set_comprehension=}")
        self.assertEqual(set_example(), set_comprehension)

    def test_dict_example(self):
        def dict_example():
            modulo_7 = {}
            for i in range(4, 9, 2):
                modulo_7[i] = i % 7
            return modulo_7
        dict_comprehension = {i: i % 7 for i in range(4, 9, 2)}

        log.debug(f"{dict_comprehension=}")
        self.assertEqual(dict_example(), dict_comprehension)

    def test_set_with_filter(self):
        words = {"abc", "", "b", "ADB", "car", "home"}

        def set_with_filter():
            filtered_words = set()
            for word in words:
                if len(word) > 2:
                    filtered_words.add(word)
            return filtered_words

        set_comprehension = {word for word in words if len(word) > 2}
        log.debug(f"{set_comprehension=}")
        self.assertEqual(set_with_filter(), set_comprehension)

    def test_exercise(self):
        """
        Define closure and similar comprehension.

        Both should create new list of words without words that start with underscore.
        """
        words = ("__init__", "__call__", "configure", "start", "stop")
        def list_of_words():
            closure_list = []
            for word in words:
                if not word.startswith("_"):
                    closure_list.append(word)
            return closure_list
        new_list = [i for i in words if not i.startswith("_")]
        self.assertEqual(list_of_words(), new_list)
if __name__ == "__main__":
    unittest.main(verbosity=2)
