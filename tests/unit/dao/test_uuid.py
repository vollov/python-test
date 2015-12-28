import logging, unittest
from dao.db import SessionManager, Base, KeyUtil
from sqlalchemy import Column, Integer, String, BINARY, func
import uuid
from uuid import UUID

logger=logging.getLogger('pytest')

class Foo(Base):
    __tablename__ = 'uuid_t'

    id = Column(Integer, primary_key=True)
    code = Column(BINARY(16))

    def __repr__(self):
        return "<Foo('%s')>" % (self.id)

class TestUuidKey(unittest.TestCase):
    
    def test_binary_uuid(self):
        '''
        Test generate uuid and save it as a binary in database.
        
        use python uuid library to generate the key 
        
        key = uuid.uuid4() #key is an UUID object
        key_str = key.hex
        key_binary = key.bytes
        
        session = SessionManager.get_session()
        m = Foo(id=12, code=key.bytes)
        session.add(m)
        session.commit()
        '''
        
        key = UUID('f341ca39-73bb-4395-80b3-4330c3118cd4')
        expected_hex_string = 'f341ca3973bb439580b34330c3118cd4'
        self.assertEquals(key.hex,expected_hex_string,'hex string should be ' + expected_hex_string)
        
        expected_bytes = '\xf3A\xca9s\xbbC\x95\x80\xb3C0\xc3\x11\x8c\xd4'
        self.assertEquals(key.bytes,expected_bytes,'hex binary should be ' + expected_bytes)
        
        #logger.debug('insert uuid4={0}'.format(key.hex))
        #logger.debug('uuid4 binary={0}'.format(repr(key.bytes)))
        
