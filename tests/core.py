import asyncio

from unittrial import TestCase
from unittrial.assertions import assert_equals


class CoreTests(TestCase):

    sleep_result = 0

    async def setup_class(self):
        await asyncio.sleep(5)
        self.sleep_result = 1

    async def sleep_test(self):
        assert_equals(1, self.sleep_result)

    def __init__(self):
        self.tests = [self.sleep_test]

