"""
Creation date: 2025/7/10
Creation Time: 21:36
DIR PATH: ZfileSDK/front
Project Name: zfile_sdk
FILE NAME: s3_tools_assistive_module.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonListS3BucketNameResult, AjaxJsonListZFileCORSRule, GetS3BucketListRequest,
                            GetS3CorsListRequest)


class S3ToolsAssistiveModule(BaseClass):
    """S3 工具辅助模块，提供与 S3 相关的操作方法。"""
    name = "S3ToolsAssistiveModule"

    def __init__(self, api_client: "ApiClient"):
        """初始化 S3 工具辅助模块。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=GetS3CorsListRequest)
    def get_cors_config(self, *, data: GetS3CorsListRequest) -> AjaxJsonListZFileCORSRule:
        """获取 S3 CORS 配置。

        Args:
            data (GetS3CorsListRequest): 包含 S3 配置的请求数据模型。

        Returns:
            AjaxJsonListSharepointSiteListResult: 包含 CORS 配置列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/s3/getCorsConfig",
            response_model=AjaxJsonListZFileCORSRule,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 S3 CORS 配置: {response.msg}")
        return response

    @auto_args_from_model(model=GetS3BucketListRequest)
    def get_buckets(self, *, data: GetS3BucketListRequest) -> AjaxJsonListS3BucketNameResult:
        """获取 S3 存储桶列表。

        Args:
            data (GetS3BucketListRequest): 包含 S3 配置的请求数据模型。

        Returns:
            AjaxJsonListSharepointSiteListResult: 包含存储桶列表的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/s3/getBuckets",
            response_model=AjaxJsonListS3BucketNameResult,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]获取 S3 存储桶列表: {response.msg}")
        return response
