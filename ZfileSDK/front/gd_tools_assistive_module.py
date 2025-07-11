"""
Creation date: 2025/7/10
Creation Time: 21:53
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: gd_tools_assistive_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import AjaxJsonListGoogleDriveInfoResult, GetGoogleDriveListRequest


class GdToolsAssistiveModule(BaseClass):
    """Google Drive 辅助工具模块，提供与 Google Drive 相关的辅助功能。"""
    name = "GdToolsAssistiveModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化 Google Drive 辅助工具模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=GetGoogleDriveListRequest)
    def drives(self, *, data: GetGoogleDriveListRequest) -> AjaxJsonListGoogleDriveInfoResult:
        """获取 Google Drive 列表。

        Args:
            data (GetGoogleDriveListRequest): 包含 Google Drive 配置的请求数据模型。

        Returns:
            AjaxJsonListGoogleDriveInfoResult: 包含 Google Drive 列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/gd/drives",
            response_model=AjaxJsonListGoogleDriveInfoResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 Google Drive 列表: {response.msg}")
        return response
