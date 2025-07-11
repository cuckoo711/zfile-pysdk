"""
Creation date: 2025/7/10
Creation Time: 15:34
DIR PATH: ZfileSDK/utils
Project Name: ZfileSDK
FILE NAME: api_client.py
Editor: cuckoo
"""

from typing import Any, Optional, Type, TypeVar

import requests
import urllib3
from pydantic import BaseModel
from requests_toolbelt import MultipartEncoder

from .exceptions import ApiException, CustomException
from .logger import LogHandler
from .models import AjaxJsonLoginResult, AjaxJsonVoid, UserLoginRequest

# 使用 TypeVar 支持泛型，使得返回类型可以被精确推断
T = TypeVar('T', bound=BaseModel)

# 禁用 SSL 警告，适用于自签名证书或开发环境
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ApiClient:
    """一个与 ZFile 后端服务交互的通用 API 客户端。

    该类封装了 HTTP 会话管理、自动登录与 token 处理、基于 Pydantic 的 请求/响应序列化以及统一的 API 错误处理逻辑。

    Attributes:
        name (str): 客户端的名称标识。
        base_url (str): API 的基础 URL。
    """
    name: str = "ApiClient"

    def __init__(self, base_url: str, token: Optional[str] = None):
        """初始化 API 客户端实例。

        Args:
            base_url (str): API 的基础 URL, 例如 "http://localhost:8080"。
            token (Optional[str]): 可选的预设 zfile-token。
        """
        self.base_url = base_url.rstrip('/')
        self._session = requests.Session()
        self._token: Optional[str] = token
        self._is_admin: bool = False
        self._logger = LogHandler(self.name).get_logger()

        self._setup_session()

    def _setup_session(self) -> None:
        """配置 requests.Session 的默认请求头。"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, */*",
            "Cookie": f"zfile-token={self._token}"
        }
        if self._token:
            headers["zfile-token"] = self._token
        self._session.headers.update(headers)

    def _make_request(
            self,
            method: str,
            endpoint: str,
            response_model: Type[T],
            data: Optional[BaseModel | Any] = None,
            params: Optional[dict[str, Any]] = None,
    ) -> type[T] | None:
        """执行 API 请求的核心方法。

        Args:
            method (str): HTTP 方法 (例如 "GET", "POST")。
            endpoint (str): API 端点路径 (例如 "/user/login")。
            response_model (Type[T]): 用于解析响应体的 Pydantic 模型。
            data (Optional[BaseModel]): 作为请求体的 Pydantic 模型实例。
            params (Optional[dict[str, Any]]): URL 查询参数。

        Returns:
            T: 解析后的 Pydantic 响应模型实例。

        Raises:
            CustomException: 当发生网络请求层面的错误时抛出。
            ApiException: 当 API 返回非 200 HTTP 状态码时抛出。
        """
        full_url = self.base_url + endpoint
        json_payload = data.model_dump_json(exclude_none=True, by_alias=True) if data else None
        self._logger.debug(f"发起 {method} 请求: {full_url}, 数据: {json_payload}, 参数: {params}")
        try:
            response = self._session.request(
                method=method,
                url=full_url,
                data=json_payload,
                params=params,
                verify=False
            )
            response.raise_for_status()  # 检查 HTTP 状态码是否为 200 系列
        except requests.HTTPError as e:
            # 将 requests 的 HTTPError 统一封装为 ApiException
            exception = ApiException(e.response)
            self._logger.error(f"API 请求失败: {exception.message} (HTTP {exception.status_code})")
            return exception.data  # 返回解析后的错误数据
        except requests.RequestException as e:
            self._logger.error(f"网络请求失败: {e}")
            raise CustomException(code=500, msg="请求失败，请检查网络连接或 API 服务状态。") from e

        # 直接使用 Pydantic 进行验证和解析
        return response_model.model_validate(response.json())

    def make_common_request(
            self,
            method: str,
            endpoint: str,
            data: dict[str, Any] | MultipartEncoder | None = None,
            params: dict[str, Any] | None = None,
            headers: Optional[dict[str, str]] = None,
    ) -> requests.Response:
        """执行通用的 HTTP 请求。

        Args:
            method (str): HTTP 方法 (例如 "GET", "POST")。
            endpoint (str): API 端点路径 (例如 "/user/login")。
            data (dict[str, Any] | None): 请求体数据。
            params (dict[str, Any] | None): URL 查询参数。
            headers (Optional[dict[str, str]]): 可选的自定义请求头。

        Returns:
            Response: requests.Response 对象，包含响应数据。

        Raises:
            ApiException: 当 API 返回非 200 HTTP 状态码时抛出。
        """
        full_url = self.base_url + endpoint
        self._logger.debug(f"发起 {method} 请求: {full_url}, 数据: {data}, 参数: {params}")
        if headers:
            self._session.headers.update(headers)
        try:
            response = self._session.request(
                method=method,
                url=full_url,
                params=params,
                data=data,
                verify=False
            )
            print(response.text)
            response.raise_for_status()
        except Exception as e:
            self._logger.error(f"网络请求失败: {e}")
            raise CustomException(code=500, msg=f"请求失败: {str(e)}") from e

        return response

    def login(
            self,
            username: str,
            password: str,
            verify_code: Optional[str] = None,
            verify_code_uuid: Optional[str] = None
    ) -> None:
        """用户登录并自动管理会话的 token。

        Args:
            username (str): 用户名。
            password (str): 密码。
            verify_code (Optional[str]): 验证码（如果需要）。
            verify_code_uuid (Optional[str]): 验证码的唯一标识。

        Raises:
            CustomException: 当登录凭据无效或 API 返回业务错误时。
        """
        login_request = UserLoginRequest(
            username=username,
            password=password,
            verifyCode=verify_code,
            verifyCodeUUID=verify_code_uuid
        )

        login_result = self.post(
            endpoint="/user/login",
            response_model=AjaxJsonLoginResult,
            data=login_request,
        )

        # 统一的业务逻辑判断
        if login_result.code != "0" or not login_result.data:
            raise CustomException(
                code=login_result.code,
                msg=login_result.msg,
                data=login_result.data
            )

        self._token = login_result.data.token
        self._is_admin = login_result.data.admin
        self._session.headers["zfile-token"] = self._token

        self._logger.info(f"登录成功。管理员状态: {self._is_admin}")

    def logout(self) -> None:
        """用户注销并清理会话状态。"""
        self.post("/user/logout", response_model=AjaxJsonVoid)

        self._token = None
        self._is_admin = False
        self._session.headers.pop("zfile-token", None)

        self._logger.info("注销成功，已清除 token 和管理员状态。")

    # --- 通用 HTTP 方法封装 ---
    def get(self, endpoint: str, response_model: Type[T], params: Optional[dict[str, Any]] = None,
            data: Optional[BaseModel | Any] = None) -> T:
        return self._make_request("GET", endpoint, response_model=response_model, params=params, data=data)

    def post(self, endpoint: str, response_model: Type[T], params: Optional[dict[str, Any]] = None,
             data: Optional[BaseModel | Any] = None) -> T:
        return self._make_request("POST", endpoint, response_model=response_model, params=params, data=data)

    def put(self, endpoint: str, response_model: Type[T], params: Optional[dict[str, Any]] = None,
            data: Optional[BaseModel | Any] = None) -> T:
        return self._make_request("PUT", endpoint, response_model=response_model, params=params, data=data)

    def delete(self, endpoint: str, response_model: Type[T], params: Optional[dict[str, Any]] = None,
               data: Optional[BaseModel | Any] = None) -> T:
        return self._make_request("DELETE", endpoint, response_model=response_model, params=params, data=data)

    def patch(self, endpoint: str, response_model: Type[T], params: Optional[dict[str, Any]] = None,
              data: Optional[BaseModel | Any] = None) -> T:
        return self._make_request("PATCH", endpoint, response_model=response_model, params=params, data=data)

    # --- 属性访问器 ---
    @property
    def token(self) -> Optional[str]:
        """获取当前会话的 zfile-token。"""
        return self._token

    @property
    def is_admin(self) -> bool:
        """检查当前用户是否为管理员。"""
        return self._is_admin

    # --- 特殊方法 (Magic Methods) ---
    def close(self) -> None:
        """关闭会话并清理资源。推荐显式调用此方法或使用上下文管理器。"""
        if self._session:
            self._session.close()
            self._logger.info("API 客户端会话已关闭。")

    def __enter__(self) -> 'ApiClient':
        """进入上下文管理器，返回自身实例。"""
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """退出上下文管理器时，自动关闭会话。"""
        self.close()

    def __del__(self) -> None:
        """实例销毁时的清理操作，作为最后的保障。"""
        self.close()

    def __repr__(self) -> str:
        """返回一个明确的、可用于调试的对象表示形式。"""
        token_status = f"token='{self._token[:8]}...'" if self._token else "token=None"
        return (
            f"<{self.__class__.__name__}(base_url='{self.base_url}', "
            f"{token_status}, is_admin={self._is_admin})>"
        )

    def __str__(self) -> str:
        """返回一个用户友好的对象字符串表示。"""
        return f"ZFile API Client for {self.base_url}"

    def __hash__(self) -> int:
        """基于 base_url 和 token 计算哈希值。

        注意：当 token 状态改变时 (例如登录后), 哈希值也会改变。
        """
        return hash((self.base_url, self._token))

    def __eq__(self, other: Any) -> bool:
        """比较两个 ApiClient 实例是否相等。

        两个实例被认为相等当且仅当它们的 base_url 和 token 相同。
        """
        if not isinstance(other, ApiClient):
            return NotImplemented
        return self.base_url == other.base_url and self._token == other._token

    def __ne__(self, other: Any) -> bool:
        """比较两个 ApiClient 实例是否不相等。

        使用 __eq__ 的结果进行反向判断。
        """
        return not self.__eq__(other)
