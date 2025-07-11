"""
Creation date: 2025/7/10
Creation Time: 22:10
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: site_basic_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import AjaxJsonFrontSiteConfigResult, AjaxJsonStorageSourceConfigResult, AjaxJsonString, \
    FileListConfigRequest


class SiteBasicModule(BaseClass):
    """站点基本模块，提供站点的基本信息和配置功能。"""
    name = "SiteBasicModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化站点基本模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=FileListConfigRequest)
    def config_storage(self, *, data: FileListConfigRequest) -> AjaxJsonStorageSourceConfigResult:
        """获取存储源设置。

        Args:
            data (FileListConfigRequest): 包含存储源配置信息的请求数据模型。

        Returns:
            AjaxJsonStorageSourceConfigResult: 包含存储源配置信息的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/api/site/config/storage",
            response_model=AjaxJsonStorageSourceConfigResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取存储源设置: {response.msg}")
        return response

    def config_user_root_path(self, storage_key: str) -> AjaxJsonString:
        """获取用户存储源路径。

        Args:
            storage_key (str): 存储源的唯一标识符。

        Returns:
            AjaxJsonString: 包含用户存储源路径的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/api/site/config/userRootPath/{storage_key}",
            response_model=AjaxJsonString
        )
        self._logger.info(f"[{response.trace_id}]获取用户存储源路径: {response}")
        return response

    def config_global(self) -> AjaxJsonFrontSiteConfigResult:
        """获取站点全局设置。

        Returns:
            AjaxJsonFrontSiteConfigResult: 包含站点全局设置的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/api/site/config/global",
            response_model=AjaxJsonFrontSiteConfigResult
        )
        self._logger.info(f"[{response.trace_id}]获取站点全局设置: {response.msg}")
        return response
