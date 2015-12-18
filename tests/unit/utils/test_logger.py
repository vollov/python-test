# -*- coding: utf-8 -*-

import os, unittest, logging

logger = logging.getLogger('pytest')

class TestLogger(unittest.TestCase):
   
    def setUp(self):
        #logs = Logger()
        logger.debug('TestLogger setup')
         
    def test_log(self):
        print 'OK'
        logger.debug("debug")
        logger.info("info")
        logger.warn("warn")
        logger.error("error")
        logger.critical("critical")

if __name__ == '__main__': unittest.main()
