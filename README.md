
---
# qiniu-uploader


**qiniu-uploader** 是一个用于上传本地文件夹到七牛云存储的Python包。它利用七牛官方Python SDK，通过指定的Access Key（AK）和Secret Key（SK）生成上传凭证，并递归遍历本地文件夹，将其中的所有文件上传至指定的七牛云存储空间（Bucket）。

### 特性

- **一键上传**：只需提供必要的七牛云账户信息和待上传文件夹路径，即可轻松将整个文件夹上传至七牛云。
- **递归遍历**：支持上传文件夹及其所有子文件夹中的文件，无需手动处理复杂的目录结构。
- **命令行支持**：提供便捷的命令行接口，方便快速执行上传任务。
- **代码调用**：亦可作为库集成到其他Python项目中，实现程序化的文件上传。

### 作者
Mrj

### 联系方式
微信: kangde0-0

### 安装

```bash
pip install qiniu-uploader
```

### 命令行使用

```bash
qiniu-uploader --help
qiniu-uploader <ACCESS_KEY> <SECRET_KEY> <DIR_PATH> <BUCKET_NAME>
```

**示例：**

```bash
qiniu-uploader oXrJe_Va0LOMdFLErzrb8KOyOCnAXo72uz83eD xOl-TMz73MuYLP77dZ3cOI5eRjN-5fmFfC45T7 E:\attachment sz
```

### 代码调用

```python
from qiniu_uploader.core import upload_dir

upload_dir(
    ak="oXrJe_Va0LOMdFLErRSzrb8CnAXo72uz83eD",
    sk="xOl-TMz73MuYLP77dMKeRjN-5fmFfC45T7",
    dir_path="E:\\attachment",
    bucket_name="sz",
)
```

### 开发与贡献

欢迎提交问题、建议和 Pull Requests 到 [GitHub 仓库](https://github.com/Mr-J-J/qiniu_uploader)。

---

**注意：** 请替换上述链接为实际的GitHub仓库地址。如果您还没有创建相应的GitHub仓库，请先创建，并将您的代码推送至该仓库。同时，记得替换实际的PyPI包名和版本号对应的徽章链接。

---

**版权声明：** 该项目最终版权归属Mrj所有。

---

**友情提示：** 请确保您的七牛云账户信息及使用行为符合七牛云服务条款。在公开README或其他文档时，避免直接暴露敏感的Access Key和Secret Key。此处仅作示例，实际使用时应确保密钥安全。

---