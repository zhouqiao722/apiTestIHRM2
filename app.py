# 编写初始化日志的函数
import logging
from logging import handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "HTTP://182.92.81.159"
HEADERS = {"Content-Type": "application/json"}
EMP_ID = 0


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置处理器
    # 设置处理器控制台
    sh = logging.StreamHandler()
    # 设置文件处理器
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when="M", interval=1, backupCount=7)
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(fh)
    logger.addHandler(sh)
