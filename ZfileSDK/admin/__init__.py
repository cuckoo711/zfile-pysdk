"""
ZFile SDK Admin 模块
提供管理员相关的API接口功能
"""

from .direct_link_log_management import DirectLinkLogManagement
from .direct_link_management import DirectLinkManagement
from .ip_address_helper import IpAddressHelper
from .login_log_management import LoginLogManagement
from .login_module import LoginModule
from .permission_module import PermissionModule
from .rule_management_upload_rules import RuleManagementUploadRules
from .rule_management_view_rules import RuleManagementViewRules
from .rule_matcher_helper import RuleMatcherHelper
from .single_sign_on_management import SingleSignOnManagement
from .site_setting_module import SiteSettingModule
from .storage_source_module_basic import StorageSourceModuleBasic
from .storage_source_module_filter_file import StorageSourceModuleFilterFile
from .storage_source_module_metadata import StorageSourceModuleMetadata
from .storage_source_module_permission import StorageSourceModulePermission
from .storage_source_module_readme import StorageSourceModuleReadme
# 导入所有管理员功能模块
from .user_management import UserManagement

# 版本信息
__version__ = "1.1.1"

# 导出的类列表
__all__ = [
    # 用户和权限管理
    "UserManagement",
    "LoginModule",
    "PermissionModule",
    "LoginLogManagement",
    "SingleSignOnManagement",

    # 站点设置
    "SiteSettingModule",

    # 存储源管理
    "StorageSourceModuleBasic",
    "StorageSourceModuleFilterFile",
    "StorageSourceModuleMetadata",
    "StorageSourceModulePermission",
    "StorageSourceModuleReadme",

    # 规则管理
    "RuleManagementViewRules",
    "RuleManagementUploadRules",
    "RuleMatcherHelper",

    # 直链管理
    "DirectLinkManagement",
    "DirectLinkLogManagement",

    # 辅助工具
    "IpAddressHelper",

    # 版本信息
    "__version__"
]
