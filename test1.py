# -*- coding: utf-8 -*-
"""
上传文件夹到七牛云存储的Python脚本

使用七牛官方Python SDK，通过指定的Access Key（AK）和Secret Key（SK）生成上传凭证，
然后递归遍历本地文件夹并将其中的所有文件上传至指定的七牛云存储空间（Bucket）。

所需依赖：
    qiniu (七牛官方Python SDK)

环境变量：
    AK (str): 七牛云账户的Access Key
    SK (str): 七牛云账户的Secret Key
    dir (str): 待上传文件夹的绝对路径
    bucket_name (str): 七牛云存储空间名称

主要函数说明：
    updir(dirpath): 递归上传文件夹及其子文件夹中的所有文件
    getKey(file): 根据文件路径生成七牛云存储中的文件Key
"""

from qiniu import Auth, put_file
import os
import traceback

# 定义七牛云账户的Access Key与Secret Key
AK = ''
SK = ''

# 指定待上传文件夹的绝对路径
dir = ''

# 七牛云存储空间名称
bucket_name = ''

# 使用七牛官方SDK创建Auth对象，并生成上传凭证（Token）
q = Auth(AK, SK)
token = q.upload_token(bucket_name)


def updir(dirpath):
    """
    递归上传文件夹及其子文件夹中的所有文件至七牛云存储空间

    参数：
        dirpath (str): 当前处理的目录路径
    """

    # 检查当前路径是否为文件夹
    if os.path.isdir(dirpath):  # 文件夹
        # 获取该文件夹下所有子文件/子文件夹名
        sublist = os.listdir(dirpath)
        # 遍历子文件/子文件夹并递归调用updir函数
        for sub in sublist:
            updir(dirpath + '\\' + sub)
    else:  # 文件
        # 分离文件路径与文件名
        fpath, fname = os.path.split(dirpath)
        # 将文件路径转换为列表，便于处理
        patharr = fpath.split('\\')

        try:
            # 计算文件在七牛云存储中的Key
            key = getKey(dirpath)
            print(key)

            # 使用put_file方法上传文件至七牛云存储空间
            ret, info = put_file(token, key, dirpath)
            print(ret)
        except Exception as e:
            # 打印异常信息
            traceback.print_exc()


def getKey(file):
    """
    根据本地文件路径生成七牛云存储中的文件Key

    参数：
        file (str): 本地文件路径

    返回值：
        str: 文件在七牛云存储中的Key
    """

    key = ''

    # 分离文件路径与文件名
    fpath, fname = os.path.split(file)
    # 将文件路径转换为列表，便于处理
    patharr = fpath.split('\\')

    # 如果文件路径包含至少两个元素（即非根目录下的文件）
    if len(patharr) >= 2:
        # 使用'/'连接路径元素，生成Key（注意：七牛云存储中路径分隔符为'/')
        key = '/'.join(patharr[2:]) + '/' + fname
    else:
        # 文件位于根目录，直接使用文件名作为Key
        key = fname

    return key


if __name__ == '__main__':
    # 调用updir函数，开始上传指定文件夹至七牛云存储
    updir(dir)