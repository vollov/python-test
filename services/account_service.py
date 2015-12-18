#!/usr/bin/python
import logging

logger = logging.getLogger('pytest')
class AccountService:
    '''
    account service template
    '''

    def place_order(self):
        '''authentication'''
        print 'account service - authentication'
        logger.info('account service - authentication')

    @staticmethod
    def get_service_name():
        '''get service name'''
        logger.debug('account service - get service name')
