# -*- coding:UTF-8 -*-
# file_name     : main.py
# create_date   : 2022/6/21 
# author        : victor2022

from utils.ConfigEntity import Config
from utils.Converter import Converter
from utils.tools import *

def main():
    # 程序启动
    print("Converter started...")
    # 读取配置文件
    config = Config()
    # 读取用户参数
    print("Please insert filename or path: ",end="")
    aimPath = input()
    while(not isPathOrFile(aimPath)):
        print("Filename or path is not valid! Please insert again: ",end="")
        aimPath = input()
    config.aimPath = aimPath
    # 开始转换
    converter = Converter()
    converter.setConfig(config)
    converter.start()
    print("Exiting...")


if __name__ == '__main__':
    main()