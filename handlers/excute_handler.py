#!/usr/bin/python
# encoding=utf-8
### 成都动物园定制版 -- 推货记录

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# 调用系统的方法
import os
import time
import logging
import json
# tornado 框架
import tornado.web
# tornado 异步
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
# 自定义模块
from base_handler import BaseHandler
from utilities.utils import *
# 引入自定义数据库操作方法
from utilities.db_util import db_util
from utilities.sign_util import check_sign
from utilities.response_code import RET
# 3.0后台数据库
from utilities.sqlserver_util import ssdb_util_2

# 查询设备出货记录
class QueryDataInfo(BaseHandler):
    # 异步
    executor = ThreadPoolExecutor(5)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        res = yield self.asyc_query_data_info()

    @run_on_executor
    def asyc_query_data_info(self):
        api_log_start("asyc_query_data_info")
        ExpectParams = ["start_time", "end_time", "medal_user", "medal_password", "signkey"]
        RqstDt = verify_request_body(self, ExpectParams)
        if not RqstDt:
            return self.write(dict(code=RET.PARAMERR, msg="Required Arguments Missing", data=str(self.request.body)))
        start_time = str(RqstDt.get("start_time"))
        end_time = str(RqstDt.get("end_time"))
        medal_user = str(RqstDt.get("medal_user"))
        medal_password = str(RqstDt.get("medal_password"))
        signkey = str(RqstDt.get("signkey"))
        param = {
            "start_time": start_time,
            "end_time": end_time,
            "medal_user": medal_user,
            "medal_password": medal_password
        }
        result = check_sign(param, signkey)
        device_data = []
        device_data_param = []
        if result:
            if medal_user == "chengdu_zoo" and medal_password == "chengdu_zoo_3b93ce":
                try:
                    DbInit = ssdb_util_2()
                    _sql = "select dd.id from dbo.D_Devices as dd, dbo.M_Company as mc where dd.company = mc.id and mc.id = 'eac5b2642e094078';"
                    DbRsSel = DbInit.selectSQL(_sql, _type="all")
                    if DbRsSel:
                        for row in DbRsSel:
                            device = row[0]
                            device_data.append(device)
                    else:
                        pass
                except Exception as e:
                    logging.error(e)
                    return self.write(dict(code=RET.DBERR, msg="Query Exception"))
                try:
                    device_1 = ''
                    j = 0
                    if len(device_data) < 1:
                        return self.write(dict(code=RET.DATAEMPTY, msg="Data Is Empty"))
                    for i in device_data:
                        j += 1
                        if j < len(device_data):
                            device = "device_id='" + i + "'" + ' or '
                            device_1 += device
                        else:
                            device_1 = device_1 + "device_id='" + i + "'"
                    DbInit_1 = ssdb_util_2()
                    _sql_1 = "SELECT distinct dev_trade_id,device_id ,dd.name,goods_id, gs.name, CAST (amount as FLOAT ),channel, pay_type, platform_ind_id,wx_app_id,wx_mch_id, partner, add_time,out_state,refund_state, buyer_id,wx_openid FROM (X_Trades as xt left join D_Devices as dd on xt.device_id = dd.id )left join Goodses as gs on xt.goods_id = gs.id WHERE  ("+ device_1 +") and (xt.pay_type = '0'or xt.pay_type = '1'or xt.pay_type = '3')  AND add_time between  '"+start_time +"' and  (SELECT DATEADD(DAY,1,'"+end_time+"')) ORDER BY add_time DESC;"
                    DbRsSel_1 = DbInit_1.selectSQL(_sql_1, _type="all")
                    if DbRsSel_1:
                        for row in DbRsSel_1:
                            m = {
                                "dev_trade_id": row[0],
                                "device_id": row[1],
                                "device_name": row[2],
                                "goods_id": row[3],
                                "goods_name": row[4],
                                "sale_price": row[5],
                                "sale_quantity": 1,
                                "sale_price_total": row[5],
                                "sale_channel": row[6],
                                "sale_pay_type": row[7],
                                "platform_ind_id": row[8],
                                "wx_app_id": row[9],
                                "wx_mch_id": row[10],
                                "partner": row[11],
                                "sale_time": row[12].strftime("%Y-%m-%d %H:%M:%S"),
                                "sale_out_state": row[13],
                                "refund_state": row[14],
                                "buyer_id": row[15],
                                "wx_openid": row[16],
                            }

                            device_data_param.append(m)
                    else:
                        return self.write(dict(code=RET.DATAEMPTY, msg="Data Is Empty"))
                except Exception as e:
                    logging.error(e)
                    return self.write(dict(code=RET.DBERR, msg="Query Exception"))

            else:
                return self.write(dict(code=RET.ROLEERR, msg="User Identity Error"))
        else:
            return self.write(dict(code=RET.REQERR, msg="Illegal Request"))

        api_log_end("asyc_query_id_card_binging_info")
        return self.write(dict(code=RET.OK, msg="OK",data=device_data_param))


