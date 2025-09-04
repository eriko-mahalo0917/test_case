#問題①
def say_hello():
    print('こんにちは！')
say_hello()

#問題②
#関数のmultiply_numberに引数a,b
def multiply_numbers(a,b):
#answerをa✕ｂの変数に定義する　変数の箱！
    answer = a * b
#returnで戻り値
    return  answer
#は変数で箱！他の名前にしてもいい　自分で決めてOK
get_answer = multiply_numbers(3, 5)
print(get_answer)


#練習用「ありがとう！」と表示する関数 say_thanks を定義し、それを呼び出す
def say_thanks():
    print("ありがとう！")
say_thanks()

#練習用「お疲れ様です！」と表示する関数 say_good_job を定義し、それを呼び出す
def say_good_job():
    print('お疲れ様です！')
say_good_job()

#練習用「またね！」と表示する関数 say_bye を定義し、それを呼び出す
def say_bye():
    print('またね！')
say_bye()

#練習用「プログラミングは楽しい！」と表示する関数 say_fun を定義し、それを呼び出す
def say_fun():
    print('プログラミングは楽しい！')
say_fun()

#練習用「頑張ろう！」と表示する関数 fight を定義し、それを呼び出す
def fight():
    print('頑張ろう!')
fight()

#ちょっとだけ上より応用編　引数を使った関数を定義・呼び出す問題
#練習用　引数として名前を受け取り、「こんにちは、____さん！」と表示する関数 say_hello_name を定義し、引数にあなたの名前を渡して呼び出してください。
def say_hello_name(name):
    print('こんにちは、' + name + 'さん')
say_hello_name('えりんこ')

#練習用　引数として1つの数字を受け取り、その数字を2倍にして表示する関数 double_number を定義し、好きな数字を渡して呼び出してください。
def double_number(a):
    print(a*2)
double_number(5)

#練習用　引数として1つの単語を受け取り、「あなたの好きな単語は____です」と表示する関数 like_word を定義し、好きな単語を渡して呼び出してください。
def like_word(word='ケセラセラ'):
    print('あなたの好きな単語は' + word + 'です')
like_word('happy')
like_word()

#練習用　引数として2つの数字を受け取り、それらの合計を表示する関数 show_sum を定義し、好きな2つの数字を渡して呼び出してください。
def show_sum(a,b):
    print(a+b)
show_sum(3,9)

#引数として1つの数字を受け取り、その数字が偶数か奇数かを判断し、
# 「____は偶数です」または「____は奇数です」と表示する関数 check_even_odd を定義し、好きな数字を渡して呼び出してください。
def check_even_odd(number):
    if number % 2 == 0:
        print(str(number) + 'は偶数です')
    else:
        print(str(number) + 'は奇数です')
check_even_odd(5)

#練習用「ようこそ！」と表示する関数 say_welcome を定義し、それを呼び出してください。
def say_welcome():
    print('ようこそ！')
say_welcome()

#練習用「さようなら。」と表示する関数 say_goodbye を定義し、それを呼び出してください。
def say_goodbye():
    print('さようなら。')
say_goodbye()

#練習用　引数として名前を受け取り、その名前を使って「こんにちは、〇〇さん！」と表示する関数 say_hello_to を定義し、好きな名前を渡して呼び出してください。
def say_hello_to(name):
    print('こんにちは、' + name + 'さん！')
say_hello_to('えりんこ')

#練習用　引数として2つの数値を受け取り、その合計を返す関数 add_numbers を定義し、その結果を変数に代入して表示してください。
def add_numbers(a,b):
    answer = (a + b)
    return answer
result = add_numbers(4,5)
print(result)

#練習用　字列の結合2つの文字列 "Hello, " と "World!" を引数として受け取り、それらを結合した新しい文字列を返す関数 combine_strings を定義し、その結果を変数に代入して表示してください。
def combine_strings(text1,text2):
    sum_word = (text1 + text2)
    return sum_word
result = combine_strings('Hello,','World!')
print(result)

#練習用　2つの文字列 "Python " と "is awesome!" を引数として受け取り、それらを連結した新しい文字列を返す関数 join_words を定義し、その結果を変数に代入して表示してください。
def join_words(word1,word2):
    two_words = (word1 + word2)
    return two_words
result = join_words('Python','is awesome!')
print(result)

#練習用　2つの日本語の文字列、"こんにちは、" と "皆さん！" を引数として受け取り、それらを連結した新しい文字列を返す関数 double_words を定義し、その結果を変数に代入して表示してください。
def double_words(text1,text2):
    words = (text1 + text2)
    return words
result = double_words('こんにちは、','皆さん！')
print(result)

#練習用　２つの日本語の文字列、"今日も" と "一日お疲れ様！" を引数として受け取り、それらを連結した新しい文字列を返す関数 add_text を定義し、その結果を変数に代入して表示してください。
def add_text(text1,text2):
    double_texts = (text1 + text2)
    return double_texts
result = add_text('今日も','一日お疲れ様！')
print(result)

#練習用　2つの数値を引数として受け取り、その合計を返す関数 add_numbers を定義し、その結果を変数に代入して表示してください。
def add_numbers(a,b):
    answer = (a + b)
    return answer
result = add_numbers(5,120)
print(result)

#練習用　2つの数値を引数として受け取り、1つ目の数値から2つ目の数値を引いた差を返す関数 subtract_numbers を定義し、その結果を変数に代入して表示してください。
def subtract_numbers(c,d):
    answer = (c - d)
    return answer
