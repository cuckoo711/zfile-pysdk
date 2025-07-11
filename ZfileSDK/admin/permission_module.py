"""
Creation date: 2025/7/12
Creation Time: 05:52
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: permission_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass
from ..utils.models import AjaxJsonListPermissionInfoResult


class PermissionModule(BaseClass):
    """权限模块接口，定义了权限相关的操作方法。"""
    name = "PermissionModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化权限模块接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def list_permissions(self) -> AjaxJsonListPermissionInfoResult:
        """获取权限列表。

        Returns:
            AjaxJsonListPermissionInfoResult: 系统权限信息列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/permission/list",
            response_model=AjaxJsonListPermissionInfoResult
        )
        self._logger.info(f"[{response.trace_id}]获取权限列表: {response.msg}")
        return response
