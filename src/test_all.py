#!/usr/bin/python
import unittest, sys
from oo.test.test_line import *
from oo.test.test_vehicle import *


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestLine))
    suite.addTests(unittest.makeSuite(TestVehicle))
    return suite

# Make the test suite; run the tests.
def test():
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    runner.run(testsuite)
    
if __name__=='__main__': test()