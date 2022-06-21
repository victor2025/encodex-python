# -*- coding:UTF-8 -*-
# file_name     : tools.py
# create_date   : 2022/6/21 
# author        : victor2022
# 工具方法文件
import os

def isPath(path:str):
    return os.path.isdir(path)

def isFile(path:str):
    return os.path.isfile(path)

def isPathOrFile(path:str):
    if(os.path.isdir(path)):
        return True
    if(os.path.isfile(path)):
        return True
    return False

# 包含通配符的字符串比较
def equalIgnoreCase(str1:str, str2:str):
    if(str1=="*" or str2=="*"):
        return True
    return (str1.lower()==str2.lower())