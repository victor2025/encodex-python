# Encodex
## 基于Python的文件转码工具
### 配置文件
- exclusion: 需要排除的目录或文件(0~n)
- subfix: 需要转码的文件扩展名(1~n, 默认"m")，可使用通配符"*"(不推荐)
- fromEncode: 需要转码的文件的原字符集(1~n, 默认"gbk")，可使用通配符"*"(不推荐)
- toEncode: 需要将文件转成的字符集(1, 默认"utf-8")

````ini
[config]
exclusion=
subfix=m
fromEncode=gbk
toEncode=utf-8
````
---
### 源代码
##### 1. encodex.py

- 程序入口
- 用户输入控制
- 程序流程控制
  
##### 2. ConfigEntity.py
- 配置文件读取
- 配置保存
  
##### 3. Converter.py
- 配置处理
- 文件扫描
- 文件过滤
- 文件验证
- 转码
  
##### 4. tools.py
- 工具方法

---
### 环境和依赖
##### Linux
- python 3.8.8
  - chardet 4.0.0
  - pyinstaller 5.1

##### Windows
- python 3.8.3
  - chardet 3.0.4
  - pyinstaller 5.1

**对于与上述不一致的环境，建议重新构建(执行pack.sh/pack.cmd)或直接运行源代码*

**pyinstaller 仅用于构建程序，与程序运行无关*