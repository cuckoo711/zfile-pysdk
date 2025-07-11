"""
Creation date: 2025/7/12
Creation Time: 05:48
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: storage_source_module_metadata.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass
from ..utils.models import (AjaxJsonListStorageSourceParamDef, AjaxJsonListStorageTypeEnum, StorageTypeEnum)


class StorageSourceModuleMetadata(BaseClass):
    """存储源模块-元数据接口，定义了存储源元数据相关的操作方法。"""
    name = "StorageSourceModuleMetadata"

    def __init__(self, api_client: "ApiClient"):
        """初始化存储源模块-元数据接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def support_storage(self) -> AjaxJsonListStorageTypeEnum:
        """获取支持的存储源类型。

        Returns:
            AjaxJsonListStorageTypeEnum: 系统支持的存储源类型列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/support-storage",
            response_model=AjaxJsonListStorageTypeEnum
        )
        self._logger.info(f"[{response.trace_id}]获取支持的存储源类型: {response.msg}")
        return response

    def get_form_by_storage_type(self, storage_type: StorageTypeEnum) -> AjaxJsonListStorageSourceParamDef:
        """获取指定存储源类型的所有参数信息。

        Args:
            storage_type (StorageTypeEnum): 存储源类型，如 LOCAL、ALIYUN、WEBDAV 等。

        Returns:
            AjaxJsonListStorageSourceParamDef: 指定存储源类型的参数定义列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        params = {"storageType": storage_type.value}
        response = self.api_client.get(
            endpoint="/admin/storage-params",
            response_model=AjaxJsonListStorageSourceParamDef,
            params=params
        )
        self._logger.info(f"[{response.trace_id}]获取存储源类型 {storage_type.value} 的参数信息: {response.msg}")
        return response
