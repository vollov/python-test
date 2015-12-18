from services.order_service import OrderService
from services.account_service import AccountService

import logging.config
import settings as app_settings

def run():
    '''run app'''

    #initial logging logging config
    logging.config.dictConfig(app_settings.LOGGING)

    OrderService.get_service_name()
    AccountService.get_service_name()

if __name__ == '__main__':
    run()
