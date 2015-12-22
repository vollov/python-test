from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base for database schema
Base = declarative_base()

import settings as app_settings

class SessionManager():
    '''SQL alchemy session manager, make this singleton'''

    def __init__(self, db_type):
        '''initialize session by db tyep: (prod | test) '''

        if not self.session:
            self.init_session(db_type)

    def init_session(self, db_type):
        db_url = app_settings.DATABASE_URL
        #defualt to prod'
        db_name = app_settings.PROD_DB
        if db_type=='test':
            db_name = app_settings.TEST_DB
        
        self.engine = create_engine(db_url + db_name)
        self.session = sessionmaker(bind_engine)

    def getSession(self):
        return self.session

