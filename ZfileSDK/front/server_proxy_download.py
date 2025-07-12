"""
Creation date: 2025/7/10
Creation Time: 22:52
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: server_proxy_download.py
Editor: cuckoo
"""
from ..utils.models import FileTypeEnum
from ..utils.base import ApiClient, BaseClass
from ..utils.exceptions import CustomException


class FileDownloadStorageKey(BaseClass):
    """文件下载存储键，定义了文件下载的存储键。"""
    name = "FileDownloadStorageKey"

    def __init__(self, api_client: "ApiClient"):
        """初始化文件上传存储键。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def download_proxy(self, storage_key: str, signature: str, filename: str = None,
                       file_type: FileTypeEnum = "FILE") -> bytes:
        """通过代理下载文件。

        Args:
            storage_key (str): 存储键。
            signature (str): 请求签名。
            filename (str, optional): 文件名。如果未提供，默认下载原文件。
            file_type (FileTypeEnum): 下载类型，默认是"FILE"。

        Returns:
            bytes: 文件内容的字节流。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        storage_key = storage_key.strip(" /")
        filename = filename.strip(" /") if filename else None
        url = f"/pd/{storage_key}/{filename or ''}?signature={signature}&type={file_type}"

        response = self.api_client.make_common_request(
            method="GET",
            endpoint=url
        )

        if response.status_code == 200:
            return response.content  # 返回文件流
        else:
            raise CustomException(500, f"Failed to download file: {response.text}")
