"""
Creation date: 2025/7/11
Creation Time: 23:34
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: site_setting_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass


class SiteSettingModule(BaseClass):
    """站点设置模块，定义了站点相关的操作方法。"""
    name = "SiteSettingModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化站点设置模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)
