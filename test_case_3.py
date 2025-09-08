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
        #大文字にすることを変数にしてみる   
        ans_upper_text = text.upper()
        return ans_upper_text
    
    def reverse_text(self,text):
        #逆から読むことを変数に入れる
        ans_reverse_text = text[::-1]
        return ans_reverse_text

text_editor_instance = TextEditor()

#犬を変数にすることでここだけ変えれば全部が変わる
original_text = "dog"

print(text_editor_instance .to_upper(original_text))
print(text_editor_instance .reverse_text(original_text ))


#TextEditor クラスを作ってください。下記の内容を反映させた次の2つのメソッドを定義してインスタンスを作成し、それぞれのメソッドを呼び出して結果を出力してください。
#・to_upper(text)：文字列 text を大文字に変換して返すメソッド
#・reverse_text(text)：文字列 text を逆順にし

class TextEditor:
    #メソッドを定義する
    def to_upper(self,text):
        #大文字にしたテキストを変数に入れる
        ans_upper_text = text.upper()
        #戻り値を受け取る
        return ans_upper_text
    
    #メソッドを定義する
    def reverse_text(self,text):
        #一文字を逆順番で表示を変数へ入れる
        ans_reverse_text = text[::-1]
        #戻り値を受け取る
        return ans_reverse_text
    
    #インスタンスを作成する
text_editor_instance = TextEditor()
    
    
original_text = "apple"
    
print(text_editor_instance.to_upper(original_text))
print(text_editor_instance.reverse_text(original_text))


#練習問題
class Recipe:
    def print_ingredients(self):
        print(self.ingredients)

    def add_ingredient(self, new_ingredient):
        self.ingredients.append(new_ingredient)

# 1. インスタンスを作成する
recipe_instance = Recipe()

# 2. インスタンスに ingredients という属性を作成し、初期リストを代入
ingredient_list = ["卵", "ご飯"]
recipe_instance.ingredients = ingredient_list

# 3. 最初の材料リストを出力
print("最初の材料:")
recipe_instance.print_ingredients()

# 4. 新しい材料を追加する
app_ingredient = "ケチャップ"
recipe_instance.add_ingredient(app_ingredient)

# 5. 材料を追加した後のリストを出力
print("ケチャップを追加した後の材料:")
recipe_instance.print_ingredients()

#TextEditor クラスを作ってください。下記の内容を反映させた次の2つのメソッドを定義してインスタンスを作成し、それぞれのメソッドを呼び出して結果を出力してください。
#・to_upper(text)：文字列 text を大文字に変換して返すメソッド
#・reverse_text(text)：文字列 text を逆順にして返すメソッド

#クラスを作る
class TextEditor:
    #メソッドを定義する、第一引数はself
    def to_upper(self,text):
        #textを大文字にしてね！.upper()←ここ忘れない！２回目！を引数に代入、このままだと出力できないから次に戻り値を受け取るようにする
        upper_text = text.upper()
        return upper_text
    
    def reverse_text(self,text):
        #textを逆から表示するは、text[::-1]で文字の最初から最後まで１つずつ逆再生
        ans_reverse_text = text[::-1]
        return ans_reverse_text
    
#インスタンスを作成する
text_editor_instance = TextEditor()

#呼び出したい言葉を変数にいれる
update_text = "soccer"

#メソッドを呼び出す
print(text_editor_instance.to_upper(update_text))
print(text_editor_instance.reverse_text(update_text))


#練習問題
#まずはクラスを設定する
class TextProcessor:
    #メソッドを定義する 大文字
    def to_upper(self,text):
        #大文字の変数
        upper_text = text.upper()
        return upper_text
    
    
    def slice_text(self,text):
        #文字を逆から２個飛ばしの文字をゲット
        add_slice_text = text[::-2]
        return add_slice_text
 
    
#インデントなし！メソッドの外になる　→　インスタンスを定義
text_processor_instance = TextProcessor()

#代入する言葉を変数に入れる
original_text = "september"

#メソッドを２つ呼び出す
print(text_processor_instance.to_upper(original_text))
print(text_processor_instance.slice_text(original_text))


#練習問題
class TextEditor:
    #メソッドを定義する
    def to_upper(self,text):
        #大文字にしたtextを変数へ
        upper_text = text.upper()
        return upper_text
    
    def slice_text(self,text):
        #2番目から開始の2個とびで文字をゲット、文字は1文字目が０だからスタートは１
        get_slice_text = text[1::2]
        return get_slice_text
    
#インスタンスを作成
text_editor_instance = TextEditor()

#どの文字かの変数を作る
original_text = "coffee"

#メソッドを呼び出して、出力する
print(text_editor_instance.to_upper(original_text))
print(text_editor_instance.slice_text(original_text))

#練習問題
class TextEditor:
    #メソッドを定義
    def to_upper(self,text):
        upper_text = text.upper()
        return upper_text
    
    #2個目のメソッド
    def slice_text(self,text):
        #逆から２こ飛ばし
        get_slice_text = text[::-2]
        return get_slice_text
    
#インタンスを作成
text_editor_instance = TextEditor()

#どの文字にする？
original_text = "happy birthday"

#メソッドを呼び出して出力
print(text_editor_instance.to_upper(original_text))
print(text_editor_instance.slice_text(original_text))

#練習問題
class TextEditor:
    #メソッドを定義
    def to_upper(self,text):
        #大文字にする変数
        upper_text = text.upper()
        return upper_text
    
    def slice_and_reverse(self,text):
        #2番目から3つおきに、逆順に表示して返しす
        slice_and_reverse_text = text[1::-3]
        return slice_and_reverse_text
    
#インスタンスを作る
text_editor_instance = TextEditor()

original_text = "october"

#メソッドを呼んで出力
print(text_editor_instance.to_upper(original_text))
print(text_editor_instance.slice_and_reverse(original_text))

#練習問題
class TextEditor:
    #メソッド
    def to_upper(self,text):
        #大文字にするよという変数
        upper_text = text.upper()
        return upper_text
    
    #メソッド２
    def reverse_text(self,text):
        #逆戻りにするよという変数
        get_reverse_text = text[::-1]
        return get_reverse_text
    
#インスタンスを作成
text_editor_instance = TextEditor()
#この文字を変数へ代入
original_text = "sunny day"

#メソッドを呼び出して、出力する！ここに定義したメソッドがあるから、ここにreturnが入る
print(text_editor_instance.to_upper(original_text))
print(text_editor_instance.reverse_text(original_text))


#練習問題
class TextEditor:
    #メソッド①
    def to_upper(self,text):
        #変数作成する、大きくするときは()忘れない
        upper_text = text.upper()
        return upper_text
    
    #メソッド②
    def slice_and_reverse(self,text):
        #2番目から3つおきに、逆順に表示 0スタート
        slice_and_reverse_text = text[1::-3]
        return slice_and_reverse_text
        
#インスタンスを作成
text_editor_instance = TextEditor()
#表示する文字を変数へ代入する
original_text = "tuesday"

#メソッドを呼び出して出力する
print(text_editor_instance.to_upper(original_text))
print(text_editor_instance.slice_and_reverse(original_text))