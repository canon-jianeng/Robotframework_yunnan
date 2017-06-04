#-*- coding:utf8 -*- 
#Edit by yuzr

import time
import hashlib

class CustomRequest:
    """
    此Library包含2个方法：
    1.获取当前时间戳，返回单位为毫秒的时间戳
    2.根据传入的参数自动添加时间戳后生成MD5值

    """
    def GetTimestamp(self):
        """
        获取当前时间戳，返回单位为毫秒的时间戳

        Example:
        | ${time} | GetCureentTime |
        | log | ${time} |
        
        """
        a = time.time()
        b = long(a*1000)
        c = str(b)
        return c
    def CreateKey(self,time_stamp,sysCode = 'QXSJ',salt = 'hskfsaf=='):
        """
        根据传入的参数生成MD5值
        sysCode为空时默认：QXSJ
        salt为空时默认：hskfsaf==

        Example:
        | ${md5} | CreateKey | time_stamp | sysCode | salt |
        | log | ${md5} |
        
        """
        n = sysCode + time_stamp + salt
        m = hashlib.md5()
        m.update(n)
        j = m.hexdigest()
        return j
        
