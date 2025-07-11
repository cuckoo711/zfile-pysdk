"""
Creation date: 2025/7/10
Creation Time: 16:11
DIR PATH: ZfileSDK/utils
Project Name: ZfileSDK
FILE NAME: models.py
Editor: cuckoo
"""

import json
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set

from pydantic import BaseModel, Field


# =======================================================================
#  基础模型 (Base Models)
# =======================================================================

class CustomBaseModel(BaseModel):
    """
    扩展 Pydantic 的 BaseModel，添加自定义的 JSON 导入和导出方法。
    """

    @classmethod
    def from_json(cls, json_str: str) -> "CustomBaseModel":
        """
        从 JSON 字符串创建 Pydantic 模型实例。
        """
        try:
            data = json.loads(json_str)
            return cls.model_validate(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"无效的 JSON 数据: {e}")
        except Exception as e:
            raise ValueError(f"创建模型时发生错误: {e}")

    def to_json(self) -> str:
        """
        将 Pydantic 模型实例导出为 JSON 字符串。
        """
        try:
            return self.model_dump_json(indent=2, exclude_none=True, by_alias=True)
        except Exception as e:
            raise ValueError(f"导出模型为 JSON 时发生错误: {e}")

    def to_str(self) -> str:
        """
        将 Pydantic 模型实例转换为字符串表示。
        """
        string = ""
        for field, value in self.model_dump(exclude_none=True, by_alias=True).items():
            if isinstance(value, datetime):
                value = value.isoformat()
            string += f"{field}: {value}\n"
        return string.strip()

    def to_dict(self) -> Dict[str, Any]:
        """
        将 Pydantic 模型实例转换为字典。
        """
        return self.model_dump(exclude_none=True, by_alias=True)

    def __str__(self) -> str:
        """
        返回模型的字符串表示。
        """
        return self.to_str()

    def __repr__(self) -> str:
        """
        返回模型的详细字符串表示。
        """
        return f"{self.__class__.__name__}({self.to_dict()})"

    class Config:
        """
        Pydantic 模型配置。
        """
        populate_by_name = True
        # anystr_strip_whitespace = True # Optional: auto-strip whitespace
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else v,
            # 可以添加更多类型的编码器
        }


class AjaxJsonBase(CustomBaseModel):
    """Ajax 响应的基础模型，定义通用字段"""
    code: str = Field(..., title="业务状态码，0 为正常")
    msg: str = Field(..., title="响应消息")
    data_count: Optional[int] = Field(None, title="数据总条数，分页情况有效", alias="dataCount")
    trace_id: Optional[str] = Field(None, title="跟踪 ID", alias="traceId")


# =======================================================================
#  枚举类型 (Enum Types)
# =======================================================================

class FileTypeEnum(str, Enum):
    """文件类型枚举"""
    FILE = "FILE"
    FOLDER = "FOLDER"


class FileClickModeEnum(str, Enum):
    """文件点击模式枚举"""
    CLICK = "click"
    DBCLICK = "dbclick"


class ReadmeDisplayModeEnum(str, Enum):
    """Readme 显示模式枚举"""
    TOP = "top"
    BOTTOM = "bottom"
    DIALOG = "dialog"


class MatchModeEnum(str, Enum):
    """匹配模式枚举"""
    FULL = "full"
    CONTAIN = "contain"


class PermissionOperatorEnum(str, Enum):
    """操作权限枚举"""
    AVAILABLE = "available"
    NEW_FOLDER = "newFolder"
    UPLOAD = "upload"
    PREVIEW = "preview"
    DOWNLOAD = "download"
    BATCH_DOWNLOAD = "batchDownload"
    PACKAGE_DOWNLOAD = "packageDownload"
    COPY_DOWNLOAD_LINK = "copyDownloadLink"
    RENAME = "rename"
    COPY = "copy"
    MOVE = "move"
    DELETE = "delete"
    SEARCH = "search"
    GENERATE_LINK = "generateLink"
    GENERATE_SHORT_LINK = "generateShortLink"
    IGNORE_PASSWORD = "ignorePassword"
    IGNORE_HIDDEN = "ignoreHidden"


class StorageSourceParamDefTypeEnum(str, Enum):
    """存储源参数定义类型枚举"""
    INPUT = "input"
    TEXTAREA = "textarea"
    SELECT = "select"
    SWITCH = "switch"


class MatchTypeEnum(str, Enum):
    """匹配目标类型枚举"""
    FILE = "file"
    DIR = "dir"
    ALL = "all"


class FilterModeEnum(str, Enum):
    """文件过滤模式枚举"""
    HIDDEN = "hidden"
    INACCESSIBLE = "inaccessible"
    DISABLE_DOWNLOAD = "disable_download"


class RuleTypeEnum(str, Enum):
    """规则类型枚举"""
    SIMPLE = "simple"
    REGEX = "regex"


class AllowModeEnum(str, Enum):
    """允许/拒绝模式枚举"""
    ONLY_ALLOW = "only_allow"
    ONLY_DENY = "only_deny"


class UploadTypeEnum(str, Enum):
    """存储源上传类型枚举"""
    MICROSOFT = "MICROSOFT"
    PROXY = "PROXY"
    S3 = "S3"
    UPYUN = "UPYUN"
    OPEN115 = "OPEN115"


class SearchModeEnum(str, Enum):
    """搜索模式枚举"""
    SEARCH_CURRENT_FOLDER = "search_current_folder"
    SEARCH_CURRENT_FOLDER_AND_CHILD = "search_current_folder_and_child"
    SEARCH_ALL = "search_all"


class LoginVerifyModeEnum(str, Enum):
    """登录验证模式枚举"""
    OFF = "off"
    IMAGE = "image"
    TWO_FA = "2fa"


class StorageTypeEnum(str, Enum):
    """存储源类型枚举"""
    LOCAL = "LOCAL"
    ALIYUN = "ALIYUN"
    WEBDAV = "WEBDAV"
    TENCENT = "TENCENT"
    UPYUN = "UPYUN"
    FTP = "FTP"
    SFTP = "SFTP"
    HUAWEI = "HUAWEI"
    MINIO = "MINIO"
    S3 = "S3"
    ONE_DRIVE = "ONE_DRIVE"
    ONE_DRIVE_CHINA = "ONE_DRIVE_CHINA"
    SHAREPOINT_DRIVE = "SHAREPOINT_DRIVE"
    SHAREPOINT_DRIVE_CHINA = "SHAREPOINT_DRIVE_CHINA"
    GOOGLE_DRIVE = "GOOGLE_DRIVE"
    QINIU = "QINIU"
    DOGE_CLOUD = "DOGE_CLOUD"
    OPEN115 = "OPEN115"


class LoginLogModeEnum(str, Enum):
    """登录日志模式枚举"""
    OFF = "off"
    ALL = "all"
    IGNORE_SUCCESS_PWD = "ignoreSuccessPwd"
    IGNORE_ALL_PWD = "ignoreAllPwd"


class SessionTrackingModeEnum(str, Enum):
    """会话跟踪模式枚举 (根据新 OpenAPI 添加)"""
    COOKIE = "COOKIE"
    URL = "URL"
    SSL = "SSL"


class RefererTypeEnum(str, Enum):
    """Referer 防盗链类型枚举"""
    OFF = "off"
    WHITE_LIST = "white_list"
    BLACK_LIST = "black_list"


class StorageSearchModeEnum(str, Enum):
    """存储源搜索模式枚举"""
    SEARCH_CACHE = "SEARCH_CACHE"
    SEARCH_ALL = "SEARCH_ALL"


# =======================================================================
#  核心业务模型 (Core Business Models)
# =======================================================================

class FileItemResult(CustomBaseModel):
    """文件列表信息结果类"""
    id: Optional[str] = Field(None, title="文件id(部分存储源)")
    name: Optional[str] = Field(None, title="文件名")
    time: Optional[datetime] = Field(None, title="时间")
    size: Optional[int] = Field(None, title="大小")
    type: Optional[FileTypeEnum] = Field(None, title="类型")
    path: Optional[str] = Field(None, title="所在路径")
    url: Optional[str] = Field(None, title="下载地址")


class FileInfoResult(CustomBaseModel):
    """文件列表信息结果类"""
    files: Optional[List[FileItemResult]] = Field(None, title="文件列表")
    password_pattern: Optional[str] = Field(None, title="当前目录密码路径表达式", alias="passwordPattern")


class StorageSourceMetadata(CustomBaseModel):
    """存储源元数据"""
    upload_type: Optional[UploadTypeEnum] = Field(None, alias="uploadType")
    support_rename_folder: Optional[bool] = Field(None, alias="supportRenameFolder")
    support_move_folder: Optional[bool] = Field(None, alias="supportMoveFolder")
    support_copy_folder: Optional[bool] = Field(None, alias="supportCopyFolder")
    support_delete_not_empty_folder: Optional[bool] = Field(None, alias="supportDeleteNotEmptyFolder")
    need_create_folder_before_upload: Optional[bool] = Field(None, alias="needCreateFolderBeforeUpload")


class LinkExpireDTO(CustomBaseModel):
    """短链过期时间设置"""
    value: Optional[int] = None
    unit: Optional[str] = None
    seconds: Optional[int] = None


class FrontSiteConfigResult(CustomBaseModel):
    """全局站点设置响应类"""
    installed: Optional[bool] = Field(None, title="是否已初始化")
    debug_mode: Optional[bool] = Field(None, title="Debug 模式", alias="debugMode")
    direct_link_prefix: Optional[str] = Field(None, title="直链地址前缀", alias="directLinkPrefix")
    site_name: Optional[str] = Field(None, title="站点名称", alias="siteName")
    icp: Optional[str] = Field(None, title="备案号")
    layout: str = Field(..., title="页面布局")
    mobile_layout: Optional[str] = Field(None, title="移动端页面布局", alias="mobileLayout")
    table_size: str = Field(..., title="列表尺寸", alias="tableSize")
    show_link_btn: bool = Field(..., title="是否显示生成直链功能", alias="showLinkBtn")
    show_short_link: bool = Field(..., title="是否显示生成短链功能", alias="showShortLink")
    show_path_link: bool = Field(..., title="是否显示生成路径链接功能", alias="showPathLink")
    show_document: bool = Field(..., title="是否显示文档区", alias="showDocument")
    show_announcement: bool = Field(..., title="是否显示网站公告", alias="showAnnouncement")
    announcement: Optional[str] = Field(None, title="网站公告")
    custom_js: Optional[str] = Field(None, title="自定义 JS", alias="customJs")
    custom_css: Optional[str] = Field(None, title="自定义 CSS", alias="customCss")
    custom_video_suffix: Optional[str] = Field(None, alias="customVideoSuffix")
    custom_image_suffix: Optional[str] = Field(None, alias="customImageSuffix")
    custom_audio_suffix: Optional[str] = Field(None, alias="customAudioSuffix")
    custom_text_suffix: Optional[str] = Field(None, alias="customTextSuffix")
    custom_office_suffix: Optional[str] = Field(None, alias="customOfficeSuffix")
    custom_kk_file_view_suffix: Optional[str] = Field(None, alias="customKkFileViewSuffix")
    root_show_storage: bool = Field(..., title="根目录是否显示所有存储源", alias="rootShowStorage")
    force_backend_address: Optional[str] = Field(None, title="强制后端地址", alias="forceBackendAddress")
    front_domain: Optional[str] = Field(None, title="前端域名", alias="frontDomain")
    show_login: Optional[bool] = Field(None, title="是否在前台显示登陆按钮", alias="showLogin")
    login_log_mode: Optional[LoginLogModeEnum] = Field(None, title="登录日志模式", alias="loginLogMode")
    file_click_mode: Optional[FileClickModeEnum] = Field(None, title="默认文件点击习惯", alias="fileClickMode")
    mobile_file_click_mode: Optional[FileClickModeEnum] = Field(None, title="移动端默认文件点击习惯",
                                                                alias="mobileFileClickMode")
    max_file_uploads: Optional[int] = Field(None, title="最大同时上传文件数", alias="maxFileUploads")
    only_office_url: Optional[str] = Field(None, title="onlyOffice 在线预览地址", alias="onlyOfficeUrl")
    kk_file_view_url: Optional[str] = Field(None, title="kkFileView 在线预览地址", alias="kkFileViewUrl")
    kk_file_view_open_mode: Optional[str] = Field(None, title="kkFileView 预览方式", alias="kkFileViewOpenMode")
    max_show_size: Optional[int] = Field(None, title="默认最大显示文件数", alias="maxShowSize")
    load_more_size: Optional[int] = Field(None, title="每次加载更多文件数", alias="loadMoreSize")
    default_sort_field: Optional[str] = Field(None, title="默认排序字段", alias="defaultSortField")
    default_sort_order: Optional[str] = Field(None, title="默认排序方向", alias="defaultSortOrder")
    site_home_name: Optional[str] = Field(None, title="站点 Home 名称", alias="siteHomeName")
    site_home_logo: Optional[str] = Field(None, title="站点 Home Logo", alias="siteHomeLogo")
    site_home_logo_link: Optional[str] = Field(None, title="站点 Logo 点击后链接", alias="siteHomeLogoLink")
    site_home_logo_target_mode: Optional[str] = Field(None, title="站点 Logo 链接打开方式",
                                                      alias="siteHomeLogoTargetMode")
    link_expire_times: Optional[List[LinkExpireDTO]] = Field(None, title="短链过期时间设置", alias="linkExpireTimes")
    default_save_pwd: Optional[bool] = Field(None, title="是否默认记住密码", alias="defaultSavePwd")
    enable_hover_menu: Optional[bool] = Field(None, title="是否启用 hover 菜单", deprecated=True,
                                              alias="enableHoverMenu")
    guest: Optional[bool] = Field(None, title="是否是游客")


