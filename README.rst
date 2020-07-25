Unittrial | Simple Unit Testing
===============================
Unittrial is a unit testing framework with the mindset of being **simple** and **explicit**.

Installation
------------
``pip3 install unittrial``

Test Example
------------
.. code:: python

    import random
    from unittrial.assertions import assert_equals, assert_is_not_none, expect_failure, assert_greater
    from unittrial.logger import logger
    from unittrial.test import TestCase, run_tests


    class OrderTest(TestCase):

        # Any test or setup/teardown function can be async or sync
        async def setup_class(self):
            logger.info("This is run once before 'OrderTest' tests are run")

        def setup(self):
            logger.info("This is run once before each each test")

        def syncTest(self):
            user = {'id': 1}
            logger.info(f"Retrieved user with id of {user['id']}")
            assert_is_not_none(user)

        async def asyncTest(self):
            user = {'id': 1, 'username': "TestUsername"}
            logger.info(f"Retrieved user with id of {user['id']} via async")
            assert_equals(user['username'], "TestUsername")

        def teardown(self):
            logger.info("This is run once after each each")

        async def teardown_class(self):
            logger.info("This is run once after all of 'OrderTest' tests are finished")

        def __init__(self):
            self.tests = [self.syncTest, self.asyncTest]


    class RandomTest(TestCase):
        def random_int(self):
            assert_greater(random.randint(1, 10), 0)
            logger.warning("This is kinda a dumb test since it will always be > 0")

        # This test should pass since an IndexError will be raised
        @expect_failure(IndexError)
        async def async_failure(self):
            _list = [1, 2, 3]
            _list[100]
            logger.error("This shouldn't print since it is after when an exception is raised")

        def __init__(self):
            self.tests = [self.random_int, self.asyncTest]


    def some_global_setup_function():
        logger.info("This is run once before any class or test is loaded or called")


    async def some_global_teardown_function():
        logger.info("This is run once after all tests and classes have completed")


    if __name__ == '__main__':
        run_tests(
            [OrderTest(), RandomTest()],
            global_setup=some_global_setup_function,
            global_teardown=some_global_teardown_function)


**Results**

.. code::

    _global_setup                                                       [Success]
       [INFO] This is run once before any class or test is loaded or called
    OrderTest                                                                 [2]
       setup_class                                                      [Success]
          [INFO] This is run once before 'OrderTest' tests are run
       setup                                                            [Success]
          [INFO] This is run once before each each test
       syncTest                                                         [Success]
          [INFO] Retrieved user with id of 1
       teardown                                                         [Success]
          [INFO] This is run once after each each
       setup                                                            [Success]
          [INFO] This is run once before each each test
       asyncTest                                                        [Success]
          [INFO] Retrieved user with id of 1 via async
       teardown                                                         [Success]
          [INFO] This is run once after each each
       teardown_class                                                   [Success]
          [INFO] This is run once after all of 'OrderTest' tests are finished

    RandomTest                                                                [2]
       random_int                                                       [Success]
          [WARNING] This is kinda a dumb test since it will always be > 0
       async_failure                                                    [Success]

    _global_teardown                                                    [Success]
       [INFO] This is run once after all tests and classes have completed