"""
ZFile SDK - Python SDK for ZFile API
提供完整的ZFile API访问功能
"""

# 导入主要模块
from .utils import ApiClient, ApiException, CustomException, ErrorDataModel, LogHandler

# 版本信息
__version__ = "1.1.1"
__author__ = "cuckoo"
__description__ = "Python SDK for ZFile API"

# 导出的主要类列表
__all__ = [
    # 核心工具类
    "ApiClient",
    "LogHandler",

    # 异常处理
    "ApiException",
    "CustomException",
    "ErrorDataModel",

    # 版本信息
    "__version__",
    "__author__",
    "__description__"
]
