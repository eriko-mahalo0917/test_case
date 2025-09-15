#【課題】Product クラスを作ってください。
#・コンストラクタ（__init__）で name（商品名）と stock（在庫数）を受け取り、インスタンス変数に保存する
#・add_stock(amount) メソッドで在庫を amount 増やす
#・show_stock() メソッドで 「〇〇の在庫は△△個です」と表示する　インスタンスを作成し、在庫を追加して表示してください。

class Product:
    #コンストラクタはインスタンスを作成したと同時に呼び出される場所！通常のメソッドは呼び出さないと出てこないやつ！初期設定
    def __init__(self,name,stock):
        #ただの商品名をお店の実際の商品名で呼び出しているみたいな？個々を呼び出すイメージ
        self.name = name
        #ただの在庫数をお店の在庫数にするみたいな？
        self.stock = stock
    
    #在庫を追加するメソッド
    def add_stock(self,amount):
        self.stock = self.stock + amount
        print(f'{self.name}の在庫を{amount}増やしました。')
        
    #在庫を表示するメソッド
    def show_stock(self):
        print(f"{self.name} の在庫は {self.stock} 個です。")
        
#インスタンスを作成する　現在の在庫
product_instance = Product("ハニーチュロ",100)

#現在の在庫を表示する
product_instance.show_stock()

#在庫を追加
product_instance.add_stock(10)

# 在庫を追加した後の在庫を表示
product_instance.show_stock()



#もう一度頭ので整理用ーーーーーーーーーーーーーー
#クラスを作る
class Product:
    #初期設定をする イニット 最初に現状の商品名と在庫を呼び出すとしてのコンストラクト
    def __init__(self,name,stock):
        #nameはまだ設定せれていなくて、個別の名前が必要になる
        self.name = name
        #stockも同じように、お店の在庫を入れられるように
        self.stock = stock
    
    #メソッド①在庫の追加を入れる 
    def add_stock(self,amount):
        #在庫を増やすからコンストラクトで呼び出した在庫に追加するようにする
        self.stock = self.stock + amount
        #在庫が何個増やしたかをここで１回教えてあげる！その方が分かりやすいけど、なぜこのamountにはselfはなくていいのかわからない（一時的なデータだから）
        print(f'{self.name}の在庫を{amount}個増やしました。')
        
    #メソッド②在庫増やしたあとの最終的な在庫を出す!ここでは出力するだけでいいから引数は不要だけど第一引数のselfはいるよ！
    def show_stock(self):
        print(f'{self.name}の在庫は{self.stock}個です')
        

#インスタンスを作成する　def __init__(self, name, stock)　←でnameとstockとしたから
product_instance = Product("ホームカットパイ",24)
#これだけだと何も表示されないから最初の在庫を表示するためメソッド②で表示する
product_instance.show_stock()

#在庫を追加するためのメソッドを呼び出す！メソッド時点で在庫増えた表示のprintを設定していたから、増えた個数を教えてくれる
product_instance.add_stock(100)

#最終の在庫を出力する 増えた数との総合が表示される
product_instance.show_stock()


#頭の整理パート②ーーーーーーーーーーーーーー
#クラスを作る
class Product:
    #初期設定のコンストラクト 一番はじめの商品名と在庫数をここで呼び出す
    def __init__(self,name,stock):
        #その商品名と在庫数を表示　今までとは違って、商品自体がデータを持っているということ！前のはtextとしていして、それ自体が色々な情報をもっていなかったから、これはいらなかった！
        #引数外でもselfがいるのは、商品に対して在庫数などの個々のデータがいるからここでもself!
        self.name = name
        self.stock = stock
        
    #メソッド①　在庫を追加する amountは増やした在庫の数の変数
    def add_stock(self,amount):
        #在庫を加算する　ここではすぐに必要がなけど、増えるという括りでここで計算
        self.stock = self.stock + amount
        #何個増えたのかをここで出力する amountは一時的な在庫を増やしたデータの数で、ずっとこのデータを持っているわけではない
        print(f'{self.name}の在庫を{amount}個増やしました。')
        
    #メソッド②　相互の在庫を出力する
    def show_stock(self):
        print(f'{self.name}の在庫は{self.stock}個です')
        

#インスタンを作って呼び出す
product_instance = Product("チョコレートココナッツ",39)
#現状の在庫を呼び出す
product_instance.show_stock()
#在庫を追加する
product_instance.add_stock(55)
#最終の在庫を表示
product_instance.show_stock()

