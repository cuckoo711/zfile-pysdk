# ZFile SDK

一个功能完整的 Python SDK，用于与 ZFile 文件管理系统进行交互。该 SDK 封装了前端用户和管理员的完整 API 接口，提供了基于
Pydantic 的类型安全请求/响应处理和统一的错误管理机制。

## ✨ 特性

- 🔐 **完整的认证系统** - 支持用户登录、管理员认证、验证码和会话管理
- 📁 **文件管理功能** - 文件列表查看、文件操作（上传、下载、重命名、移动、复制、删除）
- 🔗 **链接管理** - 批量生成直链和短链
- 🌐 **多平台集成** - 支持 Google Drive、OneDrive、SharePoint、S3、115网盘等存储源
- ⚙️ **站点配置** - 获取站点全局设置、存储源配置等
- 👨‍💼 **管理员功能** - 完整的后台管理功能，包括用户管理、权限控制、存储源管理等
- 📝 **类型安全** - 基于 Pydantic 2.x 的强类型支持和数据验证
- 🛡️ **错误处理** - 统一的异常处理和错误管理机制
- 📊 **日志记录** - 完整的操作日志和调试信息
- 🔧 **装饰器支持** - 自动参数解析和模型验证

## 📦 安装（两种安装方式选择一种即可，建议从PyPI安装）

### 从 PyPI 安装（推荐）

```bash
pip install zfile-pysdk
```

### 从源码安装

```bash
git clone https://github.com/cuckoo711/zfile_sdk.git
cd zfile_sdk
pip install -r requirements.txt
pip install -e .
```

### 依赖要求

- Python 3.10+
- requests ~= 2.32.4
- pydantic ~= 2.11.7
- urllib3 ~= 2.5.0

### 更新方式

#### 从 PyPI 更新

```bash
pip install --upgrade zfile-pysdk
```

#### 从源码更新

```bash
git pull origin main
pip install -r requirements.txt
pip install -e .
```

## 🚀 快速开始

### 基础用法

```python
# 导入核心客户端
from ZfileSDK.utils import ApiClient
```

### 创建客户端实例

```python
# 创建客户端实例
client = ApiClient(base_url="http://localhost:8080")

# 用户登录
client.login(username="your_username", password="your_password")

# 检查登录状态
print(f"是否为管理员: {client.is_admin}")
print(f"当前 Token: {client.token}")

# 使用完毕后注销
client.logout()
```

### 使用上下文管理器

```python
# 使用上下文管理器自动处理登录和注销
with ApiClient(base_url="http://localhost:8080") as client:
    client.login(username="admin", password="password")
    # 执行各种操作...
    # 自动清理资源
```

### 文件操作示例

```python
from ZfileSDK.front import FileListModule, FileOperationModule

# 获取文件列表
file_list_module = FileListModule(client)
files = file_list_module.storage_files(
    storage_key="local",
    path="/",
    password=None
)

# 创建文件夹
file_op_module = FileOperationModule(client)
result = file_op_module.mkdir(
    storage_key="local",
    path="/",
    name="新文件夹",
    password=None
)
```

### 管理员功能示例

```python
from ZfileSDK.admin import UserManagement, StorageSourceModuleBasic

# 用户管理
user_mgmt = UserManagement(client)
users = user_mgmt.list_users(
    page=1,
    size=10,
    order_by="id",
    order_direction="desc"
)

# 存储源管理
storage_mgmt = StorageSourceModuleBasic(client)
storages = storage_mgmt.list_storage_sources()
```

### 短链生成示例

```python
from ZfileSDK.front import DirectShortChainModule

# 生成短链
short_link_module = DirectShortChainModule(client)
links = short_link_module.batch_generate(
    storage_key="local",
    paths=["/file1.txt", "/file2.txt"],
    expire_time=3600,
)
```

## 📁 项目结构

