'''
this file demo how to manage instances
'''
import logging, unittest
logger=logging.getLogger('pytest')

class A(object):

    conn='shared connection here'
    
    def foo(self,x):
        logger.debug('instance method call conn:' + self.conn)
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        logger.debug('class method call conn:' + cls.conn)
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        logger.debug('static method call conn:' + A.conn)
        print "executing static_foo(%s)"%x 

class Session:
    
    bind = None

    def __init__(self):
        logger.debug('Session initialize')

    #def __init__(self, bind):
    #    self.bind = bind

    def configure(self, bind):
        self.bind = bind

    def get_bind(self):
        return self.bind

class DummyManager:
    '''
    To get session:
    DummyManager.set_type('test')
    session = DummyManager.get_session()

    '''
    engine = None
    session = None
    db_type = None

    @classmethod
    def get_session(cls):
        if not cls.session:
            cls.session = Session()
            cls.load_engine()
           
        return cls.session

    @classmethod
    def load_engine(cls):
        # set default db_type
        if not cls.db_type:
            cls.db_type = 'prod'
        
        if cls.db_type == 'prod':
            cls.engine = 'prod_db_engine'
        else:
            cls.engine = 'test_db_engine'
        
        cls.session.configure(bind=cls.engine)

    @classmethod
    def set_type(cls, db_type):
        cls.db_type = db_type
        

class TestDummyManager(unittest.TestCase):

    def test_run(self):
        #m1 = DummyManager()
        DummyManager.set_type('test')
        s1 = DummyManager.get_session()
        logger.debug('s1 bind={0}'.format(s1.get_bind()))

        #m2 = DummyManager()
        DummyManager.set_type('prod')
        DummyManager.load_engine()
        s2 = DummyManager.get_session()

        logger.debug('s1 after set engine bind={0}'.format(s1.get_bind()))
        logger.debug('s2 bind={0}'.format(s2.get_bind()))

        logger.debug('s1 address={0}'.format(id(s1)))
        logger.debug('s2 address={0}'.format(id(s2)))

    def test_method(self):
        a = A()
        a.foo(1)
        A.class_foo(2)
        A.static_foo(3)
