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

#練習問題
class TextEditor:
    #メソッド
    def to_upper(self,text):
        upper_text = text.upper()
        return upper_text
    
    def slice_and_reverse(self,text):
        slice_and_reverse_text = text[1::-3]
        return slice_and_reverse_text
    
#インスタンスを作成
text_editor_instance = TextEditor()

#変数へ変更する言葉を代入
original_text = "Pneumonoultramicroscopicsilicovolcanoconiosis"

#メソッドを実行して出力
print(text_editor_instance.to_upper(original_text))
print(text_editor_instance.slice_and_reverse(original_text))

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#【自分だけで解いた解答】
#クラスを作る
class Calculator:
    #メソッド①
    def add(self,x,y):
        add_answer = x + y
        return add_answer
    
    #メソッド②
    def double_x(self,x):
        double_x_answer = x * 2
        return double_x_answer
    
    
#インタンスを作る
calculator_instance = Calculator()

#add_resultで戻り値を受け取って、メソッドを実行
add_result = calculator_instance.add(3,5)
print(add_result)

#double_x_answer_resultで戻り値を受け取って、メソッドを実行
double_x_answer_result = calculator_instance.double_x(3)
print(double_x_answer_result)



#【AIを利用して修正した解答】
#クラスを作る
class Calculator:
    #メソッド①　３行構成
    def add(self,x,y):
        add_answer = x + y
        return add_answer
    
    #メソッド②　３行構成
    def double_x(self,x):
        double_x_answer = x * 2
        return double_x_answer
    
    
#インタンスを作る
calculator_instance = Calculator()

#数字を変数へ代入する
x_num = 3
y_num = 5

#add_resultで戻り値を受け取って、メソッドを実行　名前=値 の形で渡すことが、キーワード引数ということ！
add_result = calculator_instance.add(x=x_num,y=y_num)
print(add_result)

#double_x_answer_resultで戻り値を受け取って、メソッドを実行　名前=値 の形で渡すことが、キーワード引数ということ！
double_x_answer_result = calculator_instance.double_x(x=x_num)
print(double_x_answer_result)


#【引数とキーワード引数を同じにした修正した解答】
#クラスを作る
class Calculator:
    #メソッド①　３行構成
    def add(self,x_num,y_num):
        add_answer = x_num + y_num
        return add_answer
    
    #メソッド②　３行構成
    def double_x(self,x_num):
        double_x_answer = x_num * 2
        return double_x_answer
    
    
#インタンスを作る
calculator_instance = Calculator()

#数字を変数へ代入する
x_num = 3
y_num = 5

#add_resultで戻り値を受け取って、メソッドを実行　名前=値 の形で渡すことが、キーワード引数ということ！
add_result = calculator_instance.add(x_num,y_num)
print(add_result)

#double_x_answer_resultで戻り値を受け取って、メソッドを実行　名前=値 の形で渡すことが、キーワード引数ということ！
double_x_answer_result = calculator_instance.double_x(x_num)
print(double_x_answer_result)

#練習
#クラスを作る
class Calculator:
    #メソッド①の第一引数にはself
    def add(self,x_num,y_num):
        add_answer = x_num + y_num
        return add_answer
    
    #メソッド②
    def double_x(self,x_num):
        double_x_answer = x_num * 2
        return double_x_answer
    
#インスタンスを作成する
calculator_instance = Calculator()

#キーワード引数へ代入
x_num = 3
y_num = 5

#メソッドを呼び出して出力
add_result = calculator_instance.add(x_num,y_num)
print(add_result)

double_x_answer_result = calculator_instance.double_x(x_num)
print(double_x_answer_result)

#類似問題
class Box:
    def get_volume(self,length,width,height):
        volume = length * width * height
        return volume
    
    
    def get_surface_area(self,length,width,height):
        surface_area  = 2 * (length * width + width * height + height * length)
        return surface_area

#インスタンス作成
box_instance = Box()

#数を代入
length = 10
width = 5
height = 3

#メソッドを呼び出す
volume_result = box_instance.get_volume(length,width,height)
print(volume_result)

surface_ara_result = box_instance.get_surface_area(length,width,height)
print(surface_ara_result)

#練習問題
#クラスを作る
class Geometry:
    #メソッド① get_circle_area(): 半径（radius）を使った円の面積
    def get_circle_area(self,radius):
        area = radius * radius * 3.14
        return area
    
    #メソッド② 一辺の長さ（side）を使った正方形の周りの長さ
    def get_square_perimeter(self,side):
        perimeter = side * 4
        return perimeter
    
    
#インダンスを作成
geometry = Geometry()

#数を代入
radius = 10
side = 5

#メソッドを呼び出して実行&出力
area_result = geometry.get_circle_area(radius)
print(area_result)

perimeter_result = geometry.get_square_perimeter(side)
print(perimeter_result)

#練習　Arithmetic クラスを定義してください。
class Arithmetic:
    #メソッド①
    def subtract(self,x_num,y_num):
        #x - y の結果を result に入れて、それを返す
        ans_subtract = x_num - y_num
        return ans_subtract
    
    #メソッド② t
    def triple_y(self,y_num):
        #triple_y()：y * 3 の結果を result に入れて、それを返す。
        triple_y_ans = y_num * 3
        return triple_y_ans
    
#インスタンスを作成
arithmetic_instance = Arithmetic()

#キーワード引数へ代入
x_num = 10
y_num = 4

#メソッドを呼び出す
ans_subtract_result = arithmetic_instance.subtract(x_num,y_num)
print(ans_subtract_result)

triple_y_ans_result = arithmetic_instance.triple_y(y_num)
print(triple_y_ans_result)


