"""
Creation date: 2025/7/10
Creation Time: 19:52
DIR PATH: ZfileSDK/utils
Project Name: zfile_sdk
FILE NAME: base.py
Editor: cuckoo
"""

import inspect
from functools import wraps
from typing import Any, Callable, Type

from pydantic import BaseModel

from .api_client import ApiClient
from .logger import LogHandler


class BaseClass:
    def __init__(self, api_client: "ApiClient", name: str):
        """初始化用户接口。

        Args:
            api_client: API 客户端实例，用于发送请求。
        """
        self.api_client = api_client
        self.name = name

        self._logger = LogHandler(self.name).get_logger()

    def __getattr__(self, item):
        """获取属性或方法。

        Args:
            item: 属性或方法名。

        Returns:
            属性或方法的值。
        """
        if hasattr(self.api_client, item):
            return getattr(self.api_client, item)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def __repr__(self):
        """返回类的字符串表示。

        Returns:
            类的字符串表示。
        """
        return f"<{self.__class__.__name__} name={self.name}>"

    def __str__(self):
        """返回类的字符串表示。

        Returns:
            类的字符串表示。
        """
        return f"{self.__class__.__name__}({self.name})"


def auto_args_from_model(
        model: Type[BaseModel],
        model_kwarg_name: str = "data",
        use_alias: bool = False
) -> Callable:
    """
    一个装饰器，用于从 Pydantic 模型动态生成函数参数。

    Args:
        model (Type[BaseModel]): 用于生成参数的 Pydantic 模型。
        model_kwarg_name (str): 传递给被装饰函数的模型实例的关键字参数名称。
        use_alias (bool): 如果为 True, 则使用模型的字段别名(alias)作为函数参数名。
                          如果为 False, 则使用字段的原始属性名。
    """

    def decorator(func: Callable) -> Callable:
        model_fields = model.model_fields
        original_sig = inspect.signature(func)
        original_params = list(original_sig.parameters.values())
        self_or_cls_param = [original_params[0]] if original_params and original_params[0].name in ('self',
                                                                                                    'cls') else []

        new_params = []
        model_param_names = set()

        for field_name, field_info in model_fields.items():
            if use_alias and field_info.alias:
                param_name = field_info.alias
            else:
                param_name = field_name

            model_param_names.add(param_name)

            default_value = inspect.Parameter.empty if field_info.is_required() else field_info.get_default()

            new_params.append(
                inspect.Parameter(
                    name=param_name,
                    kind=inspect.Parameter.KEYWORD_ONLY,
                    default=default_value,
                    annotation=field_info.annotation
                )
            )

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            bound_args = original_sig.bind_partial(*args)

            model_kwargs = {}
            other_kwargs = {}

            for key, value in kwargs.items():
                if key in model_param_names:
                    model_kwargs[key] = value
                else:
                    other_kwargs[key] = value

            model_instance = model.model_validate(model_kwargs)

            final_kwargs = {**other_kwargs, model_kwarg_name: model_instance}

            return func(*bound_args.args, **final_kwargs)

        final_params = self_or_cls_param + new_params
        for param in original_params:
            if param.name not in ('self', 'cls', model_kwarg_name) and param not in final_params:
                final_params.append(param)

        wrapper.__signature__ = inspect.Signature(parameters=final_params)

        return wrapper

    return decorator
