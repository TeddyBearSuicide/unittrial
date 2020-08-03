from unittrial import TestCase
from unittrial.assertions import assert_equals, assert_greater, assert_greater_or_equal, assert_is_instance, \
    assert_is_none, assert_is_not_none, assert_lesser, assert_lesser_or_equal, expect_failure, assert_false, assert_true


class AssertionTests(TestCase):

    def assert_equals(self):
        assert_equals(1, 1)

        try:
            assert_equals(1, 2)
        except AssertionError:
            pass

    def assert_false(self):
        assert_false(False)

        try:
            assert_false(True)
        except AssertionError:
            pass

    def assert_greater(self):
        assert_greater(2, 1)

        try:
            assert_greater(1, 2)
        except AssertionError:
            pass

    def assert_greater_or_equal(self):
        assert_greater_or_equal(2, 2)
        assert_greater_or_equal(3, 2)

        try:
            assert_greater_or_equal(1, 2)
        except AssertionError:
            pass

    def assert_is_instance(self):
        assert_is_instance("", str)

        try:
            assert_is_instance(1, str)
        except AssertionError:
            pass

    def assert_is_none(self):
        assert_is_none(None)

        try:
            assert_is_none(1)
        except AssertionError:
            pass

    def assert_is_not_none(self):
        assert_is_not_none(2)

        try:
            assert_is_not_none(None)
        except AssertionError:
            pass

    def assert_lesser(self):
        assert_lesser(1, 2)

        try:
            assert_lesser(2, 2)
        except AssertionError:
            pass

        try:
            assert_lesser(2, 1)
        except AssertionError:
            pass

    def assert_lesser_or_equal(self):
        assert_lesser_or_equal(1, 1)
        assert_lesser_or_equal(1, 2)

        try:
            assert_lesser_or_equal(3, 2)
        except AssertionError:
            pass

    def assert_true(self):
        assert_true(True)

        try:
            assert_true(False)
        except AssertionError:
            pass

    @expect_failure(IndexError)
    def expect_failure(self):
        list()[1]

    def __init__(self):
        self.tests = [
            self.assert_equals,
            self.assert_false,
            self.assert_greater,
            self.assert_greater_or_equal,
            self.assert_is_instance,
            self.assert_is_none,
            self.assert_is_not_none,
            self.assert_lesser,
            self.assert_lesser_or_equal,
            self.assert_true,
            self.expect_failure
        ]
