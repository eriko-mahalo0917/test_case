#今日の日付を取得する モジュールを取得する
from datetime import date


today =date.today()
print(today)
print(type(today))

#現在の日時を取得する場合
from datetime import datetime


now = datetime.now()
print(now)
print(type(now))

print("-----------------------")

d = date(2025,9,23)
print(d)

d = datetime(2025,9,23,15,12,11)
print(d)

year = d.year
month = d.month
day = d.day
print(day)

d1 = date(2025,9,23)
d2 = date(2025,9,20)
delta = d1 - d2
print(delta)

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
RED = "\033[91m"
print(f'{RED}これはERRORです')
print("リセットしなければそのまま赤です")

#リセットする
RESET = "\033[0m"
print(f'{RESET}基本の色にリセットしました')

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 使う部品は最初にまとめて定義しておく
RED = "\033[91m"
RESET = "\033[0m"

# メッセージをカラーコードとリセットコードで挟む
print(f'{RED}これはERRORです{RESET}')

# 上の行でリセット済みなので、この行は通常の色で表示される
print("ここはもう赤色にはなりません。")

#==============================================================

# 1. LoggerBasicColorクラスにあったCOLORS辞書を再現
COLORS = {
    "DEBUG": "\033[90m",
    "INFO": "\033[94m",
    "WARNING": "\033[93m",
    "ERROR": "\033[91m",
}
RESET = "\033[0m" # 色をリセットするコード

log_level_1 = "INFO"
#ここでINFOを入れている
color_1 = COLORS.get(log_level_1,"")
print(f"{log_level_1}を探した場合：{color_1}この文字が青色になります{RESET}")

log_level_2 = "SPECIAL"
color_2 = COLORS.get(log_level_2,"")
print(f"{log_level_2}を探した場合：{color_2}{RESET}")

log_level_3 = "DEBUG"
color_3 = COLORS.get(log_level_3)
print(f"{log_level_3}を探した場合：{color_3}この文字がグレーになります{RESET}")


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ーー
#親のクラス（師匠）を定義
class Master:
    def greet(self,message):
        #師匠の仕事は、メッセージの前に「師匠より：」とつけること
        return f"師匠より：「{message}」"
    

#子クラスの（弟子）のメッセージ
#親の力を呼び出す
class Apprentice(Master):
    def greet(self,message):
        #ここで師匠で定義して基本の文章を呼び出す
        message_greeting = super().greet(message)
        #師匠が作った挨拶の自分の言葉を加える
        return f"{message_greeting}...弟子より追伸"

#インスタンスを定義する
apprentice = Apprentice()
#上書きされるとどうなる？
final_greeting = apprentice.greet("おはよう")
print(final_greeting)

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#親のクラスを定義
class Vehicle:
    #メソッドを作成する
    def start_engine(self):
        #エンジンがかかったとメッセージを返す
        print("エンジンがかかりました")
    
 #親のクラスをバージョンアップ   
class Car(Vehicle):
    def start_engine(self):
        super().start_engine() #親のメッセージをここで呼び出している
        print("安全のため、シートベルトを締めてください。")
    
#インスタンスを作成する
car = Car()
car.start_engine()

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#親クラス
class Vehicle:
    def start_engine(self):
        message = "エンジンがかかりました"
        return message
    
    
#子クラス
class Car(Vehicle):
    def start_engine(self):
        parent_message = super().start_engine()
        child_message = "安全のため、シートベルトを締めようぜ！"
        final_message = f"{parent_message}\n{child_message}"
        return final_message
    
#インスタンスを作成する
car = Car()
full_message = car.start_engine()
print(full_message)

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#簡単な翻訳
#親クラスを作る
class Translator:
    #メソッド
    def translate(self,word):
        return f"翻訳できません：{word}"
    
class JapaneseTranslator(Translator):
    #辞書をここで定義する
    WORDS = {"hello":"こんにちは","world":"世界"}
    
    # ★修正1: メソッド名を "translate" に直す
    def translate(self, word):
        #辞書の翻訳があるのかゲットで呼ぶ
        # ※前回のタイプミス self.WORDS も修正済み
        translation = self.WORDS.get(word)
        #もし、翻訳がみつかったら
        if translation:
            return translation
        
        else:
            # ★修正2: 呼び出すメソッド名も "translate" に直す
            return super().translate(word)
        
# --- 実行部分 ---
# インスタンスを作成
translator = JapaneseTranslator()

# "hello" を翻訳
print(translator.translate("hello"))

# "python" を翻訳
print(translator.translate("python"))

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#getの練習
#商品リストを作る
drinks = {"cola": "コーラ", "tea": "お茶", "water": "水"}

def get_drink(drink_code):
    push_get_drink = drinks.get(drink_code)
    #もしあればValueを呼び出す
    if push_get_drink:
        return push_get_drink
    else:
        return "売り切れです"
    
print(get_drink("tea"))
print(get_drink("juice"))


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#会員IDを伝えると、現在のポイント残高を教えてくれるプログラムを作ります。
#辞書を作成する

point_balances = {"user001": 500, "user002": 1200, "user003": 80}
point_balances["user004"] = 0

#ポイント残高を確認する関数を作成する
def check_points(user_id):
    #ユーザーIDを探して、なければ会員ではありません
    check_user = point_balances.get(user_id)
    
    if check_user is not None:
        return check_user
    
    else:
        return "会員ではありません"
    
print(check_points("user002"))
print(check_points("user004"))

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#果物の名前を伝えると、その値段を教えてくれるプログラムを作ります
#値段リストを作成

prices = {"apple": 150, "banana": 100, "orange": 120}

#値段を調べる関数を作る
def get_price(fruit_name):
    #辞書の中にあればそれを選んで、なければ取扱なし出力
    return  prices.get(fruit_name, "その果物は取り扱っていません")

print(get_price("apple"))
print(get_price("grape"))

#===============================================================
#チームの名簿を作る

team_roles = {"Tanaka": "Leader", "Suzuki": "Engineer", "Sato": "Designer"}

#関数を作成し、受け取った名前が名簿にあれば役職を、なければありません表記
def find_role(name):
    return team_roles.get(name, "チームメンバーではありません")

#実行して確認
print(find_role("Suzuki"))
print(find_role("yamada"))


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#classバージョン
#生徒のclassを作成

class Student:
    def __init__(self,name,score):
        #受け取った名前を保存する
        self.name = name
        
        #これから点数を入れる空っぽの辞書を用意
        self.scores = {}
        
    #メソッド①点数を追加するメソッド
    def add_score(self,subject,score):
        # self.scores辞書に、subjectをキー、scoreを値として追加
        self.scores[subject] = score
        
    #メソッド②　得点を取得する
    def get_score(self,subject):
        return self.score.get(subject, "まだその科目のテストは受けていません") 
    

#実行する
