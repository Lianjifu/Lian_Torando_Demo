# coding:utf-8

"""
主启动程序
author: lianjifu
data: 2019/10/28
"""

import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os
import config
from urls import urls
from tornado.options import options


class Application(tornado.web.Application):
    def __init__(self,*args, **kwargs):
        base_dir = os.path.dirname(__file__)
        settings = dict(
            template_path=os.path.join(base_dir, "template"),
            static_path=os.path.join(base_dir, "static"),
            cookie_secret='MuG7xxa/cQdGPH',
            # xsrf_cookies=True,
            debug=True
        )
        super(Application, self).__init__(urls, **settings)


def main():
    options.log_file_prefix = config.log_path
    options.logging = config.log_level
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port=config.ser_port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()