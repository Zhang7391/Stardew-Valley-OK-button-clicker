# Stardew Valley Tool(星露谷物語工具)

When we set the economy to be shared in Stardew Valley, whenever someone sells anything, we all have to click the "OK" button on the settlement screen. For regular players, this is no problem, but as the server host, we constantly need to be ready to help click the "OK" button. This tool is designed to free the server host's hands from this repetitive task.  

當我們在星露谷物語中設定經濟為共用的時候，當其他人有販賣任何東西的時候，我們都必須點擊結算畫面上的 OK 按鈕，對於一般玩家來說當然沒有問題，但是當我們是伺服器主的時候，就必須時時刻刻準備幫忙點擊OK按鈕，此工旨在解放伺服器主的雙手。

## dependency（此工具的依賴）
- VNC  
  (Recommend/推薦VNC) [TightVNC](https://www.tightvnc.com/)

## Getting start(讓我們開始吧)
### Windows
```cmd
git clone https://github.com/Zhang7391/Stardew-Valley-OK-button-clicker.git
cd Stardew-Valley-OK-button-clicker
python -m pip install -r requirements.txt
& "C:\Program Files\TightVNC\tvnserver.exe" -run
python stardewValleyAutoConfirm.py
```
From now on, there is no need to move the mouse, or the remote desktop can be minimized and placed in the foreground (but not in the background).  

接下來就不用移動滑鼠或是可以將遠端桌面縮小放在前景（請不要縮到最小）