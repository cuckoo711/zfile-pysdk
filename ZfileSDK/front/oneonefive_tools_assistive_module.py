"""
Creation date: 2025/7/10
Creation Time: 22:49
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: 115_tools_assistive_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonOpen115AuthDeviceCodeResult, AjaxJsonOpen115GetStatusResult,
                            Open115AuthDeviceCodeResult)


class OneOneFiveToolsAssistiveModule(BaseClass):
    """115 辅助工具模块，提供与 115 相关的辅助功能。"""
    name = "OneOneFiveToolsAssistiveModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化 115 辅助工具模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=Open115AuthDeviceCodeResult)
    def qr_code_status(self, *, data: Open115AuthDeviceCodeResult) -> AjaxJsonOpen115GetStatusResult:
        """获取 115 二维码状态。

        Args:
            data (Open115AuthDeviceCodeResult): 包含二维码状态请求数据的模型。

        Returns:
            AjaxJsonOpen115GetStatusResult: 包含二维码状态的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/115/qrCodeStatus",
            response_model=AjaxJsonOpen115GetStatusResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 115 二维码状态: {response.msg}")
        return response

    def qr_code(self, app_id: str) -> AjaxJsonOpen115AuthDeviceCodeResult:
        """获取 115 二维码。

        Args:
            app_id (str): 应用 ID。

        Returns:
            AjaxJsonOpen115AuthDeviceCodeResult: 包含二维码信息的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/115/qrcode",
            response_model=AjaxJsonOpen115AuthDeviceCodeResult,
            params={"appId": app_id}
        )
        self._logger.info(f"[{response.trace_id}]获取 115 二维码: {response.msg}")
        return response
