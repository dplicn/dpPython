# dpPython

## 环境配置

### Python pip 安装与使用


pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。

+ 你可以通过以下命令来判断是否已安装：

`pip --version`

+ 如果你还未安装，则可以使用以下方法来安装：

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
$ sudo python get-pip.py    # 运行安装脚本
```
注意：用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本，如果是 Python3 则执行以下命令：

```

$ sudo python3 get-pip.py    # 运行安装脚本。
```
一般情况 pip 对应的是 Python 2.7，pip3 对应的是 Python 3.x。

部分 Linux 发行版可直接用包管理器安装 pip，如 Debian 和 Ubuntu：

```
sudo apt-get install python-pip
```

### pip 最常用命令

```
pip --version  #显示版本和路径
pip --help #获取帮助
pip install -U pip #升级 pip
```
如果这个升级命令出现问题 ，可以使用以下命令：

```
sudo easy_install --upgrade pip

pip install SomePackage              # 安装包最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本

pip install --upgrade SomePackage #升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。

pip uninstall SomePackage #卸载包

pip search SomePackage #搜索包

pip show  #显示安装包信息

pip show -f SomePackage #查看指定包的详细信息

pip list #列出已安装的包

pip list -o #查看可升级的包
```
#### 注意事项

如果 Python2 和 Python3 同时有 pip，则使用方法如下：

+ Python2：
```
python2 -m pip install XXX
```

+ Python3:
```
python3 -m pip install XXX
```