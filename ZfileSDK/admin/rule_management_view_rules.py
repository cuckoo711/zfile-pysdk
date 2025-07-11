"""
Creation date: 2025/7/12
Creation Time: 05:18
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: rule_management_view_rules.py
Editor: cuckoo
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import (AjaxJsonBoolean, AjaxJsonCollectionRuleView, AjaxJsonInteger, AjaxJsonRuleDTORuleViewItem,
                            AjaxJsonRuleViewItem, AjaxJsonUserRuleSettingDTO, CheckRuleDuplicateRequest,
                            QueryRuleRequest, RuleDTORuleViewItem, TestViewRuleRequest, UserRuleSettingDTO)


class RuleManagementViewRules(BaseClass):
    """规则管理-显示规则接口，定义了显示规则相关的操作方法。"""
    name = "RuleManagementViewRules"

    def __init__(self, api_client: "ApiClient"):
        """初始化规则管理-显示规则接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=UserRuleSettingDTO)
    def save_or_update_user_rule(self, *, data: UserRuleSettingDTO) -> AjaxJsonUserRuleSettingDTO:
        """添加或更新用户上传规则。

        Args:
            data (UserRuleSettingDTO): 包含用户规则设置的请求数据模型。

        Returns:
            AjaxJsonUserRuleSettingDTO: 用户规则设置操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/user/rule/saveOrUpdate",
            response_model=AjaxJsonUserRuleSettingDTO,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]添加或更新用户上传规则: {response.msg}")
        return response

    @auto_args_from_model(model=TestViewRuleRequest)
    def test_view_rule(self, *, data: TestViewRuleRequest) -> AjaxJsonRuleViewItem:
        """测试显示规则。

        Args:
            data (TestViewRuleRequest): 包含测试显示规则的请求数据模型。

        Returns:
            AjaxJsonRuleViewItem: 测试结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/rule/view/test",
            response_model=AjaxJsonRuleViewItem,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]测试显示规则: {response.msg}")
        return response

    @auto_args_from_model(model=RuleDTORuleViewItem)
    def save_or_update_view_rule(self, *, data: RuleDTORuleViewItem) -> AjaxJsonRuleDTORuleViewItem:
        """添加或更新显示规则。

        Args:
            data (RuleDTORuleViewItem): 包含显示规则的请求数据模型。

        Returns:
            AjaxJsonRuleDTORuleViewItem: 显示规则操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/rule/view/saveOrUpdate",
            response_model=AjaxJsonRuleDTORuleViewItem,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]添加或更新显示规则: {response.msg}")
        return response

    def get_user_rule_by_id(self, user_id: int) -> AjaxJsonUserRuleSettingDTO:
        """获取用户上传规则信息。

        Args:
            user_id (int): 用户 ID。

        Returns:
            AjaxJsonUserRuleSettingDTO: 用户上传规则信息。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/user/rule/{user_id}",
            response_model=AjaxJsonUserRuleSettingDTO
        )
        self._logger.info(f"[{response.trace_id}]获取用户上传规则信息 {user_id}: {response.msg}")
        return response

    def get_view_rule_by_id(self, rule_id: int) -> AjaxJsonRuleDTORuleViewItem:
        """获取显示规则信息。

        Args:
            rule_id (int): 规则 ID。

        Returns:
            AjaxJsonRuleDTORuleViewItem: 显示规则信息。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint=f"/admin/rule/view/{rule_id}",
            response_model=AjaxJsonRuleDTORuleViewItem
        )
        self._logger.info(f"[{response.trace_id}]获取显示规则信息 {rule_id}: {response.msg}")
        return response

    @auto_args_from_model(model=QueryRuleRequest)
    def list_view_rules(self, *, data: QueryRuleRequest) -> AjaxJsonCollectionRuleView:
        """获取显示规则列表。

        Args:
            data (QueryRuleRequest): 包含查询条件的请求数据模型。

        Returns:
            AjaxJsonCollectionRuleView: 显示规则列表。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/rule/view/list",
            response_model=AjaxJsonCollectionRuleView,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]获取显示规则列表: {response.msg}")
        return response

    @auto_args_from_model(model=CheckRuleDuplicateRequest)
    def check_rule_duplicate(self, *, data: CheckRuleDuplicateRequest) -> AjaxJsonBoolean:
        """检查规则名称是否重复。

        Args:
            data (CheckRuleDuplicateRequest): 包含检查重复信息的请求数据模型。

        Returns:
            AjaxJsonBoolean: 检查结果，True 表示重复。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.get(
            endpoint="/admin/rule/view/checkDuplicate",
            response_model=AjaxJsonBoolean,
            params=data.to_dict()
        )
        self._logger.info(f"[{response.trace_id}]检查规则名称重复: {response.msg}")
        return response

    def delete_user_rule(self, user_id: int) -> AjaxJsonInteger:
        """删除用户上传规则。

        Args:
            user_id (int): 用户 ID。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/user/rule/delete/{user_id}",
            response_model=AjaxJsonInteger
        )
        self._logger.info(f"[{response.trace_id}]删除用户上传规则 {user_id}: {response.msg}")
        return response

    def delete_view_rule(self, rule_id: int) -> AjaxJsonInteger:
        """删除显示规则。

        Args:
            rule_id (int): 规则 ID。

        Returns:
            AjaxJsonInteger: 操作结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.delete(
            endpoint=f"/admin/rule/view/delete/{rule_id}",
            response_model=AjaxJsonInteger
        )
        self._logger.info(f"[{response.trace_id}]删除显示规则 {rule_id}: {response.msg}")
        return response
