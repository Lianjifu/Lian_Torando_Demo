#!/usr/bin/python
# encoding=utf-8
# tornado 框架
import tornado.web
from utilities import utils as utils


# Handlers 共享的 Handler 方法。API 使用不正确错误处理
class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.add_header("Access-Control-Allow-Origin", "*")
        self.add_header("Access-Control-Allow-Origin", "*")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header("Access-Control-Expose-Headers", "Authorization")


# 错误 API 链接处理
class ErrorLinkHandler(BaseHandler):
    def get(self):
        self.set_status(404, 'Page Not Found')
        self.write(utils.f_rsp("Opps......", 404))
