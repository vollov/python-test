import os, unittest, logging

logger = logging.getLogger('pytest')

# Prototype for with cluse

class MySessionQueryException(Exception):
    '''if query = lana, raise Exception :)'''
    pass

class MySession:
    def __init__(self):
        logger.debug('init MySession')
        self.dbType='mysql'

    def close(self):
        logger.debug('close MySession')

    def query(self, sql):
        if sql == 'lana':
            raise MySessionQueryException('query can not be lana!')

        logger.debug('MySession query =' + sql);

class SessionManager:
    def __enter__(self):
        logger.debug('prepare my session')
        self.session = MySession()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()

class ThingTwo():
    def go(self, session, sql):
        session.query(sql)


class TestWith(unittest.TestCase):

    def setUp(self):
        #logs = Logger()
        logger.debug('TestWith setup')

    def test_with(self):
        with SessionManager() as my_session:
            ThingTwo().go(my_session, 'select 1')

    def test_with_exception(self):
        try:
            with SessionManager() as my_session:
                ThingTwo().go(my_session, 'lana')
        except MySessionQueryException, e:
            logger.error('Error test_with_exception')
            logger.error(e)

    
def run():
    with SessionManager() as my_session:
        ThingTwo().go(my_session)

if __name__ == '__main__':
    run()
    
        
