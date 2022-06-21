# -*- coding:UTF-8 -*-
# file_name     : ConfigEntity.py
# create_date   : 2022/6/21 
# author        : victor2022
# 配置文件类

from configparser import ConfigParser
import os


class Config:

    def __init__(self,filename = "config.ini"):
        print("Loading Configurations...")
        self.exclusion = []
        self.subfix = [".m"]
        self.fromEncode = ["GBK"]
        self.toEncode = "UTF-8"
        # 调用函数读取配置文件
        self._readConfig(filename)
        # 配置读取完成
        print("Configure load completed...\n")

    def _readConfig(self, filename):
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
        exclusionStr = ""
        try:
            exclusionStr = parser.get(group, 'exclusion')
            if(not ""==exclusionStr):
                self.exclusion.extend(exclusionStr.split(","))
        except:
            pass
        finally:
            print("- exclusion: "+exclusionStr)

        subfixStr = ""
        try:
            subfixStr = parser.get(group, 'subfix').lower()
            self.subfix = subfixStr.split(",")
            # 通配符
            if("*" in self.subfix):
                subfixStr = "*"
                self.subfix = ["*"]
        except:
            pass
        finally:
            print("- subfix: "+subfixStr)

        fromEncodeStr = ""
        try:
            fromEncodeStr = parser.get(group, 'fromEncode').lower()
            self.fromEncode = fromEncodeStr.split(",")
            # 通配符
            if("*" in self.fromEncode):
                fromEncodeStr = "*"
                self.fromEncode = ["*"]
        except:
            pass
        finally:
            print("- fromEncode: "+fromEncodeStr)

        try:
            self.toEncode = parser.get(group, 'toEncode')
        except:
            pass
        finally:
            print("- toEncode: "+self.toEncode)