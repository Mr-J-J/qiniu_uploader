from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="qiniu-uploader",
    version="0.1.0",
    author="Mrj",
    author_email="806189218@qq.com",
    description="一个用于将目录上传至七牛云存储的Python包,将服务器数据迁移到七牛云",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mr-J-J/qiniu_uploader",  # Replace with your repository URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7,>=3.6",
    install_requires=["qiniu"],
    entry_points={
        "console_scripts": [
            "qiniu-uploader=qiniu_uploader.cli:main",
        ],
    },
)