import logging
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class CtxMgr:

    def __init__(self):
        log.info("Object created")
        self.__exception_handled = False
    
    def __enter__(self):
        log.info("Context entered")
        self.__exception_handled = False
        return self
    
    def __exit__(self, exc_type, exc_value, trace):
        log.info("Exit context")
        log.debug(f"{exc_type=} {exc_value=} {trace=}")

        if exc_type not in {AssertionError, NameError}:
            self.__exception_handled = True
        return self.__exception_handled


class Tests(unittest.TestCase):
    def setUp(self):
        print("\n" + 50 * "-")

    def test_ok(self):
        with CtxMgr() as ctx:
            self.assertIsInstance(ctx, CtxMgr)

    def test_unexpected_exception(self):
        with self.assertRaises(Exception):
            with CtxMgr():
                log.debug(hehe) 

    def test_expected_exception(self):
        with CtxMgr():
            raise TimeoutError

if __name__ == "__main__":
    unittest.main(verbosity=2)
