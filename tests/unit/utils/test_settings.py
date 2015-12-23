import logging, unittest
import settings as app_settings

logger=logging.getLogger('pytest')

class TestSettings(unittest.TestCase): 
    
    def test_is_prod(self):
        is_product_mode = app_settings.PROD
        self.assertFalse(is_product_mode, 'is_product_mode should be false')
    
    def test_db_name(self):
        db_name = app_settings.DB_NAME
        expected_db_name = 'pytest_test'
        self.assertEqual(db_name, expected_db_name, 'db_name should be '+ expected_db_name)
