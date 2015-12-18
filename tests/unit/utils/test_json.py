
'''
Test load json from local file
'''

import json, os, unittest, logging
import settings as app_settings

from pprint import pprint

logger=logging.getLogger('pytest')
#user_file_path = os.path.join(app_settings.BASE_DIR,'python-test', 'user.json')
#with open(user_file_path) as data_file:    
#    data = json.load(data_file)
#pprint(data) 


class TestJson(unittest.TestCase):

    def setUp(self):
        '''initial data path'''
        logger.debug('BASE_DIR={0}'.format(app_settings.BASE_DIR))

    def test_load_json(self):
        logger.debug('loading json file')
