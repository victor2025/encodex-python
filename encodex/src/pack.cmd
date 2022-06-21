::编译打包
pyinstaller -F encodex.py
rm -r ./build encodex.spec
:: 移动文件
set dirname=encodex-win-x86_64-%1%
mkdir %dirname%
mv ./dist/encodex %dirname%/encodex
rm -r dist
copy config.ini %dirname%
:: 压缩
tar -cf %dirname%.tar.gz %dirname%
:: 移动压缩包
mv %dirname%.tar.gz %dirname%/%dirname%.tar.gz
:: # 移动文件夹
set para=%1%
set home=%cd%
cd ../release
mkdir %para%
cd %home%
mv %dirname% ../release/%para%/%dirname%