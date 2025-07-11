"""
Creation date: 2025/7/10
Creation Time: 19:51
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: server_proxy_upload.py
Editor: cuckoo
"""

from requests_toolbelt import MultipartEncoder

from ..utils.base import ApiClient, BaseClass
from ..utils.models import AjaxJsonString


class FileUploadStorageKey(BaseClass):
    """文件上传存储键，定义了文件上传的存储键。"""
    name = "FileUploadStorageKey"

    def __init__(self, api_client: "ApiClient"):
        """初始化文件上传存储键。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def upload_proxy(self, storage_key: str, path: str, filestream: bytes, filename: str) -> AjaxJsonString:
        """通过代理上传文件。

        Args:
            storage_key (str): 存储键。
            path (str): 文件路径。
            filestream (bytes): 文件内容的字节流。
            filename (str): 文件名

        Returns:
            AjaxJsonString: 包含上传结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        storage_key = storage_key.strip(" /")
        path = path.strip(" /")
        filename = filename.strip(" /")
        multipart_encoder = MultipartEncoder(
            fields={
                "file": (filename, filestream),
            }
        )
        headers = {
            'Content-Type': multipart_encoder.content_type
        }
        url = f"/file/upload/{storage_key}/{path}/{filename}".replace("//", "/")

        response = self.api_client.make_common_request(
            method="PUT",
            endpoint=url,
            data=multipart_encoder,
            headers=headers
        )
        return AjaxJsonString.model_validate(response.json())
