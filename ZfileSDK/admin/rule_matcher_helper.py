"""
Creation date: 2025/7/12
Creation Time: 05:43
DIR PATH: ZfileSDK/admin
Project Name: zfile_sdk
FILE NAME: rule_matcher_helper.py
Editor: assistant
"""

from ..utils.base import ApiClient, BaseClass, auto_args_from_model
from ..utils.models import AjaxJsonString, TestRuleMatcherRequest


class RuleMatcherHelper(BaseClass):
    """规则匹配辅助 Controller，定义了规则匹配测试相关的操作方法。"""
    name = "RuleMatcherHelper"

    def __init__(self, api_client: "ApiClient"):
        """初始化规则匹配辅助 Controller。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        super().__init__(api_client, name=self.name)

    @auto_args_from_model(model=TestRuleMatcherRequest)
    def test_rule(self, *, data: TestRuleMatcherRequest) -> AjaxJsonString:
        """测试规则匹配。

        Args:
            data (TestRuleMatcherRequest): 包含规则匹配测试的请求数据模型。

        Returns:
            AjaxJsonString: 规则匹配测试结果。

        Raises:
            CustomException: 当请求失败或 API 返回错误时。
        """
        response = self.api_client.post(
            endpoint="/admin/rule-test",
            response_model=AjaxJsonString,
            data=data
        )
        self._logger.info(f"[{response.trace_id}]测试规则匹配: {response.msg}")
        return response