class StorageSourceConfigResult(CustomBaseModel):
    """存储源设置响应类"""
    readme_text: Optional[str] = Field(None, title="readme 文本内容, 支持 md 语法.", alias="readmeText")
    readme_display_mode: ReadmeDisplayModeEnum = Field(..., title="显示模式", alias="readmeDisplayMode")
    default_switch_to_img_mode: Optional[bool] = Field(None, title="是否默认开启图片模式",
                                                       alias="defaultSwitchToImgMode")
    permission: Optional[Dict[str, bool]] = None
    metadata: Optional[StorageSourceMetadata] = None
    root_path: Optional[str] = Field(None, alias="rootPath")


class BatchGenerateLinkResponse(CustomBaseModel):
    """批量生成直链结果类"""
    address: Optional[str] = None


class BatchOperatorResult(CustomBaseModel):
    """批量操作结果类"""
    name: Optional[str] = None
    path: Optional[str] = None
    success: Optional[bool] = None
    message: Optional[str] = None


class LoginResult(CustomBaseModel):
    """登录结果类"""
    token: Optional[str] = None
    admin: Optional[bool] = None


class SharepointSiteResult(CustomBaseModel):
    """SharePoint 站点结果类"""
    id: Optional[str] = Field(None, title="站点 id")
    display_name: Optional[str] = Field(None, title="站点名称", alias="displayName")
    web_url: Optional[str] = Field(None, title="站点地址", alias="webUrl")


class SharepointSiteListResult(CustomBaseModel):
    """Sharepoint 网站 list 列表"""
    id: Optional[str] = Field(None, title="站点目录 id")
    display_name: Optional[str] = Field(None, title="站点目录名称", alias="displayName")
    created_date_time: Optional[datetime] = Field(None, title="站点目录创建时间", alias="createdDateTime")
    web_url: Optional[str] = Field(None, title="站点目录地址", alias="webUrl")


class ZFileCORSRule(CustomBaseModel):
    """S3 CORS 规则"""
    id: Optional[str] = None
    allowed_methods: Optional[List[str]] = Field(None, alias="allowedMethods")
    allowed_origins: Optional[List[str]] = Field(None, alias="allowedOrigins")
    max_age_seconds: Optional[int] = Field(None, alias="maxAgeSeconds")
    exposed_headers: Optional[List[str]] = Field(None, alias="exposedHeaders")
    allowed_headers: Optional[List[str]] = Field(None, alias="allowedHeaders")


class S3BucketNameResult(CustomBaseModel):
    """S3 bucket 名称结果类"""
    name: Optional[str] = Field(None, title="bucket 名称")
    date: Optional[datetime] = Field(None, title="bucket 创建时间")


class GoogleDriveInfoResult(CustomBaseModel):
    """gd drive 基本信息结果类"""
    id: Optional[str] = Field(None, title="drive id")
    name: Optional[str] = Field(None, title="drive 名称")


class DeleteItem(CustomBaseModel):
    """待删除文件详情"""
    path: Optional[str] = None
    name: Optional[str] = None
    type: Optional[FileTypeEnum] = None
    password: Optional[str] = None


class Open115AuthDeviceCodeResult(CustomBaseModel):
    """115 扫码登录设备代码结果"""
    uid: Optional[str] = None
    time: Optional[int] = None
    sign: Optional[str] = None
    code_verifier: Optional[str] = Field(None, alias="codeVerifier")
    qrcode: Optional[str] = None


class Open115GetStatusResult(CustomBaseModel):
    """115 扫码登录状态结果"""
    status: Optional[str] = None
    msg: Optional[str] = None
    access_token: Optional[str] = Field(None, alias="accessToken")
    refresh_token: Optional[str] = Field(None, alias="refreshToken")
    expired_at: Optional[int] = Field(None, alias="expiredAt")


class CheckLoginResult(CustomBaseModel):
    """检查登录状态结果"""
    is_login: Optional[bool] = Field(None, alias="isLogin")
    is_admin: Optional[bool] = Field(None, alias="isAdmin")
    username: Optional[str] = None
    nickname: Optional[str] = None


class LoginVerifyImgResult(CustomBaseModel):
    """生成图片验证码结果类"""
    img_base64: Optional[str] = Field(None, title="验证码图片", alias="imgBase64")
    uuid: Optional[str] = Field(None, title="验证码 UUID")


class StorageSourceResult(CustomBaseModel):
    """存储源基本信息响应类"""
    name: Optional[str] = Field(None, title="存储源名称")
    key: Optional[str] = Field(None, title="存储源别名")
    type: Optional[StorageTypeEnum] = Field(None, title="存储源类型")
    search_enable: Optional[bool] = Field(None, title="是否开启搜索", alias="searchEnable")
    default_switch_to_img_mode: Optional[bool] = Field(None, title="是否默认开启图片模式",
                                                       alias="defaultSwitchToImgMode")


class SsoLoginItemResponse(CustomBaseModel):
    """SSO 登录项响应"""
    provider: Optional[str] = Field(None, title="OIDC/OAuth2 厂商名")
    name: Optional[str] = Field(None, title="显示名称")
    icon: Optional[str] = Field(None, title="ICON")


class Action(CustomBaseModel):
    """OnlyOffice 回调 Action"""
    type: Optional[int] = None
    userid: Optional[str] = None


class OnlyOfficeCallback(CustomBaseModel):
    """OnlyOffice 回调模型"""
    key: Optional[str] = None
    status: Optional[int] = None
    url: Optional[str] = None
    history: Optional[Dict[str, Any]] = None
    users: Optional[List[str]] = None
    actions: Optional[List[Action]] = None
    lastsave: Optional[datetime] = None
    notmodified: Optional[bool] = None
    token: Optional[str] = None
    filetype: Optional[str] = None


# =======================================================================
#  Spring Actuator / Context 模型 (Spring Actuator / Context Models)
# =======================================================================

class PackageDescriptor(CustomBaseModel):
    """Java 包描述符"""
    name: Optional[str] = Field(None, title="包名称")
    annotations: Optional[List[Dict[str, Any]]] = Field(None, title="注解")
    declared_annotations: Optional[List[Dict[str, Any]]] = Field(None, title="声明的注解", alias="declaredAnnotations")
    sealed: Optional[bool] = Field(None, title="是否密封")
    specification_title: Optional[str] = Field(None, title="规范标题", alias="specificationTitle")
    specification_version: Optional[str] = Field(None, title="规范版本", alias="specificationVersion")
    specification_vendor: Optional[str] = Field(None, title="规范供应商", alias="specificationVendor")
    implementation_title: Optional[str] = Field(None, title="实现标题", alias="implementationTitle")
    implementation_version: Optional[str] = Field(None, title="实现版本", alias="implementationVersion")
    implementation_vendor: Optional[str] = Field(None, title="实现供应商", alias="implementationVendor")


class ClassLoaderDescriptor(CustomBaseModel):
    """类加载器描述符"""
    name: Optional[str] = Field(None, title="类加载器名称")
    registered_as_parallel_capable: Optional[bool] = Field(None, title="是否注册为并行能力",
                                                           alias="registeredAsParallelCapable")
    parent: Optional['ClassLoaderDescriptor'] = Field(None, title="父类加载器")
    unnamed_module: Optional['ModuleDescriptor'] = Field(None, title="未命名模块", alias="unnamedModule")
    defined_packages: Optional[List[PackageDescriptor]] = Field(None, title="定义的包", alias="definedPackages")
    default_assertion_status: Optional[bool] = Field(None, title="默认断言状态", alias="defaultAssertionStatus")


class ModuleDescriptor(CustomBaseModel):
    """Java 模块描述符"""
    name: Optional[str] = Field(None, title="模块名称")
    class_loader: Optional[ClassLoaderDescriptor] = Field(None, title="类加载器", alias="classLoader")
    descriptor: Optional[Dict[str, Any]] = Field(None, title="模块描述符属性")
    named: Optional[bool] = Field(None, title="是否命名模块")
    annotations: Optional[List[Dict[str, Any]]] = Field(None, title="注解")
    declared_annotations: Optional[List[Dict[str, Any]]] = Field(None, title="声明的注解", alias="declaredAnnotations")
    packages: Optional[List[str]] = Field(None, title="包列表")
    native_access_enabled: Optional[bool] = Field(None, title="是否启用本机访问", alias="nativeAccessEnabled")
    layer: Optional[Dict[str, Any]] = Field(None, title="模块层")


class AutowireCapableBeanFactory(CustomBaseModel):
    """Spring 的 AutowireCapableBeanFactory 接口 (通常为空)"""
    pass


class BeanFactory(CustomBaseModel):
    """Spring 的 BeanFactory 接口 (通常为空)"""
    pass


class Environment(CustomBaseModel):
    """Spring 环境配置"""
    active_profiles: Optional[List[str]] = Field(None, title="激活的 Profile", alias="activeProfiles")
    default_profiles: Optional[List[str]] = Field(None, title="默认的 Profile", alias="defaultProfiles")


class ApplicationContext(CustomBaseModel):
    """Spring 应用上下文信息"""
    parent: Optional['ApplicationContext'] = Field(None, title="父应用上下文")
    id: Optional[str] = Field(None, title="应用 ID")
    display_name: Optional[str] = Field(None, title="显示名称", alias="displayName")
    startup_date: Optional[int] = Field(None, title="启动时间戳", alias="startupDate")
    application_name: Optional[str] = Field(None, title="应用名称", alias="applicationName")
    autowire_capable_bean_factory: Optional[AutowireCapableBeanFactory] = Field(None, title="AutowireCapable Bean 工厂",
                                                                                alias="autowireCapableBeanFactory")
    environment: Optional[Environment] = Field(None, title="环境信息")
    bean_definition_count: Optional[int] = Field(None, title="Bean 定义数量", alias="beanDefinitionCount")
    bean_definition_names: Optional[List[str]] = Field(None, title="Bean 定义名称列表", alias="beanDefinitionNames")
    parent_bean_factory: Optional[BeanFactory] = Field(None, title="父 Bean 工厂", alias="parentBeanFactory")
    class_loader: Optional[ClassLoaderDescriptor] = Field(None, title="类加载器", alias="classLoader")


