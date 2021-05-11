#!/usr/bin/python
# encoding=utf-8

import os

from tornado.options import define, options
import logging

define("port", default='7008', help="run on the given port", type=str)
define("env", default='local', help="run on the given env", type=str)
options.parse_command_line()
ser_port = options.port
env = options.env

# 生产配置
if env == 'prod':
    host = "localhost"
    base_url = "http://" + host + ":" + ser_port + "/"
    ser_debug = False
    # MYSQL
    pps_db = ""
    db_host = ""
    db_usr = ""
    db_pw = ""
    db_port = 3306
    db_charset = "utf8"

# 开发配置
elif env == 'dev':
    host = "localhost"
    base_url = "http://" + host + ":" + ser_port + "/"
    # MYSQL
    pps_db = ""
    db_host = ""
    db_usr = ""
    db_pw = ""
    db_port = 3306
    db_charset = "utf8"

# 本地服务，远端测试库
elif env == 'local':
    host = "localhost"
    base_url = "http://" + host + ":" + ser_port + "/"
    # MYSQL
    pps_db = 'ywg_genesis_admin_local'
    db_host = "localhost"
    db_usr = "root"
    db_pw = "mysql"
    db_port = 3306
    db_charset = "utf8"

logging.info("Environment: " + env)
logging.info("Server Port: " + str(ser_port))

# 日志配置
log_path = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"

image_path = os.path.join(os.path.dirname(__file__), "static/image")


# 微信证书路径
SSH_KEYS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "CERT")

WX_APICLIENT_CERT = os.path.join(SSH_KEYS_PATH, "apiclient_cert.pem")

WX_APICLIENT_KEY = os.path.join(SSH_KEYS_PATH, "apiclient_key.pem")