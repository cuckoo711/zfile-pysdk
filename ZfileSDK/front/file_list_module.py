"""
Creation date: 2025/7/10
Creation Time: 21:56
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: file_list_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonFileInfoResult, AjaxJsonFileItemResult, AjaxJsonListFileItemResult,
                            AjaxJsonListStorageSourceResult, FileItemRequest, FileListRequest,
                            SearchStorageRequest)


class FileListModule(BaseClass):
    """文件列表模块，提供获取文件列表的功能。"""
    name = "FileListModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化文件列表模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=SearchStorageRequest)
    def storage_search(self, *, data: SearchStorageRequest) -> AjaxJsonListFileItemResult:
        """搜索存储中的文件。

        Args:
            data (SearchStorageRequest): 包含搜索参数的请求数据模型。

        Returns:
            AjaxJsonListFileItemResult: 包含搜索结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/storage/search",
            response_model=AjaxJsonListFileItemResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]搜索存储中的文件: {response.msg}")
        return response

    @auto_args_from_model(model=FileListRequest)
    def storage_files(self, *, data: FileListRequest) -> AjaxJsonFileInfoResult:
        """获取存储中的文件列表。

        Args:
            data (FileListRequest): 包含存储参数的请求数据模型。

        Returns:
            AjaxJsonFileInfoResult: 包含文件列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/storage/files",
            response_model=AjaxJsonFileInfoResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取存储中的文件列表: {response.msg}")
        return response

    @auto_args_from_model(model=FileItemRequest)
    def storage_files_item(self, *, data: FileItemRequest) -> AjaxJsonFileItemResult:
        """获取存储中的单个文件信息。

        Args:
            data (FileItemRequest): 包含文件参数的请求数据模型。

        Returns:
            AjaxJsonFileItemResult: 包含单个文件信息的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/storage/file/item",
            response_model=AjaxJsonFileItemResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取存储中的单个文件信息: {response.msg}")
        return response

    def storage_list(self) -> AjaxJsonListStorageSourceResult:
        """获取存储列表。

        Returns:
            AjaxJsonListStorageSourceResult: 包含存储列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/api/storage/list",
            response_model=AjaxJsonListStorageSourceResult
        )
        self._logger.info(f"[{response.trace_id}]获取存储列表: {response.msg}")
        return response