class FilterRegistration(CustomBaseModel):
    """Servlet 过滤器注册信息"""
    servlet_name_mappings: Optional[List[str]] = Field(None, title="Servlet 名称映射", alias="servletNameMappings")
    url_pattern_mappings: Optional[List[str]] = Field(None, title="URL 模式映射", alias="urlPatternMappings")
    name: Optional[str] = Field(None, title="过滤器名称")
    class_name: Optional[str] = Field(None, title="过滤器类名", alias="className")
    init_parameters: Optional[Dict[str, str]] = Field(None, title="初始化参数", alias="initParameters")


class HttpStatusCode(CustomBaseModel):
    """HTTP 状态码详情"""
    error: Optional[bool] = Field(None, title="是否为错误状态")
    is_4xx_client_error: Optional[bool] = Field(None, title="是否为 4xx 客户端错误", alias="is4xxClientError")
    is_5xx_server_error: Optional[bool] = Field(None, title="是否为 5xx 服务器错误", alias="is5xxServerError")
    is_1xx_informational: Optional[bool] = Field(None, title="是否为 1xx 信息性状态", alias="is1xxInformational")
    is_2xx_successful: Optional[bool] = Field(None, title="是否为 2xx 成功状态", alias="is2xxSuccessful")
    is_3xx_redirection: Optional[bool] = Field(None, title="是否为 3xx 重定向状态", alias="is3xxRedirection")


class TaglibDescriptor(CustomBaseModel):
    """JSP 标签库描述符"""
    taglib_uri: Optional[str] = Field(None, title="标签库 URI", alias="taglibURI")
    taglib_location: Optional[str] = Field(None, title="标签库位置", alias="taglibLocation")


class JspPropertyGroupDescriptor(CustomBaseModel):
    """JSP 属性组描述符"""
    buffer: Optional[str] = Field(None, title="缓冲区大小")
    el_ignored: Optional[str] = Field(None, title="是否忽略 EL 表达式", alias="elIgnored")
    is_xml: Optional[str] = Field(None, title="是否为 XML 格式", alias="isXml")
    url_patterns: Optional[List[str]] = Field(None, title="URL 模式", alias="urlPatterns")
    default_content_type: Optional[str] = Field(None, title="默认内容类型", alias="defaultContentType")
    include_codas: Optional[List[str]] = Field(None, title="包含的 Coda", alias="includeCodas")
    include_preludes: Optional[List[str]] = Field(None, title="包含的 Prelude", alias="includePreludes")
    page_encoding: Optional[str] = Field(None, title="页面编码", alias="pageEncoding")
    error_on_el_not_found: Optional[str] = Field(None, title="EL 未找到时是否报错", alias="errorOnELNotFound")
    scripting_invalid: Optional[str] = Field(None, title="脚本是否无效", alias="scriptingInvalid")
    deferred_syntax_allowed_as_literal: Optional[str] = Field(None, title="是否允许延迟语法作为字面量",
                                                              alias="deferredSyntaxAllowedAsLiteral")
    trim_directive_whitespaces: Optional[str] = Field(None, title="是否去除指令间的空格",
                                                      alias="trimDirectiveWhitespaces")
    error_on_undeclared_namespace: Optional[str] = Field(None, title="未声明命名空间时是否报错",
                                                         alias="errorOnUndeclaredNamespace")


class JspConfigDescriptor(CustomBaseModel):
    """JSP 配置描述符"""
    taglibs: Optional[List[TaglibDescriptor]] = Field(None, title="标签库描述符列表")
    jsp_property_groups: Optional[List[JspPropertyGroupDescriptor]] = Field(None, title="JSP 属性组描述符列表",
                                                                            alias="jspPropertyGroups")


class ServletRegistration(CustomBaseModel):
    """Servlet 注册信息"""
    run_as_role: Optional[str] = Field(None, title="运行角色", alias="runAsRole")
    mappings: Optional[List[str]] = Field(None, title="URL 映射")
    name: Optional[str] = Field(None, title="Servlet 名称")
    class_name: Optional[str] = Field(None, title="Servlet 类名", alias="className")
    init_parameters: Optional[Dict[str, str]] = Field(None, title="初始化参数", alias="initParameters")


class SessionCookieConfig(CustomBaseModel):
    """会话 Cookie 配置"""
    max_age: Optional[int] = Field(None, title="最大生命周期", alias="maxAge")
    path: Optional[str] = Field(None, title="路径")
    domain: Optional[str] = Field(None, title="域名")
    name: Optional[str] = Field(None, title="Cookie 名称")
    attributes: Optional[Dict[str, str]] = Field(None, title="属性")
    comment: Optional[str] = Field(None, title="备注", deprecated=True)
    http_only: Optional[bool] = Field(None, title="是否为 HttpOnly", alias="httpOnly")
    secure: Optional[bool] = Field(None, title="是否为 Secure")


class ServletContext(CustomBaseModel):
    """Servlet 上下文信息"""
    class_loader: Optional[ClassLoaderDescriptor] = Field(None, title="类加载器", alias="classLoader")
    major_version: Optional[int] = Field(None, title="主版本号", alias="majorVersion")
    minor_version: Optional[int] = Field(None, title="次版本号", alias="minorVersion")
    server_info: Optional[str] = Field(None, title="服务器信息", alias="serverInfo")
    context_path: Optional[str] = Field(None, title="上下文路径", alias="contextPath")
    attribute_names: Optional[Dict[str, Any]] = Field(None, title="属性名称", alias="attributeNames")
    init_parameter_names: Optional[Dict[str, Any]] = Field(None, title="初始化参数名称", alias="initParameterNames")
    session_timeout: Optional[int] = Field(None, title="会话超时时间(分钟)", alias="sessionTimeout")
    session_cookie_config: Optional[SessionCookieConfig] = Field(None, title="会话 Cookie 配置",
                                                                 alias="sessionCookieConfig")
    virtual_server_name: Optional[str] = Field(None, title="虚拟服务器名称", alias="virtualServerName")
    servlet_context_name: Optional[str] = Field(None, title="Servlet 上下文名称", alias="servletContextName")
    filter_registrations: Optional[Dict[str, FilterRegistration]] = Field(None, title="过滤器注册信息",
                                                                          alias="filterRegistrations")
    jsp_config_descriptor: Optional[JspConfigDescriptor] = Field(None, title="JSP 配置描述符",
                                                                 alias="jspConfigDescriptor")
    effective_major_version: Optional[int] = Field(None, title="有效主版本号", alias="effectiveMajorVersion")
    effective_minor_version: Optional[int] = Field(None, title="有效次版本号", alias="effectiveMinorVersion")
    servlet_registrations: Optional[Dict[str, ServletRegistration]] = Field(None, title="Servlet 注册信息",
                                                                            alias="servletRegistrations")
    session_tracking_modes: Optional[List[SessionTrackingModeEnum]] = Field(None, title="会话跟踪模式",
                                                                            alias="sessionTrackingModes")
    default_session_tracking_modes: Optional[List[SessionTrackingModeEnum]] = Field(None, title="默认会话跟踪模式",
                                                                                    alias="defaultSessionTrackingModes")
    request_character_encoding: Optional[str] = Field(None, title="请求字符编码", alias="requestCharacterEncoding")
    response_character_encoding: Optional[str] = Field(None, title="响应字符编码", alias="responseCharacterEncoding")
    effective_session_tracking_modes: Optional[List[SessionTrackingModeEnum]] = Field(None, title="有效会话跟踪模式",
                                                                                      alias="effectiveSessionTrackingModes")


class RedirectView(CustomBaseModel):
    """Spring 重定向视图"""
    application_context: Optional[ApplicationContext] = Field(None, alias="applicationContext")
    servlet_context: Optional[ServletContext] = Field(None, alias="servletContext")
    content_type: Optional[str] = Field(None, alias="contentType")
    request_context_attribute: Optional[str] = Field(None, alias="requestContextAttribute")
    static_attributes: Optional[Dict[str, Any]] = Field(None, alias="staticAttributes")
    expose_path_variables: Optional[bool] = Field(None, alias="exposePathVariables")
    expose_context_beans_as_attributes: Optional[bool] = Field(None, alias="exposeContextBeansAsAttributes")
    exposed_context_bean_names: Optional[List[str]] = Field(None, alias="exposedContextBeanNames")
    bean_name: Optional[str] = Field(None, alias="beanName")
    url: Optional[str] = Field(None)
    context_relative: Optional[bool] = Field(None, alias="contextRelative")
    http_10_compatible: Optional[bool] = Field(None, alias="http10Compatible")
    expose_model_attributes: Optional[bool] = Field(None, alias="exposeModelAttributes")
    encoding_scheme: Optional[str] = Field(None, alias="encodingScheme")
    status_code: Optional[HttpStatusCode] = Field(None, alias="statusCode")
    expand_uri_template_variables: Optional[bool] = Field(None, alias="expandUriTemplateVariables")
    propagate_query_params: Optional[bool] = Field(None, alias="propagateQueryParams")
    hosts: Optional[List[str]] = Field(None)
    redirect_view: Optional[bool] = Field(None, alias="redirectView")
    propagate_query_properties: Optional[bool] = Field(None, alias="propagateQueryProperties")
    attributes: Optional[Dict[str, str]] = Field(None)
    attributes_map: Optional[Dict[str, Any]] = Field(None, alias="attributesMap")
    attributes_csv: Optional[str] = Field(None, alias="attributesCSV")


# =======================================================================
#  请求模型 (Request Models)
# =======================================================================

class FileListRequest(CustomBaseModel):
    """获取文件夹下文件列表请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="请求路径")
    password: Optional[str] = Field(None, title="文件夹密码")
    order_by: Optional[str] = Field(None, alias="orderBy")
    order_direction: Optional[str] = Field(None, alias="orderDirection")


class FileListConfigRequest(CustomBaseModel):
    """获取文件夹参数请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="请求路径")
    password: Optional[str] = Field(None, title="文件夹密码")


class BatchGenerateLinkRequest(CustomBaseModel):
    """批量生成直链请求类"""
    storage_key: str = Field(..., alias="storageKey")
    paths: List[str]
    expire_time: int = Field(..., alias="expireTime")


class InstallSystemRequest(CustomBaseModel):
    """系统初始化请求类"""
    site_name: Optional[str] = Field(None, title="站点名称", alias="siteName")
    username: Optional[str] = Field(None, title="用户名")
    password: Optional[str] = Field(None, title="密码")


class BatchMoveOrCopyFileRequest(CustomBaseModel):
    """(移动/复制)(文件/文件夹)请求"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: str = Field(..., title="请求路径")
    name_list: List[str] = Field(..., title="文件夹名称", alias="nameList")
    target_path: str = Field(..., title="目标路径", alias="targetPath")
    target_name_list: List[str] = Field(..., title="目标文件夹名称", alias="targetNameList")
    src_path_password: Optional[str] = Field(None, title="源文件夹密码", alias="srcPathPassword")
    target_path_password: Optional[str] = Field(None, title="目标文件夹密码", alias="targetPathPassword")


class ResetAdminUserNameAndPasswordRequest(CustomBaseModel):
    """重置管理员用户名和密码请求"""
    username: str
    password: str


class UpdateUserPwdRequest(CustomBaseModel):
    """更新用户密码请求"""
    old_password: Optional[str] = Field(None, alias="oldPassword", title="旧密码")
    new_password: str = Field(..., alias="newPassword", title="新密码")
    confirm_password: str = Field(..., alias="confirmPassword", title="确认新密码")


class UserLoginRequest(CustomBaseModel):
    """用户登录请求参数类"""
    username: str = Field(..., title="用户名")
    password: str = Field(..., title="密码")
    verify_code: Optional[str] = Field(None, title="验证码", alias="verifyCode")
    verify_code_uuid: Optional[str] = Field(None, title="验证码 UUID", alias="verifyCodeUUID")


class SharePointSearchSitesRequest(CustomBaseModel):
    """SharePoint 搜索站点请求"""
    type: Optional[str] = None
    access_token: str = Field(..., title="访问令牌", alias="accessToken")


class SharePointSiteListsRequest(CustomBaseModel):
    """SharePoint 站点列表请求"""
    type: Optional[str] = None
    access_token: str = Field(..., title="访问令牌", alias="accessToken")
    site_id: str = Field(..., title="站点 ID", alias="siteId")


class SharePointInfoRequest(CustomBaseModel):
    """SharePoint 信息请求类"""
    type: str = Field(..., title="SharePoint 类型")
    access_token: str = Field(..., title="访问令牌", alias="accessToken")
    domain_prefix: str = Field(..., title="域名前缀", alias="domainPrefix")
    site_type: str = Field(..., title="站点类型", alias="siteType")
    site_name: str = Field(..., title="站点名称", alias="siteName")
    domain_type: Optional[str] = Field(None, title="域名类型", alias="domainType")


class GetS3CorsListRequest(CustomBaseModel):
    """S3 bucket 列表请求类"""
    access_key: str = Field(..., title="accessKey", alias="accessKey")
    secret_key: str = Field(..., title="secretKey", alias="secretKey")
    end_point: str = Field(..., title="Endpoint 接入点", alias="endPoint")
    region: str = Field(..., title="Endpoint 接入点")
    bucket_name: str = Field(..., title="存储桶名称", alias="bucketName")


class GetS3BucketListRequest(CustomBaseModel):
    """S3 bucket 列表请求类"""
    access_key: str = Field(..., title="accessKey", alias="accessKey")
    secret_key: str = Field(..., title="secretKey", alias="secretKey")
    end_point: str = Field(..., title="Endpoint 接入点", alias="endPoint")
    region: str = Field(..., title="Endpoint 接入点")


class FileItemRequest(CustomBaseModel):
    """获取指定文件信息的请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="请求路径")
    password: Optional[str] = Field(None, title="文件夹密码")


