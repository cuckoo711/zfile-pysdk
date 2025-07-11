"""
Creation date: 2025/7/10
Creation Time: 19:51
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: server_proxy_upload.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass


class FileUploadStorageKey(BaseClass):
    """文件上传存储键，定义了文件上传的存储键。"""
    name = "FileUploadStorageKey"

    def __init__(self, api_client: "ApiClient"):
        """初始化文件上传存储键。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)
