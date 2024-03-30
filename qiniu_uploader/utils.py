# coding=utf-8
import os
from qiniu import put_file
def get_key(file):
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

def updir(token, dirpath):
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
            updir(token, dirpath + '\\' + sub)
    else:  # 文件
        # 分离文件路径与文件名
        fpath, fname = os.path.split(dirpath)
        # 将文件路径转换为列表，便于处理
        patharr = fpath.split('\\')

        try:
            # 计算文件在七牛云存储中的Key
            key = get_key(dirpath)
            print(key)

            # 使用put_file方法上传文件至七牛云存储空间
            ret, info = put_file(token, key, dirpath)
            print(ret)
        except Exception as e:
            # 打印异常信息
            traceback.print_exc()