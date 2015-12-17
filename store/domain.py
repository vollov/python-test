# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Sequence, DateTime
from datetime import datetime
import time
from dao.database import Base

class Customer(Base):
    __tablename__ = 'customer'
    
    id = Column(String(20), primary_key=True)
    name = Column(String(16))
    phone = Column(String(12))
    address = Column(String(125))
    
    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.phone)