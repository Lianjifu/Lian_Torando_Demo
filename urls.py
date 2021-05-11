#!/usr/bin/python
# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from handlers import base_handler as bh
from handlers import excute_handler as eh


urls = [
    #################################################
    # APIs									        #
    #################################################
    (r"/medal/data/trade/query", eh.QueryDataInfo),
    (r"/medal/data/refund/query", eh.QueryRefundsInfo),

    (r".*", bh.ErrorLinkHandler),
]
