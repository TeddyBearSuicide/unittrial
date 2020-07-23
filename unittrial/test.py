import asyncio
import inspect

from unittrial.console import Console
from typing import Callable, List, Union


_current_cls = None


class TestConfig(object):
    stopOnFail = False


_config: TestConfig


class TestCase(object):
    tests: List[Callable] = []

    def setup_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def teardown_class(self):
        pass

    async def __call__(self, *args, **kwargs):
        await _check_and_run(self.setup_class)

        for test in self.tests:

            await _check_and_run(self.setup)

            await _check_and_run(test)

            await _check_and_run(self.teardown)

        await _check_and_run(self.teardown_class)


def _global_setup_wrapper(global_setup):
    def _global_setup():
        return global_setup()
    return _global_setup


def _global_teardown_wrapper(global_teardown):
    def _global_teardown():
        return global_teardown()
    return _global_teardown


async def _check_and_run(test: Union[Callable, TestCase]):
    global _config

    if isinstance(test, TestCase):
        Console.writeStatus(f"{test.__class__.__name__}", f"{Console.BrightBlue}{len(test.tests)}")
        Console.indention += 1
        result = await test()
        Console.indention -= 1
        print('')

    else:
        _print = True
        if test.__name__ in ["_global_setup", "setup_class", "setup", "teardown", "teardown_class", "_global_teardown"]:
            _print = False

        if _print:
            Console.writeStatus(f"{test.__name__}", f"{Console.BrightYellow}Running")

        result = None

        try:
            if inspect.iscoroutinefunction(test):
                result = await test()
            else:
                result = test()

            if _print:
                Console.updateStatus(f"{test.__name__}", f"{Console.BrightGreen}Success")

        except AssertionError as e:
            Console.updateStatus(f"{test.__name__}", f"{Console.BrightRed}Fail")
            Console.indention += 1
            Console.writeError(str(e))
            Console.indention -= 1

            if _config.stopOnFail:
                raise Exception()

        except Exception as e:
            print(e)

        return result


def run_tests(
        tests: List[Union[Callable, TestCase]],
        config: TestConfig = TestConfig(),
        global_setup: Union[Callable] = lambda: None,
        global_teardown: Union[Callable] = lambda: None):

    async def async_start():

        await _check_and_run(_global_setup_wrapper(global_setup))

        for test in tests:

            await _check_and_run(test)

        await _check_and_run(_global_teardown_wrapper(global_teardown))

    global _config
    _config = config

    try:
        asyncio.run(async_start())
    except Exception:
        pass

