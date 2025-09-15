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
        #在庫が何個増やしたかをここで１回教えてあげる！その方が分かりやすい
        print(f'{self.name}の在庫を{amount}増やしました。')
        
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