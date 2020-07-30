from tests.assertions import AssertionTests
from tests.core import CoreTests
from unittrial import run_tests

if __name__ == '__main__':
    run_tests(
        [AssertionTests(), CoreTests()],
        global_setup=lambda: None,
        global_teardown=lambda: None)