product_instance = Product("ハニーオールドファッション",50)
#現状の在庫を呼び出す
product_instance.show_stock()
#在庫を追加する
product_instance.add_stock(5)
#最終の在庫を表示
product_instance.show_stock()


#【類似問題】とりあえず数をこなして身につけよう！

class Book:
    #コンストラクタ:title（本のタイトル）と author（著者名）を受け取り、インスタンス変数に保存する。
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    #メソッド①「タイトル: 〇〇、著者: △△」という形式で、本の情報を表示する。※第一引数を（）のとき忘れない
    def display_info(self):
        print(f'タイトル: {self.title}、著者: {self.author}')
        

#インスタンスを作る
book_instance1 = Book('お金の大冒険','学長')
#メソッド①を呼び出す
book_instance1.display_info()

#インスタンスを作る
book_instance2 = Book('つかめ！理科ダマン','シン・テフン')
#メソッド①を呼び出す
book_instance2.display_info()


#【類似問題】
#コンストラクタ（__init__）color（車の色）と maker（メーカー名）を受け取り、インスタンス変数に保存する。
class Car:
    def __init__(self,color,maker):
        #車自体の色とメーカーを定義する
        self.color = color
        self.maker = maker
        
    #メソッド①「〇〇色の、△△製の車がエンジンをかけました。」と表示する。第一引数selfを忘れない
    def start_engine(self):
        print(f'{self.color}色の、{self.maker}製の車がエンジンをかけました。')
        
        
#インスタンスを作成①
car_instance1 = Car('イエロー','TOYOTA')
car_instance1.start_engine()

#インスタンスを作成②
car_instance2 = Car('ブラック','ワーゲン')
car_instance2.start_engine()


#【類似問題】関数２つにちょいレベアップ
#コンストラクトにname（生徒の名前）と grade（学年）を受け取り、インスタンス変数に保存する。
#Student クラス
class Student:
    #コンストラクト
    def __init__(self,name,grade):
        #ここで受け取ったデータを引数に代入しているらしい！だから、これからインスタンスで指定したものがここに入るイメージ
        self.name = name
        self.grade = grade
        
    #今の学年を表示する！initとは別の役割だから、表示だけのためを作成
    def show_grade(self):
        print(f'現在の学年：{self.grade}')
        
    #メソッド①「〇〇（名前）は熱心に勉強しています。」と表示する。
    def study(self):
        print(f'{self.name}は熱心に勉強しています。')
        
    #メソッド②graduate()「〇〇（名前）は学校を卒業しました！」と表示し、学年 (self.grade) を「卒業」という文字列に更新する。
    def graduate(self):
        print(f'{self.name}は学校を卒業しました！')
        #学年を卒業へ更新
        self.grade = '卒業'
        
        
#インスタンスを作って呼び出す
student = Student('青森りんご','高校3年生')
# 現在の学年データを表示
student.show_grade()
student.study()
student.graduate()
# 現在の学年データを表示
student.show_grade()


#【類似問題】
#Student クラスを作成
class Student:
    #コンストラクタ（__init__）:name（生徒の名前）と age（年齢）を受け取り、インスタンス変数に保存
    def __init__(self,name,age):
        #受け取ったデータを入れるとこ、インスタンスで作成した名前と年齢が入る場所
        self.name = name
        self.age = age
        
    #メソッド①greet() メソッド:"こんにちは、私は〇〇（名前）です。" と表示させる
    def greet(self):
        print(f'こんにちは、私は{self.name}です。')
        
    #メソッド②celebrate_birthday() メソッド:"〇〇（名前）は誕生日を迎えました！" と表示し、age を1歳増やす
    def celebrate_birthday(self):
        print(f'{self.name}は誕生日を迎えました！')
        #1歳加算した年齢へ更新
        self.age = self.age + 1
        
    #表示するためのメソッド
    def show_info(self):
        print(f'名前：{self.name},年齢：{self.age}歳') 
        
        
#インスタンスを作成する
student_instance = Student('ナンシー',30)
#現状を呼び出す
student_instance.show_info()
#メソッド①を呼び出す
student_instance.greet()
#メソッド②を呼び出す
student_instance.celebrate_birthday()
#現状を呼び出す
student_instance.show_info()

