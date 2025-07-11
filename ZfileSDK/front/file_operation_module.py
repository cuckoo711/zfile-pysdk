"""
Creation date: 2025/7/10
Creation Time: 22:30
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: file_operation_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonListBatchOperatorResult, AjaxJsonString, AjaxJsonVoid, BatchMoveOrCopyFileRequest,
                            FrontBatchDeleteRequest, NewFolderRequest, RenameFileRequest, RenameFolderRequest,
                            UploadFileRequest)


class FileOperationModule(BaseClass):
    """文件操作模块，提供文件的上传、下载、删除等操作。"""
    name = "FileOperationModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化文件操作模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=BatchMoveOrCopyFileRequest)
    def action_type(self, *, action: str, _type: str,
                    data: BatchMoveOrCopyFileRequest) -> AjaxJsonListBatchOperatorResult:
        """移动或复制文件或文件夹。

        Args:
            action (str): 操作类型，"move" 或 "copy"。
            _type (str): 文件类型，"file" 或 "folder"。
            data (BatchMoveOrCopyFileRequest): 包含批量操作请求数据的模型。

        Returns:
            AjaxJsonListBatchOperatorResult: 包含操作结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        if action not in ["move", "copy"]:
            raise ValueError("Action must be 'move' or 'copy'.")
        if _type not in ["file", "folder"]:
            raise ValueError("Type must be 'file' or 'folder'.")

        response = self.api_client.post(
            endpoint=f"/api/file/operator/{action}/{_type}",
            response_model=AjaxJsonListBatchOperatorResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]执行文件操作({action} {_type}): {response.msg}")
        return response

    @auto_args_from_model(model=UploadFileRequest)
    def upload_file(self, *, data: UploadFileRequest) -> AjaxJsonString:
        """上传文件。

        Args:
            data (UploadFileRequest): 包含上传文件请求数据的模型。

        Returns:
            AjaxJsonString: 包含上传结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/file/operator/upload/file",
            response_model=AjaxJsonString,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]上传文件: {response.msg}")
        return response

    @auto_args_from_model(model=RenameFolderRequest)
    def rename_folder(self, *, data: RenameFolderRequest) -> AjaxJsonVoid:
        """重命名文件夹。

        Args:
            data (RenameFolderRequest): 包含重命名请求数据的模型。

        Returns:
            AjaxJsonVoid: 包含操作结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/file/operator/rename/folder",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]重命名文件夹: {response.msg}")
        return response

    @auto_args_from_model(model=RenameFileRequest)
    def rename_file(self, *, data: RenameFileRequest) -> AjaxJsonVoid:
        """重命名文件。

        Args:
            data (RenameFileRequest): 包含重命名请求数据的模型。

        Returns:
            AjaxJsonVoid: 包含操作结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/file/operator/rename/file",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]重命名文件: {response.msg}")
        return response

    @auto_args_from_model(model=NewFolderRequest)
    def mkdir(self, *, data: NewFolderRequest) -> AjaxJsonVoid:
        """创建文件夹。

        Args:
            data (NewFolderRequest): 包含创建文件夹请求数据的模型。

        Returns:
            AjaxJsonVoid: 包含操作结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/file/operator/mkdir",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]创建文件夹: {response.msg}")
        return response

    @auto_args_from_model(model=FrontBatchDeleteRequest)
    def delete_batch(self, *, data: FrontBatchDeleteRequest) -> AjaxJsonListBatchOperatorResult:
        """批量删除文件或文件夹。

        Args:
            data (FrontBatchDeleteRequest): 包含批量删除请求数据的模型。

        Returns:
            AjaxJsonListBatchOperatorResult: 包含操作结果的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/file/operator/delete/batch",
            response_model=AjaxJsonListBatchOperatorResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]批量删除文件/文件夹: {response.msg}")
        return response
