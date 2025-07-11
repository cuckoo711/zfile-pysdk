"""
Creation date: 2025/7/12
Creation Time: 05:48
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: login_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonLoginTwoFactorAuthenticatorResult, AjaxJsonVoid,
                            VerifyLoginTwoFactorAuthenticatorRequest)


class LoginModule(BaseClass):
    """登录模块接口，定义了登录相关的操作方法。"""
    name = "LoginModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化登录模块接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=VerifyLoginTwoFactorAuthenticatorRequest)
    def device_verify(self, *, data: VerifyLoginTwoFactorAuthenticatorRequest) -> AjaxJsonVoid:
        """2FA 验证并绑定。

        Args:
            data (VerifyLoginTwoFactorAuthenticatorRequest): 包含 2FA 验证信息的请求数据模型。

        Returns:
            AjaxJsonVoid: 验证结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/2fa/verify",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]2FA 验证并绑定: {response.msg}")
        return response

    def setup_device(self) -> AjaxJsonLoginTwoFactorAuthenticatorResult:
        """生成 2FA。

        Returns:
            AjaxJsonLoginTwoFactorAuthenticatorResult: 2FA 生成结果，包含二维码和密钥。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/2fa/setup",
            response_model=AjaxJsonLoginTwoFactorAuthenticatorResult
        )
        self._logger.info(f"[{response.trace_id}]生成 2FA: {response.msg}")
        return response
