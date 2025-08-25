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