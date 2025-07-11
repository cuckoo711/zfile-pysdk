"""
Creation date: 2025/7/10
Creation Time: 16:11
DIR PATH: ZfileSDK/utils
Project Name: ZfileSDK
FILE NAME: logger.py
Editor: cuckoo
"""

import logging
import os
from typing import Literal

LogLevel = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]


class LogHandler:
    """日志处理器类，用于配置和管理日志"""

    def __init__(self,
                 name: str,
                 level: LogLevel = "INFO",
                 log_dir: str = "logs",
                 log_to_file: bool = False):
        """
        初始化日志处理器
        :param log_dir: 日志文件存储目录
        :param level: 日志级别
        """
        self.logger = logging.getLogger(name)

        if not self.logger.handlers:
            log_level_obj = getattr(logging, level.upper(), logging.INFO)
            self.logger.setLevel(log_level_obj)

            # 确保日志记录器不会向父记录器传播日志
            self.logger.propagate = False

            # 设置日志处理器
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # 控制台处理器
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # 文件处理器
            if log_to_file:
                if not os.path.exists(log_dir):
                    os.makedirs(log_dir)
                log_file_path = os.path.join(log_dir, f"{name.replace('.', '_')}.log")
                file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """获取配置好的日志记录器实例"""
        return self.logger
