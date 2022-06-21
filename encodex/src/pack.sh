# 编译打包
pyinstaller -F encodex.py
rm -r ./build encodex.spec
# 移动文件
dirname=encodex-linux-amd64-$1
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
mv $dirname ../release/$1/$dirname
