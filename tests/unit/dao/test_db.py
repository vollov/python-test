from dao.db import SessionManager, Base
import logging, unittest

from dao.db import SessionManager, Base

logger=logging.getLogger('pytest')

from sqlalchemy import Column, Integer, String, BINARY
class Customer(Base):
    __tablename__ = 'customer'

    id = Column(BINARY(16), primary_key=True)
    name = Column(String(16))
    phone = Column(String(12))
    address = Column(String(125))

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.phone)


class TestSessionManager(unittest.TestCase):
    
    session = None
    engine =None

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
        cls.session = SessionManager.get_session() 
        
        #get engine
        cls.engine = cls.session.get_bind()
        
        # this is not working
        #Base.metadata.create_all(cls.engine, tables=['customer'])
        Base.metadata.tables['customer'].create(bind = cls.engine)
        logger.debug('TestSessionManager setup class')
        #customers = [ Customer(name='Dave', phone='416-223-8652', address='9 King ST'),
        #              Customer(name='Leah', phone='416-216-7529', address='19 King ST'),
        #              Customer(name='Skyler', phone='416-220-3386', address='79 King ST')]
        # session.add_all() requires pk defined
        #cls.session.bulk_save_objects(customers)
        session = cls.session

        #session.add(Customer(name='Dave', phone='416-223-8652', address='9 King ST'))
        pkid = KeyUtil.get_uuid4()
        session.add(Customer(id = pkid, name='Leah', phone='416-216-7529', address='19 King ST'))
        session.commit()

    @classmethod
    def tearDownClass(cls):
        '''
        1) remove customer table
        2) release session by call session.close()
        '''
        Base.metadata.tables['customer'].drop(bind = cls.engine)
        logger.debug('TestSessionManager tear down class')

    def test_query(self):
        '''testing a sql query'''
        
        session = self.session
        customers = session.query(Customer)
        for c in customers:
            logger.debug('TestSessionManager query customer: {0}'.format(c.name))
        session.commit()

