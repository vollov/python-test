# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# engine = create_engine(app.config['DATABASE_URL'], echo=True,\
#                         convert_unicode=True)
# 
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# 
# Base = declarative_base()
# Base.query = db_session.query_property()

engine = create_engine('mysql://root:justdoit@localhost/flaskr_store')
session_factory  = sessionmaker(bind=engine)

# use scoped_session to link the scope of a Session with a web request 
Session = scoped_session(session_factory)
Base = declarative_base()

Base.query = Session.query_property()