result = subtract_numbers(10,5)
print(result)

#練習用　2つの数値を引数として受け取り、その積を返す関数 multiply_numbers を定義し、その結果を変数に代入して表示してください。
def multiply_numbers(e,f):
    answer = (e * f)
    return answer
result = multiply_numbers(3,9)
print(result)

#練習用　2つの数値を引数として受け取り、1つ目の数値を2つ目の数値で割った商を返す関数 divide_numbers を定義し、その結果を変数に代入して表示してください。
def divide_number(a,b):
    answer = (a / b)
    return answer
result = divide_number(9,3)
print(result)

#練習用　名前と年齢を引数として受け取り、「私は〇〇です。〇〇歳です。」という自己紹介メッセージを返す関数 introduce_yourself を定義し、その結果を変数に代入して表示してください。
def introduce_yourself(name,age):
    massage = ('私は' + name + 'です。' + str(age) + '歳です。')
    return massage
result = introduce_yourself('えりんこ', 38)
print(result)

#練習用　名前と趣味を引数として受け取り、「私は〇〇です。趣味は〇〇です。」という自己紹介メッセージを返す関数 my_hobby を定義し、その結果を変数に代入して表示してください。
def my_hobby(name,hobby):
    message = ('私は' + name + 'です。' + '趣味は' + hobby + 'です。')
    return message
result = my_hobby('えりんこ','フラダンス')
print(result)

#練習用　好きな食べ物を引数として受け取り、「私の好きな食べ物は〇〇です。」というメッセージを返す関数 favorite_food を定義し、その結果を変数に代入して表示してください。
def favorite_food(food):
    message = ('私の好きな食べ物は'+ food + 'です。')
    return message
result = favorite_food('小籠包')
print(result)

#練習用「10+5=15」と表示する関数 print_sum を定義し、呼び出してください。
def print_sum():
    print('10+5=15')
print_sum()

#練習用「こんにちは、世界！」と表示する関数 say_hello を定義し、呼び出してください。
def say_hello():
    print('こんにちは、世界！')
say_hello()

#できなかった！練習用　引数として2つの数値をを受け取り、その合計を「〇+〇=〇」の形式で表示する関数 print_calculation を定義し、呼び出してください。
def print_calculation(a,b):
    add_answer = (a + b)
    print( str(a) + '+' + str(b) + '=' + str(add_answer) )
print_calculation(5,10)

#練習用　引数として2つの数値をを受け取り、その合計を返す関数 get_sum を定義し、その結果を変数に代入して表示してください。
def get_sum(a,b):
    answer = (a + b)
    return answer
result = get_sum(5,100)
print(result)

#練習用　引数として名前と年齢を受け取り、「私は〇〇です。〇〇歳です。」という自己紹介メッセージを返す関数 create_intro を定義し、その結果を変数に代入して表示してください。
def create_intro(name,age):
    intro_yourself = ('私は' + name + 'です。' + str(age) + '歳です。')
    return intro_yourself
result = create_intro('えりんこ',39)
print(result)

def create_intro(name,age):
    print('私は' + name + 'です。' + str(age) + '歳です。')
create_intro('えりんこ',39)

#練習用「プログラミングは楽しい！」と表示する関数 programming_fun を定義し、呼び出してください。
def programming_fun():
    print('プログラミングは楽しい！')
programming_fun()

#練習用　引数として好きな飲み物を受け取り、「今日の飲み物は〇〇です。」と表示する関数 todays_drink を定義し、呼び出してください。
def todays_drink(drink):
    print('今日の飲み物は' + drink + 'です。')
todays_drink('ブラックコーヒー')

#練習用　2つの数値を引数として受け取り、それらを足し算して結果を戻り値として返す関数 add_numbers を定義し、その結果を変数に代入して表示してください。
def add_numbers(a,b):
    sum_numbers = (a + b)
    return sum_numbers
result = add_numbers(10,50)
print(result)

#練習用　引数として2つの文字列を受け取り、それらを結合して「〇〇＋〇〇」の形式で表示する関数 join_strings を定義し、呼び出してください。
def join_strings(word1,word2):
    print(word1 + word2)
join_strings('今日は','晴れ')

#練習用　引数として好きな数値を受け取り、その数値を2乗して結果を戻り値として返す関数 square_number を定義し、その結果を変数に代入して表示してください。
def square_number(a):
    answer = ( a * a )
    return answer
result = square_number(4)
print(result)

#練習用　「晴れの日！」と表示する関数 sunny_day を定義し、呼び出してください。
def sunny_day():
    print('晴れの日！')
sunny_day()

#練習用　引数として好きな色を受け取り、「好きな色は〇〇です。」と表示する関数 favorite_color を定義し、呼び出してください。
def favorite_color(color):
    print('好きな色は' + color + 'です。')
favorite_color('イエロー')

#練習用　2つの数値を引数として受け取り、それらを割り算して結果を戻り値として返す関数 divide_numbers を定義し、その結果を変数に代入して表示してください。
def divide_number(a,b):
    answer = (a / b)
    return answer
result = divide_number(10,5)
print(result)

#練習用　引数として名前と年齢を受け取り、「〇〇は〇〇歳です。」というメッセージを文字列として戻り値で返す関数 profile を定義し、その結果を変数に代入して表示してください。
def profile(name,age):
    pro = ( name + 'は' + str(age) + '歳です。')
    return pro