# 查询设备退款记录
class QueryRefundsInfo(BaseHandler):
    # 异步
    executor = ThreadPoolExecutor(5)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        res = yield self.asyc_query_refunds_info()

    @run_on_executor
    def asyc_query_refunds_info(self):
        api_log_start("asyc_query_refunds_info")
        ExpectParams = ["start_time", "end_time", "medal_user", "medal_password", "signkey"]
        RqstDt = verify_request_body(self, ExpectParams)
        if not RqstDt:
            return self.write(dict(code=RET.PARAMERR, msg="Required Arguments Missing", data=str(self.request.body)))
        start_time = str(RqstDt.get("start_time"))
        end_time = str(RqstDt.get("end_time"))
        medal_user = str(RqstDt.get("medal_user"))
        medal_password = str(RqstDt.get("medal_password"))
        signkey = str(RqstDt.get("signkey"))
        param = {
            "start_time": start_time,
            "end_time": end_time,
            "medal_user": medal_user,
            "medal_password": medal_password
        }
        result = check_sign(param, signkey)
        device_data = []
        refunds_info = []
        if result:
            if medal_user == "chengdu_zoo" and medal_password == "chengdu_zoo_3b93ce":
                try:
                    DbInit = ssdb_util_2()
                    _sql = "select dd.id from dbo.D_Devices as dd, dbo.M_Company as mc where dd.company = mc.id and mc.id = 'eac5b2642e094078';"
                    DbRsSel = DbInit.selectSQL(_sql, _type="all")
                    if DbRsSel:
                        for row in DbRsSel:
                            device = row[0]
                            device_data.append(device)
                    else:
                        pass
                except Exception as e:
                    logging.error(e)
                    return self.write(dict(code=RET.DBERR, msg="1Query Exception"))

                try:
                    device_1 = ''
                    j = 0
                    if len(device_data) < 1:
                        return self.write(dict(code=RET.DATAEMPTY, msg="Data Is Empty"))
                    for i in device_data:
                        j += 1
                        if j < len(device_data):
                            device = "device_id='" + i + "'" + ' or '
                            device_1 += device
                        else:
                            device_1 = device_1 + "device_id='" + i + "'"
                    DbInit_1 = ssdb_util_2()
                    _sql_1 = "SELECT dev_trade_id,device_id,dd.name,platform_ind_id,add_time,net_details,CAST (amount as FLOAT ),refund_code FROM dbo.X_Refunds as xr left join D_Devices as dd on xr.device_id = dd.id  WHERE ("+ device_1 +") AND add_time between  '"+start_time +"' and  (SELECT DATEADD(DAY,1,'"+end_time+"')) and refund_code = 1 ORDER BY add_time DESC;"
                    DbRsSel_1 = DbInit_1.selectSQL(_sql_1, _type="all")
                    if DbRsSel_1:
                        for row in DbRsSel_1:
                            data = self.query_refund_goods(row[0])
                            m = {
                                "dev_trade_id": row[0],
                                "device_id": row[1],
                                "device_name": row[2],
                                "goods_id": data[0],
                                "goods_name": data[1],
                                "sale_pay_type": data[2],
                                "wx_app_id": data[3],
                                "wx_mch_id": data[4],
                                "partner": data[5],
                                "platform_ind_id": row[3],
                                "refund_time": row[4].strftime("%Y-%m-%d %H:%M:%S"),
                                "net_details": row[5],
                                "refund_price": row[6],
                                "refund_quantity": 1,
                                "refund_code": row[7]
                            }
                            refunds_info.append(m)
                    else:
                        return self.write(dict(code=RET.DATAEMPTY, msg="Data Is Empty"))
                except Exception as e:
                    logging.error(e)
                    return self.write(dict(code=RET.DBERR, msg="2Query Exception"))
            else:
                return self.write(dict(code=RET.ROLEERR, msg="User Identity Error"))

        else:
            return self.write(dict(code=RET.REQERR, msg="Illegal Request"))

        api_log_end("asyc_query_refunds_info")
        return self.write(dict(code=RET.OK, msg="OK", data= refunds_info))

    def query_refund_goods(self, dev_trade_id):
        good_id = ''
        good_name = ''
        pay_type = ''
        wx_app_id = ''
        wx_mch_id = ''
        partner = ''
        try:
            DbInit_1 = ssdb_util_2()
            _sql_1 = "SELECT goods_id, gs.name,pay_type, wx_app_id,wx_mch_id,partner FROM (X_Trades as xt left join D_Devices as dd on xt.device_id = dd.id )left join Goodses as gs on xt.goods_id = gs.id WHERE dev_trade_id='"+dev_trade_id+"';"

            DbRsSel_1 = DbInit_1.selectSQL(_sql_1, _type="all")
            if DbRsSel_1:
                for row in DbRsSel_1:
                    good_id = row[0]
                    good_name = row[1]
                    pay_type = row[2]
                    wx_app_id = row[3]
                    wx_mch_id = row[4]
                    partner = row[5]
                return good_id, good_name, pay_type,wx_app_id, wx_mch_id, partner
        except Exception as e:
            logging.error(e)
            return self.write(dict(code=RET.DBERR, msg="3Query Exception"))