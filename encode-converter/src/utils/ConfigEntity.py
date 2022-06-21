# -*- coding:UTF-8 -*-
# file_name     : ConfigEntity.py
# create_date   : 2022/6/21 
# author        : victor2022
# 配置文件类

from configparser import ConfigParser
import os


class Config:

    def __init__(self):
        print("Loading Configurations...")
        self.exclusion = ""
        self.subfix = ".m"
        self.fromEncode = "GBK"
        self.toEncode = "UTF-8"
        # 调用函数读取配置文件
        self.readConfig("config.ini")
        # 配置读取完成
        print("Configure loading completed...")

    def readConfig(self, filename):
        # 初始化
        parser = ConfigParser()
        filepath = os.path.join(os.path.abspath('.'), filename)
        # 判断文件是否存在
        if not os.path.exists(filepath):
            print("Configure file not exist, use default config!")
            return
        # 读取配置
        parser.read(filepath)
        group = 'config'
        try:
            self.exclusion = parser.get(group, 'exclusion')
        except:
            pass
        finally:
            print("- exclusion: "+self.exclusion)

        try:
            self.subfix = parser.get(group, 'subfix')
        except:
            pass
        finally:
            print("- subfix: "+self.subfix)
        try:
            self.fromEncode = parser.get(group, 'fromEncode')
        except:
            pass
        finally:
            print("- fromEncode: "+self.fromEncode)

        try:
            self.toEncode = parser.get(group, 'toEncode')
        except:
            pass
        finally:
            print("- toEncode: "+self.toEncode)