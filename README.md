# 天堂M外掛說明: 
- 每秒擷取 bluestack 畫面, 影像辨識確認是否已經每日簽到、領取信件(每日獎勵).....等，透過呼叫 win32 api 執行 click 等動作
- 由於透過抓取桌面畫面進行判斷與對應操作. 運行電腦必須全畫面且前景執行. 

# 實際執行環境:
Python 3.7.0
Bluestacks 4

# 安裝套件:
$ pip install pillow
$ pip install numpy
$ pip install win32gui
$ pip install pywin32
$ pip install imagehash
$ pip install opencv-python
#pip install configparser

# 執行 
$python Main.py