class GetGoogleDriveListRequest(CustomBaseModel):
    """gd drive 列表请求类"""
    access_token: str = Field(..., title="accessToken", alias="accessToken")


class SearchStorageRequest(CustomBaseModel):
    """搜索存储源中文件请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    search_keyword: str = Field(..., title="搜索关键字", alias="searchKeyword")
    search_mode: SearchModeEnum = Field(..., title="搜索模式", alias="searchMode")
    path: Optional[str] = Field(None, title="搜索路径")
    password_cache: Optional[Dict[str, str]] = Field(None, title="密码缓存", alias="passwordCache")


class UploadFileRequest(CustomBaseModel):
    """上传文件请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="上传路径")
    name: str = Field(..., title="上传的文件名")
    size: Optional[int] = Field(None, title="文件大小")
    password: Optional[str] = Field(None, title="文件夹密码")


class RenameFolderRequest(CustomBaseModel):
    """重命名文件夹请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="请求路径")
    name: str = Field(..., title="重命名的原文件夹名称")
    new_name: str = Field(..., title="重命名后的文件名称", alias="newName")
    password: Optional[str] = Field(None, title="文件夹密码")


class RenameFileRequest(CustomBaseModel):
    """重命名文件请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="请求路径")
    name: str = Field(..., title="重命名的原文件名称")
    new_name: str = Field(..., title="重命名后的文件名称", alias="newName")
    password: Optional[str] = Field(None, title="文件夹密码")


