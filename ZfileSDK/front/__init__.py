"""
ZFile SDK Front 模块
提供前端相关的API接口功能
"""

# 导入所有前端模块
from .direct_short_chain_module import DirectShortChainModule
from .file_list_module import FileListModule
from .file_operation_module import FileOperationModule
from .gd_tools_assistive_module import GdToolsAssistiveModule
from .initialization_module import InitializationModule
from .onedrive_authentication_callback_module import OneDriveAuthenticationCallbackModule
from .oneonefive_tools_assistive_module import OneOneFiveToolsAssistiveModule
from .onlyoffice_related_interfaces import OnlyOfficeModule
from .open_115_url_controller import Open115UrlController
from .s3_tools_assistive_module import S3ToolsAssistiveModule
from .server_proxy_download import FileDownloadStorageKey
from .server_proxy_upload import FileUploadStorageKey
from .sharepoint_tools_assistive_module import SharePointToolsAssistiveModule
from .short_link import ShortLinkModule
from .single_sign_on import SingleSignOnModule
from .single_sign_on_interface import SingleSignOnInterface
from .site_basic_module import SiteBasicModule
from .user_interface import UserInterface

# 版本信息
__version__ = "1.1.1"

# 导出的类列表
__all__ = [
    "DirectShortChainModule",
    "FileListModule",
    "FileOperationModule",
    "GdToolsAssistiveModule",
    "InitializationModule",
    "OneDriveAuthenticationCallbackModule",
    "OneOneFiveToolsAssistiveModule",
    "OnlyOfficeModule",
    "Open115UrlController",
    "S3ToolsAssistiveModule",
    "FileDownloadStorageKey",
    "FileUploadStorageKey",
    "SharePointToolsAssistiveModule",
    "ShortLinkModule",
    "SingleSignOnModule",
    "SingleSignOnInterface",
    "SiteBasicModule",
    "UserInterface"
]
