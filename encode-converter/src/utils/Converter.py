# -*- coding:UTF-8 -*-
# file_name     : Converter.py
# create_date   : 2022/6/21 
# author        : victor2022

import os, sys
import chardet
from utils.tools import *

class Converter:

    def __init__(self):
        self.exclusion = ""
        self.subfix = ".m"
        self.fromEncode = "GBK"
        self.toEncode = "UTF-8"
        self.aimPath = "./"
        self._fileList = list()
        self.cnt = 0

    def setConfig(self, config):
        self.fromEncode = config.fromEncode
        self.toEncode = config.toEncode
        self.exclusion = config.exclusion
        self.subfix = config.subfix
        self.aimPath = config.aimPath

    def start(self):
        print("Starting...\n")
        if isFile(self.aimPath):
            self._convert(self.aimPath)
        else:
            # 查找并过滤文件夹
            print("Exploring paths...")
            self._fileList = self._explore(self.aimPath)
            print("Explore completed!\n")
            # 过滤文件
            self._fileList = self._filter(self._fileList)
            print("Filter completed!\n")
            # 开始转换
            self._convertAll()
        self._endShow()

    def _explore(self, path:str):
        print("Exploring: " + path)
        res = list()
        for root, dirs, files in os.walk(path):
            fullRoot = os.path.abspath(root)
            for file in files:
                res.append(os.path.join(fullRoot,file))
            for dir in dirs:
                # 递归添加
                res.extend(self._explore(os.path.join(fullRoot,dir)))
        return res

    def _convertAll(self):
        for file in self._fileList:
            self._convert(file)

    def _convert(self, filepath:str):
        try:
            with open(filepath,'rb') as file:
                content = file.read()
                charset = chardet.detect(content).get('encoding')
                if(equalIgnoreCase(self.fromEncode,charset) and
                        not equalIgnoreCase(self.toEncode,charset)):
                    print("Converting: "+filepath+" from "+self.fromEncode+" to "+self.toEncode)
                    # 写入文件
                    newFile = open(filepath,"wb")
                    newContent = content.decode(self.fromEncode).encode(self.toEncode)
                    newFile.write(newContent)
                    self.cnt+=1
                else:
                    return
            print("Complete for: "+filepath)
        except Exception as e:
            print(e)
            print("Failure for: "+filepath)



    # 找到指定后缀的文件
    def _filter(self, fileList:list):
        print("Filtering paths...")
        res = list()
        # 排除制定文件，筛选以subfix结尾的文件
        for file in fileList:
            if(not file.endswith(self.subfix) or not self._included(file)):
                print("Exclude: " + file)
                continue
            res.append(file)
        return res

    def _included(self, path:str):
        if(len(self.exclusion) == 0 or self.exclusion is None):
            return True
        # 开始筛选
        exPath = os.path.abspath(self.exclusion)
        if (path.find(exPath)!=-1):
            return False
        return True

    def _endShow(self):
        print("Conversion completed!")
        print("There are "+str(self.cnt)+" files successful converted.")
