"""
Creation date: 2025/7/10
Creation Time: 22:25
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: initialization_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import AjaxJsonBoolean, AjaxJsonVoid, InstallSystemRequest


class InitializationModule(BaseClass):
    """初始化模块，提供系统初始化相关功能。"""
    name = "InitializationModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化初始化模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=InstallSystemRequest)
    def install(self, *, data: InstallSystemRequest) -> AjaxJsonVoid:
        """初始化系统。

        Args:
            data (InstallSystemRequest): 包含初始化请求数据的模型。

        Returns:
            AjaxJsonVoid: 包含操作结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/install",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]初始化系统: {response.msg}")
        return response

    def install_status(self) -> AjaxJsonBoolean:
        """获取系统初始化状态。

        Returns:
            AjaxJsonBoolean: 包含系统初始化状态的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/api/install/status",
            response_model=AjaxJsonBoolean
        )
        self._logger.info(f"[{response.trace_id}]获取系统初始化状态: {response.msg}")
        return response
