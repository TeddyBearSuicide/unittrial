import asyncio

from unittrial import TestCase, run_blocking
from unittrial.assertions import assert_equals, expect_failure


class CoreTests(TestCase):

    sleep_result = 0

    async def setup_class(self):
        await asyncio.sleep(1)
        self.sleep_result = 1

    async def sleep_test(self):
        assert_equals(1, self.sleep_result)

    async def run_blocking_test(self):
        await run_blocking(asyncio.sleep(1))

    @expect_failure(IndexError)
    async def run_blocking_raise_exception_test(self):
        async def _raise_exception():
            list()[100]

        await run_blocking(_raise_exception())

    def __init__(self):
        self.tests = [self.sleep_test, self.run_blocking_test, self.run_blocking_raise_exception_test]

