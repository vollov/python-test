from utils.testcases import TestCase
import logging

logger=logging.getLogger('pytest')

class TestFoo(TestCase):

    fixtures = ['auth.json', 'store.json']

    #def setUp(self):
    #    super(TestUT, self).setUp()
    #    logger.debug('TestUT set up')
    
    def test_case1(self):
        logger.debug('TestFoo run test case 1')

    def test_case2(self):
        logger.debug('TestFoo run test case 2')
