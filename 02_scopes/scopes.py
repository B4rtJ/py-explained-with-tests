import os
import sys
import unittest
import logging

# Python sys path is created out of distribution packages, user packages installed with pip
# and PYTHONPATH environment variable. Inside those directories interpreter searches for modules to import.

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "site-packages"))


import pack

# dbg is global boolean variable
# Flags is static class with debug flag
from pack import dbg, Flags

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()

debug = True

def init():
    pass

class Counter:
    value = 0

class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_a_modules_imported_only_once(self):
        self.assertEqual(Flags.counter, 1)
        import pack
        self.assertEqual(pack.Flags.counter, 1)

    def test_b_no_alloc_in_fun_definition(self):
        new_dict = pack.do_not_allocate_resources_in_declaration(("new_key", 123))
        self.assertEqual(new_dict, {"new_key":123})
        new_dict2 = pack.do_not_allocate_resources_in_declaration(("new_key2", 345))
        self.assertNotEqual(new_dict2, {"new_key2":345})
        self.assertIs(new_dict, new_dict2)

    def test_c_global_nonmutable(self):
        global dbg
        log.debug(f"dbg address is {hex(id(dbg))}")
        log.debug(f"pack.dbg address is {hex(id(pack.dbg))}")
        self.assertEqual(dbg, True)
        log.info('Change imported "dbg" to False')
        dbg = False
        log.debug(f"dbg address is {hex(id(dbg))}")
        log.debug(f"pack.dbg address is {hex(id(pack.dbg))}")

        # When using non-mutable global objects, changing its value
        # changes its address as well, so if other modules uses it as
        # well theirs value won't be updated
        self.assertNotEqual(dbg, pack.dbg)

    def test_d_global_mutable(self):
        log.debug(f"Flags address is {hex(id(pack.Flags))}")
        log.debug(f"Flags.debug address is {hex(id(pack.Flags.debug))}")
        log.info(f'Set "Flags.debug" to False')
        pack.clear_debug()
        log.debug(f"Flags address is {hex(id(pack.Flags))}")
        log.debug(f"Flags.debug address is {hex(id(pack.Flags.debug))}")

        # Flags class stores address of debug and if debug gets changes
        # address in Flags gets updated as well. So correct value of
        # debug will be use in every module that import Flags
        self.assertEqual(Flags.debug, pack.Flags.debug)

    def test_e_local(self):
        Flags = {"debug": True}

        # Global scope object redefinition, especially risky in large function
        # when we would like to use global variable, but it is redefined by local one
        # Once global variable gets redefined in functions, it cannot be accessed

        log.debug(f"{Flags=}")
        self.assertEqual(Flags["debug"], True)


    def test_f_global(self):
        global debug
        log.debug(f"debug address is {hex(id(debug))}")
        debug = False
        log.debug(f"debug address is {hex(id(debug))}")
        self.assertTrue("debug" in globals())
        self.assertFalse("debug" in locals())


    def test_g_flag_in_class(self):
        log.debug(f"Flags address is {hex(id(Flags))}")
        log.debug(f"debug address is {hex(id(Flags.debug))}")
        Flags.debug = True
        log.debug(f"debug address is {hex(id(Flags.debug))}")
        log.debug(f"Flags address is {hex(id(Flags))}")


    def test_h_local_override_global(self):
        debug = False
        self.assertTrue("debug" in globals())
        self.assertTrue("debug" in locals())

    def test_i_global_function_local_variable(self):
        init = False
        with self.assertRaises(Exception):
            init()

    def test_j_example_part_1(self):
        """
        Define variable accessible globally, increment its value and check if it is propely incremented
        in test_example_part_2. Tests are executed in alphabetical order.
        """

    def test_k_example_part_2(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
