# coding=utf-8
'''
    上传指定文件夹到七牛云存储。

    参数:
        ak (str): 七牛云账户的Access Key
        sk (str): 七牛云账户的Secret Key
        dir_path (str): 待上传文件夹的绝对路径
        bucket_name (str): 七牛云存储空间名称
'''
from utils import updir
from qiniu import Auth

def upload_dir(ak, sk, dir_path, bucket_name):
    q = Auth(ak, sk)
    token = q.upload_token(bucket_name)

    updir(token, dir_path)