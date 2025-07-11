"""
Creation date: 2025/7/10
Creation Time: 20:33
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: sharepoint_tools_assistive_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonListSharepointSiteListResult, AjaxJsonListSharepointSiteResult,
                            AjaxJsonString, SharePointInfoRequest, SharePointSearchSitesRequest,
                            SharePointSiteListsRequest)


class SharePointToolsAssistiveModule(BaseClass):
    """SharePoint 工具辅助模块，提供与 SharePoint 相关的操作方法。"""
    name = "SharePointToolsAssistiveModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化 SharePoint 工具辅助模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=SharePointSearchSitesRequest)
    def get_sites(self, *, data: SharePointSearchSitesRequest) -> AjaxJsonListSharepointSiteResult:
        """获取 SharePoint 网站列表。

        Args:
            data (SharePointSearchSitesRequest): 包含搜索参数的请求数据模型。

        Returns:
            AjaxJsonListSharepointSiteResult: 包含网站列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/sharepoint/getSites",
            response_model=AjaxJsonListSharepointSiteResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 SharePoint 网站列表: {response.msg}")
        return response

    @auto_args_from_model(model=SharePointSiteListsRequest)
    def get_site_lists(self, *, data: SharePointSiteListsRequest) -> AjaxJsonListSharepointSiteListResult:
        """获取指定 SharePoint 网站下的子目录列表。

        Args:
            data (SharePointSiteListsRequest): 包含网站信息的请求数据模型。

        Returns:
            AjaxJsonListSharepointSiteListResult: 包含子目录列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/sharepoint/getSiteLists",
            response_model=AjaxJsonListSharepointSiteListResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 SharePoint 网站下的子目录: {response.msg}")
        return response

    @auto_args_from_model(model=SharePointInfoRequest)
    def get_site_id(self, *, data: SharePointInfoRequest) -> AjaxJsonString:
        """获取 SharePoint 网站的 SiteId。

        Args:
            data (SharePointInfoRequest): 包含网站信息的请求数据模型。

        Returns:
            AjaxJsonString: 包含 SiteId 的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/sharepoint/getSiteId",
            response_model=AjaxJsonString,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 SharePoint 网站 SiteId : {response.msg}")
        return response

    @auto_args_from_model(model=SharePointInfoRequest)
    def get_domain_prefix(self, *, data: SharePointInfoRequest) -> AjaxJsonString:
        """获取 SharePoint 网站的域名前缀。

        Args:
            data (SharePointInfoRequest): 包含网站信息的请求数据模型。

        Returns:
            AjaxJsonString: 包含域名前缀的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/sharepoint/getDomainPrefix",
            response_model=AjaxJsonString,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 SharePoint 网站域名前缀: {response.msg}")
        return response
