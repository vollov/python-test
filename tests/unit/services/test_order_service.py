#!/usr/bin/python
import unittest

from services.order_service import OrderService

class TestOrderService(unittest.TestCase):
    '''Unit Test for order service'''

    def setUp(self):
        "Create test points"
        print 'set up test'
        self.service = OrderService()

    def test_place_order(self):
        self.service.place_order()
        
    def test_get_service_name(self):
        OrderService.get_service_name()