```
zfile_sdk/
├── ZfileSDK/
│   ├── __init__.py                                     # 主模块初始化导入
│   ├── admin/                                          # 管理员功能模块
│   │   ├── __init__.py                                 # 后台管理员模块导入
│   │   ├── user_management.py                          # 用户管理
│   │   ├── login_module.py                             # 登录模块
│   │   ├── permission_module.py                        # 权限模块
│   │   ├── login_log_management.py                     # 登录日志管理
│   │   ├── single_sign_on_management.py                # 单点登录管理
│   │   ├── site_setting_module.py                      # 站点设置
│   │   ├── storage_source_module_basic.py              # 存储源基础管理
│   │   ├── storage_source_module_filter_file.py        # 存储源过滤文件
│   │   ├── storage_source_module_metadata.py           # 存储源元数据
│   │   ├── storage_source_module_permission.py         # 存储源权限
│   │   ├── storage_source_module_readme.py             # 存储源README
│   │   ├── rule_management_view_rules.py               # 显示规则管理
│   │   ├── rule_management_upload_rules.py             # 上传规则管理
│   │   ├── rule_matcher_helper.py                      # 规则匹配辅助
│   │   ├── direct_link_management.py                   # 直链管理
│   │   ├── direct_link_log_management.py               # 直链日志管理
│   │   └── ip_address_helper.py                        # IP地址辅助工具
│   ├── front/                                          # 前台用户功能模块
│   │   ├── __init__.py                                 # 用户前台初始化导入
│   │   ├── file_list_module.py                         # 文件列表模块
│   │   ├── file_operation_module.py                    # 文件操作模块
│   │   ├── site_basic_module.py                        # 站点基础模块
│   │   ├── user_interface.py                           # 用户接口模块
│   │   ├── short_link.py                               # 短链模块
│   │   ├── direct_short_chain_module.py                # 直链短链模块
│   │   ├── initialization_module.py                    # 初始化模块
│   │   ├── single_sign_on.py                           # 单点登录模块
│   │   ├── single_sign_on_interface.py                 # 单点登录接口
│   │   ├── server_proxy_download.py                    # 服务器代理下载
│   │   ├── server_proxy_upload.py                      # 服务器代理上传
│   │   ├── onlyoffice_related_interfaces.py            # OnlyOffice 接口
│   │   ├── gd_tools_assistive_module.py                # Google Drive 工具
│   │   ├── sharepoint_tools_assistive_module.py        # SharePoint 工具
│   │   ├── s3_tools_assistive_module.py                # S3 工具
│   │   ├── oneonefive_tools_assistive_module.py        # 115网盘工具
│   │   ├── open_115_url_controller.py                  # 115网盘 URL 控制器
│   │   └── onedrive_authentication_callback_module.py  # OneDrive 认证回调
│   ├── utils/                                          # 核心工具模块
│   │   ├── __init__.py                                 # 工具初始化导入
│   │   ├── api_client.py                               # HTTP 客户端封装
│   │   ├── models.py                                   # Pydantic 数据模型
│   │   ├── exceptions.py                               # 异常定义
│   │   ├── logger.py                                   # 日志处理
│   │   └── base.py                                     # 基础类和装饰器
│   └── py.typed                                        # 类型标注文件
├── docs/                                               # 文档目录
│   ├── README.md                                       # 项目说明
│   ├── LICENSE                                         # 许可证
│   └── LICENSE_CN                                      # 中文许可证
├── requirements.txt                                    # 依赖列表
├── setup.py                                            # 安装脚本
├── pyproject.toml                                      # 项目配置
├── MANIFEST.in                                         # 打包配置
├── clean_for_release.sh                                # 发布清理脚本
└── update_version.py                                   # 版本更新脚本
```

## 🔧 核心功能

### 前台功能模块 (front/)

| 模块                                          | 功能描述                     |
|---------------------------------------------|--------------------------|
| **file_list_module**                        | 文件列表查看、存储搜索、单个文件信息获取     |
| **file_operation_module**                   | 文件操作（创建、删除、重命名、移动、复制、上传） |
| **site_basic_module**                       | 站点基础信息和配置获取、存储源配置        |
| **user_interface**                          | 用户登录、密码管理、验证码获取          |
| **short_link**                              | 批量生成直链和短链                |
| **direct_short_chain_module**               | 直链短链生成和管理                |
| **initialization_module**                   | 系统初始化和配置检查               |
| **single_sign_on**                          | 单点登录功能                   |
| **single_sign_on_interface**                | 单点登录接口                   |
| **server_proxy_download**                   | 服务器代理下载                  |
| **server_proxy_upload**                     | 服务器代理上传                  |
| **onlyoffice_related_interfaces**           | OnlyOffice 文档预览和在线编辑     |
| **gd_tools_assistive_module**               | Google Drive 集成和文件操作     |
| **sharepoint_tools_assistive_module**       | SharePoint 集成和文件管理       |
| **s3_tools_assistive_module**               | AWS S3 兼容存储集成            |
| **oneonefive_tools_assistive_module**       | 115网盘集成                  |
| **open_115_url_controller**                 | 115网盘 URL 控制器            |
| **onedrive_authentication_callback_module** | OneDrive 认证回调            |

### 管理员功能模块 (admin/)

