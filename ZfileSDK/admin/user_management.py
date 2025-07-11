"""
Creation date: 2025/7/12
Creation Time: 05:08
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: user_management.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonBoolean, AjaxJsonCollectionUserDetailResponse, AjaxJsonInteger, AjaxJsonUser,
                            AjaxJsonUserDetailResponse, CheckUserDuplicateRequest, CopyUserRequest, QueryUserRequest,
                            SaveUserRequest)


class UserManagement(BaseClass):
    """用户管理接口，定义了用户管理相关的操作方法。"""
    name = "UserManagement"

    def __init__(self, api_client: "ApiClient"):
        """初始化用户管理接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=SaveUserRequest)
    def save_or_update(self, *, data: SaveUserRequest) -> AjaxJsonUser:
        """添加或更新用户。

        Args:
            data (SaveUserRequest): 包含用户信息的请求数据模型。

        Returns:
            AjaxJsonUser: 用户操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/user/saveOrUpdate",
            response_model=AjaxJsonUser,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]添加或更新用户: {response.msg}")
        return response

    def enable(self, user_id: int) -> AjaxJsonInteger:
        """启用用户。

        Args:
            user_id (int): 用户 ID。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint=f"/admin/user/enable/{user_id}",
            response_model=AjaxJsonInteger
        )
        self._logger.info(f"[{response.trace_id}]启用用户 {user_id}: {response.msg}")
        return response

    def disable(self, user_id: int) -> AjaxJsonInteger:
        """禁用用户。

        Args:
            user_id (int): 用户 ID。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint=f"/admin/user/disable/{user_id}",
            response_model=AjaxJsonInteger
        )
        self._logger.info(f"[{response.trace_id}]禁用用户 {user_id}: {response.msg}")
        return response

    @auto_args_from_model(model=CopyUserRequest)
    def copy_user(self, *, data: CopyUserRequest) -> AjaxJsonInteger:
        """复制用户配置。

        Args:
            data (CopyUserRequest): 包含复制用户信息的请求数据模型。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/user/copy",
            response_model=AjaxJsonInteger,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]复制用户配置: {response.msg}")
        return response

    def get_user(self, user_id: int) -> AjaxJsonUserDetailResponse:
        """获取用户信息。

        Args:
            user_id (int): 用户 ID。

        Returns:
            AjaxJsonUserDetailResponse: 用户详情信息。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/user/{user_id}",
            response_model=AjaxJsonUserDetailResponse
        )
        self._logger.info(f"[{response.trace_id}]获取用户信息 {user_id}: {response.msg}")
        return response

    @auto_args_from_model(model=QueryUserRequest)
    def list_users(self, *, data: QueryUserRequest) -> AjaxJsonCollectionUserDetailResponse:
        """获取用户列表。

        Args:
            data (QueryUserRequest): 包含查询条件的请求数据模型。

        Returns:
            AjaxJsonCollectionUserDetailResponse: 用户列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/user/list",
            response_model=AjaxJsonCollectionUserDetailResponse,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]获取用户列表: {response.msg}")
        return response

    @auto_args_from_model(model=CheckUserDuplicateRequest)
    def check_duplicate(self, *, data: CheckUserDuplicateRequest) -> AjaxJsonBoolean:
        """检查用户名是否重复。

        Args:
            data (CheckUserDuplicateRequest): 包含检查重复信息的请求数据模型。

        Returns:
            AjaxJsonBoolean: 检查结果，True 表示重复。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/user/checkDuplicate",
            response_model=AjaxJsonBoolean,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]检查用户名重复: {response.msg}")
        return response

    def delete_user(self, user_id: int) -> AjaxJsonInteger:
        """删除用户。

        Args:
            user_id (int): 用户 ID。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/user/delete/{user_id}",
            response_model=AjaxJsonInteger
        )
        self._logger.info(f"[{response.trace_id}]删除用户 {user_id}: {response.msg}")
        return response
