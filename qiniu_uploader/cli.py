# coding=utf-8
import argparse
from core import upload_dir

def main():
    parser = argparse.ArgumentParser(description="上传目录到七牛云存储")
    parser.add_argument("access_key", help="Qiniu Access Key")
    parser.add_argument("secret_key", help="Qiniu Secret Key")
    parser.add_argument("dir_path", help="待上传目录的绝对路径")
    parser.add_argument("bucket_name", help="Name of the Qiniu bucket")

    args = parser.parse_args()
    upload_dir(args.access_key, args.secret_key, args.dir_path, args.bucket_name)

if __name__ == "__main__":
    main()