"""
Creation date: 2025/7/12
Creation Time: 05:45
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: direct_link_management.py
Editor: assistant
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (
    AdminBatchDeleteRequest,
    AjaxJsonInteger,
    AjaxJsonListCacheInfoStringAtomicInteger,
    AjaxJsonListShortLinkResult,
    AjaxJsonVoid,
    QueryShortLinkLogRequest
)


class DirectLinkManagement(BaseClass):
    """直链管理接口，定义了直链管理相关的操作方法。"""
    name = "DirectLinkManagement"

    def __init__(self, api_client: "ApiClient"):
        """初始化直链管理接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=AdminBatchDeleteRequest)
    def batch_delete(self, *, data: AdminBatchDeleteRequest) -> AjaxJsonVoid:
        """批量删除短链。

        Args:
            data (AdminBatchDeleteRequest): 包含批量删除请求数据的模型。

        Returns:
            AjaxJsonVoid: 批量删除操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/link/delete/batch",
            response_model=AjaxJsonVoid,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]批量删除短链: {response.msg}")
        return response

    @auto_args_from_model(model=QueryShortLinkLogRequest)
    def list_short_links(self, *, data: QueryShortLinkLogRequest) -> AjaxJsonListShortLinkResult:
        """搜索短链。

        Args:
            data (QueryShortLinkLogRequest): 包含查询条件的请求数据模型。

        Returns:
            AjaxJsonListShortLinkResult: 短链列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/link/list",
            response_model=AjaxJsonListShortLinkResult,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]搜索短链: {response.msg}")
        return response

    def get_link_limit_info(self) -> AjaxJsonListCacheInfoStringAtomicInteger:
        """获取直链访问限制信息。

        Returns:
            AjaxJsonListCacheInfoStringAtomicInteger: 直链访问限制信息。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/link/limit/info",
            response_model=AjaxJsonListCacheInfoStringAtomicInteger
        )
        self._logger.info(f"[{response.trace_id}]获取直链访问限制信息: {response.msg}")
        return response

    def delete_expire_link(self) -> AjaxJsonInteger:
        """删除过期短链。

        Returns:
            AjaxJsonInteger: 删除操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint="/admin/link/deleteExpireLink",
            response_model=AjaxJsonInteger
        )
        self._logger.info(f"[{response.trace_id}]删除过期短链: {response.msg}")
        return response

    def delete_by_id(self, link_id: int) -> AjaxJsonVoid:
        """删除短链。

        Args:
            link_id (int): 短链 ID。

        Returns:
            AjaxJsonVoid: 删除操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/link/delete/{link_id}",
            response_model=AjaxJsonVoid
        )
        self._logger.info(f"[{response.trace_id}]删除短链 {link_id}: {response.msg}")
        return response
