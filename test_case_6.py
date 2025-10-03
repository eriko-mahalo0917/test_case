

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ライブラリにあるクラスからインスタンスを作成
options = Options()
#アーギュメントでウィンドウのサイズを指定
options.add_argument("--window-size=1000,860")
#options=optionsはさっき指定した通りに実行してねというお約束
chrome_gu = webdriver.Chrome(options=options)
url = "https://gu-global.com/jp/ja/kids"

chrome_gu.get(url)
input("ブラウザを閉じるにはEnterキーを押してください...")