result = profile('えりんこ',39)
print(result)

#練習用　引数として好きな色を受け取り、「好きな色は〇〇です。」と表示する関数 favorite_color を定義し、呼び出してください。
def favorite_color(color):
    print('好きな色は' + color + 'です。')
favorite_color('yellow')

#練習用　2つの数値を引数として受け取り、それらを割り算して結果を戻り値として返す関数 divide_numbers を定義し、その結果を変数に代入して表示してください。
def divide_numbers(a,b):
    answer = (a / b)
    return answer
result = divide_numbers(200,100)
print(result)

#練習用　2つの文字列を引数として受け取り、それらを結合して「〇〇＋〇〇」の形式で表示する関数 join_strings を定義し、呼び出してください。
def join_strings(text1,text2):
    words = text1 + '+' + text2
    return words
two_words = join_strings('高さ','横')
print(two_words)

#問題③
def greet_person(name,age):
    intro_yourself = ('私の名前は' + name + 'です。' + str(age) + '歳です。')
    return intro_yourself
result = greet_person('えりんこ',39)
print(result)

def greet_person(name,age):
    intro_yourself = f'私の名前は{name}です。{age}歳です。'
    return intro_yourself
result = greet_person('えりんこ',39)
print(result)

#練習用　引数として**city (都市名)とweather (天気)**を受け取り、「今日の〇〇の天気は〇〇です。」という形式の文字列を返す関数 report_weather を作成してください。
def report_weather(city,weather):
    message = f'今日の{city}天気は{weather}です。'
    return message
result = report_weather('ハワイ','晴れ')
print(result)

#練習用 引数として**product (商品名)とprice (価格)**を受け取り、「〇〇の価格は〇〇円です。」という形式の文字列を返す関数 get_price を作成してください。
def get_price(product,price):
    message = f'{product}の価格は{price}円です。'
    return message
result = get_price('ロコモコ',10000)
print(result)

#練習用　引数として**base (底辺)とheight (高さ)**を受け取り、三角形の面積を計算し、「底辺〇〇、高さ〇〇の三角形の面積は〇〇です。」という形式の文字列を返す関数 calculate_area を作成してください。
def calculate_area(base,height):
    message = f'底辺{base}、高さ{height}の三角形の面積は{base * height / 2}です。'
    return message
result = calculate_area(50,50)
print(result)

#練習用　引数として**year (年)とmonth (月)**を受け取り、「〇〇年〇〇月のイベント情報」という形式の文字列を返す関数 get_event_info を作成してください。
def get_event_info(year,month):
    message = f'{year}年{month}月のイベント情報'
    return message
result = get_event_info(2025,10)
print(result)

#練習用　引数として**movie_title (映画タイトル)とdirector (監督名)**を受け取り、「映画『〇〇』の監督は〇〇です。」という形式の文字列を返す関数 get_movie_info を作成してください。
def get_movie_info(movie_title,director):
    message = f'映画『{movie_title}』の監督は{director}です。'
    return message
result = get_movie_info('50回目のファーストキス','福田雄一')
print(result)

#練習用　引数として**student_name (学生名)とgrade (成績)**を受け取り、「〇〇さんの成績は〇〇点でした。」という形式の文字列を返す関数 show_grade を作成してください。
def show_grade(student_name,grade):
    message = f'{student_name}さんの成績は{grade}点でした。'
    return message
result = show_grade('えりんこ',100)
print(result)

#練習用　引数として**book_title (本のタイトル)とauthor (著者名)**を受け取り、「『〇〇』の著者は〇〇です。」という形式の文字列を返す関数 get_book_details を作成してください。
def get_book_details(book_title,author):
    message = f'『{book_title}』の著者は{author}です。'
    return message
result = get_book_details('お金の大学','両学長')
print(result)

#練習用　引数として**color (色)とfruit (果物)**を受け取り、「〇〇色の果物は〇〇です。」という形式の文字列を返す関数 describe_fruit を作成してください。
def describe_fruit(color,fruit):
    message = f'{color}色の果物は{fruit}です。'
    return message
result = describe_fruit('黄','パイナップル')
print(result)

#練習用　引数として**food_name (料理名)とcuisine (ジャンル)**を受け取り、「〇〇は〇〇料理です。」という形式の文字列を返す関数 get_food_genre を作成してください。
def get_food_genre(food_name,cuisine):
    message = f'{food_name}は{cuisine}料理です。'
    return message
result = get_food_genre('ロコモコ','ハワイ')
print(result)

#練習用　引数として**start_time (開始時刻)とend_time (終了時刻)**を受け取り、「会議は〇〇時から〇〇時までです。」という形式の文字列を返す関数 get_meetingを作成してください。
def get_meeting(start_time,end_time):
    message = f'会議は{start_time}時から{end_time}時までです。'
    return message
result = get_meeting(9,12)
print(result)

#練習用　引数として好きな色を受け取り、「好きな色は〇〇です。」と表示する関数 favorite_color を定義し、呼び出してください。
def favorite_color(color):
    print(f'好きな色は{color}です。')
favorite_color('黄色')

#練習用　2つの数値を引数として受け取り、それらを割り算して結果を戻り値として返す関数 divide_numbers を定義し、その結果を変数に代入して表示してください。
def divide_numbers(a,b):
    get_answer = a / b
    return get_answer
result = divide_number(25,5)
print(result)

