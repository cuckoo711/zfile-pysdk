"""
Creation date: 2025/7/10
Creation Time: 22:52
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: single_sign_on.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass
from ..utils.models import RedirectView


class SingleSignOnModule(BaseClass):
    """单点登录模块，提供单点登录相关功能。"""
    name = "SingleSignOnModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化单点登录模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def provider_login(self, provider: str) -> RedirectView:
        """获取指定单点登录提供者的登录地址。

        Args:
            provider (str): 单点登录提供者的名称。

        Returns:
            RedirectView: 包含重定向地址的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/sso/{provider}/login",
            response_model=RedirectView
        )
        self._logger.info(f"[{response.trace_id}]获取单点登录地址: {response.msg}")
        return response

    def provider_login_callback(self, provider: str, code: str, state: str) -> RedirectView:
        """处理单点登录提供者的回调。

        Args:
            provider (str): 单点登录提供者的名称。
            code (str): 授权码。
            state (str): 状态参数。

        Returns:
            RedirectView: 包含重定向地址的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/sso/{provider}/login/callback",
            response_model=RedirectView,
            params={"code": code, "state": state}
        )
        self._logger.info(f"[{response.trace_id}]处理单点登录回调: {response.msg}")
        return response
