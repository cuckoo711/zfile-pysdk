"""
Creation date: 2025/7/10
Creation Time: 22:52
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: server_proxy_download.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass


class FileDownloadStorageKey(BaseClass):
    """文件下载存储键，定义了文件下载的存储键。"""
    name = "FileDownloadStorageKey"

    def __init__(self, api_client: "ApiClient"):
        """初始化文件上传存储键。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)
