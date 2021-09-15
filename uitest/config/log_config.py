# 1.导包
import logging
import logging.handlers
import os
# #
# BASE_PATH = os.path.dirname(os.path.abspath("__file__"))
BASE_PATH = os.path.abspath(os.path.join(os.getcwd(), ".."))

def set_log_config():
    # 2.创建日志器对象 / 设置日志级别
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 3.创建输出到控制台 / 文件(按时间切割)的处理器对象
    ls = logging.StreamHandler()
    lf = logging.handlers.TimedRotatingFileHandler(filename="./log/testlog.log", when="d", backupCount=5)
    # 4.创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    # 5.将格式化器添加到处理器
    ls.setFormatter(formatter)
    lf.setFormatter(formatter)
    # 6.添加处理器到日志器
    logger.addHandler(ls)
    logger.addHandler(lf)
