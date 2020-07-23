import inspect


def assertEquals(a, b):
    if a != b:
        raise AssertionError(f"Expected: {a} | Got: {b}")


def assertGreater(a, b):
    if a <= b:
        raise AssertionError(f"Expected: Greater than {a} | Got: {b}")


def assertGreaterOrEqual(a, b):
    if a < b:
        raise AssertionError(f"Expected: Greater than or equal {a} | Got: {b}")


def assertIsInstance(a, t):
    if a.__class__ == type:
        raise AssertionError(f"Type of {a} was passed but an instance is required.")

    if not isinstance(a, t):
        raise AssertionError(f"Expected: Instance of {t} | Got: {a} Type: {type(a)}")


def assertIsNone(a):
    if a is not None:
        raise AssertionError(f"Expected: None | Got: {a} Type: {type(a)}")


def assertIsNotNone(a):
    if a is None:
        raise AssertionError(f"Expected: Any | Got: None")


def assertLesser(a, b):
    if a >= b:
        raise AssertionError(f"Expected: Lesser than {a} | Got: {b}")


def assertLesserOrEqual(a, b):
    if a > b:
        raise AssertionError(f"Expected: Lesser than or equal {a} | Got: {b}")


def expectFailure(exception=Exception):
    def inner(test):
        async def wrapper(self=None):
            raised = None
            try:
                if inspect.iscoroutinefunction(test):
                    await test(self)
                else:
                    test(self)
            except Exception as e:
                raised = e
                if isinstance(e, exception):
                    return
            raise AssertionError(f"Expected a '{exception.__name__}' but '{type(raised).__name__}' was raised.")
        wrapper.__name__ = test.__name__
        return wrapper
    return inner
