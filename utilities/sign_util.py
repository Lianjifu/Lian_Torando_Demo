# coding=utf-8
import hashlib
from urllib import quote


def formatted_parameter(paraMap, urlencode):
    """格式化参数，签名过程需要使用"""
    slist = sorted(paraMap)
    buff = []
    for k in slist:
        v = quote(paraMap[k] if urlencode else paraMap[k])
        buff.append("{0}={1}".format(k, v))
    return "&".join(buff)


def check_sign(param, signkey):
    """校验签名"""
    secret = "04b28cdcf316e7039c5329d3037b5afc"
    String = formatted_parameter(param, False)
    String = "{0}&secret={1}".format(String, secret)
    md = hashlib.md5(String).hexdigest().upper()
    signkey = str(signkey)
    if(md == signkey):
        return True
    else:
        return False
