# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/22 21:59
@Author  : WJC
@File    : DailyFunc.py
@Desc    : 
"""

def gather_all_xx_files(source_dir, dest_dir, suffix):
    '''
    获取 source_dir 目录下（递归）的所有 suffix后缀文件 复制到 dest_dir目录
    :param source_dir str: 需要扫描的目录
    :param dest_dir str: 文件移到的目录
    :param suffix tuple: 文件后缀（含.）
    :return: None
    '''
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)
    for root, dirs, files in os.walk(source_dir):
        if root != dest_dir:
            for file in files:
                if file.endswith(suffix) and not file.startswith("~"):
                    file_path = os.path.join(root, file)
                    shutil.copy(file_path, dest_dir)


if __name__ == '__main__':
    source_dir = r'F:\黑马-java\5、超哇塞的Java基础教程\资料\基础篇'
    dest_dir = r'F:\黑马-java\5、超哇塞的Java基础教程\资料\基础篇\ppt汇总'
    suffix = ('.pptx', '.exe')
    gather_all_xx_files(source_dir, dest_dir, suffix)