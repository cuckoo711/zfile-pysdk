"""
Creation date: 2025/7/10
Creation Time: 22:38
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: onlyoffice_related_interfaces.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import AjaxJsonJSONObject, FileItemRequest


class OnlyOfficeModule(BaseClass):
    """OnlyOffice 模块，提供与 OnlyOffice 相关的接口。"""
    name = "OnlyOfficeModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化 OnlyOffice 模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=FileItemRequest)
    def config_token(self, *, data: FileItemRequest) -> AjaxJsonJSONObject:
        """OnlyOffice 预览文件

        Args:
            data (FileItemRequest): 包含文件项请求数据的模型。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/onlyOffice/config/token",
            response_model=AjaxJsonJSONObject,
            data=data
        )
        self._logger.info(f"[{response.trace_id}] OnlyOffice 预览文件: {response.msg}")
        return response
