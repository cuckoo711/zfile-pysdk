"""
Creation date: 2025/7/12
Creation Time: 05:25
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: storage_source_module_basic.py
Editor: cuckoo
"""

from typing import List

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonBoolean, AjaxJsonInteger, AjaxJsonListStorageSourceAdminResult,
                            AjaxJsonStorageSourceDTO, AjaxJsonVoid, CopyStorageSourceRequest, SaveStorageSourceRequest,
                            UpdateStorageSortRequest)


class StorageSourceModuleBasic(BaseClass):
    """存储源模块-基础接口，定义了存储源管理相关的操作方法。"""
    name = "StorageSourceModuleBasic"

    def __init__(self, api_client: "ApiClient"):
        """初始化存储源模块-基础接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=SaveStorageSourceRequest)
    def save_storage_item(self, *, data: SaveStorageSourceRequest) -> AjaxJsonInteger:
        """保存存储源参数。

        Args:
            data (SaveStorageSourceRequest): 包含存储源参数的请求数据模型。

        Returns:
            AjaxJsonInteger: 保存操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/storage",
            response_model=AjaxJsonInteger,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]保存存储源参数: {response.msg}")
        return response

    def enable(self, storage_id: int) -> AjaxJsonVoid:
        """启用存储源。

        Args:
            storage_id (int): 存储源 ID。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint=f"/admin/storage/{storage_id}/enable",
            response_model=AjaxJsonVoid
        )
        self._logger.info(f"[{response.trace_id}]启用存储源 {storage_id}: {response.msg}")
        return response

    def disable(self, storage_id: int) -> AjaxJsonVoid:
        """停止存储源。

        Args:
            storage_id (int): 存储源 ID。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint=f"/admin/storage/{storage_id}/disable",
            response_model=AjaxJsonVoid
        )
        self._logger.info(f"[{response.trace_id}]停止存储源 {storage_id}: {response.msg}")
        return response

    def change_compatibility_readme(self, storage_id: int, status: bool) -> AjaxJsonVoid:
        """修改 readme 兼容模式。

        Args:
            storage_id (int): 存储源 ID。
            status (bool): 存储源兼容模式状态。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint=f"/admin/storage/{storage_id}/compatibility_readme/{status}",
            response_model=AjaxJsonVoid
        )
        self._logger.info(f"[{response.trace_id}]修改存储源 {storage_id} readme 兼容模式为 {status}: {response.msg}")
        return response

    def update_storage_sort(self, data: List[UpdateStorageSortRequest]) -> AjaxJsonVoid:
        """更新存储源顺序。

        Args:
            data (List[UpdateStorageSortRequest]): 包含存储源排序信息的请求数据列表。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        # 将列表转换为字典列表
        sort_data = [item.model_dump_json(exclude_none=True, by_alias=True) for item in data]

        response = self.api_client.post(
            endpoint="/admin/storage/sort",
            response_model=AjaxJsonVoid,
            data=sort_data
        )
        self._logger.info(f"[{response.trace_id}]更新存储源顺序: {response.msg}")
        return response

    @auto_args_from_model(model=CopyStorageSourceRequest)
    def copy_storage(self, *, data: CopyStorageSourceRequest) -> AjaxJsonInteger:
        """复制存储源。

        Args:
            data (CopyStorageSourceRequest): 包含复制存储源信息的请求数据模型。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/storage/copy",
            response_model=AjaxJsonInteger,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]复制存储源配置: {response.msg}")
        return response

    def storage_list(self) -> AjaxJsonListStorageSourceAdminResult:
        """获取所有存储源列表。

        Returns:
            AjaxJsonListStorageSourceAdminResult: 存储源列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/storages",
            response_model=AjaxJsonListStorageSourceAdminResult
        )
        self._logger.info(f"[{response.trace_id}]获取所有存储源列表: {response.msg}")
        return response

    def storage_item(self, storage_id: int) -> AjaxJsonStorageSourceDTO:
        """获取指定存储源参数。

        Args:
            storage_id (int): 存储源 ID。

        Returns:
            AjaxJsonStorageSourceDTO: 存储源详情信息。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/storage/{storage_id}",
            response_model=AjaxJsonStorageSourceDTO
        )
        self._logger.info(f"[{response.trace_id}]获取存储源信息 {storage_id}: {response.msg}")
        return response

    def delete_storage(self, storage_id: int) -> AjaxJsonVoid:
        """删除存储源。

        Args:
            storage_id (int): 存储源 ID。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/storage/{storage_id}",
            response_model=AjaxJsonVoid
        )
        self._logger.info(f"[{response.trace_id}]删除存储源 {storage_id}: {response.msg}")
        return response

    def exist_key(self, storage_key: str) -> AjaxJsonBoolean:
        """校验存储源 key 是否重复。

        Args:
            storage_key (str): 存储源 key。

        Returns:
            AjaxJsonBoolean: 校验结果，True 表示重复。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/storage/exist/key",
            response_model=AjaxJsonBoolean,
            params={"storageKey": storage_key}
        )
        self._logger.info(f"[{response.trace_id}]校验存储源key重复 {storage_key}: {response.msg}")
        return response
