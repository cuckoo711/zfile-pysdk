"""
Creation date: 2025/7/12
Creation Time: 05:36
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: storage_source_module_filter_file.py
Editor: cuckoo
"""

from typing import List

from ..utils.base import ApiClient, BaseClass
from ..utils.models import AjaxJsonListFilterConfig, AjaxJsonVoid, FilterConfig


class StorageSourceModuleFilterFile(BaseClass):
    """存储源模块-过滤文件接口，定义了过滤文件管理相关的操作方法。"""
    name = "StorageSourceModuleFilterFile"

    def __init__(self, api_client: "ApiClient"):
        """初始化存储源模块-过滤文件接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def get_filters(self, storage_id: int) -> AjaxJsonListFilterConfig:
        """获取存储源过滤文件列表。

        根据存储源 ID 获取存储源设置的过滤文件列表。

        Args:
            storage_id (int): 存储源 ID。

        Returns:
            AjaxJsonListFilterConfig: 过滤文件列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/storage/{storage_id}/filters",
            response_model=AjaxJsonListFilterConfig
        )
        self._logger.info(f"[{response.trace_id}]获取存储源 {storage_id} 过滤文件列表: {response.msg}")
        return response

    def save_filters(self, storage_id: int, filters: List[FilterConfig]) -> AjaxJsonVoid:
        """保存存储源过滤文件列表。

        保存指定存储源 ID 设置的过滤文件列表。

        Args:
            storage_id (int): 存储源 ID。
            filters (List[FilterConfig]): 过滤文件配置列表。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        # 将过滤配置列表转换为字典列表
        filter_data = [filter_item.model_dump(exclude_none=True, by_alias=True) for filter_item in filters]

        response = self.api_client.post(
            endpoint=f"/admin/storage/{storage_id}/filters",
            response_model=AjaxJsonVoid,
            data=filter_data
        )
        self._logger.info(f"[{response.trace_id}]保存存储源 {storage_id} 过滤文件列表: {response.msg}")
        return response
