from dao.db import SessionManager, Base
import logging, unittest

logger=logging.getLogger('pytest')

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(String(20), primary_key=True)
    name = Column(String(16))
    phone = Column(String(12))
    address = Column(String(125))

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.phone)


class TestSessionManager(unittest.TestCase):
    
    session = None

    def setUp(self):
        '''set up test db'''
        pass

    def tearDown(self):
        '''tear down test db'''
        pass

    @classmethod
    def setUpClass(cls):
        ''' 
        1) inint session
        2) create customer table
        3) insert data to customer table
        '''
        pass

    @classmethod
    def tearDownClass(cls):
        '''
        1) remove customer table
        2) release session by call session.close()
        '''

        logger.debug('TestCase tear down class')

    def test_query(self):
        '''testing a sql query'''
        pass


