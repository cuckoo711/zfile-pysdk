"""
Creation date: 2025/7/12
Creation Time: 05:47
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: direct_link_log_management.py
Editor: assistant
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AdminBatchDeleteRequest, AjaxJsonListDownloadTopFileDTO, AjaxJsonListDownloadTopIpDTO,
                            AjaxJsonListDownloadTopRefererDTO, AjaxJsonStreamDownloadLogResult, AjaxJsonVoid,
                            DownloadTopInfoRequest, QueryDownloadLogRequest)


class DirectLinkLogManagement(BaseClass):
    """直链日志管理接口，定义了直链日志管理相关的操作方法。"""
    name = "DirectLinkLogManagement"

    def __init__(self, api_client: "ApiClient"):
        """初始化直链日志管理接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=AdminBatchDeleteRequest)
    def batch_delete(self, *, data: AdminBatchDeleteRequest) -> AjaxJsonVoid:
        """批量删除直链。

        Args:
            data (AdminBatchDeleteRequest): 包含批量删除请求数据的模型。

        Returns:
            AjaxJsonVoid: 批量删除操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/download/log/delete/batch",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]批量删除直链: {response.msg}")
        return response

    @auto_args_from_model(model=QueryDownloadLogRequest)
    def batch_delete_by_search_params(self, *, data: QueryDownloadLogRequest) -> AjaxJsonVoid:
        """根据查询条件批量删除直链。

        Args:
            data (QueryDownloadLogRequest): 包含查询条件的请求数据模型。

        Returns:
            AjaxJsonVoid: 批量删除操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/download/log/delete/batch/query",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]根据查询条件批量删除直链: {response.msg}")
        return response

    @auto_args_from_model(model=DownloadTopInfoRequest)
    def download_top_referer(self, *, data: DownloadTopInfoRequest) -> AjaxJsonListDownloadTopRefererDTO:
        """指定时间段内，下载次数最多的前 N 个 Referer。

        Args:
            data (DownloadTopInfoRequest): 包含下载排行信息的请求数据模型。

        Returns:
            AjaxJsonListDownloadTopRefererDTO: 下载来源排行列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/download/log/top/referer",
            response_model=AjaxJsonListDownloadTopRefererDTO,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]获取下载次数最多的前 N 个 Referer: {response.msg}")
        return response

    @auto_args_from_model(model=DownloadTopInfoRequest)
    def download_top_ip(self, *, data: DownloadTopInfoRequest) -> AjaxJsonListDownloadTopIpDTO:
        """指定时间段内，下载次数最多的前 N 个IP。

        Args:
            data (DownloadTopInfoRequest): 包含下载排行信息的请求数据模型。

        Returns:
            AjaxJsonListDownloadTopIpDTO: 下载IP排行列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/download/log/top/ip",
            response_model=AjaxJsonListDownloadTopIpDTO,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]获取下载次数最多的前 N 个IP: {response.msg}")
        return response

    @auto_args_from_model(model=DownloadTopInfoRequest)
    def download_top_file(self, *, data: DownloadTopInfoRequest) -> AjaxJsonListDownloadTopFileDTO:
        """指定时间段内，下载次数最多的前 N 个文件。

        Args:
            data (DownloadTopInfoRequest): 包含下载排行信息的请求数据模型。

        Returns:
            AjaxJsonListDownloadTopFileDTO: 下载文件排行列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/download/log/top/file",
            response_model=AjaxJsonListDownloadTopFileDTO,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]获取下载次数最多的前 N 个文件: {response.msg}")
        return response

    @auto_args_from_model(model=QueryDownloadLogRequest)
    def list_download_logs(self, *, data: QueryDownloadLogRequest) -> AjaxJsonStreamDownloadLogResult:
        """直链下载日志。

        Args:
            data (QueryDownloadLogRequest): 包含查询条件的请求数据模型。

        Returns:
            AjaxJsonStreamDownloadLogResult: 下载日志列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/download/log/list",
            response_model=AjaxJsonStreamDownloadLogResult,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]获取直链下载日志: {response.msg}")
        return response

    def delete_by_id(self, log_id: int) -> AjaxJsonVoid:
        """删除直链。

        Args:
            log_id (int): 直链 ID。

        Returns:
            AjaxJsonVoid: 删除操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/download/log/delete/{log_id}",
            response_model=AjaxJsonVoid
        )
        self._logger.info(f"[{response.trace_id}]删除直链 {log_id}: {response.msg}")
        return response
