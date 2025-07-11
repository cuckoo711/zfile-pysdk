"""
Creation date: 2025/7/11
Creation Time: 23:34
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: site_setting_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonString, AjaxJsonSystemConfigDTO, AjaxJsonVoid,
                            UpdateAccessSettingRequest,
                            UpdateLinkSettingRequest,
                            UpdateSecuritySettingRequest,
                            UpdateSiteSettingRequest,
                            UpdateViewSettingRequest,
                            UpdateWebDAVRequest)


class SiteSettingModule(BaseClass):
    """站点设置模块，定义了站点相关的操作方法。"""
    name = "SiteSettingModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化站点设置模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(UpdateWebDAVRequest)
    def config_webdav(self, *, data: UpdateWebDAVRequest) -> AjaxJsonVoid:
        """修改 webdav 设置。

        Args:
            data: 修改 webdav 设置的参数。

        Returns:
            AjaxJsonVoid: 修改 webdav 设置的返回结果。
        """
        response = self.api_client.put(
            endpoint="/admin/config/webdav",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}] 修改 webdav 设置: {response.msg}")
        return response

    @auto_args_from_model(UpdateViewSettingRequest)
    def config_view(self, *, data: UpdateViewSettingRequest) -> AjaxJsonVoid:
        """修改显示设置。

        Args:
            data: 修改显示设置的参数。

        Returns:
            AjaxJsonVoid: 修改显示设置的返回结果。
        """
        response = self.api_client.put(
            endpoint="/admin/config/view",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}] 修改显示设置: {response.msg}")
        return response

    @auto_args_from_model(UpdateSiteSettingRequest)
    def config_site(self, *, data: UpdateSiteSettingRequest) -> AjaxJsonVoid:
        """修改站点设置。

        Args:
            data: 站点设置参数。

        Returns:
            AjaxJsonVoid: 修改站点设置的返回结果。
        """
        response = self.api_client.put(
            endpoint="/admin/config/site",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}] 站点设置: {response.msg}")
        return response

    @auto_args_from_model(UpdateSecuritySettingRequest)
    def config_security(self, *, data: UpdateSecuritySettingRequest) -> AjaxJsonVoid:
        """修改登陆安全设置。

        Args:
            data: 登陆安全设置参数。

        Returns:
            AjaxJsonVoid: 修改登陆安全设置的返回结果。
        """
        response = self.api_client.put(
            endpoint="/admin/config/security",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}] 修改登陆安全设置: {response.msg}")
        return response

    @auto_args_from_model(UpdateLinkSettingRequest)
    def config_link(self, *, data: UpdateLinkSettingRequest) -> AjaxJsonVoid:
        """修改直链设置。

        Args:
            data: 直链设置参数。

        Returns:
            AjaxJsonVoid: 修改直链设置的返回结果。
        """
        response = self.api_client.put(
            endpoint="/admin/config/link",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}] 修改直链设置: {response.msg}")
        return response

    @auto_args_from_model(UpdateAccessSettingRequest)
    def config_access(self, *, data: UpdateAccessSettingRequest) -> AjaxJsonVoid:
        """修改访问控制设置。

        Args:
            data: 访问控制设置参数。

        Returns:
            AjaxJsonVoid: 修改访问控制设置的返回结果。
        """
        response = self.api_client.put(
            endpoint="/admin/config/access",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}] 修改访问控制设置: {response.msg}")
        return response

    def config(self) -> AjaxJsonSystemConfigDTO:
        response = self.api_client.get(
            endpoint="/admin/config",
            response_model=AjaxJsonSystemConfigDTO
        )
        self._logger.info(f"[{response.trace_id}] 获取站点信息: {response.msg}")
        return response

    def config_hardwareCode(self) -> AjaxJsonString:
        response = self.api_client.get(
            endpoint="/admin/config/hardwareCode",
            response_model=AjaxJsonString
        )
        self._logger.info(f"[{response.trace_id}] 获取授权硬件校验码: {response.msg}")
        return response
