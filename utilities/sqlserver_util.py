#!/usr/bin/python2
# encoding=utf-8
# Python 和 SQLSERVER 交互
import pymssql

# 只对数据库数据进行读模式，不可进行修改或者其它操作

# 连接3.0后台数据库
class ssdb_util_2(object):
    def __init__(self):
        self.host = "47.96.122.240"
        self.user = "sa"
        self.pwd = "ShYwg20190625"
        self.db = "YWG_2.SELLER"
        conn = None
        cur = None
        try:
            conn = pymssql.connect(server=self.host, user=self.user, password=self.pwd, database=self.db,
                                        charset='utf8')
            cur = conn.cursor()  # 将数据库连接信息，赋值给cur。
            if not cur:
                cur = None

        except Exception, e:
            conn = None
            cur = None

        self.conn = conn
        self.cur = cur

    # 执行查询语句,返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    def selectSQL(self, _sql_str=None, _tuple=None, _type=0):  # 执行Sql语句函数，返回结果
        db_result = ()

        if _sql_str:
            try:
                if _type == 0:
                    if _tuple:
                        self.cur.execute(_sql_str, _tuple)
                        db_result = self.cur.fetchone()
                    else:
                        self.cur.execute(_sql_str)
                        db_result = self.cur.fetchone()
                else:
                    if _tuple:
                        self.cur.execute(_sql_str, _tuple)
                        db_result = self.cur.fetchall()
                    else:
                        self.cur.execute(_sql_str)
                        db_result = self.cur.fetchall()

            except Exception, e:
                db_result = ()
        else:
            pass
        return db_result