#練習用　2つの文字列を引数として受け取り、それらを結合して「〇〇＋〇〇」の形式で表示する関数 join_strings を定義し、呼び出してください。
def join_strings(text1,text2):
    message = f'{text1}+{text2}'
    return message
result = join_strings('青','黄')
print(result)

#練習用　引数として名前を受け取り、「こんにちは、〇〇さん！」という挨拶メッセージをf-stringを使って返す関数 greet_hello を定義し、その結果を変数に代入して表示してください。
def greet_hello(name):
    message = f'こんにちは、{name}さん！'
    return message
result = greet_hello('えりんこ')
print(result)

#練習用　引数として2つの数値をを受け取り、その合計をf-stringを使って「〇＋〇＝〇」の形式で表示する関数 print_sumを定義し、呼び出してください。
def print_sum(a,b):
    sum_number = f'{a}+{b}={a+b}'
    return sum_number
result = print_sum(5,9)
print(result)

#【問題】names = ["たろう", "はなこ", "じろう"]
names = ["たろう", "はなこ", "じろう"]
def add_names(new_names):
    names.extend(new_names)
add_names(["さぶろう", "しろう", "ごろう"])
print(names)

#【問題】names = ["たろう", "はなこ", "じろう"]
names = ["たろう", "はなこ", "じろう"]
def add_names(new_names):
    names.extend(new_names)
add_names(["さぶろう", "しろう", "ごろう"])
print(names)

#次のリストがあります。colors = ["赤", "青", "緑"]練習問題 複数の色をまとめて受け取り、すべてリストに追加する関数 add_colors(new_colors) を作ってください。
#関数を使って ["黄", "白", "黒"] を追加し、リストの中身をすべて表示してください。
colors = ["赤", "青", "緑"]
def add_colors(new_color):
    colors.extend(new_color)
add_colors(["黄","白","黒"])
print(colors)

#のリストがあります。numbers = [1, 2, 3] 複数の数値をまとめて受け取り、すべてリストに追加する関数 add_numbers(new_numbers) を作ってください。
#関数を使って (4, 5, 6) を追加し、リストの中身をすべて表示してください。
numbers = [1,2,3]
def add_numbers(new_numbers):
    numbers.extend(new_numbers)
#リストに追加する！だから[]を忘れない！
add_numbers([4,5,6])
print(numbers)

#次のリストがあります。fruits = ["りんご", "みかん", "バナナ"]
#複数の果物をまとめて受け取り、すべてリストに追加する関数 add_fruits(new_fruits) を作ってください。関数を使って ("ぶどう", "いちご", "メロン") を追加し、リストの中身をすべて表示してください。
fruits = ["りんご","みかん","バナナ"]
def add_fruits(new_fruits):
    fruits.extend(new_fruits)
add_fruits(["ぶどう", "いちご", "メロン"])
print(fruits)

#次のリストがあります。animals = ["犬", "猫", "うさぎ"]
#複数の動物をまとめて受け取り、すべてリストに追加する関数 add_animals(new_animals) を作ってください。関数を使って "パンダ" と "コアラ" を追加し、リストの中身をすべて表示してください。
animals = ["犬","猫","うさぎ"]
def add_animals(new_animals):
    animals.extend(new_animals)
add_animals(["パンダ","コアラ"])
print(animals)

#次のリストがあります。names = ["たろう", "はなこ"]
#新しい名前 "じろう" をリストの末尾に追加する関数 add_name(new_name) を作ってください。関数を使って名前を追加し、リストの中身をすべて表示してください。
names = ["たろう","はなこ"]
def add_name(new_name):
    names.extend(new_name)
add_name(["じろう"])
print(names)

#次のリストがあります。items = ["本", "ペン", "ノート"]新しいアイテム "消しゴム" をリストの末尾に追加する関数 add_item(new_item) を作ってください。
#関数を使ってアイテムを追加し、リストの中身をすべて表示してください。
items = ["本","ペン","ノート"]
def add_items(new_item):
    items.extend(new_item)
add_items(["消しゴム"])
print(items)

#次のリストがあります。numbers = [10, 20, 30]新しい数値 40 をリストの末尾に追加する関数 add_number(new_number) を作ってください。
#関数を使って数値を追加し、リストの中身をすべて表示してください。
items = [10,20,30]
def add_number(new_number):
    items.extend(new_number)
add_number([40])
print(items)

#次のリストがあります。names = ["たろう", "はなこ"]
#3つのリスト["じろう"]、["さぶろう"]、["ごろう"]をそれぞれ順番にリストnamesに追加する関数 add_namesを作ってください。関数を使って名前を追加し、リストの中身をすべて表示してください。
names = ["たろう", "はなこ"]
def add_names(new_names):
    names.extend(new_names)
add_names(["じろう","さぶろう","ごろう"])
print(names)

#次のリストがあります。data = ["A", "B"]3つのリスト["C"]、["D"]、["E"]をそれぞれ順番にリストdataに追加する関数 add_dataを作ってください。
#関数を使ってデータを追加し、リストの中身をすべて表示してください。
data = ["A","B"]
def add_data(new_data):
    data.extend(new_data)
add_data(["C","D","E"])
print(data)

items = ["本", "ペン", "ノート"]
def add_item(new_item):
    items.extend(new_item)
add_item(["消しゴム","えんぴつ"])
print(items)

#引数として好きな色を受け取り、「好きな色は〇〇です。」と表示する関数 favorite_color を定義し、呼び出してください。
def favorite_color(color):
    print(f'好きな色は{color}です。')
