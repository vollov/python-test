from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base for database schema
Base = declarative_base()

import settings as app_settings

class SessionManager():
    '''SQL alchemy session manager, make this singleton
    usage:
    #only need set db for once
     
    session = SessionManager.get_session()
    create_all(bind=None, tables=None, checkfirst=True)
    drop_all(bind=None, tables=None, checkfirst=True)
    '''

    #class level instance, gloable shared instances
    engine = None
    session = None

    @classmethod
    def init_engine(cls):
        '''initialize db engine with settings'''
        db_url = app_settings.DATABASE_URL
        db_name = app_settings.DB_NAME
                
        cls.engine = create_engine(db_url + db_name)
        

    @classmethod
    def get_session(cls):
        ''' initial session if it is None'''
        if not cls.session:
            cls.init_engine() 
            Session = sessionmaker(bind=cls.engine)
            cls.session = Session()
        return cls.session

class DataTools():
    '''
    manage import and export database tables
    '''
    @classmethod
    def export_table(cls, table_name):
        '''
        giving a table name export table as json file
        '''
        pass
    
    @classmethod
    def import_table(cls, json_file_name):
        '''
        giving a json file name import table data
        '''
        pass
    
import uuid

class KeyUtil:
    '''Utility class for pirmary key management'''
    
    @staticmethod
    def get_uuid():
        '''return an UUID() object key.
        
        to get a char(32) hex string, call key.hex 
        to get a binary(16) data, call key.bytes'''
        return uuid.uuid4()
         
        
        
