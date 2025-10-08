#復習#####################
#インポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#探す役目の人
from selenium.webdriver.common.by import By
#型ヒント？
from selenium.webdriver.remote.webdriver import WebDriver
from my_logger import SimpleLogger

#=========================================
#ChromeDriverManagerクラスを作成する ブラウザのサイズ変更
class ChromeDriverManager:
    #初期設定
    def __init__(self):
        #ログは全部共通なのでここでセット
        self.getLogger = SimpleLogger() #インスタンス作成
        self.logger = self.getLogger.get_logger() #一行前のメソッドを呼び出す
        
        
    #①ウィンドウサイズを設定する係
    def get_chrome_option():
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1000,1000")
        #設定した内容を戻り値でゲット
        return chrome_options
    
    
    #ブラウザを立ち上げるドライバー係
    def chrome_process(self):
        service = Service()
        #①ウィンドウザイズの係を呼ぶ
        chrome_options = self.get_chrome_options()
        #うまくできなかった場合で処理を分ける
        try:
            self.logger.info(f"ドライバーの起動をします")
            #①を呼んでここに連れてくる！ウィンドウのサイズの係の人を第ぬ有
            chrome =  webdriver.Chrome(service=Service ,Options = chrome_options)
            self.logger.info(f"ドライバーを起動しました")
            return chrome
        except Exception as e:
            self.logger.error(f"ドライバーの起動に失敗しました")
            self.logger.error(f"エラーの内容：{e}")
            #処理停止
            raise