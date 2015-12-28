import logging, unittest
from dao.db import SessionManager, Base, KeyUtil
from sqlalchemy import Column, Integer, String, BINARY, func
import uuid

logger=logging.getLogger('pytest')

class Foo(Base):
    __tablename__ = 'uuid_t'

    id = Column(Integer, primary_key=True)
    code = Column(BINARY(16))

    def __repr__(self):
        return "<Foo('%s')>" % (self.id)

class TestUuidKey(unittest.TestCase):
    
    def test_insert(self):
        #session = SessionManager.get_session()
        key = uuid.uuid4()
        key_str = key.hex
        logger.debug('insert uuid4={0}'.format(key.hex))
        logger.debug('uuid4 binary={0}'.format(repr(key.bytes)))
        
        #b = "".join(["/x%02x" % ord(c) for c in key_str])
        #logger.debug('string uuid to binary={0}'.format(b))
        #id_hex_str = 'f341ca3973bb439580b34330c3118cd4'
        #m = Foo(id=12, code=key.bytes)
        #session.add(m)
        #session.commit()