favorite_color("黄色")

#2つの数値を引数として受け取り、それらを割り算して結果を戻り値として返す関数 divide_numbers を定義し、その結果を変数に代入して表示してください。
def divide_numbers(a,b):
    answer = a / b
    return answer
result = divide_numbers(150,600)
print(result)

#names = ["たろう", "はなこ", "じろう"]　複数の名前をまとめて受け取り、すべてリストに追加する関数 add_names(new_names) を作ってください。
#関数を使って ["さぶろう", "しろう", "ごろう"] を追加し、リストの中身をすべて表示してください。
name = ["たろう", "はなこ", "じろう"]
def add_name(new_names):
    name.append(new_names)
add_name(["さぶろう", "しろう", "ごろう"])
print(name)

#次のリストがあります。colors = ["赤", "青", "緑"]
#複数の色をまとめて受け取り、すべてリストに追加する関数 add_colors(new_colors) を作ってください。関数を使って ["黄", "白", "黒"] を追加し、リストの中身をすべて表示してください。
color = ["赤", "青", "緑"]
def add_colors(new_colors):
    color.append(new_colors)
add_colors(["黄", "白", "黒"])
print(color)

#2つの数値を引数として受け取り、それらを掛け算して結果を戻り値として返す関数 multiply_numbers を作ってください。その関数を呼び出して、戻り値をターミナルに出力してください。
def multiply_numbers(a,b):
    answer = a * b
    return answer
result = multiply_numbers(7,9)
print(result)

#「こんにちは！」と表示する関数 say_hello を定義し、それを呼び出してください。
def say_hello():
    print("こんにちは！")
say_hello()

#引数として2つの数値をを受け取り、その合計を f-string を使って「〇＋〇＝〇」の形式で表示する関数 print_sum を定義し、呼び出してください。
def print_sum (a,b):
    print(f'{a}+{b}={a+b}')
print_sum(5,5)

#新しい動物 "パンダ" をリストの末尾に追加する関数 add_animal(new_animal) を作ってください。関数を使って名前を追加し、リストの中身をすべて表示してください。
animals = ["犬", "猫", "うさぎ"]
def add_animal(new_animal):
    animals.append(new_animal)
add_animal(["パンダ"])
print(animals)

#新しいデータ "テスト" をリストの末尾に追加する関数 add_data(new_data) を作ってください。関数を使ってデータを追加し、リストの中身をすべて表示してください。
data = [10, 20, 30]
def add_data(new_data):
    data.append(new_data)
add_data("テスト")
print(data)

#①「ようこそ、プログラミングの世界へ！」と表示する関数 say_welcome を定義し、それを呼び出してください。
def say_welcome():
    print("ようこそ、プログラミングの世界へ！")
say_welcome()

#②「またのご利用をお待ちしております。」と表示する関数 say_farewell を定義し、それを呼び出してください。
def say_farewell():
    print("またのご利用をお待ちしております。")
say_farewell()

#③2つの数字を引数として受け取り、それらを足し算して結果を戻り値として返す関数 add_numbers を作ってください。この関数を呼び出して、戻り値を出力。ただし、関数の呼び出し例では 100 と 200 を使ってください。
def add_numbers(a,b):
    answer = a + b
    return answer
result = add_numbers(100,200)
print(result)

#2つの数字を引数として受け取り、それらを割り算して結果を戻り値として返す関数 divide_numbers を作ってください。この関数を呼び出して、戻り値をターミナルに出力.ただし、関数の呼び出し例では 50 と 5 を使ってください。
def divide_numbers(a,b):
    answer = a / b
    return answer
result = divide_numbers(50,5)
print(result)

#2つの引数 item（商品名）と price（価格）を受け取り、f文字列を使って「〇〇の価格は△△円です。」のような文を作る関数 create_item_message を作成してください。呼び出し例では "ノート" と 300 を使ってください。
def reate_item_messa(item,price):
    message = f'{item}の価格は{price}円です。'
    return message
result = reate_item_messa("ノート",300)
print(result)

#2つの引数 month（月）と event（イベント名）を受け取り、f文字列を使って「△月は〇〇の季節です。」のような文を作る関数 season_message を作成してください。関数を呼び出し. 呼び出し例では 8 と "花火" を使ってください。
def season_message(month,event):
    message = f'{month}月は{event}の季節です。'
    return message
result = season_message(8,"花火")
print(result)

fruits = ["りんご", "バナナ", "ぶどう"]
def add_fruits(new_fruits):
    fruits.append(new_fruits)
add_fruits(["いちご", "みかん"])
print(fruits)

numbers = [1, 2, 3, 4]
def remove_numbers(numbers_to_remove):
    numbers.append(numbers_to_remove)
remove_numbers([5, 6])
print(numbers)

#課題
names = ["たろう", "はなこ", "じろう"]
def add_names(new_names):
    for name in new_names:
        names.append(name)

add_names(["さぶろう", "しろう", "ごろう"])
for name in names:
    print(name)

#課題
names = ["たろう", "はなこ", "じろう"]
def add_names(new_names):
    for name in new_names:
        names.append(name)

add_names(["さぶろう", "しろう", "ごろう"])
for name in names:
    print(name)

#課題
names = ["たろう", "はなこ", "じろう"]
def add_names(new_names):
    for name in new_names:
        names.append(name)
    
