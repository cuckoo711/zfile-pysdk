"""
Creation date: 2025/7/12
Creation Time: 05:35
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: single_sign_on_management.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonBoolean, AjaxJsonCollectionSsoConfig, AjaxJsonSsoConfig, AjaxJsonVoid,
                            CheckProviderDuplicateRequest, SsoConfig)


class SingleSignOnManagement(BaseClass):
    """单点登录管理接口，定义了SSO服务商管理相关的操作方法。"""
    name = "SingleSignOnManagement"

    def __init__(self, api_client: "ApiClient"):
        """初始化单点登录管理接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=SsoConfig)
    def save_or_update_provider(self, *, data: SsoConfig) -> AjaxJsonSsoConfig:
        """保存SSO服务商。

        添加或更新SSO服务商配置信息。

        Args:
            data (SsoConfig): 包含SSO服务商配置信息的请求数据模型。

        Returns:
            AjaxJsonSsoConfig: 保存操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/sso/provider",
            response_model=AjaxJsonSsoConfig,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]保存SSO服务商: {response.msg}")
        return response

    def list_providers(self) -> AjaxJsonCollectionSsoConfig:
        """获取SSO服务商列表。

        获取所有已配置的SSO服务商列表。

        Returns:
            AjaxJsonCollectionSsoConfig: SSO服务商列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/sso/providers",
            response_model=AjaxJsonCollectionSsoConfig
        )
        self._logger.info(f"[{response.trace_id}]获取SSO服务商列表: {response.msg}")
        return response

    @auto_args_from_model(model=CheckProviderDuplicateRequest)
    def check_duplicate(self, *, data: CheckProviderDuplicateRequest) -> AjaxJsonBoolean:
        """检查服务商简称是否重复。

        检查指定的服务商简称是否已经存在。

        Args:
            data (CheckProviderDuplicateRequest): 包含检查重复信息的请求数据模型。

        Returns:
            AjaxJsonBoolean: 检查结果，True 表示重复。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/sso/provider/checkDuplicate",
            response_model=AjaxJsonBoolean,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]检查服务商简称重复: {response.msg}")
        return response

    def delete_provider(self, provider: str) -> AjaxJsonVoid:
        """删除SSO服务商。

        根据服务商简称删除指定的SSO服务商配置。

        Args:
            provider (str): 服务商简称。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/sso/provider/{provider}",
            response_model=AjaxJsonVoid
        )
        self._logger.info(f"[{response.trace_id}]删除SSO服务商 {provider}: {response.msg}")
        return response
