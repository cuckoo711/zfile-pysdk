#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
版本更新脚本
用于一次性更新项目中所有文件的版本号
"""

import os
import re
from typing import List, Tuple


class VersionUpdater:
    """版本更新器"""

    def __init__(self, project_root: str = None):
        """初始化版本更新器
        
        Args:
            project_root: 项目根目录，默认为当前目录
        """
        self.project_root = project_root or os.getcwd()

        # 定义需要更新版本的文件及其匹配规则
        self.version_files = [
            {
                'file': 'pyproject.toml',
                'pattern': r'version = "([^"]+)"',
                'replacement': 'version = "{version}"'
            },
            {
                'file': 'setup.py',
                'pattern': r'version="([^"]+)"',
                'replacement': 'version="{version}"'
            },
            {
                'file': 'ZfileSDK/__init__.py',
                'pattern': r'__version__ = "([^"]+)"',
                'replacement': '__version__ = "{version}"'
            },
            {
                'file': 'ZfileSDK/admin/__init__.py',
                'pattern': r'__version__ = "([^"]+)"',
                'replacement': '__version__ = "{version}"'
            },
            {
                'file': 'ZfileSDK/front/__init__.py',
                'pattern': r'__version__ = "([^"]+)"',
                'replacement': '__version__ = "{version}"'
            },
            {
                'file': 'docs/README.md',
                'pattern': r'- 当前版本：\*\*([^*]+)\*\*',
                'replacement': '- 当前版本：**{version}**'
            },
        ]

    def get_current_version(self) -> str:
        """从pyproject.toml或update_version.py获取当前版本号

        Returns:
            当前版本号
        """
        pyproject_path = os.path.join(self.project_root, 'pyproject.toml')

        if os.path.exists(pyproject_path):
            with open(pyproject_path, 'r', encoding='utf-8') as f:
                content = f.read()
            match = re.search(r'version = "([^"]+)"', content)
            if match:
                return match.group(1)

        raise ValueError("无法从pyproject.toml中找到版本号")

    @staticmethod
    def validate_version_format(version: str) -> bool:
        """验证版本号格式
        
        Args:
            version: 版本号字符串
            
        Returns:
            是否为有效的版本号格式
        """
        # 支持语义化版本号格式：x.y.z 或 x.y.z-alpha.1 等，以及 x.y.z-pre.1+build.123
        pattern = r'^\d+\.\d+\.\d+(?:-[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*)?(?:\+[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*)?$'
        return bool(re.match(pattern, version))

    def update_file_version(self, file_info: dict, new_version: str) -> Tuple[bool, str]:
        """更新单个文件的版本号
        
        Args:
            file_info: 文件信息字典
            new_version: 新版本号
            
        Returns:
            (是否成功, 消息)
        """
        file_path = os.path.join(self.project_root, file_info['file'])

        if not os.path.exists(file_path):
            return False, f"文件不存在: {file_path}"

        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 查找并替换版本号
            pattern = file_info['pattern']
            replacement = file_info['replacement'].format(version=new_version)

            # 检查是否找到匹配项
            if not re.search(pattern, content):
                return False, f"在文件 {file_info['file']} 中未找到版本号模式"

            # 执行替换
            new_content = re.sub(pattern, replacement, content)

            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True, f"成功更新 {file_info['file']}"

        except Exception as e:
            return False, f"更新文件 {file_info['file']} 时出错: {str(e)}"

    def update_all_versions(self, new_version: str, dry_run: bool = False) -> List[Tuple[str, bool, str]]:
        """更新所有文件的版本号
        
        Args:
            new_version: 新版本号
            dry_run: 是否为试运行（不实际修改文件）
            
        Returns:
            更新结果列表：[(文件名, 是否成功, 消息), ...]
        """
        if not self.validate_version_format(new_version):
            raise ValueError(f"无效的版本号格式: {new_version}")

        results = []

        for file_info in self.version_files:
            if dry_run:
                # 试运行模式，只检查文件是否存在和模式是否匹配
                file_path = os.path.join(self.project_root, file_info['file'])
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        if re.search(file_info['pattern'], content):
                            results.append((file_info['file'], True, "[试运行] 将会更新"))
                        else:
                            results.append((file_info['file'], False, "[试运行] 未找到版本号模式"))
                    except Exception as e:
                        results.append((file_info['file'], False, f"[试运行] 读取文件出错: {str(e)}"))
                else:
                    results.append((file_info['file'], False, "[试运行] 文件不存在"))
            else:
                # 实际更新
                success, message = self.update_file_version(file_info, new_version)
                results.append((file_info['file'], success, message))

        return results

    @staticmethod
    def print_results(results: List[Tuple[str, bool, str]]):
        """打印更新结果
        
        Args:
            results: 更新结果列表
        """
        print("\n=== 版本更新结果 ===")
        for file_name, success, message in results:
            status = "✅" if success else "❌"
            print(f"{status} {file_name}: {message}")

        # 统计
        success_count = sum(1 for _, success, _ in results if success)
        total_count = len(results)
        print(f"\n总计: {success_count}/{total_count} 个文件更新成功")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description='更新项目中所有文件的版本号')
    parser.add_argument('version', help='新版本号 (例如: 1.0.0)')
    parser.add_argument('--dry-run', action='store_true', help='试运行模式，不实际修改文件')
    parser.add_argument('--project-root', help='项目根目录路径，默认为当前目录')

    args = parser.parse_args()

    try:
        # 创建版本更新器
        updater = VersionUpdater(args.project_root)

        # 显示当前版本
        current_version = updater.get_current_version()
        print(f"当前版本: {current_version}")
        print(f"目标版本: {args.version}")

        if current_version == args.version:
            print("⚠️  新版本号与当前版本相同，无需更新")
            return

        if args.dry_run:
            print("\n🔍 试运行模式 - 不会实际修改文件")

        # 执行更新
        results = updater.update_all_versions(args.version, dry_run=args.dry_run)

        # 打印结果
        updater.print_results(results)

        if not args.dry_run:
            print(f"\n🎉 版本已从 {current_version} 更新到 {args.version}")

    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        exit(1)


if __name__ == '__main__':
    main()