add_names(["さぶろう", "しろう", "ごろう"])
for name in names:
    print(name)

#課題
members = ["山田", "佐藤", "鈴木"]
def add_member(new_member):
    for member in new_member:
        members.append(member)

add_member(["田中","高橋"])
for member in members:
    print(member)
    
fruits = ["りんご", "バナナ", "みかん"]
def add_fruit(new_fruits):
    for fruit in new_fruits:
        fruits.append(fruit)

add_fruit(["いちご", "ぶどう"])
for fruit in fruits:
    print(fruit)
    
planets = ["水星", "金星", "地球", "火星"]
def add_planets(new_planets):
    for planet in new_planets:
        planets.append(planet)

add_planets(["木星", "土星", "天王星"])
for planet in planets:
    print(planet)
    
foods = ["おにぎり", "パン", "サラダ"]
def add_food(new_food):
    for food in new_food:
        foods.append(food)
        
add_food(["カレー","ラーメン"])
for food in foods:
    print(food)


animals = ["犬", "猫", "鳥"]
def add_animal(new_animal):
    for animal in new_animal:
        animals.append(animal)

add_animal(["ペンギン","パンダ"])
for animal in animals:
    print(animal)
    
#次のリストのすべての数を2倍にして、新しいリストとして返す関数 double_list(numbers) を作成してください。
numbers = [1, 3, 5, 7]
def double_list(numbers):
#新しいリストを準備
    double_number = []
    for number in numbers:
        double_number.append(number * 2)
#このままでは処理結果を受け取れないからreturn
    return double_number

result = double_list(numbers)
print(result)


numbers = [1, 3, 5, 7]
def double_number(number):
    #新しいリストを準備
    double_number_list = []
    for number in numbers:
        double_number = number * 2
        double_number_list.append(double_number)
    return double_number_list


result = double_number(numbers)
print(result)

#次のリストのすべての要素を3倍にして、新しいリストとして返す関数 triple_list(numbers) を作成してください。
numbers = [2, 4, 6, 8]
def triple_list(numbers):
    triple_number_list = []
    for number in numbers:
        triple_number = number * 3
        triple_number_list.append(triple_number)
    return triple_number_list


result = triple_list(numbers)
print(result)

#次のリストのすべての要素から10を引いて、新しいリストとして返す関数 subtract_ten(numbers) を作成してください。
numbers = [15, 20, 25, 30]
def subtract_ten(numbers):
    subtract_numbers_list = []
    for number in numbers:
        subtract_numbers = number - 10
        subtract_numbers_list.append(subtract_numbers)
    return subtract_numbers_list


result = subtract_ten(numbers)
print(result)

#次のリストのすべての文字列の最後に "さん" を追加して、新しいリストとして返す関数 add_honorific(names) を作成してください。
names = ["たなか", "さとう", "すずき"]
def add_honorific(names):
    honorific_name_list = []
    for name in names:
        honorific_name = name + "さん"
        honorific_name_list.append(honorific_name)
    return honorific_name_list

result = add_honorific(names)
print(result)

#のリストのすべての文字列の最後に "さん" を追加して、新しいリストとして返す関数 add_san(names) を作成してください。
names = ["たなか", "さとう", "すずき"]
def add_san(names):
    new_name_list = []
    for name in names:
        new_name = name + "さん"
        new_name_list.append(new_name)
    return new_name_list


result = add_san(names)
print(result)

#次のリストのすべての数値に100を足して、新しいリストとして返す関数 add_hundred(numbers) を作成してください。
numbers = [10, 20, 30]
def add_hundred(numbers):
    new_hundred_list = []
    for number in numbers:
        new_add_hundred = number + 100
        new_hundred_list.append(new_add_hundred)
    return new_hundred_list
    
result = add_hundred(numbers)
print(result) 

#次のリストのすべての数値を10倍にして、新しいリストとして返す関数 multiply_by_ten(numbers) を作成してください。
numbers = [1, 2, 3, 4, 5]
def multiply_by_ten(numbers):
    new_numbers_list = []
    for number in numbers:
        new_number = number * 10
        new_numbers_list.append(new_number)
    return new_numbers_list

result = multiply_by_ten(numbers)
print(result)

#次のリストのすべての数値から5を引いて、新しいリストとして返す関数 subtract_five(numbers) を作成してください。
numbers = [10, 15, 20, 25]
def subtract_five(numbers):
    new_minus_list = []
    for number in numbers:
        minus_number = number - 5
        new_minus_list.append(minus_number)
    return new_minus_list
        
        
result = subtract_five(numbers)
print(result)

#次のリストのすべての数値を2で割って、新しいリストとして返す関数 divide(nums) を作成してください。
nums = [2, 4, 6, 8, 10]
def divide(nums):
    new_divide_list = []
    for num in nums:
        num_answer = num / 2
        new_divide_list.append(num_answer)
    return new_divide_list


result = divide(nums)
print(result)

#次のリストのすべての数値から100を引いて、新しいリストとして返す関数 minus(numbers) を作成してください。
numbers = [110, 120, 130, 140]
def minus(numbers):
    new_minus_list = []
    for number in numbers:
        minus_number = number - 100
        new_minus_list.append(minus_number)
    return new_minus_list


result = minus(numbers)
print(result)

#次のリストのすべての数値を3倍にして、新しいリストとして返す関数 triple(numbers) を作成してください。
numbers = [1, 5, 10, 15]
def triple(numbers):
    new_triple_list = []
    for number in numbers:
        new_triple_ans = number * 3
        new_triple_list.append(new_triple_ans)
    return new_triple_list


