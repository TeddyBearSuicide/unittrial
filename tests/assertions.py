from unittrial.assertions import assertEquals, assertGreater, assertGreaterOrEqual, assertIsInstance, assertIsNone, \
    assertIsNotNone, assertLesser, assertLesserOrEqual, expectFailure
from unittrial.test import TestCase


class AssertionTests(TestCase):
    def assertEquals(self):
        assertEquals(1, 1)

        try:
            assertEquals(1, 2)
        except AssertionError:
            pass

    def assertGreater(self):
        assertGreater(2, 1)

        try:
            assertGreater(1, 2)
        except AssertionError:
            pass

    def assertGreaterOrEqual(self):
        assertGreaterOrEqual(2, 2)
        assertGreaterOrEqual(3, 2)

        try:
            assertGreaterOrEqual(1, 2)
        except AssertionError:
            pass

    def assertIsInstance(self):
        assertIsInstance("", str)

        try:
            assertIsInstance(1, str)
        except AssertionError:
            pass

    def assertIsNone(self):
        assertIsNone(None)

        try:
            assertIsNone(1)
        except AssertionError:
            pass

    def assertIsNotNone(self):
        assertIsNotNone(2)

        try:
            assertIsNotNone(None)
        except AssertionError:
            pass

    def assertLesser(self):
        assertLesser(1, 2)

        try:
            assertLesser(2, 2)
        except AssertionError:
            pass

        try:
            assertLesser(2, 1)
        except AssertionError:
            pass

    def assertLesserOrEqual(self):
        assertLesserOrEqual(1, 1)
        assertLesserOrEqual(1, 2)

        try:
            assertLesserOrEqual(3, 2)
        except AssertionError:
            pass

    @expectFailure(IndexError)
    def expectFailure(self):
        list()[1]

    def __init__(self):
        self.tests = [
            self.assertEquals,
            self.assertGreater,
            self.assertGreaterOrEqual,
            self.assertIsInstance,
            self.assertIsNone,
            self.assertIsNotNone,
            self.assertLesser,
            self.assertLesserOrEqual,
            self.expectFailure
        ]
