"""
Creation date: 2025/7/10
Creation Time: 23:02
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: open_115_url_controller.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass


class Open115UrlController(BaseClass):
    """Open115 URL 控制器，提供处理 Open115 URL 的相关功能。"""
    name = "Open115UrlController"

    def __init__(self, api_client: "ApiClient"):
        """初始化 Open115 URL 控制器。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)