result = triple(numbers)
print(result)

#次のリストのすべての数値に20を足して、新しいリストとして返す関数 add_twenty(numbers) を作成してください。
numbers = [5, 10, 15, 20]
def add_twenty(numbers):
    new_twenty_list = []
    for number in numbers:
        add_twenty_ans = number + 20
        new_twenty_list.append(add_twenty_ans)
    return new_twenty_list


result = add_twenty(numbers)
print(result)

#次のリストに、新しい動物の名前をまとめて追加する関数 add_animals(new_animals) を作成してください。
animals = ["犬", "猫"]
def add_animals(new_animals):
    for animal in new_animals:
        animals.append(animal)
    
add_animals(["パンダ", "キリン", "ライオン"])

for animal in animals:
    print(animal) 
    
#次のリストに、新しい車の名前をまとめて追加する関数 add_cars(new_cars) を作成してください。
cars = ["トヨタ", "ホンダ"]
def add_cars(new_cars):
    for car in new_cars:
        cars.append(car)
        
add_cars(["日産", "マツダ", "スバル"])

for car in cars:
    print(car)
    
cars = ["トヨタ", "ホンダ"]
def add_cars(new_cars):
    cars.append(new_cars)
    
add_cars(['日産', 'マツダ', 'スバル'])
print(cars)

#次のリストのすべての数値を3乗して、新しいリストとして返す関数 triple_power(numbers) を作成してください。
numbers = [2, 4, 6]
def triple_power(numbers):
    new_triple_list = []
    for number in numbers:
        triple_numbers = number * 3
        new_triple_list.append(triple_numbers)
    return new_triple_list


result = triple_power(numbers)
print(result)

#次のリストのすべての文字列の先頭に「Hello, 」を追加して、新しいリストとして返す関数 greet_list(names) を作成してください。
names = ["Alice", "Bob", "Charlie"]
def greet_list(names):
    new_greet_list = []
    for name in names:
        greet_word = "hello," + name
        new_greet_list.append(greet_word)
    return new_greet_list


result = greet_list(names)
print(result)


names = ["たろう", "はなこ", "じろう"]
def add_names_at_start(new_names):
    for name in new_names:
        names.append(name)
        
add_names_at_start(["さぶろう", "しろう", "ごろう"])
print(names)


numbers = [10, 20, 30]
def add_numbers(new_numbers):
    #新しいリストを繰り返してもとのリストに追加
    for number in new_numbers:
        numbers.append(number)

#追加されるリスト
add_numbers([40, 50, 60])
print(numbers)

#総復習　「ありがとう！」と表示する関数 say_thank_you を作り、それを呼び出してください。
def say_thank_you():
    print("ありがとう")


say_thank_you()


#「がんばって！」と表示する関数 say_good_luck を作り、それを呼び出してください。
def say_good_luck():
    print("がんばって！")
    
    
say_good_luck()

#2つの数字を引数として受け取り、それらを足し算して結果を戻り値として返す関数を作りましょう。
def add_numbers(x,y):
    answer = x + y
    return answer

result = add_numbers(10,20)
print(result)

#2つの数字を引数として受け取り、それらを割り算して結果を戻り値として返す関数を作りましょう。
def divide_numbers(num1,num2):
    answer = num1 / num2
    return answer

result = divide_numbers(40,8)
print(result)

#2つの引数 item（商品名）と price（価格）を受け取り、f文字列（f-string）を使って「〇〇の価格は〇〇円です。」というあいさつ文を作る関数を作成してください。
def display_price(item,price):
    message = f'{item}の価格は{price}円です。'
    return message

result = display_price('リンゴ',150)
print(result)

#2つの引数 city（都市名）と weather（天気）を受け取り、f文字列（f-string）を使って「〇〇の今日の天気は〇〇です。」というあいさつ文を作る関数を作成してください。
def display_weather(city,weather):
    message = f'{city}の今日の天気は{weather}です。'
    return message
    
result = display_weather("東京","晴れ")
print(result)

#与えられたリスト numbers に、複数の数字をまとめて追加する関数 add_numbers を作ってください。関数を使って [10, 20, 30] を追加し、リストの中身をすべて表示してください。
numbers = [1, 2, 3]
def add_numbers(new_number):
    for number in new_number:
        numbers.append(number)
        
add_numbers([10, 20, 30])
print(numbers)

#与えられたリスト fruits に、複数の果物の名前をまとめて追加する関数 add_fruits を作ってください。関数を使って ["バナナ", "ぶどう"] を追加し、リストの中身をすべて表示してください。
fruits = ["りんご", "みかん"]
def add_fruits(new_fruits):
    for fruit in new_fruits:
        fruits.append(fruit)
        
add_fruits( ["バナナ", "ぶどう"])
print(fruits)

#次のリストのすべての文字列の最後に「！」を加えて、新しいリストとして返す関数 add_exclamation を作成してください。
words = ["こんにちは", "ありがとう", "さようなら"]
def add_exclamation(new_message):
    new_message_list = []
    for word in words:
        new_message_word = word + "!"
        new_message_list.append(new_message_word)
    return new_message_list
    
result = add_exclamation(words)
print(result)

