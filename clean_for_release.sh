#!/bin/bash
echo "开始清理项目..."

# 删除Python缓存
echo "清理Python缓存..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete

# 删除构建文件
echo "清理构建文件..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# 删除系统文件
echo "清理系统文件..."
find . -name ".DS_Store" -delete

## 删除IDE文件
#echo "清理IDE文件..."
#rm -rf .vscode/
#rm -rf .idea/

echo "清理完成！"
echo "项目已准备好发布。"