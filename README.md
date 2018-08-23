### 安装 opencv 依赖库
```
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install python3-pyqt5
```

### 虚拟环境
```
mkvirtualenv -p python3 pyqrcode-env
workon pyqrcode-env
```

### 安装 Python 依赖库
```
pip install -r requirements.txt
```

### 运行程序
```
python src/barcode_scanner_image.py --image test.png
```

