"""
Creation date: 2025/7/10
Creation Time: 22:59
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: single_sign_on_interface.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass
from ..utils.models import AjaxJsonListSsoLoginItemResponse


class SingleSignOnInterface(BaseClass):
    """单点登录接口，提供单点登录相关功能。"""
    name = "SingleSignOnInterface"

    def __init__(self, api_client: "ApiClient"):
        """初始化单点登录接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def list(self) -> AjaxJsonListSsoLoginItemResponse:
        """获取登录页面 SSO 服务商列表。

        Returns:
            AjaxJsonListSsoLoginItemResponse: 包含 SSO 服务商列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/sso/list",
            response_model=AjaxJsonListSsoLoginItemResponse
        )
        self._logger.info(f"[{response.trace_id}]获取 SSO 服务商列表: {response.msg}")
        return response
