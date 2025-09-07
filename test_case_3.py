#TextEditor クラスを作ってください。下記の内容を反映させた次の2つのメソッドを定義してインスタンスを作成し、それぞれのメソッドを呼び出して結果を出力してください。
#・to_upper(text)：文字列 text を大文字に変換して返すメソッド
#・reverse_text(text)：文字列 text を逆順にして返すメソッド
#・init（コンストラクタ）は記述しない。

#クラスを作る！クラスの名前は最初は大文字ルール！
class TextEditor:
    #クラスの中に作った関数をメソッドという！第一引数はselfが絶対の条件でここにインスタンスの情報が入っていく
    def to_upper(self,text):
        #文字.upper()で大文字にする　→　大文字の戻り値をゲット
        return text.upper()
    
    #逆順のメソッドを作るここでも第一引数はself
    def reverse_text(self,text):
        #逆から読んでもは：←最初：←最後　−１←順番だから、textを1個ずつ逆戻り（スライス）　→戻り値をゲット
        return text[::-1]

#クラスのインスタンスを変数名を作って設定する　この箱の中にはメソッドの関数が２つ入っている
text_editor1 = TextEditor()

#ここでクラスで作ったメソッドの戻り値がそれぞれ入って、表示される
print(text_editor1.to_upper("dog"))
print(text_editor1.reverse_text("dog"))


class TextEditor:
    def to_upper(self,text):        
        return text.upper()
    
    def reverse_text(self,text):
        return text[::-1]

text_editor_instance = TextEditor()

original_text = "dog"

print(text_editor_instance .to_upper(original_text))
print(text_editor_instance .reverse_text(original_text ))