| 模块                                    | 功能描述               |
|---------------------------------------|--------------------|
| **user_management**                   | 用户管理（增删改查、复制、权限设置） |
| **login_module**                      | 登录模块（2FA验证、设备绑定）   |
| **permission_module**                 | 权限模块（权限列表查看）       |
| **login_log_management**              | 登录日志管理（日志查询）       |
| **single_sign_on_management**         | 单点登录管理（SSO服务商配置）   |
| **site_setting_module**               | 站点设置（全局配置管理）       |
| **storage_source_module_basic**       | 存储源基础管理（增删改查、排序）   |
| **storage_source_module_filter_file** | 存储源过滤文件管理          |
| **storage_source_module_metadata**    | 存储源元数据（支持类型、参数定义）  |
| **storage_source_module_permission**  | 存储源权限控制            |
| **storage_source_module_readme**      | 存储源README和密码文件夹管理  |
| **rule_management_view_rules**        | 显示规则管理（规则增删改查、测试）  |
| **rule_management_upload_rules**      | 上传规则管理（规则增删改查、测试）  |
| **rule_matcher_helper**               | 规则匹配测试辅助工具         |
| **direct_link_management**            | 直链管理（直链增删改查）       |
| **direct_link_log_management**        | 直链日志管理（日志查询）       |
| **ip_address_helper**                 | IP地址辅助工具（IP信息查询）   |

### 工具模块 (utils/)

- **ApiClient**: 核心 HTTP 客户端，提供统一的 API 调用接口和会话管理
- **Models**: 基于 Pydantic 2.x 的数据模型，确保类型安全和数据验证
- **Exceptions**: 自定义异常类，提供详细的错误信息和统一的错误处理
- **Logger**: 日志处理工具，支持多级别日志记录
- **Base**: 基础类和装饰器，提供自动参数解析功能

## 🔐 认证和安全

### 登录认证

```python
# 基础登录
client.login(username="user", password="pass")

# 带验证码登录
client.login(
    username="user",
    password="pass",
    verify_code="1234",
    verify_code_uuid="uuid-string"
)
```

### Token 管理

```python
# 获取当前 token
token = client.token

# 使用预设 token 创建客户端
client = ApiClient(base_url="http://localhost:8080", token="your-token")

# 检查管理员权限
if client.is_admin:
    print("当前用户具有管理员权限")
```

## 🛠️ 高级用法

### 自定义请求

```python
from ZfileSDK.utils.models import AjaxJsonVoid

# GET 请求
response = client.make_common_request("GET", "/api/endpoint", params={"key": "value"})

# POST 请求
response = client.post("POST", "/api/endpoint", data={"key": "value"})
```

### 错误处理

```python
from ZfileSDK.utils import ApiException, CustomException

try:
    client.login(username="invalid", password="invalid")
except CustomException as e:
    print(f"业务错误: {e.msg} (代码: {e.code})")
except ApiException as e:
    print(f"API 错误: {e.message}")
```

### 使用装饰器

```python
from ZfileSDK.utils.base import auto_args_from_model
from ZfileSDK.utils.models import FileListRequest


# 装饰器自动解析参数
@auto_args_from_model(model=FileListRequest)
def get_files(*, data: FileListRequest):
    # 自动验证和解析参数
    pass
```

## 📚 API 文档

详细的 API 文档请参考 [ZFile 官方API文档](https://api.zfile.vip/)。

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request
6. 确保代码符合 PEP 8 风格指南

> 请确保您的代码经过测试，并且添加了必要的文档注释。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](./LICENSE) 文件了解详情，或查看 [LICENSE_CN](./LICENSE_CN) 文件的中文版本。

## 🔗 相关链接

- [PyPI 包页面](https://pypi.org/project/zfile-pysdk/)
- [ZFile 官方网站](https://www.zfile.vip/)
- [ZFile GitHub](https://github.com/zfile-dev/zfile)
- [问题反馈](https://github.com/cuckoo711/zfile_sdk/issues)

## 📞 支持

如果您在使用过程中遇到问题，请通过以下方式获取帮助：

- 查看 [官方API文档](https://api.zfile.vip/)
- 提交 [Issue](https://github.com/cuckoo711/zfile_sdk/issues)
- 向我发送[邮件](mailto:3038604221@qq.com)获取支持

## 📝 注意事项

- 本 SDK 仅支持 ZFile 版本 4.0.1 及以上。
- 当前版本：**1.1.1**
- 包名：**zfile-pysdk**

---

**注意**: 本 SDK 需要配合 ZFile 后端服务使用，请确保您的 ZFile 服务正常运行。