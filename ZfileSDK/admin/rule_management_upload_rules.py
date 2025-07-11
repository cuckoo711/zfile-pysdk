"""
Creation date: 2025/7/12
Creation Time: 05:40
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: rule_management_upload_rules.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonBoolean, AjaxJsonCollectionRuleUpload, AjaxJsonInteger,
                            AjaxJsonRuleDTORuleUploadItem,
                            AjaxJsonRuleUploadItem, CheckRuleDuplicateRequest, QueryRuleRequest, RuleDTORuleUploadItem,
                            TestUploadRuleRequest)


class RuleManagementUploadRules(BaseClass):
    """规则管理-上传规则接口，定义了上传规则相关的操作方法。"""
    name = "RuleManagementUploadRules"

    def __init__(self, api_client: "ApiClient"):
        """初始化规则管理-上传规则接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=TestUploadRuleRequest)
    def test_upload_rule(self, *, data: TestUploadRuleRequest) -> AjaxJsonRuleUploadItem:
        """测试上传规则。

        测试指定的上传规则配置是否正确。

        Args:
            data (TestUploadRuleRequest): 包含测试上传规则的请求数据模型。

        Returns:
            AjaxJsonRuleUploadItem: 测试结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/rule/upload/test",
            response_model=AjaxJsonRuleUploadItem,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]测试上传规则: {response.msg}")
        return response

    @auto_args_from_model(model=RuleDTORuleUploadItem)
    def save_or_update_upload_rule(self, *, data: RuleDTORuleUploadItem) -> AjaxJsonRuleDTORuleUploadItem:
        """添加或更新上传规则。

        Args:
            data (RuleDTORuleUploadItem): 包含上传规则的请求数据模型。

        Returns:
            AjaxJsonRuleDTORuleUploadItem: 上传规则操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/rule/upload/saveOrUpdate",
            response_model=AjaxJsonRuleDTORuleUploadItem,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]添加或更新上传规则: {response.msg}")
        return response

    def get_upload_rule_by_id(self, rule_id: int) -> AjaxJsonRuleDTORuleUploadItem:
        """获取上传规则信息。

        根据规则 ID 获取上传规则的详细信息。

        Args:
            rule_id (int): 规则 ID。

        Returns:
            AjaxJsonRuleDTORuleUploadItem: 上传规则信息。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/rule/upload/{rule_id}",
            response_model=AjaxJsonRuleDTORuleUploadItem
        )
        self._logger.info(f"[{response.trace_id}]获取上传规则信息 {rule_id}: {response.msg}")
        return response

    @auto_args_from_model(model=QueryRuleRequest)
    def list_upload_rules(self, *, data: QueryRuleRequest) -> AjaxJsonCollectionRuleUpload:
        """获取上传规则列表。

        根据查询条件获取上传规则列表。

        Args:
            data (QueryRuleRequest): 包含查询条件的请求数据模型。

        Returns:
            AjaxJsonCollectionRuleUpload: 上传规则列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/rule/upload/list",
            response_model=AjaxJsonCollectionRuleUpload,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]获取上传规则列表: {response.msg}")
        return response

    @auto_args_from_model(model=CheckRuleDuplicateRequest)
    def check_rule_duplicate(self, *, data: CheckRuleDuplicateRequest) -> AjaxJsonBoolean:
        """检查规则名称是否重复。

        检查指定的规则名称是否已经存在。

        Args:
            data (CheckRuleDuplicateRequest): 包含检查重复信息的请求数据模型。

        Returns:
            AjaxJsonBoolean: 检查结果，True 表示重复。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/rule/upload/checkDuplicate",
            response_model=AjaxJsonBoolean,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]检查上传规则名称重复: {response.msg}")
        return response

    def delete_upload_rule(self, rule_id: int) -> AjaxJsonInteger:
        """删除上传规则。

        根据规则 ID 删除指定的上传规则。

        Args:
            rule_id (int): 规则 ID。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/rule/upload/delete/{rule_id}",
            response_model=AjaxJsonInteger
        )
        self._logger.info(f"[{response.trace_id}]删除上传规则 {rule_id}: {response.msg}")
        return response
