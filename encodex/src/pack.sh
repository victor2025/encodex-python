osname=$(uname -s|tr A-Z a-z)
# 处理win下的osname
result=$(echo $osname|grep "mingw")
if [ "$result" != "" ]
then
	osname="win"
fi
# 处理其他名称
archname=$(uname -m|tr A-Z a-z)
dirname=encodex-$osname-$archname-$1
# 编译打包
pyinstaller -F encodex.py
rm -r ./build encodex.spec
# 移动文件
mkdir $dirname
mv ./dist/encodex $dirname/encodex
rm -r dist
cp config.ini $dirname/config.ini
# 压缩
tar -czvf $dirname.tar.gz $dirname
# 移动压缩包
mv $dirname.tar.gz ./$dirname/$dirname.tar.gz
# 移动文件夹
mkdir ../release/$1
rm -r ../release/$1/$dirname
mv $dirname ../release/$1/$dirname