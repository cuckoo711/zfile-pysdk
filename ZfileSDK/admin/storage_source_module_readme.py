"""
Creation date: 2025/7/12
Creation Time: 05:34
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: storage_source_module_readme.py
Editor: cuckoo
"""

from typing import List

from ..utils.base import ApiClient, BaseClass
from ..utils.models import AjaxJsonListReadmeConfig, AjaxJsonVoid, PasswordConfig


class StorageSourceModuleReadme(BaseClass):
    """存储源模块-README接口，定义了README文档和密码文件夹相关的操作方法。"""
    name = "StorageSourceModuleReadme"

    def __init__(self, api_client: "ApiClient"):
        """初始化存储源模块-README接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    def get_readme_list(self, storage_id: int) -> AjaxJsonListReadmeConfig:
        """获取存储源文档文件夹列表。

        根据存储源 ID 获取存储源设置的文档文件夹列表。

        Args:
            storage_id (int): 存储源 ID。

        Returns:
            AjaxJsonListReadmeConfig: 文档文件夹列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/storage/{storage_id}/readme",
            response_model=AjaxJsonListReadmeConfig
        )
        self._logger.info(f"[{response.trace_id}]获取存储源 {storage_id} 文档文件夹列表: {response.msg}")
        return response

    def save_password_list(self, storage_id: int, password_configs: List[PasswordConfig]) -> AjaxJsonVoid:
        """保存存储源密码文件夹列表。

        保存指定存储源 ID 设置的密码文件夹列表。

        Args:
            storage_id (int): 存储源 ID。
            password_configs (List[PasswordConfig]): 密码文件夹配置列表。

        Returns:
            AjaxJsonVoid: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        # 将密码配置列表转换为字典列表
        password_data = [config.model_dump_json(exclude_none=True, by_alias=True) for config in password_configs]

        response = self.api_client.post(
            endpoint=f"/admin/storage/{storage_id}/readme",
            response_model=AjaxJsonVoid,
            data=password_data
        )
        self._logger.info(f"[{response.trace_id}]保存存储源 {storage_id} 密码文件夹列表: {response.msg}")
        return response
