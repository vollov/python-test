# python-test
show how to build and test python applications with invoke

pip install -U pytest
pip install invoke

http://pytest.org/latest/usage.html

tree -f -I "bin|unitTest" -P "*.[ch]|*.[ch]pp." your_dir/
tree -I "*.pyc"

##manage test fixtures
class ProductTestCase(TestCase):
    fixtures = ['user.json', 'store.json']
    
    def test_create_store(self):
        """user anna can create store"""