class NewFolderRequest(CustomBaseModel):
    """新建文件夹请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="请求路径")
    name: str = Field(..., title="新建的文件夹名称")
    password: Optional[str] = Field(None, title="文件夹密码")


class FrontBatchDeleteRequest(CustomBaseModel):
    """删除文件夹请求类"""
    storage_key: str = Field(..., title="存储源 key", alias="storageKey")
    delete_items: List[DeleteItem] = Field(..., title="删除的文件详情", alias="deleteItems")


class UpdateWebDAVRequest(CustomBaseModel):
    """WebDAV 设置请求参数类"""
    webdav_enable: Optional[bool] = Field(None, title="启用 WebDAV", alias="webdavEnable")
    webdav_proxy: Optional[bool] = Field(None, title="WebDAV 服务器中转下载", alias="webdavProxy")
    webdav_username: Optional[str] = Field(None, title="WebDAV 账号", alias="webdavUsername")
    webdav_password: Optional[str] = Field(None, title="WebDAV 密码", alias="webdavPassword")


class UpdateViewSettingRequest(CustomBaseModel):
    """显示设置请求参数类"""
    root_show_storage: bool = Field(..., title="根目录是否显示所有存储源",
                                    description="勾选则根目录显示所有存储源列表, 反之会自动显示第一个存储源的内容.",
                                    alias="rootShowStorage")
    layout: str = Field(..., title="页面布局", description="full:全屏,center:居中")
    mobile_layout: Optional[str] = Field(None, title="移动端页面布局", description="full:全屏,center:居中",
                                         alias="mobileLayout")
    table_size: str = Field(..., title="列表尺寸", description="large:大,default:中,small:小", alias="tableSize")
    custom_video_suffix: Optional[str] = Field(None, title="自定义视频文件后缀格式", alias="customVideoSuffix")
    custom_image_suffix: Optional[str] = Field(None, title="自定义图像文件后缀格式", alias="customImageSuffix")
    custom_audio_suffix: Optional[str] = Field(None, title="自定义音频文件后缀格式", alias="customAudioSuffix")
    custom_text_suffix: Optional[str] = Field(None, title="自定义文本文件后缀格式", alias="customTextSuffix")
    custom_office_suffix: Optional[str] = Field(None, title="自定义Office后缀格式", alias="customOfficeSuffix")
    custom_kk_file_view_suffix: Optional[str] = Field(None, title="自定义kkFileView后缀格式",
                                                      alias="customKkFileViewSuffix")
    show_document: bool = Field(..., title="是否显示文档区", alias="showDocument")
    show_announcement: bool = Field(..., title="是否显示网站公告", alias="showAnnouncement")
    announcement: Optional[str] = Field(None, title="网站公告")
    custom_css: Optional[str] = Field(None, title="自定义 CSS", alias="customCss")
    custom_js: Optional[str] = Field(None, title="自定义 JS", alias="customJs")
    file_click_mode: Optional[FileClickModeEnum] = Field(None, title="默认文件点击习惯", alias="fileClickMode")
    mobile_file_click_mode: Optional[FileClickModeEnum] = Field(None, title="移动端默认文件点击习惯",
                                                                alias="mobileFileClickMode")
    only_office_url: Optional[str] = Field(None, title="onlyOffice 在线预览地址", alias="onlyOfficeUrl")
    only_office_secret: Optional[str] = Field(None, title="onlyOffice Secret", alias="onlyOfficeSecret")
    kk_file_view_url: Optional[str] = Field(None, title="kkFileView 在线预览地址", alias="kkFileViewUrl")
    kk_file_view_open_mode: Optional[str] = Field(None, title="kkFileView 预览方式", alias="kkFileViewOpenMode")
    max_show_size: Optional[int] = Field(None, title="默认最大显示文件数", alias="maxShowSize")
    load_more_size: Optional[int] = Field(None, title="每次加载更多文件数", alias="loadMoreSize")
    default_sort_field: Optional[str] = Field(None, title="默认排序字段", alias="defaultSortField")
    default_sort_order: Optional[str] = Field(None, title="默认排序方向", alias="defaultSortOrder")
    default_save_pwd: Optional[bool] = Field(None, title="是否默认记住密码", alias="defaultSavePwd")
    enable_hover_menu: Optional[bool] = Field(None, title="是否启用 hover 菜单", deprecated=True,
                                              alias="enableHoverMenu")


class UpdateSiteSettingRequest(CustomBaseModel):
    """站点设置请求参数类"""
    site_name: str = Field(..., title="站点名称", alias="siteName")
    force_backend_address: Optional[str] = Field(None, title="强制后端地址",
                                                 description="强制指定生成直链，短链，获取回调地址时的地址。",
                                                 alias="forceBackendAddress")
    front_domain: Optional[str] = Field(None, title="前端域名", description="前端域名，前后端分离情况下需要配置.",
                                        alias="frontDomain")
    avatar: Optional[str] = Field(None, title="头像地址")
    icp: Optional[str] = Field(None, title="备案号")
    auth_code: Optional[str] = Field(None, title="授权码", alias="authCode")
    max_file_uploads: Optional[int] = Field(None, title="最大同时上传文件数", alias="maxFileUploads")
    site_home_name: Optional[str] = Field(None, title="站点 Home 名称", alias="siteHomeName")
    site_home_logo: Optional[str] = Field(None, title="站点 Home Logo", alias="siteHomeLogo")
    site_home_logo_link: Optional[str] = Field(None, title="站点 Logo 点击后链接", alias="siteHomeLogoLink")
    site_home_logo_target_mode: Optional[str] = Field(None, title="站点 Logo 链接打开方式",
                                                      alias="siteHomeLogoTargetMode")
    favicon_url: Optional[str] = Field(None, title="网站 favicon 图标地址", alias="faviconUrl")
    site_admin_logo_target_mode: Optional[str] = Field(None, title="管理员页面点击 Logo 回到首页打开方式",
                                                       alias="siteAdminLogoTargetMode")
    site_admin_version_open_change_log: Optional[bool] = Field(None, title="管理员页面点击版本号打开更新日志",
                                                               alias="siteAdminVersionOpenChangeLog")


class UpdateSecuritySettingRequest(CustomBaseModel):
    """登陆安全设置请求参数类"""
    show_login: Optional[bool] = Field(None, title="是否在前台显示登陆按钮", alias="showLogin")
    login_log_mode: Optional[LoginLogModeEnum] = Field(None, title="登录日志模式", alias="loginLogMode")
    login_img_verify: Optional[bool] = Field(None, title="是否启用登陆验证码", alias="loginImgVerify")
    admin_two_factor_verify: Optional[bool] = Field(None, title="是否为管理员启用双因素认证",
                                                    alias="adminTwoFactorVerify")
    login_verify_secret: Optional[str] = Field(None, title="2FA登陆验证 Secret", alias="loginVerifySecret")
    guest_index_html: Optional[str] = Field(None, title="匿名用户首页显示内容", alias="guestIndexHtml")


class UpdateLinkSettingRequest(CustomBaseModel):
    """直链设置请求参数类"""
    record_download_log: Optional[bool] = Field(None, title="是否记录下载日志", alias="recordDownloadLog")
    referer_type: Optional[RefererTypeEnum] = Field(None, title="直链 Referer 防盗链类型", alias="refererType")
    referer_allow_empty: Optional[bool] = Field(None, title="直链 Referer 是否允许为空", alias="refererAllowEmpty")
    referer_value: Optional[str] = Field(None, title="直链 Referer 值", alias="refererValue")
    direct_link_prefix: str = Field(..., title="直链地址前缀", alias="directLinkPrefix")
    show_link_btn: bool = Field(..., title="是否显示生成直链功能（含直链和路径短链）", alias="showLinkBtn")
    show_short_link: bool = Field(..., title="是否显示生成短链功能", alias="showShortLink")
    show_path_link: bool = Field(..., title="是否显示生成路径链接功能", alias="showPathLink")
    allow_path_link_anon_access: bool = Field(..., title="是否允许路径直链可直接访问", alias="allowPathLinkAnonAccess")
    link_limit_second: Optional[int] = Field(None, title="限制直链下载秒数", alias="linkLimitSecond")
    link_download_limit: Optional[int] = Field(None, title="限制直链下载次数", alias="linkDownloadLimit")
    link_expire_times: Optional[List[LinkExpireDTO]] = Field(None, title="短链过期时间设置", alias="linkExpireTimes")


class UpdateAccessSettingRequest(CustomBaseModel):
    """站点访问控制参数类"""
    access_ip_blocklist: Optional[str] = Field(None, title="访问 ip 黑名单", alias="accessIpBlocklist")
    access_ua_blocklist: Optional[str] = Field(None, title="访问 ua 黑名单", alias="accessUaBlocklist")


class UserStorageSource(CustomBaseModel):
    """授予给用户的存储策略列表"""
    id: Optional[int] = None
    user_id: Optional[int] = Field(None, alias="userId")
    storage_source_id: Optional[int] = Field(None, alias="storageSourceId")
    root_path: Optional[str] = Field(None, alias="rootPath")
    enable: Optional[bool] = None
    permissions: Optional[Set[str]] = None


class SaveUserRequest(CustomBaseModel):
    """保存用户请求类"""
    id: Optional[int] = Field(None, title="用户 id")
    username: Optional[str] = Field(None, title="用户名")
    nickname: Optional[str] = Field(None, title="昵称")
    password: Optional[str] = Field(None, title="密码")
    salt: Optional[str] = Field(None, title="盐")
    default_permissions: Optional[Set[str]] = Field(None, title="用户默认权限",
                                                    description="当新增存储源时, 自动授予该用户新存储源的权限.",
                                                    alias="defaultPermissions")
    user_storage_source_list: Optional[List[UserStorageSource]] = Field(None, title="授予给用户的存储策略列表",
                                                                        alias="userStorageSourceList")
    enable: Optional[bool] = Field(None, title="是否启用")


class User(CustomBaseModel):
    """用户响应数据"""
    id: Optional[int] = None
    username: Optional[str] = None
    nickname: Optional[str] = None
    enable: Optional[bool] = None
    create_time: Optional[datetime] = Field(None, alias="createTime")
    update_time: Optional[datetime] = Field(None, alias="updateTime")
    default_permissions: Optional[Set[str]] = Field(None, alias="defaultPermissions")


class UserUploadRule(CustomBaseModel):
    """用户上传规则"""
    id: Optional[int] = None
    user_id: Optional[int] = Field(None, alias="userId")
    rule_upload_id: Optional[int] = Field(None, alias="ruleUploadId")
    storage_allow_mode: Optional[AllowModeEnum] = Field(None, alias="storageAllowMode")
    storage_ids: Optional[Set[int]] = Field(None, alias="storageIds")
    create_time: Optional[datetime] = Field(None, alias="createTime")
    update_time: Optional[datetime] = Field(None, alias="updateTime")


class UserViewRule(CustomBaseModel):
    """用户查看规则"""
    id: Optional[int] = None
    user_id: Optional[int] = Field(None, alias="userId")
    rule_view_id: Optional[int] = Field(None, alias="ruleViewId")
    storage_allow_mode: Optional[AllowModeEnum] = Field(None, alias="storageAllowMode")
    storage_ids: Optional[Set[int]] = Field(None, alias="storageIds")
    create_time: Optional[datetime] = Field(None, alias="createTime")
    update_time: Optional[datetime] = Field(None, alias="updateTime")


class UserRuleSettingDTO(CustomBaseModel):
    """用户规则设置"""
    id: Optional[int] = None
    user_id: Optional[int] = Field(None, alias="userId")
    upload_rule_allow_mode: Optional[AllowModeEnum] = Field(None, alias="uploadRuleAllowMode")
    upload_rule_apply_to_rename: Optional[bool] = Field(None, alias="uploadRuleApplyToRename")
    view_rule_allow_mode: Optional[AllowModeEnum] = Field(None, alias="viewRuleAllowMode")
    upload_rule_list: Optional[List[UserUploadRule]] = Field(None, alias="uploadRuleList")
    view_rule_list: Optional[List[UserViewRule]] = Field(None, alias="viewRuleList")


class CopyUserRequest(CustomBaseModel):
    """复制用户名请求类"""
    from_id: int = Field(..., title="存储源 ID", alias="fromId")
    to_username: str = Field(..., title="复制后用户名", alias="toUsername")
    to_nickname: str = Field(..., title="复制后用户昵称", alias="toNickname")
    to_password: str = Field(..., title="复制后用户密码", alias="toPassword")


class StorageSourceAllParamDTO(CustomBaseModel):
    """存储源所有拓展参数"""
    end_point: Optional[str] = Field(None, title="Endpoint 接入点", alias="endPoint")
    end_point_scheme: Optional[str] = Field(None, title="Endpoint 接入点协议", alias="endPointScheme")
    path_style: Optional[str] = Field(None, title="路径风格", alias="pathStyle")
    is_private: Optional[bool] = Field(None, title="是否是私有空间", alias="isPrivate")
    proxy_private: Optional[bool] = Field(None, title="代理下载生成签名链接", alias="proxyPrivate")
    access_key: Optional[str] = Field(None, title="accessKey", alias="accessKey")
    secret_key: Optional[str] = Field(None, title="secretKey", alias="secretKey")
    bucket_name: Optional[str] = Field(None, title="bucket 名称", alias="bucketName")
    origin_bucket_name: Optional[str] = Field(None, title="原 bucket 名称", alias="originBucketName")
    host: Optional[str] = Field(None, title="域名或 IP")
    port: Optional[str] = Field(None, title="端口")
    access_token: Optional[str] = Field(None, title="访问令牌", alias="accessToken")
    refresh_token: Optional[str] = Field(None, title="刷新令牌", alias="refreshToken")
    secret_id: Optional[str] = Field(None, title="secretId", alias="secretId")
    file_path: Optional[str] = Field(None, title="文件路径", alias="filePath")
    username: Optional[str] = Field(None, title="用户名")
    password: Optional[str] = Field(None, title="密码")
    private_key: Optional[str] = Field(None, title="密钥", alias="privateKey")
    passphrase: Optional[str] = Field(None, title="密钥 passphrase")
    domain: Optional[str] = Field(None, title="域名")
    base_path: Optional[str] = Field(None, title="基路径", alias="basePath")
    token: Optional[str] = Field(None, title="token")
    token_time: Optional[int] = Field(None, title="token 有效期", alias="tokenTime")
    proxy_token_time: Optional[int] = Field(None, title="token 有效期", alias="proxyTokenTime")
    site_id: Optional[str] = Field(None, title="siteId", alias="siteId")
    list_id: Optional[str] = Field(None, title="listId", alias="listId")
    site_name: Optional[str] = Field(None, title="站点名称", alias="siteName")
    site_type: Optional[str] = Field(None, title="站点类型", alias="siteType")
    proxy_domain: Optional[str] = Field(None, title="下载反代域名", alias="proxyDomain")
    download_link_type: Optional[str] = Field(None, title="下载链接类型", alias="downloadLinkType")
    client_id: Optional[str] = Field(None, title="clientId", alias="clientId")
    client_secret: Optional[str] = Field(None, title="clientSecret", alias="clientSecret")
    redirect_uri: Optional[str] = Field(None, title="回调地址", alias="redirectUri")
    region: Optional[str] = Field(None, title="区域")
    url: Optional[str] = Field(None, title="url")
    encoding: Optional[str] = Field(None, title="编码格式")
    limit_speed: Optional[int] = Field(None, title="单连接限速",
                                       description="可限制单连接的下载速度, 单位为 KB/s. (多线程下载, 则为每个线程最大速度)",
                                       alias="limitSpeed")
    proxy_limit_speed: Optional[int] = Field(None, title="单连接限速",
                                             description="可限制单连接的下载速度, 单位为 KB/s. (多线程下载, 则为每个线程最大速度)",
                                             alias="proxyLimitSpeed")
    enable_range: Optional[bool] = Field(None, title="允许多线程下载", alias="enableRange")
    drive_id: Optional[str] = Field(None, title="存储源 ID", alias="driveId")
    enable_proxy_upload: Optional[bool] = Field(None, title="启用代理上传", alias="enableProxyUpload")
    enable_proxy_download: Optional[bool] = Field(None, title="启用代理下载", alias="enableProxyDownload")
    redirect_mode: Optional[bool] = Field(None, title="下载重定向模式", alias="redirectMode")
    ftp_mode: Optional[str] = Field(None, title="FTP 模式", alias="ftpMode")
    proxy_upload_timeout_second: Optional[int] = Field(None, title="代理上传超时时间(秒)",
                                                       alias="proxyUploadTimeoutSecond")
    max_connections: Optional[int] = Field(None, title="最大连接数", alias="maxConnections")
    proxy_link_force_download: Optional[bool] = Field(None, title="下载链接强制下载", alias="proxyLinkForceDownload")
    cors_config_list: Optional[str] = Field(None, title="S3 跨域配置", alias="corsConfigList")


class SaveStorageSourceRequest(CustomBaseModel):
    """存储源基本参数"""
    id: Optional[int] = Field(None, title="ID, 新增无需填写")
    name: Optional[str] = Field(None, title="存储源名称")
    key: Optional[str] = Field(None, title="存储源别名")
    remark: Optional[str] = Field(None, title="存储源备注")
    type: Optional[StorageTypeEnum] = Field(None, title="存储源类型")
    enable: Optional[bool] = Field(None, title="是否启用")
    enable_file_operator: Optional[bool] = Field(None, title="是否启用文件操作功能",
                                                 description="是否启用文件上传，编辑，删除等操作.",
                                                 alias="enableFileOperator")
    enable_file_anno_operator: Optional[bool] = Field(None, title="是否允许匿名进行文件操作",
                                                      description="是否允许匿名进行文件上传，编辑，删除等操作.",
                                                      alias="enableFileAnnoOperator")
    enable_cache: Optional[bool] = Field(None, title="是否开启缓存", alias="enableCache")
    auto_refresh_cache: Optional[bool] = Field(None, title="是否开启缓存自动刷新", alias="autoRefreshCache")
    search_enable: Optional[bool] = Field(None, title="是否开启搜索", alias="searchEnable")
    search_ignore_case: Optional[bool] = Field(None, title="搜索是否忽略大小写", alias="searchIgnoreCase")
    search_mode: Optional[StorageSearchModeEnum] = Field(None, title="搜索模式",
                                                         description="仅从缓存中搜索或直接全量搜索", alias="searchMode")
    order_num: Optional[int] = Field(None, title="排序值", alias="orderNum")
    storage_source_all_param: Optional[StorageSourceAllParamDTO] = Field(None, alias="storageSourceAllParam")
    default_switch_to_img_mode: Optional[bool] = Field(None, title="是否默认开启图片模式",
                                                       alias="defaultSwitchToImgMode")
    compatibility_readme: Optional[bool] = Field(None, title="兼容 readme 模式",
                                                 description="兼容模式, 目录文档读取 readme.md 文件",
                                                 alias="compatibilityReadme")


class ReadmeConfig(CustomBaseModel):
    """readme 文档配置"""
    id: Optional[int] = Field(None, title="ID, 新增无需填写")
    storage_id: Optional[int] = Field(None, title="存储源 ID", alias="storageId")
    description: str = Field(..., title="表达式描述")
    expression: Optional[str] = Field(None, title="路径表达式")
    readme_text: Optional[str] = Field(None, title="readme 文本内容, 支持 md 语法.", alias="readmeText")
    display_mode: ReadmeDisplayModeEnum = Field(..., title="显示模式", alias="displayMode")


class PasswordConfig(CustomBaseModel):
    """密码设置"""
    id: Optional[int] = Field(None, title="ID, 新增无需填写")
    storage_id: int = Field(..., title="存储源 ID", alias="storageId")
    expression: str = Field(..., title="密码文件夹表达式")
    password: str = Field(..., title="密码值")
    description: str = Field(..., title="表达式描述")


class FilterConfig(CustomBaseModel):
    """存储源过滤配置"""
    id: Optional[int] = Field(None, title="ID, 新增无需填写")
    storage_id: int = Field(..., title="存储源 ID", alias="storageId")
    expression: str = Field(..., title="过滤表达式")
    description: str = Field(..., title="表达式描述")
    mode: FilterModeEnum = Field(..., title="模式")


class UpdateStorageSortRequest(CustomBaseModel):
    """更新存储源排序值请求类"""
    id: int = Field(..., title="存储源 ID")
    order_num: int = Field(..., title="排序值，值越小越靠前", alias="orderNum")


class CopyStorageSourceRequest(CustomBaseModel):
    """复制存储源请求请求类"""
    from_id: int = Field(..., title="存储源 ID", alias="fromId")
    to_name: str = Field(..., title="复制后存储源名称", alias="toName")
    to_key: str = Field(..., title="复制后存储源别名", alias="toKey")


class SsoConfig(CustomBaseModel):
    """单点登录厂商配置"""
    id: Optional[int] = None
    provider: str = Field(..., title="OIDC/OAuth2 厂商名", description="简称，仅可包含数字、字母，-，_")
    name: str = Field(..., title="显示名称", description="登录页悬浮到图标上的名称")
    icon: str = Field(..., title="ICON", description="登录页显示的图标，支持 URL、SVG、Base64 格式")
    client_id: str = Field(..., title="在 SSO 厂商处生成的 ID", alias="clientId")
    client_secret: str = Field(..., title="在 SSO 厂商处生成的密钥", alias="clientSecret")
    auth_url: str = Field(..., title="SSO 厂商提供的授权端点", alias="authUrl")
    token_url: str = Field(..., title="SSO 厂商提供的 Token 端点", alias="tokenUrl")
    user_info_url: str = Field(..., title="SSO 厂商提供的用户信息端点", alias="userInfoUrl")
    scope: str = Field(..., title="SSO 厂商提供的授权范围")
    binding_field: str = Field(..., title="SSO 系统中用户与本系统中用户互相的绑定字段", alias="bindingField")
    enabled: bool = Field(..., title="是否启用")
    order_num: Optional[int] = Field(None, title="排序", description="数字越小越靠前", alias="orderNum")


class RuleViewItem(CustomBaseModel):
    """查看规则项"""
    id: Optional[int] = None
    rule_view_id: Optional[int] = Field(None, alias="ruleViewId")
    rule_type: Optional[RuleTypeEnum] = Field(None, alias="ruleType")
    rule_expression: Optional[str] = Field(None, alias="ruleExpression")
    match_mode: Optional[MatchModeEnum] = Field(None, alias="matchMode")
    match_type: Optional[MatchTypeEnum] = Field(None, alias="matchType")
    rule_description: Optional[str] = Field(None, alias="ruleDescription")
    create_time: Optional[datetime] = Field(None, alias="createTime")
    update_time: Optional[datetime] = Field(None, alias="updateTime")


class TestViewRuleRequest(CustomBaseModel):
    """测试查看规则请求"""
    items: Optional[List[RuleViewItem]] = None
    full_path: Optional[str] = Field(None, alias="fullPath")
    file_type: Optional[str] = Field(None, alias="fileType")


class RuleDTORuleViewItem(CustomBaseModel):
    """查看规则 DTO"""
    id: Optional[int] = None
    name: Optional[str] = None
    remark: Optional[str] = None
    items: Optional[List[RuleViewItem]] = None


class RuleUploadItem(CustomBaseModel):
    """上传规则项"""
    id: Optional[int] = None
    rule_upload_id: Optional[int] = Field(None, alias="ruleUploadId")
    rule_type: Optional[RuleTypeEnum] = Field(None, alias="ruleType")
    rule_expression: Optional[str] = Field(None, alias="ruleExpression")
    match_mode: Optional[MatchModeEnum] = Field(None, alias="matchMode")
    rule_description: Optional[str] = Field(None, alias="ruleDescription")
    create_time: Optional[datetime] = Field(None, alias="createTime")
    update_time: Optional[datetime] = Field(None, alias="updateTime")


class TestUploadRuleRequest(CustomBaseModel):
    """测试上传规则请求"""
    items: Optional[List[RuleUploadItem]] = None
    folder_path: Optional[str] = Field(None, alias="folderPath")
    file_name: Optional[str] = Field(None, alias="fileName")


class RuleDTORuleUploadItem(CustomBaseModel):
    """上传规则 DTO"""
    id: Optional[int] = None
    name: Optional[str] = None
    remark: Optional[str] = None
    items: Optional[List[RuleUploadItem]] = None


class TestRuleMatcherRequest(CustomBaseModel):
    """测试规则匹配器请求"""
    rule_type: str = Field(..., alias="ruleType")
    rules: str = Field(...)
    test_value: str = Field(..., alias="testValue")


class AdminBatchDeleteRequest(CustomBaseModel):
    """批量删除请求"""
    ids: Optional[List[int]] = None


class QueryDownloadLogRequest(CustomBaseModel):
    """查询下载日志请求"""
    page: Optional[int] = Field(None, title="分页页数")
    limit: Optional[int] = Field(None, title="每页条数")
    order_by: Optional[str] = Field(None, title="排序字段", alias="orderBy")
    order_direction: Optional[str] = Field(None, title="排序顺序", alias="orderDirection")
    path: Optional[str] = Field(None, title="文件路径")
    storage_key: Optional[str] = Field(None, title="存储源 key", alias="storageKey")
    link_type: Optional[str] = Field(None, title="链接类型", alias="linkType")
    short_key: Optional[str] = Field(None, title="短链 key", alias="shortKey")
    search_date: Optional[List[datetime]] = Field(None, title="访问时间", alias="searchDate")
    ip: Optional[str] = Field(None, title="访问 ip")
    user_agent: Optional[str] = Field(None, title="访问 user_agent", alias="userAgent")
    referer: Optional[str] = Field(None, title="访问 referer")
    date_from: Optional[datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime] = Field(None, alias="dateTo")


class VerifyLoginTwoFactorAuthenticatorRequest(CustomBaseModel):
    """验证二步验证结果"""
    secret: str = Field(..., title="二步验证二维码")
    code: str = Field(..., title="APP 生成的二步验证验证码")


class UserStorageSourceDetailDTO(CustomBaseModel):
    """用户存储源详情 DTO"""
    id: Optional[int] = Field(None, title="id")
    user_id: Optional[int] = Field(None, title="用户 id", alias="userId")
    storage_source_id: Optional[int] = Field(None, title="存储源 ID", alias="storageSourceId")
    storage_source_name: Optional[str] = Field(None, title="存储源名称", alias="storageSourceName")
    storage_source_type: Optional[StorageTypeEnum] = Field(None, title="存储策略类型", alias="storageSourceType")
    root_path: Optional[str] = Field(None, title="允许访问的基础路径", alias="rootPath")
    enable: Optional[bool] = Field(None, title="是否启用")
    permissions: Optional[Set[str]] = Field(None, title="权限列表")


class UserDetailResponse(CustomBaseModel):
    """用户详情响应数据"""
    id: Optional[int] = None
    username: Optional[str] = None
    nickname: Optional[str] = None
    default_permissions: Optional[Set[str]] = Field(None, alias="defaultPermissions")
    user_storage_source_list: Optional[List[UserStorageSourceDetailDTO]] = Field(None, alias="userStorageSourceList")
    enable: Optional[bool] = None
    create_time: Optional[datetime] = Field(None, alias="createTime")


class QueryUserRequest(CustomBaseModel):
    """查询用户请求"""
    username: Optional[str] = Field(None, title="用户名")
    nickname: Optional[str] = Field(None, title="昵称")
    enable: Optional[bool] = Field(None, title="是否启用")
    search_date: Optional[List[datetime]] = Field(None, title="创建时间", alias="searchDate")
    sort_field: Optional[str] = Field(None, title="排序字段", alias="sortField")
    sort_asc: Optional[bool] = Field(None, title="排序方式", alias="sortAsc")
    hide_disabled_storage: Optional[bool] = Field(None, title="是否隐藏未启用的存储源", alias="hideDisabledStorage")
    date_from: Optional[datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime] = Field(None, alias="dateTo")


class CheckUserDuplicateRequest(CustomBaseModel):
    """检查用户重复请求"""
    id: Optional[int] = Field(None, title="用户 id")
    username: Optional[str] = Field(None, title="用户名")


class RefreshTokenInfoDTO(CustomBaseModel):
    """刷新 Token 信息 DTO"""
    access_token: Optional[str] = Field(None, alias="accessToken")
    refresh_token: Optional[str] = Field(None, alias="refreshToken")
    session_token: Optional[str] = Field(None, alias="sessionToken")
    expired_at: Optional[int] = Field(None, alias="expiredAt")
    expired_at_date: Optional[datetime] = Field(None, alias="expiredAtDate")


class RefreshTokenInfo(CustomBaseModel):
    """存储源刷新信息"""
    storage_id: Optional[int] = Field(None, alias="storageId")
    success: Optional[bool] = None
    last_refresh_time: Optional[datetime] = Field(None, alias="lastRefreshTime")
    msg: Optional[str] = None
    data: Optional[RefreshTokenInfoDTO] = None
    expired: Optional[bool] = None


class StorageSourceAdminResult(CustomBaseModel):
    """存储源设置后台管理 Result"""
    id: Optional[int] = Field(None, title="ID, 新增无需填写")
    enable: Optional[bool] = Field(None, title="是否启用")
    enable_file_operator: Optional[bool] = Field(None, title="是否启用文件操作功能",
                                                 description="是否启用文件上传，编辑，删除等操作.",
                                                 alias="enableFileOperator")
    enable_file_anno_operator: Optional[bool] = Field(None, title="是否允许匿名进行文件操作",
                                                      description="是否允许匿名进行文件上传，编辑，删除等操作.",
                                                      alias="enableFileAnnoOperator")
    enable_cache: Optional[bool] = Field(None, title="是否开启缓存", alias="enableCache")
    name: Optional[str] = Field(None, title="存储源名称")
    key: Optional[str] = Field(None, title="存储源别名")
    remark: Optional[str] = Field(None, title="存储源备注")
    auto_refresh_cache: Optional[bool] = Field(None, title="是否开启缓存自动刷新", alias="autoRefreshCache")
    type: Optional[StorageTypeEnum] = Field(None, title="存储源类型")
    search_enable: Optional[bool] = Field(None, title="是否开启搜索", alias="searchEnable")
    search_ignore_case: Optional[bool] = Field(None, title="搜索是否忽略大小写", alias="searchIgnoreCase")
    search_mode: Optional[StorageSearchModeEnum] = Field(None, title="搜索模式",
                                                         description="仅从缓存中搜索或直接全量搜索", alias="searchMode")
    order_num: Optional[int] = Field(None, title="排序值", alias="orderNum")
    default_switch_to_img_mode: Optional[bool] = Field(None, title="是否默认开启图片模式",
                                                       alias="defaultSwitchToImgMode")
    refresh_token_info: Optional[RefreshTokenInfo] = Field(None, alias="refreshTokenInfo")
    compatibility_readme: Optional[bool] = Field(None, title="兼容 readme 模式",
                                                 description="兼容模式, 目录文档读取 readme.md 文件",
                                                 alias="compatibilityReadme")


class StorageSourceDTO(CustomBaseModel):
    """存储源基本参数 DTO"""
    id: Optional[int] = Field(None, title="ID, 新增无需填写")
    name: Optional[str] = Field(None, title="存储源名称")
    key: Optional[str] = Field(None, title="存储源别名")
    remark: Optional[str] = Field(None, title="存储源备注")
    type: Optional[StorageTypeEnum] = Field(None, title="存储源类型")
    enable: Optional[bool] = Field(None, title="是否启用")
    enable_file_operator: Optional[bool] = Field(None, title="是否启用文件操作功能", alias="enableFileOperator")
    enable_file_anno_operator: Optional[bool] = Field(None, title="是否允许匿名进行文件操作",
                                                      alias="enableFileAnnoOperator")
    enable_cache: Optional[bool] = Field(None, title="是否开启缓存", alias="enableCache")
    auto_refresh_cache: Optional[bool] = Field(None, title="是否开启缓存自动刷新", alias="autoRefreshCache")
    search_enable: Optional[bool] = Field(None, title="是否开启搜索", alias="searchEnable")
    search_ignore_case: Optional[bool] = Field(None, title="搜索是否忽略大小写", alias="searchIgnoreCase")
    search_mode: Optional[StorageSearchModeEnum] = Field(None, title="搜索模式", alias="searchMode")
    order_num: Optional[int] = Field(None, title="排序值", alias="orderNum")
    storage_source_all_param: Optional[StorageSourceAllParamDTO] = Field(None, alias="storageSourceAllParam")
    default_switch_to_img_mode: Optional[bool] = Field(None, title="是否默认开启图片模式",
                                                       alias="defaultSwitchToImgMode")
    compatibility_readme: Optional[bool] = Field(None, title="兼容 readme 模式", alias="compatibilityReadme")


class PermissionConfigResult(CustomBaseModel):
    """权限配置结果"""
    operator: Optional[PermissionOperatorEnum] = None
    allow_admin: Optional[bool] = Field(None, alias="allowAdmin")
    allow_anonymous: Optional[bool] = Field(None, alias="allowAnonymous")
    operator_name: Optional[str] = Field(None, alias="operatorName")
    tips: Optional[str] = None


class Options(CustomBaseModel):
    """选项"""
    label: Optional[str] = None
    value: Optional[str] = None


class StorageSourceParamDef(CustomBaseModel):
    """存储源参数定义"""
    order: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    default_value: Optional[str] = Field(None, alias="defaultValue")
    link: Optional[str] = None
    link_name: Optional[str] = Field(None, alias="linkName")
    pro: Optional[bool] = None
    type: Optional[StorageSourceParamDefTypeEnum] = None
    options: Optional[List[Options]] = None
    option_allow_create: Optional[bool] = Field(None, alias="optionAllowCreate")
    condition: Optional[str] = None
    hidden: Optional[bool] = None


class CheckProviderDuplicateRequest(CustomBaseModel):
    """检查提供商重复请求"""
    id: Optional[int] = Field(None, title="id")
    provider: Optional[str] = Field(None, title="提供商")


class QueryRuleRequest(CustomBaseModel):
    """查询规则请求"""
    name: Optional[str] = None
    remark: Optional[str] = None


class RuleView(CustomBaseModel):
    """查看规则"""
    id: Optional[int] = None
    name: Optional[str] = None
    remark: Optional[str] = None
    create_time: Optional[datetime] = Field(None, alias="createTime")
    update_time: Optional[datetime] = Field(None, alias="updateTime")


class CheckRuleDuplicateRequest(CustomBaseModel):
    """检查规则重复请求"""
    id: Optional[int] = Field(None, title="规则 ID")
    name: Optional[str] = Field(None, title="规则名称")


class RuleUpload(CustomBaseModel):
    """上传规则"""
    id: Optional[int] = None
    name: Optional[str] = None
    remark: Optional[str] = None
    create_time: Optional[datetime] = Field(None, alias="createTime")
    update_time: Optional[datetime] = Field(None, alias="updateTime")


class PermissionInfoResult(CustomBaseModel):
    """权限信息结果"""
    name: Optional[str] = Field(None, title="权限名称")
    value: Optional[str] = Field(None, title="权限标识")
    tips: Optional[str] = Field(None, title="权限描述")


class QueryLoginLogRequest(CustomBaseModel):
    """查询登录日志请求"""
    page: Optional[int] = Field(None, title="分页页数")
    limit: Optional[int] = Field(None, title="每页条数")
    order_by: Optional[str] = Field(None, title="排序字段", alias="orderBy")
    order_direction: Optional[str] = Field(None, title="排序顺序", alias="orderDirection")
    username: Optional[str] = Field(None, title="用户名")
    password: Optional[str] = Field(None, title="密码")
    ip: Optional[str] = Field(None, title="IP")
    user_agent: Optional[str] = Field(None, title="User-Agent", alias="userAgent")
    referer: Optional[str] = Field(None, title="来源")
    result: Optional[str] = Field(None, title="登录结果")
    search_date: Optional[List[datetime]] = Field(None, title="访问时间", alias="searchDate")
    date_from: Optional[datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime] = Field(None, alias="dateTo")


class LoginLog(CustomBaseModel):
    """登录日志"""
    id: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    create_time: Optional[datetime] = Field(None, alias="createTime")
    ip: Optional[str] = None
    user_agent: Optional[str] = Field(None, alias="userAgent")
    referer: Optional[str] = None
    result: Optional[str] = None


class QueryShortLinkLogRequest(CustomBaseModel):
    """查询短链日志请求"""
    page: Optional[int] = Field(None, title="分页页数")
    limit: Optional[int] = Field(None, title="每页条数")
    order_by: Optional[str] = Field(None, title="排序字段", alias="orderBy")
    order_direction: Optional[str] = Field(None, title="排序顺序", alias="orderDirection")
    key: Optional[str] = Field(None, title="短链 key")
    storage_id: Optional[str] = Field(None, title="存储源 id", alias="storageId")
    url: Optional[str] = Field(None, title="短链文件路径")
    search_date: Optional[List[datetime]] = Field(None, title="访问时间", alias="searchDate")
    date_from: Optional[datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime] = Field(None, alias="dateTo")


class ShortLinkResult(CustomBaseModel):
    """短链结果"""
    id: Optional[int] = Field(None, title="短链 id")
    storage_name: Optional[str] = Field(None, title="存储源名称", alias="storageName")
    storage_type: Optional[StorageTypeEnum] = Field(None, title="存储源类型", alias="storageType")
    short_key: Optional[str] = Field(None, title="短链 key", alias="shortKey")
    url: Optional[str] = Field(None, title="文件 url")
    create_date: Optional[datetime] = Field(None, title="创建时间", alias="createDate")
    expire_date: Optional[datetime] = Field(None, title="过期时间", alias="expireDate")
    short_link: Optional[str] = Field(None, title="短链地址", alias="shortLink")


class AtomicInteger(CustomBaseModel):
    """原子整数（用于缓存信息）"""
    opaque: Optional[int] = None
    acquire: Optional[int] = None
    release: Optional[int] = Field(None)
    and_increment: Optional[int] = Field(None, alias="andIncrement")
    and_decrement: Optional[int] = Field(None, alias="andDecrement")
    plain: Optional[int] = None


class CacheInfoStringAtomicInteger(CustomBaseModel):
    """缓存信息"""
    key: Optional[str] = None
    value: Optional[AtomicInteger] = None
    expired_time: Optional[datetime] = Field(None, alias="expiredTime")
    ttl: Optional[int] = None


class DownloadTopInfoRequest(CustomBaseModel):
    """下载排行信息请求"""
    top: int = Field(..., title="排行数量")
    search_date: Optional[List[datetime]] = Field(None, title="时间", alias="searchDate")
    start_time: Optional[str] = Field(None, alias="startTime")
    end_time: Optional[str] = Field(None, alias="endTime")


class DownloadTopRefererDTO(CustomBaseModel):
    """下载来源排行 DTO"""
    referer: Optional[str] = Field(None, title="referer", description="来源网站")
    count: Optional[int] = Field(None, title="下载次数")


class DownloadTopIpDTO(CustomBaseModel):
    """下载 IP 排行 DTO"""
    ip: Optional[str] = Field(None, title="ip 地址")
    count: Optional[int] = Field(None, title="下载次数")


class DownloadTopFileDTO(CustomBaseModel):
    """下载文件排行 DTO"""
    short_key: Optional[str] = Field(None, title="短链 key", alias="shortKey")
    storage_key: Optional[str] = Field(None, title="存储源 key", alias="storageKey")
    path: Optional[str] = Field(None, title="文件路径")
    count: Optional[int] = Field(None, title="下载次数")
    short_link: Optional[str] = Field(None, title="短链地址", alias="shortLink")
    path_link: Optional[str] = Field(None, title="直链地址", alias="pathLink")


class StreamDownloadLogResult(CustomBaseModel):
    """流式下载日志结果"""
    parallel: Optional[bool] = None


class SystemConfigDTO(CustomBaseModel):
    """系统设置类 DTO"""
    site_name: Optional[str] = Field(None, title="站点名称", alias="siteName")
    username: Optional[str] = Field(None, title="用户名", deprecated=True)
    avatar: Optional[str] = Field(None, title="头像地址")
    icp: Optional[str] = Field(None, title="备案号")
    custom_js: Optional[str] = Field(None, title="自定义 JS", alias="customJs")
    custom_css: Optional[str] = Field(None, title="自定义 CSS", alias="customCss")
    table_size: Optional[str] = Field(None, title="列表尺寸", description="large:大,default:中,small:小",
                                      alias="tableSize")
    show_document: Optional[bool] = Field(None, title="是否显示文档区", alias="showDocument")
    announcement: Optional[str] = Field(None, title="网站公告")
    show_announcement: Optional[bool] = Field(None, title="是否显示网站公告", alias="showAnnouncement")
    layout: Optional[str] = Field(None, title="页面布局", description="full:全屏,center:居中")
    mobile_layout: Optional[str] = Field(None, title="移动端页面布局", description="full:全屏,center:居中",
                                         alias="mobileLayout")
    show_link_btn: Optional[bool] = Field(None, title="是否显示生成直链功能（含直链和路径短链）", alias="showLinkBtn")
    show_short_link: Optional[bool] = Field(None, title="是否显示生成短链功能", alias="showShortLink")
    show_path_link: Optional[bool] = Field(None, title="是否显示生成路径链接功能", alias="showPathLink")
    installed: Optional[bool] = Field(None, title="是否已初始化")
    custom_video_suffix: Optional[str] = Field(None, title="自定义视频文件后缀格式", alias="customVideoSuffix")
    custom_image_suffix: Optional[str] = Field(None, title="自定义图像文件后缀格式", alias="customImageSuffix")
    custom_audio_suffix: Optional[str] = Field(None, title="自定义音频文件后缀格式", alias="customAudioSuffix")
    custom_text_suffix: Optional[str] = Field(None, title="自定义文本文件后缀格式", alias="customTextSuffix")
    custom_office_suffix: Optional[str] = Field(None, title="自定义Office后缀格式", alias="customOfficeSuffix")
    custom_kk_file_view_suffix: Optional[str] = Field(None, title="自定义kkFileView后缀格式",
                                                      alias="customKkFileViewSuffix")
    direct_link_prefix: Optional[str] = Field(None, title="直链地址前缀", alias="directLinkPrefix")
    referer_type: Optional[RefererTypeEnum] = Field(None, title="直链 Referer 防盗链类型", alias="refererType")
    record_download_log: Optional[bool] = Field(None, title="是否记录下载日志", alias="recordDownloadLog")
    referer_allow_empty: Optional[bool] = Field(None, title="直链 Referer 是否允许为空", alias="refererAllowEmpty")
    referer_value: Optional[str] = Field(None, title="直链 Referer 值", alias="refererValue")
    login_verify_secret: Optional[str] = Field(None, title="登陆验证 Secret", alias="loginVerifySecret")
    login_img_verify: Optional[bool] = Field(None, title="是否启用登陆验证码", alias="loginImgVerify")
    admin_two_factor_verify: Optional[bool] = Field(None, title="是否为管理员启用双因素认证",
                                                    alias="adminTwoFactorVerify")
    root_show_storage: bool = Field(..., title="根目录是否显示所有存储源",
                                    description="勾选则根目录显示所有存储源列表, 反之会自动显示第一个存储源的内容.",
                                    alias="rootShowStorage")
    force_backend_address: Optional[str] = Field(None, title="强制后端地址",
                                                 description="强制指定生成直链，短链，获取回调地址时的地址。",
                                                 alias="forceBackendAddress")
    front_domain: Optional[str] = Field(None, title="前端域名", description="前端域名，前后端分离情况下需要配置.",
                                        alias="frontDomain")
    show_login: Optional[bool] = Field(None, title="是否在前台显示登陆按钮", alias="showLogin")
    login_log_mode: Optional[LoginLogModeEnum] = Field(None, title="登录日志模式", alias="loginLogMode")
    rsa_hex_key: Optional[str] = Field(None, title="RAS Hex Key", alias="rsaHexKey")
    file_click_mode: Optional[FileClickModeEnum] = Field(None, title="默认文件点击习惯", alias="fileClickMode")
    mobile_file_click_mode: Optional[FileClickModeEnum] = Field(None, title="移动端默认文件点击习惯",
                                                                alias="mobileFileClickMode")
    auth_code: Optional[str] = Field(None, title="授权码", alias="authCode")
    max_file_uploads: Optional[int] = Field(None, title="最大同时上传文件数", alias="maxFileUploads")
    only_office_url: Optional[str] = Field(None, title="onlyOffice 在线预览地址", alias="onlyOfficeUrl")
    only_office_secret: Optional[str] = Field(None, title="onlyOffice Secret", alias="onlyOfficeSecret")
    kk_file_view_url: Optional[str] = Field(None, title="kkFileView 在线预览地址", alias="kkFileViewUrl")
    kk_file_view_open_mode: Optional[str] = Field(None, title="kkFileView 预览方式", alias="kkFileViewOpenMode")
    webdav_enable: Optional[bool] = Field(None, title="启用 WebDAV", alias="webdavEnable")
    webdav_proxy: Optional[bool] = Field(None, title="WebDAV 服务器中转下载", alias="webdavProxy")
    webdav_allow_anonymous: Optional[bool] = Field(None, title="WebDAV 匿名用户访问", deprecated=True,
                                                   alias="webdavAllowAnonymous")
    webdav_username: Optional[str] = Field(None, title="WebDAV 账号", alias="webdavUsername")
    webdav_password: Optional[str] = Field(None, title="WebDAV 密码", alias="webdavPassword")
    allow_path_link_anon_access: bool = Field(..., title="是否允许路径直链可直接访问", alias="allowPathLinkAnonAccess")
    max_show_size: Optional[int] = Field(None, title="默认最大显示文件数", alias="maxShowSize")
    load_more_size: Optional[int] = Field(None, title="每次加载更多文件数", alias="loadMoreSize")
    default_sort_field: Optional[str] = Field(None, title="默认排序字段", alias="defaultSortField")
    default_sort_order: Optional[str] = Field(None, title="默认排序方向", alias="defaultSortOrder")
    site_home_name: Optional[str] = Field(None, title="站点 Home 名称", alias="siteHomeName")
    site_home_logo: Optional[str] = Field(None, title="站点 Home Logo", alias="siteHomeLogo")
    site_home_logo_link: Optional[str] = Field(None, title="站点 Logo 点击后链接", alias="siteHomeLogoLink")
    site_home_logo_target_mode: Optional[str] = Field(None, title="站点 Logo 链接打开方式",
                                                      alias="siteHomeLogoTargetMode")
    site_admin_logo_target_mode: Optional[str] = Field(None, title="管理员页面点击 Logo 回到首页打开方式",
                                                       alias="siteAdminLogoTargetMode")
    site_admin_version_open_change_log: Optional[bool] = Field(None, title="管理员页面点击版本号打开更新日志",
                                                               alias="siteAdminVersionOpenChangeLog")
    link_limit_second: Optional[int] = Field(None, title="限制直链下载秒数", alias="linkLimitSecond")
    link_download_limit: Optional[int] = Field(None, title="限制直链下载次数", alias="linkDownloadLimit")
    favicon_url: Optional[str] = Field(None, title="网站 favicon 图标地址", alias="faviconUrl")
    link_expire_times: Optional[List[LinkExpireDTO]] = Field(None, title="短链过期时间设置", alias="linkExpireTimes")
    default_save_pwd: Optional[bool] = Field(None, title="是否默认记住密码", alias="defaultSavePwd")
    enable_hover_menu: Optional[bool] = Field(None, title="是否启用 hover 菜单", deprecated=True,
                                              alias="enableHoverMenu")
    access_ip_blocklist: Optional[str] = Field(None, title="访问 ip 黑名单", alias="accessIpBlocklist")
    access_ua_blocklist: Optional[str] = Field(None, title="访问 ua 黑名单", alias="accessUaBlocklist")
    guest_index_html: Optional[str] = Field(None, title="匿名用户首页显示内容", alias="guestIndexHtml")


class LoginTwoFactorAuthenticatorResult(CustomBaseModel):
    """生成二步验证结果"""
    qrcode: Optional[str] = Field(None, title="二步验证二维码")
    secret: Optional[str] = Field(None, title="二步验证密钥")


# =======================================================================
#  Ajax 响应模型 (Ajax Response Models)
# =======================================================================


class AjaxJsonString(AjaxJsonBase):
    data: Optional[str] = Field(None, title="响应数据")


class AjaxJsonBoolean(AjaxJsonBase):
    data: Optional[bool] = Field(None, title="响应数据")


class AjaxJsonVoid(AjaxJsonBase):
    data: Optional[Dict[str, Any]] = Field(None, title="响应数据")


class AjaxJsonObject(AjaxJsonBase):
    data: Optional[Dict[str, Any]] = Field(None, title="响应数据")


class AjaxJsonJSONObject(AjaxJsonBase):
    data: Optional[Dict[str, Any]] = Field(None, title="响应数据")


class AjaxJsonMapStringString(AjaxJsonBase):
    data: Optional[Dict[str, str]] = Field(None, title="响应数据")


class AjaxJsonFileItemResult(AjaxJsonBase):
    data: Optional[FileItemResult] = None


class AjaxJsonFileInfoResult(AjaxJsonBase):
    data: Optional[FileInfoResult] = None


class AjaxJsonListFileItemResult(AjaxJsonBase):
    data: Optional[List[FileItemResult]] = Field(None, title="响应数据")


class AjaxJsonStorageSourceConfigResult(AjaxJsonBase):
    data: Optional[StorageSourceConfigResult] = None


class AjaxJsonListBatchGenerateLinkResponse(AjaxJsonBase):
    data: Optional[List[BatchGenerateLinkResponse]] = Field(None, title="响应数据")


class AjaxJsonListBatchOperatorResult(AjaxJsonBase):
    data: Optional[List[BatchOperatorResult]] = Field(None, title="响应数据")


class AjaxJsonLoginResult(AjaxJsonBase):
    data: Optional[LoginResult] = None


class AjaxJsonListSharepointSiteResult(AjaxJsonBase):
    data: Optional[List[SharepointSiteResult]] = Field(None, title="响应数据")


class AjaxJsonListSharepointSiteListResult(AjaxJsonBase):
    data: Optional[List[SharepointSiteListResult]] = Field(None, title="响应数据")


class AjaxJsonListZFileCORSRule(AjaxJsonBase):
    data: Optional[List[ZFileCORSRule]] = Field(None, title="响应数据")


class AjaxJsonListS3BucketNameResult(AjaxJsonBase):
    data: Optional[List[S3BucketNameResult]] = Field(None, title="响应数据")


class AjaxJsonListGoogleDriveInfoResult(AjaxJsonBase):
    data: Optional[List[GoogleDriveInfoResult]] = Field(None, title="响应数据")


class AjaxJsonOpen115AuthDeviceCodeResult(AjaxJsonBase):
    data: Optional[Open115AuthDeviceCodeResult] = None


class AjaxJsonOpen115GetStatusResult(AjaxJsonBase):
    data: Optional[Open115GetStatusResult] = None


class AjaxJsonLoginVerifyModeEnum(AjaxJsonBase):
    data: Optional[LoginVerifyModeEnum] = Field(None, title="响应数据")


class AjaxJsonCheckLoginResult(AjaxJsonBase):
    data: Optional[CheckLoginResult] = None


class AjaxJsonLoginVerifyImgResult(AjaxJsonBase):
    data: Optional[LoginVerifyImgResult] = None


class AjaxJsonListStorageSourceResult(AjaxJsonBase):
    data: Optional[List[StorageSourceResult]] = Field(None, title="响应数据")


class AjaxJsonListSsoLoginItemResponse(AjaxJsonBase):
    data: Optional[List[SsoLoginItemResponse]] = Field(None, title="响应数据")


class AjaxJsonFrontSiteConfigResult(AjaxJsonBase):
    data: Optional[FrontSiteConfigResult] = None


class AjaxJsonUser(AjaxJsonBase):
    data: Optional[User] = None


class AjaxJsonUserRuleSettingDTO(AjaxJsonBase):
    data: Optional[UserRuleSettingDTO] = None


class AjaxJsonInteger(AjaxJsonBase):
    data: Optional[int] = Field(None, title="响应数据")


class AjaxJsonSsoConfig(AjaxJsonBase):
    data: Optional[SsoConfig] = None


class AjaxJsonRuleViewItem(AjaxJsonBase):
    data: Optional[RuleViewItem] = None


class AjaxJsonRuleDTORuleViewItem(AjaxJsonBase):
    data: Optional[RuleDTORuleViewItem] = None


class AjaxJsonRuleUploadItem(AjaxJsonBase):
    data: Optional[RuleUploadItem] = None


class AjaxJsonRuleDTORuleUploadItem(AjaxJsonBase):
    data: Optional[RuleDTORuleUploadItem] = None


class AjaxJsonUserDetailResponse(AjaxJsonBase):
    data: Optional[UserDetailResponse] = None


class AjaxJsonCollectionUserDetailResponse(AjaxJsonBase):
    data: Optional[List[UserDetailResponse]] = Field(None, title="响应数据")


class AjaxJsonListStorageTypeEnum(AjaxJsonBase):
    data: Optional[List[StorageTypeEnum]] = Field(None, title="响应数据")


class AjaxJsonListStorageSourceAdminResult(AjaxJsonBase):
    data: Optional[List[StorageSourceAdminResult]] = Field(None, title="响应数据")


class AjaxJsonStorageSourceDTO(AjaxJsonBase):
    data: Optional[StorageSourceDTO] = None


class AjaxJsonListReadmeConfig(AjaxJsonBase):
    data: Optional[List[ReadmeConfig]] = Field(None, title="响应数据")


class AjaxJsonListPermissionConfigResult(AjaxJsonBase):
    data: Optional[List[PermissionConfigResult]] = Field(None, title="响应数据")


class AjaxJsonListPasswordConfig(AjaxJsonBase):
    data: Optional[List[PasswordConfig]] = Field(None, title="响应数据")


class AjaxJsonListFilterConfig(AjaxJsonBase):
    data: Optional[List[FilterConfig]] = Field(None, title="响应数据")


class AjaxJsonListStorageSourceParamDef(AjaxJsonBase):
    data: Optional[List[StorageSourceParamDef]] = Field(None, title="响应数据")


class AjaxJsonCollectionSsoConfig(AjaxJsonBase):
    data: Optional[List[SsoConfig]] = Field(None, title="响应数据")


class AjaxJsonCollectionRuleView(AjaxJsonBase):
    data: Optional[List[RuleView]] = Field(None, title="响应数据")


class AjaxJsonCollectionRuleUpload(AjaxJsonBase):
    data: Optional[List[RuleUpload]] = Field(None, title="响应数据")


class AjaxJsonListPermissionInfoResult(AjaxJsonBase):
    data: Optional[List[PermissionInfoResult]] = Field(None, title="响应数据")


class AjaxJsonListLoginLog(AjaxJsonBase):
    data: Optional[List[LoginLog]] = Field(None, title="响应数据")


class AjaxJsonListShortLinkResult(AjaxJsonBase):
    data: Optional[List[ShortLinkResult]] = Field(None, title="响应数据")


class AjaxJsonListCacheInfoStringAtomicInteger(AjaxJsonBase):
    data: Optional[List[CacheInfoStringAtomicInteger]] = Field(None, title="响应数据")


class AjaxJsonListDownloadTopRefererDTO(AjaxJsonBase):
    data: Optional[List[DownloadTopRefererDTO]] = Field(None, title="响应数据")


class AjaxJsonListDownloadTopIpDTO(AjaxJsonBase):
    data: Optional[List[DownloadTopIpDTO]] = Field(None, title="响应数据")


class AjaxJsonListDownloadTopFileDTO(AjaxJsonBase):
    data: Optional[List[DownloadTopFileDTO]] = Field(None, title="响应数据")


class AjaxJsonStreamDownloadLogResult(AjaxJsonBase):
    data: Optional[StreamDownloadLogResult] = Field(None, title="响应数据")


class AjaxJsonSystemConfigDTO(AjaxJsonBase):
    data: Optional[SystemConfigDTO] = None


class AjaxJsonLoginTwoFactorAuthenticatorResult(AjaxJsonBase):
    data: Optional[LoginTwoFactorAuthenticatorResult] = None
