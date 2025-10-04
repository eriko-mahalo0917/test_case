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

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝もう一回＝＝＝＝＝＝＝＝＝＝
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ログの機能の基本設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#サイズを決めるためのインスタンスを作成
chrome_options = Options()
#サイズを指定する
chrome_options.add_argument("--window-size=1000,800")
#位置を指定する
chrome_options.add_argument("--window-position=200,200")

#ログを作成する
logging.info("これからブラウザを起動します")
#ブラウザを起動させるインスタンスを作成
chrome = webdriver.Chrome(options=chrome_options)
#起動したことをログで教える
logging.info(f"ブラウザを起動できました")

url_gu = "https://gu-global.com/jp/ja/kids"

#サイトを開く前にログでお知らせ
logging.info(f"サイトを開きます：{url_gu}")
#サイトを開く
chrome.get(url_gu)
#サイトを開いたことを教える
logging.info("サイトを開きました")

input("確認をしたらエンターで閉じれます")

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ログの機能の基本設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#サイズと位置を決めるためのインスタンスを作成
chrome_options  = Options()
chrome_options.add_argument("--window-size=1100,700")
chrome_options.add_argument("--window-position=50,50")

#ログを記録して、ブラウザを起動する
logging.info("これからブラウザを起動します")
chrome_amazon = webdriver.Chrome(options=chrome_options)
logging.info("ブラウザを起動しました")

#AmazonのURLを指定
url_amazon = "https://www.amazon.co.jp/"

#ログを記録してサイトを開く
logging.info(f"サイトを開きます:{url_amazon}")
chrome_amazon.get(url_amazon)
logging.info("サイトを開きました")

input("確認後にエンターを押すと閉じます")

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#loggingを呼びだす
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#三つ星シェフ
from selenium.webdriver.chrome.service import Service

#ログの基本設定で、表示形式を指定する
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#サイズを決めるためのインスタンスを作成する
chrome_options = Options()
chrome_options.add_argument("--window-size=1100,700")
chrome_options.add_argument("--window-position=50,50")

#Serviceのインスタンスを作成
service = Service()

#ログを記録する
logging.info("これからブラウザを起動します")
#Serviceとoptionsの両方を引き渡してブラウザを起動させる　この時点で起動開始している
chrome = webdriver.Chrome(service=service, options=chrome_options)
#ログを記録
logging.info("ブラウザを起動しました")

#Amazonのurlを代入する
url_amazon = "https://www.amazon.co.jp/"

#ログを記録する
logging.info(f"これからサイトを開きます{url_amazon}")
chrome.get(url_amazon)
logging.info("サイトを開きました")

input("確認後にエンターを押してサイトを閉じてください")

#クラスを入れてみるよ=============================================================
#インポートしてくる
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#ここからクラスの設計図＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
class ChromeManager:
    
    #作られたときの初期設定を行う
    def __init__(self):
        #ログの基本えっ体をここで行う
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        print("ChromeManagerロボットの準備ができました！")
        
    def open_site(self,url):
        
        #サイズを決めるためのインスタンスを作成する
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1100,700")
        chrome_options.add_argument("--window-position=50,50")
        
        #Serviceのインスタンを作成する
        service = Service()
        
        #ログを記録して、ブラウザを起動
        logging.info("これからブラウザを起動します")
        chrome =webdriver.Chrome(service=service,options=chrome_options)
        logging.info("ブラウザを起動しました")
        
        #ログを記録してサイトを開く
        logging.info(f"サイトを開きます{url}")
        chrome.get(url)
        logging.info("サイトを開きました")
        
        input("確認後にエンターを押してサイトを閉じてください")
        
#実際にこれを動かしてみるぞ！
chrome_manager = ChromeManager()
#開きたいサイトを指定する
amazon_url = "https://www.amazon.co.jp/"

chrome_manager.open_site(url = amazon_url)


#もう一度復習で書いていきます！==============================================
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#クラスを作成していきます
class ChromeManager:
    
    #コンストラクタを作成（書記設定）
    def __init__(self):
        #ログの表示は全部一緒だから初期設定でOK
        logging.basicConfig(level=loggin.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
        print("ChromeManagerの準備ができました！")
        
        
    #サイトを開くためのメソッドを作成していく
    def open_site(self,url):
        #サイズを設定するインスタンスをメソッドの中にいれる
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1100,700")
        chrome_options.add_argument("--window-position=100,100")
        
        #serviceのインスタンを設置
        service = Service()
        
        #ログ機能を設置してブラウザを開く
        logging.info("ブラウザを開きます")
        chrome = webdriver.Chrome(service=service,options=chrome_options)
        logging.info("ブラウザを開きました")
        
        #ログを記録してサイトを開く
        logging.info(f"サイトを開きます{url}")
        chrome.get(url)
        logging.info("サイトを開きました")
        
        input("確認後にエンターを押すと閉じます")
        
#実装してみよう！！インスタンスを作成
chrome_manager = ChromeManager()
url_gu =  "https://gu-global.com/jp/ja/kids"
#メソッドを呼び出して実装
chrome_manager.open_site(url=url_gu)

#＝＝＝try exceptへ進みます＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#インポートしてくる
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#ここからクラスの設計
class ChromeManager:
    
    #コンストラクタで初期設定　ログを設置は共通事項
    def __init__(self):
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
        print("ChromeManagerロボットの準備ができました！")
        
    #専門家①を呼ぶよ！ブラウザ設定を決める係
    def get_chrome_options(self):
        logging.info("ブラウザのオプションを設定します")
        #インスタンスを作成
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1100,700")
        chrome_options.add_argument("--window-position=100,100")
        #完成した設定をここい戻り値として入れる
        return chrome_options
    
    #専門家②ブラウザ起動係
    def start_chrome(self):
        logging.info("ブラウザを起動準備を開始します。")
        #専門家①を呼び出して設定してもらう
        chrome_options = self.get_chrome_options()
        service = Service()
        
        logging.info("これからブラウザを起動します")
        chrome = webdriver.Chrome(service=service ,options=chrome_options)
        logging.info("ブラウザを起動しました")
        return chrome #ブラウザを起動したことを戻り値？
    
    #司令とが登場
    def open_site(self,url):
        #専門家②を呼ぶ
        chrome_browser = self.start_chrome()
        
        logging.info("サイトをひらいきます{url}")
        chrome_browser.get(url)
        logging.info("サイトを開きました")
        
        input("確認後はエンターを教えてサイトを閉じてください")
        
#実際に動かしてみるよ
chrome_manager = ChromeManager()
amazon_url = "https://www.amazon.co.jp/"

chrome_manager.open_site(url=amazon_url)

#インポートで呼び出すよ
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#クラスを設計するよ
class ChromeManager:
    
    #初期設定でログ機能を設置
    def __init__(self):
        logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
        print("ChromeManagerロボットの準備ができました！")
        
    #専門家①はブラウザの設定を決める係
    #インスタンスを作成する
    def get_chrome_option(self):
        logging.info("ブラウザのオプションを設定します。")
        #インスタンスを作成する
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1000,800")
        chrome_options.add_argument("--window-position=100,100")
        #完成した設定を呼び出すしてreturnの中に入れている　設定し終わった完成品を渡す感じ
        return chrome_options
    
    #専門家②ブラウザの起動係
    def start_chrome(self):
        