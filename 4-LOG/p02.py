'''
需求：
1.所有级别日志写入文件


'''

import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 为两个不同的文件设置不同的handler处理器
rf_handler = logging.Handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message1)s"))

f_handler = logging.FileHandler('error.log')
rf_handler = .setLevel(logging)
...
具体参见官网