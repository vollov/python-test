#!/usr/bin/python
import logging

logger = logging.getLogger('pytest')
class OrderService:
    '''
    order service template
    '''

    def place_order(self):
        '''place order'''
        print 'order service - place order'
        logger.info('order service - place order')

    @staticmethod
    def get_service_name():
        '''get service name'''
        logger.debug('order service - get service name')
