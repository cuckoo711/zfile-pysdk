"""
Creation date: 2025/7/10
Creation Time: 15:35
DIR PATH: ZfileSDK/utils
Project Name: ZfileSDK
FILE NAME: exceptions.py
Editor: cuckoo
"""

from typing import Any, TypeAlias

from requests import Response

from .models import AjaxJsonMapStringString, AjaxJsonObject, AjaxJsonString

# 为不同类型的错误数据模型定义类型别名，以提高代码可读性。
ErrorDataModel: TypeAlias = AjaxJsonMapStringString | AjaxJsonObject | AjaxJsonString


class ApiException(Exception):
    """封装由 ZFile API 返回的非 2xx HTTP 状态的错误。

    此异常会解析来自服务器的错误响应，并为状态码、消息和数据负载
    提供结构化的访问方式。

    Attributes:
        status_code (int): 响应的 HTTP 状态码。
        message (str): 从响应体中提取的错误消息。
        data (ErrorDataModel): 解析后的 Pydantic 错误响应模型。
    """

    def __init__(self, response: Response):
        """通过 requests.Response 对象初始化 ApiException。

        Args:
            response (Response): 失败的 `requests.Response` 对象。
        """
        self.status_code = response.status_code

        try:
            response_json = response.json()
            self.data = self._analyze_data(response_json)
            # 安全地获取 'msg' 属性，若不存在则提供一个默认值。
            self.message = getattr(self.data, 'msg', "发生未知的 API 错误。")
        except (ValueError, TypeError):
            # 处理响应体不是有效 JSON 或解析失败的情况 (例如，代理返回的 HTML 错误页)。
            raise CustomException(
                code=self.status_code,
                msg="无法解析 API 错误响应，可能是无效的 JSON 格式。",
                data=response.text
            ) from None

        super().__init__(f"HTTP {self.status_code}: {self.message}")

    def _analyze_data(self, data_json: dict[str, Any]) -> ErrorDataModel:
        """将 JSON 错误数据解析为相应的 Pydantic 模型。

        此逻辑根据 ZFile API 的预期响应结构，将特定的 HTTP 状态码
        映射到对应的错误模型。

        Args:
            data_json (dict[str, Any]): 来自响应的 JSON 字典。

        Returns:
            ErrorDataModel: 与错误数据匹配的 Pydantic 模型。

        Raises:
            ValueError: 如果状态码未被处理。
        """
        # 辅助变量，检查 JSON 负载中 'data' 字段的类型。
        data_field_is_str = isinstance(data_json.get("data"), str)

        if self.status_code == 400:
            return (
                AjaxJsonString.model_validate(data_json)
                if data_field_is_str
                else AjaxJsonMapStringString.model_validate(data_json)
            )

        if self.status_code in {401, 403, 404}:
            return AjaxJsonObject.model_validate(data_json)

        if self.status_code == 405:
            return AjaxJsonString.model_validate(data_json)

        if self.status_code == 500:
            return (
                AjaxJsonString.model_validate(data_json)
                if data_field_is_str
                else AjaxJsonObject.model_validate(data_json)
            )

        # 为未预期但结构化的错误代码提供回退方案。
        if "msg" in data_json and "code" in data_json:
            return AjaxJsonObject.model_validate(data_json)

        raise ValueError(f"不支持的状态码或错误格式: {self.status_code}")

    def __repr__(self) -> str:
        """返回一个详细的、对开发者友好的异常对象表示形式。"""
        return (f"{self.__class__.__name__}("
                f"status_code={self.status_code}, "
                f"message='{self.message}', "
                f"data={self.data!r})")

    def __str__(self) -> str:
        """返回一个简洁的、对用户友好的字符串表示形式。"""
        return f"[API 错误] HTTP {self.status_code}: {self.data!r}"


class CustomException(Exception):
    """封装来自 API 的业务逻辑错误 (例如，登录信息无效)。

    当 HTTP 请求成功 (状态码 200)，但 API 响应负载表明逻辑失败
    (例如，code != "0") 时，使用此异常。

    Attributes:
        code (int | str): 来自 API 响应的业务特定错误代码。
        msg (str): 伴随错误代码的错误消息。
        data (Any | None): 错误返回时附带的可选数据。
    """

    def __init__(self, code: int | str, msg: str, data: Any | None = None):
        """初始化 CustomException。

        Args:
            code (int | str): 业务错误代码。
            msg (str): 业务错误消息。
            data (Any | None): 可选的关联数据，默认为 None。
        """
        self.code = code
        self.msg = msg
        self.data = data
        super().__init__(f"[{code}] {msg}")

    def __repr__(self) -> str:
        """返回一个详细的、对开发者友好的异常对象表示形式。"""
        return (f"{self.__class__.__name__}("
                f"code={self.code!r}, msg='{self.msg}', data={self.data!r})")

    def __str__(self) -> str:
        """返回一个简洁的、对用户友好的字符串表示形式。"""
        return f"[业务逻辑错误] 代码 {self.code}: {self.msg}"
