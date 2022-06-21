# -*- coding:UTF-8 -*-
# file_name     : Converter.py
# create_date   : 2022/6/21 
# author        : victor2022
import errno

import chardet
from utils.tools import *

class Converter:

    def __init__(self,config):
        self.setConfig(config)
        self._fileList = list()
        self.fileCnt = 0
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

    # 编码转换核心代码
    def _convert(self, filepath:str):
        print(str(self.fileCnt)+"-Processing: "+filepath)
        self.fileCnt+=1
        try:
            with open(filepath,'rb') as file:
                content = file.read()
                charset = chardet.detect(content).get('encoding')
                charset = alias(charset)
                # 开始处理
                if(not charset is None and
                        self._checkFrom(charset) and
                        not equalIgnoreCase(self.toEncode,charset)):
                    # 写入文件
                    newContent = content.decode(charset).encode(self.toEncode)
                    newFile = open(filepath,"wb")
                    newFile.write(newContent)
                    self.cnt+=1
                    print("Convert successfully from " + charset + " to " + self.toEncode)
                else:
                    return
        except Exception as e:
            print(e)
            print("Failure for: "+filepath)

    def _checkFrom(self,charset:str):
        if("*" in self.fromEncode):
            return True
        return charset.lower() in self.fromEncode

    # 找到指定后缀的文件
    def _filter(self, fileList:list):
        print("Filtering paths...")
        res = list()
        # 排除指定文件，筛选以subfix结尾的文件
        for file in fileList:
            if(not self._checkSubfix(file) or not self._included(file)):
                print("Exclude: " + file)
                continue
            res.append(file)
        return res

    def _checkSubfix(self,fileName:str):
        if("*" in self.subfix):
            return True
        subfix = getSubfix(fileName,".")
        return subfix in self.subfix

    def _included(self, path:str):
        if(len(self.exclusion) == 0 or self.exclusion is None):
            return True
        # 开始筛选
        for exPath in self.exclusion:
            exPath = os.path.abspath(exPath)
            if (path.find(exPath)!=-1):
                return False
        return True

    def _endShow(self):
        print("\nConversion completed!")
        print("There are "+str(self.cnt)+"/"+str(self.fileCnt)+" files successfully converted.\n")