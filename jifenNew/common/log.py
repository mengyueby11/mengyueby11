#coding=utf-8
import logging
import os.path
import time

class Logger(object):

    def __init__(self, logger):

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        n_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/logs/'
        log_name = log_path + n_time + '.log'  
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s-%(funcName)s-%(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__=='_main_':
    logger = Logger("fox")
    logger.logger.debug("debug")
    logger.logger.log(logging.ERROR,'%(module)s%(info)s',{'module':'log日志','info':'error'})