#次のリストのすべての数を半分にして、新しいリストとして返す関数 half_list を作成してください。
# 元のリスト
numbers = [10, 20, 30, 40]
def half_list(list_numbers):
    #新しいリストだから新しい名前
    new_half_list = []
    #ここでは元のリストを使うから最初のリストを指定
    for number in numbers:
        get_half_number = number / 2
        #ここで新しいリストに半分に割った数を追加するよ
        new_half_list.append(get_half_number)
    #出た値を受け取る
    return new_half_list

result = half_list(numbers)
print(result)

#「ありがとう！」と表示する関数 say_thanks を定義し、それを呼び出してください。
def say_thanks():
    print("ありがとう！")

say_thanks()


#「さようなら。」と表示する関数 say_goodbye を定義し、それを呼び出してください。
def say_goodbye():
    print("さようなら。")
    
say_goodbye()

#2つの数字を引数として受け取り、それらを足し算して結果を戻り値として返す関数 add_numbers を作りましょう。
#その関数を呼び出して、戻り値をターミナルに出力してください。呼び出すときは、10 と 20 を使ってください。
def add_numbers(a,b):
    add_answer = a + b
    return add_answer

add_answer_result = add_numbers(10,20)
print(add_answer_result)

#3つの数字を引数として受け取り、それらを掛け算して結果を戻り値として返す関数 multiply_three_numbers を作りましょう。
#その関数を呼び出して、戻り値をターミナルに出力してください。呼び出すときは、2 と 3 と 4 を使ってください。
def multiply_three_number(a,b,c):
    get_answer = a * b * c
    return get_answer

get_answer_result = multiply_three_number(2,3,4)
print(get_answer_result)

#2つの引数 item（商品名）と price（価格）を受け取り、f文字列を使って「{item} の価格は {price} 円です。」という文を作る関数 display_price を作成してください。
def display_price(item,price):
    price_comment = f'{item}の価格は{price}円です。'
    return price_comment

price_comment_result = display_price("りんご",150)
print(price_comment_result)

#2つの引数 city（都市名）と temperature（気温）を受け取り、f文字列を使って「今日の {city} の気温は {temperature} 度です。」という文を作る関数 report_weather を作成してください。
def report_weather(city,temperature):
    weather_message = f'今日の{city}の気温は{temperature}度です。'
    return weather_message
    
weather_message_result = report_weather("東京",25)
print(weather_message_result)

#数字のリスト numbers = [1, 2, 3] があります。複数の数字をまとめて受け取り、すべてリストに追加する関数 add_numbers(new_numbers) を作ってください。
#関数を使って [4, 5, 6] を追加し、リストの中身をすべて表示してください。
numbers = [1,2,3]
def add_numbers(new_number):
    for number in new_number:
        numbers.append(number)

add_numbers([4, 5, 6])
for number in numbers:
    print(number)
    
    
numbers = [1,2,3]
def add_numbers(new_number):
    for number in new_number:
        numbers.append(number)
    return numbers

result = add_numbers([4, 5, 6])
print(result)

#色のリスト colors = ["赤", "青"] があります。複数の色をまとめて受け取り、すべてリストに追加する関数 add_colors(new_colors) を作ってください。
#関数を使って ["黄色", "緑"] を追加し、リストの中身をすべて表示してください。
colors =  ["赤", "青"]
def add_colors(new_colors):
    for color in new_colors:
        colors.append(color)
        
add_colors(["黄色", "緑"] )
for color in colors:
    print(color)
    
#このリストに新しい果物 ["orange", "grape"] を追加する関数 add_fruits を作ってください。
# ただし、add_fruits 関数は新しいリストを返り値として返すようにしてください。元のリストは変更しないようにしましょう。
fruits = ["apple", "banana"]
def add_fruits(new_fruits):
    for fruit in new_fruits:
        fruits.append(fruit)
    

add_fruits(["orange", "grape"])
for fruit in fruits:
    print(fruit)
    
    
friends = ["けん", "みか", "ゆうき"]
def add_new_friends(new_friend):
    for friend in new_friend:
        friends.append(friend)
        
add_new_friends(["あかり", "りょうた"])

for friend in friends:
    print(friend)
    
    
#消費税を計算するために、**すべての商品の値段を1.1倍（10%増し）**にして、新しいリストとして返す関数 add_tax(prices) を作ってください。
# そして、その関数を使って prices リストの新しい値段を計算し、結果を画面に表示してください。
prices = [100, 250, 80]
def add_tax(prices):
    new_prices_list = []
    for price in prices:
        tax_price = price * 1.1
        new_prices_list.append(tax_price)
    return new_prices_list

tax_price_result = add_tax(prices)
print(tax_price_result)

#テストの点数が70点より低かったら10点追加して、新しいリストとして返す関数 improve_scores(scores) を作ってください。70点以上の場合は、そのままの点数にしてください。
scores = [65, 80, 95]

def improve_scores(scores):
    new_scores_list = []
    for score in scores:
        if score < 70:
            new_score = score + 10
        else:
            new_score = score
        new_scores_list.append(new_score)
    return new_scores_list

improve_scores_result = improve_scores(scores)
print(improve_scores_result)


#複数の新しい動物の名前をまとめて受け取り、すべてリストに追加する関数 add_animals(new_animals) を作ってください。
animals = ["いぬ", "ねこ", "うさぎ"]
def add_animals(new_animals):
    for animal in new_animals:
        animals.append(animal)
            
add_animals(["きつね", "たぬき"] )
for animal in animals:
    print(animal)