import asyncio

from unittrial.assertions import assertEquals, expectFailure
from unittrial.test import TestCase, run_tests


class Test(TestCase):

    def failed_test(self):
        assertEquals(1, 2)

    async def successful_test(self):
        await asyncio.sleep(1)

    async def successful_test2(self):
        await asyncio.sleep(1)

    @expectFailure(IndexError)
    async def failure(self):
        await asyncio.sleep(1)
        raise IndexError()

    def __init__(self):
        self.tests = [self.failed_test, self.successful_test, self.successful_test2, self.failure]


class UserTest(TestCase):

    def another_failed_test(self):
        assertEquals(2, 1)

    async def successful_test(self):
        await asyncio.sleep(1)

    async def successful_test2(self):
        await asyncio.sleep(1)

    def __init__(self):
        self.tests = [self.successful_test, self.another_failed_test, self.successful_test2]


if __name__ == '__main__':
    run_tests([Test(), UserTest()])

