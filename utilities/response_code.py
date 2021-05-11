# encoding=utf-8
class RET:
    NOTFOUND = "404"
    OK = "2000"
    FAIL = "-1"
    DBERR = "4001"
    NODATA = "4002"
    DATAEXIST = "4003"
    DATAERR = "4004"
    DATAEMPTY = "4005"
    SESSIONERR = "4101"
    LOGINERR = "4102"
    PARAMERR = "4103"
    USERERR = "4104"
    ROLEERR = "4105"
    PWDERR = "4106"
    AUTHEMPTY = "4107"
    REQERR = "4201"
    IPERR = "4202"
    THIRDERR = "4301"
    IOERR = "4302"
    SERVERERR = "4500"
    UNKOWNERR = "4501"
    # 支付CODE
    NOTPAY = "4600"
    REFUNDERROR = "4601"


error_map = {
    RET.NOTFOUND : u"接口不存在",
    RET.OK: u"成功",
    RET.FAIL: u"失败",
    RET.DBERR: u"数据库错误",
    RET.NODATA: u"无数据",
    RET.DATAEXIST: u"数据已存在",
    RET.DATAERR: u"数据错误",
    RET.DATAEMPTY: u"数据为空",
    RET.SESSIONERR: u"用户未登录",
    RET.LOGINERR: u"用户登录失败",
    RET.PARAMERR: u"参数错误",
    RET.USERERR: u"用户不存在或未激活",
    RET.ROLEERR: u"用户身份错误",
    RET.PWDERR: u"密码错误",
    RET.AUTHEMPTY: u"验证信息为空",
    RET.REQERR: u"非法请求或请求次数受限",
    RET.IPERR: u"IP受限",
    RET.THIRDERR: u"第三方系统错误",
    RET.IOERR: u"文件读写错误",
    RET.SERVERERR: u"内部错误",
    RET.UNKOWNERR: u"未知错误",
    # 支付CODE
    RET.NOTPAY: u"未支付",
    RET.REFUNDERROR: u"退款失败"
}