#Converter クラスを定義してください。
class Converter:
    #メソッド①　multiply()：a * b の結果を result に入れて、それを返す。
    def multiply(self,a_num,b_num):
        ans_multiply = a_num * b_num
        return ans_multiply
    
    #メソッド②　half_a()：a / 2 の結果を result に入れて、それを返す。
    def half_a(self,a_num):
        ans_half_a = a_num / 2
        return ans_half_a
    
#インタンスを作成する
converter = Converter()

#数字を代入する
a_num = 20
b_num = 5

#returnを受け取ってメソッドを呼び出して出力する
ans_multiply_result = converter.multiply(a_num,b_num)
print(ans_multiply_result)

ans_half_a_result = converter.half_a(a_num)
print(ans_half_a_result)

#Geometry クラスを定義してください。
class Geometry:
    #メソッド①　get_area()：length * width の結果を result に入れて、それを返す。
    def get_rectangle_area(self,length,width):
        get_area_ans = length * width
        return get_area_ans
    
    #メソッド②　get_perimeter_sum()：length + width の結果を result に入れて、それを返す。
    def get_perimeter_sum(self,length,width):
        get_sum_ans = length + width
        return get_sum_ans
    
#インスタンスを作成
geometry = Geometry()
#数を代入
length = 8
width = 6 

#メソッドを呼び出す
get_area_ans_result = geometry.get_rectangle_area(length,width)
print(get_area_ans_result)

get_sum_ans_result = geometry.get_perimeter_sum(length,width)
print(get_sum_ans_result)


#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#復習

class TextFormatter:
    #メソッド① 小文字にする
    def to_lower(self,text):
        to_lower_text = text.lower()
        return to_lower_text
    
    #メソッド② スペースで区切って、単語のリストにして返す
    def split_text(self,text):
        get_split_text = text.split()
        return get_split_text
    
#インスタンスを作成
text_formatter = TextFormatter()

#引数に単語を代入する
my_text = 'Python Programming'

#メソッドを呼び出して出力する
to_lower_text_result = text_formatter.to_lower(my_text)
print(to_lower_text_result)

get_split_text_result = text_formatter.split_text(my_text)
print(get_split_text_result)


#クラスを作る
class TextEditor:
    #メソッド①大文字にする
    def to_upper(self,text):
        to_upper_text = text.upper()
        return to_upper_text
    
    #メソッド②逆から①文字ずつ
    def reverse_text(self,text):
        get_reverse_text = text[::-1]
        return get_reverse_text
    
#インスタンスを作成
text_editor_instance = TextEditor()

#文字を引数に代入
original_text = "happy birthday"

#メソッドを呼び出して出力する
to_upper_text_result = text_editor_instance.to_upper(original_text)
print(to_upper_text_result)

get_reverse_text_result = text_editor_instance.reverse_text(original_text) 
print(get_reverse_text_result)


#【問題文】
#【要件】Calculator クラスを定義してください。・クラスには次の2つのメソッドを定義してください（どちらも3行構成）：
#1.add（）：x＋yの結果を変数 resultに入れて、それを返す
#2.double_x（：x*2の結果を変数 resultに入れて、それを返す
#・クラスの外でメ=3、y=5を定義し、各メソッドの結果を print（）で表示してください。※キーワード引数を使って定義してください。・init （コンストラクタ）に関しては利用なし (pass)

class Calculator:
    #メソッド①第一引数はself
    def add(self,x_num,y_num):
        add_answer = x_num + y_num
        return add_answer
    
    #メソッド② 第一引数はself キーワード引数を同じにする
    def double_x(self,x_num):
        double_x_answer = x_num * 2
        return double_x_answer
    
#インスタンスを作成
calculator_instance = Calculator()
#数字を引数へ代入
x_num = 3
y_num = 5

#メソッドを呼び出して出力する
add_answer_result = calculator_instance.add(x_num,y_num)
print(add_answer_result) 

double_x_answer_result = calculator_instance.double_x(x_num)
print(double_x_answer_result)

#TextEditor クラスを作ってください。下記の内容を反映させた次の2つのメソッドを定義してインスタンスを作成し、それぞれのメソッドを呼び出して結果を出力してください。
#・to_upper(text)：文字列 text を大文字に変換して返すメソッド
#・reverse_text(text)：文字列 text を逆順にして返すメソッド

#クラスを作成する
class TextEditor:
    #メソッド①
    def to_upper(self,text):
        #大文字にするよ
        upper_text = text.upper()
        return upper_text
    
    #メソッド②
    def reverse_text(self,text):
        get_reverse_text = text[::-1]
        return get_reverse_text
    
#インスタンスを作成
text_editor_instance = TextEditor()
#textへ代入
text = "happy_birthday"

#メソッドを呼び出して出力
upper_text_result = text_editor_instance.to_upper(text)
print(upper_text_result)

get_reverse_text_result = text_editor_instance.reverse_text(text)
print(get_reverse_text_result)

#------------------------------------------------------------------------
#【課題】Product クラスを作ってください。
#・コンストラクタ（__init__）で name（商品名）と stock（在庫数）を受け取り、インスタンス変数に保存する
#・add_stock(amount) メソッドで在庫を amount 増やす
#・show_stock() メソッドで 「〇〇の在庫は△△個です」と表示する　インスタンスを作成し、在庫を追加して表示してください。

class Product:
    #コンストラクタはインスタンスを作成したと同時に呼び出される場所！通常のメソッドは呼び出さないと出てこないやつ！
    def __init__(self,name,stock):
        #ただの商品名をお店の実際の商品名で呼び出しているみたいな？
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

product_instance.show_stock()

#在庫を追加
product_instance.add_stock(10)

# 在庫を追加した後の在庫を表示
product_instance.show_stock()