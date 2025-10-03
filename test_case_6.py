from selenium import webdriver

# 1. Chromeブラウザを起動し、操作するための「リモコン」を用意する
driver = webdriver.Chrome()

# 2. 行きたいサイトのURLを変数に入れる
url = "https://www.uniqlo.com/jp/ja/"

# 3. リモコンの「移動」ボタンを押して、そのURLに移動させる
driver.get(url)

# メモ: プログラムが一瞬で終わらないように、何かキーを押すまで待つおまじない
input("ブラウザを閉じるにはEnterキーを押してください...")


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

#標準モジュールから呼び出している
from selenium import webdriver
#標準モジュールから親インスタンスを呼び出している
chrome = webdriver.Chrome()
#変数にURLを代入する
url = "https://www.yahoo.co.jp/"
#親のインスタンスを利用していて、.getでサイトを開いてって意味
chrome.get(url)

input("ブラウザを閉じるにはEnterキーを押してください...")

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#ウェブサイトを開くために呼び出す
from selenium import webdriver
#インスタンスを作成
chrome_select = webdriver.Chrome()
select_url = "https://selectshopmoca.com/"

chrome_select.get(select_url)
input("ブラウザを閉じるにはEnterキーを押してください...")


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#標準ライブラリからサイトを開くために呼び出す
from selenium import webdriver
#Chromeブラウザの起動オプション（ウィンドウサイズなど）を設定するための、あらかじめ用意された機能
from selenium.webdriver.chrome.options import Options
#インスタンスの作成
options = Options()
options.add_argument("--window-size=840,600")

#インスタンス作成で親クラスから呼び出している
chrome_gu = webdriver.Chrome(options=options)
url = "https://gu-global.com/jp/ja/kids"

chrome_gu.get(url)
input("ブラウザを閉じるにはEnterキーを押してください...")


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

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#画面をフルサイズで表示
options.add_argument("--start-maximized")
#サイトを開く準備
chrome_gu = webdriver.Chrome(options=options)

url = "https://gu-global.com/jp/ja/kids"

chrome_gu.get(url)

input("ブラウザを閉じるにはEnterキーを押してください...")

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ウィンドウサイズを指定するインスタンスを作成する
options = Options()
#画面サイズを指定
options.add_argument("--window-size=1500,1000")

#サイトを開くためのインスタンスを作成するけど、設定したサイズで開くために引数はoptions=options
chrome_uniqlo = webdriver.Chrome(options=options)
#urlを指定する
uniqlo_url = "https://www.uniqlo.com/jp/ja/baby"
#サイトを開くためにメソッドを呼び出す
chrome_uniqlo.get(uniqlo_url)
input("ブラウザを閉じるにはEnterキーを押してください...")

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#サイズを指定するためのインスタンスを作成する
chrome_options = Options()
#メソッドを呼び出してサイズを指定する
chrome_options.add_argument("--window-size=1000,800")
#開く位置を指定する
chrome_options.add_argument("--window-position=0,0")

#サイトを開くためのインスタンスを作成し、指定したサイズとポジションで開くための引数を設置
chrome = webdriver.Chrome(options=chrome_options)
#urlにサイトを代入
url_gu = "https://gu-global.com/jp/ja/kids"
#サイトを開くためのメソッドを呼び出す
chrome.get(url_gu)

input("ブラウザを閉じるにはEnterキーを押してください...")

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ウィンドウサイズを設定するインスタンスを作成
chrome_options = Options()
#メソッドを呼び出して、サイズを指定する
chrome_options.add_argument("--window-size=1200,900")
#開く位置を指定する
chrome_options.add_argument("--window-position=10,10")

#サイトを開くためのインスタンスを作成する
chrome = webdriver.Chrome(options=chrome_options)
#サイトを指定する
url_gu = "https://gu-global.com/jp/ja/kids"
#サイトを開く
chrome.get(url_gu)

input("ブラウザを閉じるにはEnterキーを押してください...")

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#次はクラスを使わずにログのコードを取得する練習　→　その後にクラス追加予定

#ログを取得するためにライブラリから呼び出す
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#-----ログ機能の基本設定‐‐‐‐‐
#INFOレベル以上のメッセージを記録するように設定 時刻・ログのレベル・記録のメッセージ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#サイズを決めるためのインスタンスを作成
chrome_options = Options()
#サイズを指定する
chrome_options.add_argument("--window-size=1000,800")
#表示位置をしていする
chrome_options.add_argument("--window-position=100,100")

#ブラウザを起動する
#このログは定型文のようなイメージ　記録したい場所に設置
logging.info("これからブラウザを起動します")
#ブラウザを起動させるインスタンスを作成
chrome = webdriver.Chrome(options=chrome_options)
#ログで起動したことを教える
logging.info("ブラウザを起動できました")

#urlを指定する
url_gu = "https://gu-global.com/jp/ja/kids"

#サイトを開く前にまたログを表示させる
logging.info(f"これからサイトを開きます：{url_gu}")
#サイトを開く
chrome.get(url_gu)
#ログを作成し開いたことを教える
logging.info("サイトを開きました")


input("ブラウザを閉じるにはEnterキーを押してください...")

#