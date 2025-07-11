"""
Creation date: 2025/7/12
Creation Time: 05:52
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: login_log_management.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import AjaxJsonListLoginLog, QueryLoginLogRequest


class LoginLogManagement(BaseClass):
    """登录日志管理接口，定义了登录日志相关的操作方法。"""
    name = "LoginLogManagement"

    def __init__(self, api_client: "ApiClient"):
        """初始化登录日志管理接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=QueryLoginLogRequest)
    def list_login_logs(self, *, data: QueryLoginLogRequest) -> AjaxJsonListLoginLog:
        """登录日志列表。

        Args:
            data (QueryLoginLogRequest): 包含查询条件的请求数据模型。

        Returns:
            AjaxJsonListLoginLog: 登录日志列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/login/log/list",
            response_model=AjaxJsonListLoginLog,
            params=data.model_dump(by_alias=True, exclude_none=True)
        )
        self._logger.info(f"[{response.trace_id}]获取登录日志列表: {response.msg}")
        return response
