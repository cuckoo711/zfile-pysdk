"""
Creation date: 2025/7/12
Creation Time: 05:52
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: ip_address_helper.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass
from ..utils.models import AjaxJsonString


class IpAddressHelper(BaseClass):
    """IP 地址辅助 Controller，定义了 IP 地址相关的操作方法。"""
    name = "IpAddressHelper"

    def __init__(self, api_client: "ApiClient"):
        """初始化 IP 地址辅助 Controller。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def client_ip(self) -> AjaxJsonString:
        """获取客户端 IP 地址。

        Returns:
            AjaxJsonString: 包含客户端 IP 地址的响应对象。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/clientIp",
            response_model=AjaxJsonString
        )
        self._logger.info(f"[{response.trace_id}]获取客户端 IP 地址: {response.msg}")
        return response
