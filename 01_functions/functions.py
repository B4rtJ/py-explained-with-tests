import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Tests(unittest.TestCase):
    def setUp(self):
        """Add print to setup to improve logs readability."""
        print()

    def test_fun_pos(self):
        """Test function with positional arguments.

        * all positional arguments are mandatory
        """

        def fun_pos(a, b):
            log.debug(f"{a=} {b=}")
            return a, b

        # pass positional arguments only
        self.assertEqual(fun_pos(1, 2), (1, 2))

        # keyword arguments can only by used for setting positional arguments
        self.assertEqual(fun_pos(1, b=2), (1, 2))

        # another example with keyword arguments only
        self.assertEqual(fun_pos(a=1, b=2), (1, 2))

        # mixing places for keyword arguments works as well
        self.assertEqual(fun_pos(b=2, a=1), (1, 2))

        # all positional arguments are mandatory, giving only one will result with an exception
        self.assertRaises(TypeError, fun_pos, 1)

    def test_fun_key(self):
        """Test function with keyword arguments.

        * all keyword arguments are optional and must have default value defined.
        """

        def fun_key(a=1, b=2):
            log.debug(f"{a=} {b=}")
            return a, b

        # positional arguments in function call can be used to set keyword arguments in definition
        self.assertEqual(fun_key(2, 4), (2, 4))

        # example with one positional argument and one keyword argument
        self.assertEqual(fun_key(3, b=4), (3, 4))

        # two keyword arguments
        self.assertEqual(fun_key(a=4, b=5), (4, 5))

        # single positional argument, for "b" kwarg default value is used
        self.assertEqual(fun_key(1), (1, 2))

        # "a" assigned with kwarg, "b" is default
        self.assertEqual(fun_key(a=1), (1, 2))

        # keyword args can be assigned in any order
        self.assertEqual(fun_key(b=2), (1, 2))

        # mixed order with two kwargs
        self.assertEqual(fun_key(b=2, a=1), (1, 2))

        # we cannot give more args than defined
        self.assertRaises(TypeError, fun_key, 1, 2, 3)

        # positional args in call cannot follow keyword args
        # fun_key(b=1, 2) - no way to test SyntaxError

    def test_fun_only_pos(self):
        """Test function restricted to be called with positional arguments only.

        * all arguments to the left from "/" mark can only be called with positional args.
        """

        def fun_only_pos(a, b, /):
            log.debug(f"{a=} {b=}")
            return a, b

        # call with two positional arguments, only option
        self.assertEqual(fun_only_pos(1, 2), (1, 2))

        # any other combination would cause an exception
        self.assertRaises(TypeError, fun_only_pos, 1, b=2)


    def test_fun_only_key(self):
        """Test function restricted to be called with kwargs only.

        * all arguments to the right from "*" mark can only by called as kwargs.
        * this way arguments must be named explicitly
        """

        def fun_only_key(*, a=1, b=2):
            log.debug(f"{a=} {b=}")
            return a, b

        # kwargs only
        self.assertEqual(fun_only_key(a=5, b=4), (5, 4))
        self.assertEqual(fun_only_key(a=5), (5, 2))
        self.assertEqual(fun_only_key(b=4), (1, 4))
        self.assertEqual(fun_only_key(b=4, a=5), (5, 4))

        # any call with positional arg will cause TypeError
        self.assertRaises(TypeError, fun_only_key, 1, 2)

    def test_fun_mix(self):
        """Test function with many rules of passing arguments."""

        def fun_mix1(a, /, *, b=2):
            log.debug(f"{a=} {b=}")
            return a, b

        # both argument passed, "a" as arg, "b" as kwarg
        self.assertEqual(fun_mix1(1, b=2), (1, 2))

        # only a argument passed, kwargs are optional
        self.assertEqual(fun_mix1(1), (1, 2))

        # only b kwarg passed, "a" is mandatory so this will raise TypeError exception
        self.assertRaises(TypeError, fun_mix1, b=1)


    def test_fun_args_list(self):
        """Test function with variable length args tuple.

        * "*" sign in function declaration indicates that parameter is a variable length tuple
        * "*" sign in function call or in return statement is an unpack operator
        * "*" sign in assignment indicates that all parameters that match should be packed inside list
        """

        def fun_args_list(a, /, *args, c=3):
            log.debug(f"{a=}, {args=}, {c=}")
            log.debug(f'"args" is a tuple - {isinstance(args, tuple)}')
            return a, *args, c

        self.assertEqual(fun_args_list(1), (1, 3))
        self.assertEqual(fun_args_list(1, 2), (1, 2, 3))
        self.assertEqual(fun_args_list(1, 2, c=3), (1, 2, 3))
        self.assertEqual(fun_args_list(*(1, 2), c=3), (1, 2, 3))

        a, *args, c = fun_args_list(5, 4, 5, 6, 7, 4, 5, 6, 2, c=6)
        self.assertEqual(args, [4, 5, 6, 7, 4, 5, 6, 2])

    def test_fun_kwargs_dict(self):
        """Test function with kwargs dictionary extension.
        
        * "**" sign in function declaration indicates that parameter is a dictionary
            that will contain any additional kwargs
        * "**" sign in function call is an dictionary unpack operator, all dictionary keys
            should be of type "str" and should match parameter names in function definition
        """

        def fun_kwargs_dict(a, /, **kwargs):
            log.debug(f"{a=}, {kwargs=}")
            log.debug(f'"kwargs" is a dict - {isinstance(kwargs, dict)}')
            kwargs.setdefault("b", 4)
            return a, kwargs

        self.assertEqual(fun_kwargs_dict(1), (1, {"b": 4}))

        returned_dict = fun_kwargs_dict(1, b = 2, c = 3)[1]
        self.assertEqual(fun_kwargs_dict(2, **returned_dict), (2, {"b": 2, "c": 3}))

    def test_exercise(self):
        """
        Define function that takes 3 arguments:

            * first one can be only positional
            * second should be keyword argument but can be passed as positional as well
            * third shall be keyword argument and only can be passed as keyword arg.

        Function should display all passed arguments and return tuple with those - as in examples above.

        With function defined test possible calls with assertEqual.
        """

if __name__ == "__main__":
    unittest.main(verbosity=2)
