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
    def GetTimestamp(
    self,
    gettime=time):
        """
        获取时间戳，返回单位为毫秒的时间戳
        gettime为空时默认值为当前时间

        Example:
        | ${time} | GetCureentTime |gettime|
        | log | ${time} |
        
        """
        a = gettime.time()
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
  
    def timestamp2datetime(self,timestamp,convert_to_local=True):
        ''' 将时间戳转换为本地时间'''
        if isinstance(timestamp, (int, long, float)):
            dt = datetime.datetime.utcfromtimestamp(timestamp)
            if convert_to_local: # 是否转化为本地时间
                dt = dt + datetime.timedelta(hours=8) # 中国默认时区                    
            return dt
        return timestamp
