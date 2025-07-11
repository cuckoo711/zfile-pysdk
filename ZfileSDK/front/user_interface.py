"""
Creation date: 2025/7/10
Creation Time: 19:01
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: user.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonCheckLoginResult, AjaxJsonLoginVerifyImgResult, AjaxJsonLoginVerifyModeEnum,
                            AjaxJsonVoid,
                            ResetAdminUserNameAndPasswordRequest,
                            UpdateUserPwdRequest)


class UserInterface(BaseClass):
    """用户接口，定义了用户相关的操作方法。"""
    name = "UserInterface"

    def __init__(self, api_client: "ApiClient"):
        """初始化用户接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=ResetAdminUserNameAndPasswordRequest)
    def reset_admin_password(self, *, data: ResetAdminUserNameAndPasswordRequest) -> AjaxJsonVoid:
        """重置管理员密码。

        Args:
            data (ResetAdminUserNameAndPasswordRequest): 包含用户名和新密码的请求数据模型。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.put(
            endpoint="/user/resetAdminPassword",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]重置管理员密码: {response.msg}")
        return response

    @auto_args_from_model(model=UpdateUserPwdRequest)
    def update_psd(self, *, data: UpdateUserPwdRequest) -> AjaxJsonVoid:
        """更新用户密码。

        Args:
            data (UpdateUserPwdRequest): 包含用户名、旧密码和新密码的请求数据模型。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/user/updatePwd",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]更新用户密码: {response.msg}")
        return response

    def login_verify_mode(self, username: str) -> AjaxJsonLoginVerifyModeEnum:
        """获取登录验证方式。

        Args:
            username (str): 用户名。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        
        Returns:
            str: 登录验证方式。
        """
        params = {"username": username}
        response = self.api_client.get(
            endpoint="/user/login/verify-mode",
            response_model=AjaxJsonLoginVerifyModeEnum,
            params=params
        )
        self._logger.info(f"[{response.trace_id}]获取登录验证方式: {response.msg}")
        return response

    def login_check(self) -> AjaxJsonCheckLoginResult:
        """检查用户是否已登录。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。

        Returns:
            AjaxJsonLoginVerifyModeEnum: 登录验证方式。
        """
        response = self.api_client.get(
            endpoint="/user/login/check",
            response_model=AjaxJsonCheckLoginResult
        )
        self._logger.info(f"[{response.trace_id}]检查登录状态: {response.msg}")
        return response

    def login_captcha(self):
        """获取图形验证码。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。

        Returns:
            AjaxJsonLoginVerifyImgResult: 图形验证码结果。
        """
        response = self.api_client.get(
            endpoint="/user/login/captcha",
            response_model=AjaxJsonLoginVerifyImgResult
        )
        self._logger.info(f"[{response.trace_id}]获取图形验证码: {response.msg}")
        return response
