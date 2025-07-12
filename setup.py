from setuptools import find_packages, setup

# 读取README文件
with open("docs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取requirements文件
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="zfile-pysdk",
    version="1.1.1",
    author="cuckoo",
    author_email="3038604221@qq.com",
    description="Python SDK for ZFile API - 功能完整的ZFile文件管理系统SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cuckoo711/zfile_sdk",
    project_urls={
        "Bug Tracker": "https://github.com/cuckoo711/zfile_sdk/issues",
        "Documentation": "https://api.zfile.vip/",
        "Source Code": "https://github.com/cuckoo711/zfile_sdk",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: System :: Filesystems",
        "Typing :: Typed",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    package_data={
        "ZfileSDK": ["py.typed"],
    },
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    keywords="zfile, file management, api, sdk, cloud storage, file sharing",
    include_package_data=True,
    zip_safe=False,
)
