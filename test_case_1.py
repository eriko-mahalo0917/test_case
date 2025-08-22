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