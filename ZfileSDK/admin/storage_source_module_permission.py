"""
Creation date: 2025/7/12
Creation Time: 05:51
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: storage_source_module_permission.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass
from ..utils.models import AjaxJsonListPermissionConfigResult


class StorageSourceModulePermission(BaseClass):
    """存储源模块-权限控制接口，定义了存储源权限控制相关的操作方法。"""
    name = "StorageSourceModulePermission"

    def __init__(self, api_client: "ApiClient"):
        """初始化存储源模块-权限控制接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def get_permission_list(self, storage_id: int) -> AjaxJsonListPermissionConfigResult:
        """获取存储源权限列表。

        Args:
            storage_id (int): 存储源 ID。

        Returns:
            AjaxJsonListPermissionConfigResult: 存储源权限配置列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/storage/{storage_id}/permission",
            response_model=AjaxJsonListPermissionConfigResult
        )
        self._logger.info(f"[{response.trace_id}]获取存储源 {storage_id} 权限列表: {response.msg}")
        return response
