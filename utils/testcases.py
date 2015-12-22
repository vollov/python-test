import unittest, logging

logger=logging.getLogger('pytest')

class TestCase(unittest.TestCase):
    # Subclasses can define fixtures which will be automatically installed.
    fixtures = None

    @classmethod
    def setUpClass(cls):
        logger.debug('TestCase setup class')
        #cls._connection = createExpensiveConnectionObject()
        if cls.fixtures:
            logger.debug('TestCase setup class -> fixtures=' + ','.join(cls.fixtures))

    @classmethod
    def tearDownClass(cls):
        logger.debug('TestCase tear down class')
        #cls._connection.destroy()

    def setUp(self):
        logger.debug('TestCase.setUp()')
        if self.fixtures:
            logger.debug('TestCase.setUp() -> fixtures=' + ','.join(self.fixtures))


    def tearDown(self):
        logger.debug('TestCase.tearDown()')
        if self.fixtures:
            logger.debug('TestCase.tearDown() -> fixtures=' + ','.join(self.fixtures))
