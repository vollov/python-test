'''
Test load json from local file
'''

import json, os, unittest, logging
import settings as app_settings

from pprint import pprint

logger=logging.getLogger('pytest')
#user_file_path = 

class TestJson(unittest.TestCase):

    def setUp(self):
        '''initial data path'''
        logger.debug('TestJson.setUp()')
        logger.debug('BASE_DIR={0}'.format(app_settings.BASE_DIR))
        self.data_path = os.path.join(app_settings.BASE_DIR,'tests', 'data')
        logger.debug('data_dir={0}'.format(self.data_path))

    def test_load_json(self):
        logger.debug('TestJson.test_load_json() loading json file')
        
        user_file_path = os.path.join(self.data_path, 'user.json')
        
        with open(user_file_path) as data_file:    
            data = json.load(data_file)
            
        pprint(data) 
