"""
Creation date: 2025/7/10
Creation Time: 21:41
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: onedrive_authentication_callback_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass


class OneDriveAuthenticationCallbackModule(BaseClass):
    """OneDrive 认证回调模块，处理 OneDrive 的 OAuth 认证流程。"""
    name = "OneDriveAuthenticationCallbackModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化 OneDrive 认证回调模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)
