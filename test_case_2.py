#以下のリストを使って、すべての名前を1つずつ表示する print_names() 関数を作ってください。条件 1. forを使ってください。
names = ["たろう", "はなこ", "じろう"]
def print_names(names_list):
    for name in names:
        print(name)

print_names(names)


names = ["たろう", "はなこ", "じろう"]
def print_names(name):
    for name in names:
        print(name)
        
print_names(names)

names = ["john", "paul", "george"]
def print_names(name):
    for name in names:
        print(name)
        
        
print_names(names)


#空のリスト numbers を用意してください。for 文を使って 1 から 5 までの数字を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
numbers = []
def print_numbers_list(num):
    for number in numbers:
        numbers.append(number)

print_numbers_list([1,2,3,4,5])
print(numbers)

#からのリストを準備
numbers = []
#rangeで１〜５を表示する
for number in range(1,6):
    #for文で受け取った数字をnumbersのリストに追加する
    numbers.append(number)
    
#空のリストに追加される    
print(numbers)

def print_number_list(number_list):
    numbers = []
    for number in number_list:
        numbers.append(number)
    return numbers


result = print_number_list([1,2,3,4,5])
print(result)

numbers = []
def print_number_list(number_list):
    for number in number_list:
        numbers.append(number)
    return numbers


result = print_number_list([1,2,3,4,5])
print(result)


#空のリスト numbers を用意してください。for 文を使って 1 から 5 までの数字を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
def print_number_list(number_list):
    numbers = []
    for number in number_list:
        numbers.append(number)
    return numbers


result = print_number_list([1,2,3,4,5])
print(result)

#空のリスト fruits を用意してください。for 文を使って「りんご」「バナナ」「ぶどう」を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
def print_fruits_list(fruits_list):
    fruits = []
    for fruit in fruits_list:
        fruits.append(fruit)
    return fruits


result = print_fruits_list(["りんご","バナナ","ぶどう"])
print(result)


#空のリスト scores を用意してください。for 文を使って 10, 20, 30 を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
def print_scores_list(scores_list):
    scores = []
    for score in scores_list:
        scores.append(score)
    return scores

result = print_scores_list([10, 20, 30])
print(result)


#空のリスト even_numbers を用意してください。for文を使って2, 4, 6, 8, 10を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
def event_numbers_list(number_list):
    event_numbers = []
    for event_number in number_list:
        event_numbers.append(event_number)
    return event_numbers

result = event_numbers_list([2, 4, 6, 8, 10])
print(result)

#空のリスト vowel を用意してください。for文を使って「a」「i」「u」「e」「o」を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
def vowels_list(vowel_list):
    vowel = []
    for add_vowel in vowel_list:
        #ここをよく間違えるから気をつける！
        vowel.append(add_vowel)
    return vowel

result = vowels_list(["a","i","u","e","o"])
print(result)

#空のリスト odd_numbers を用意してください。for文を使って 1, 3, 5, 7, 9 を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
def odd_numbers_list(number_list):
    odd_numbers = []
    for odd_number in number_list:
        odd_numbers.append(odd_number)
    return odd_numbers

result = odd_numbers_list([1, 3, 5, 7, 9])
print(result)

#空空のリスト months を用意してください。for 文を使って「Jan」「Feb」「Mar」を順に取得し、1つずつリストに追加してください。最後にリストの中身を表示してください。
def print_months_list(month_list):
    months = []
    for month in month_list:
        months.append(month)
    return months


result = print_months_list(["Jan","Feb","Mar"])
print(result)

#空のリスト scores_multiplied を用意してください。for 文を使って 10, 20, 30 を順に取得し、それぞれ2倍にした数を1つずつリストに追加してください。最後にリストの中身を表示してください。
def scores_multiplied_list(multiplied_list):
    scores_multiplied = []
    for score in multiplied_list:
        add_score = score * 2
        scores_multiplied.append(add_score)
    return scores_multiplied
    
result = scores_multiplied_list([10, 20, 30])
print(result)

#空のリスト greeting_messages を用意してください。for文を使って ["Hello", "Hi", "Good morning"] を順に取得し、
#それぞれの文字列の最後に「, Python!」を加えて、1つずつリストに追加してください。最後にリストの中身を表示してください。
def messages_list(message_word_list):
    greeting_messages = []
    for message in message_word_list:
        add_message = message + ", Python!"
        greeting_messages.append(add_message)
    return greeting_messages


result = messages_list(["Hello", "Hi", "Good morning"])
print(result)


#年齢を引数として受け取り、18歳以上なら「大人です」、そうでなければ「未成年です」と表示する関数 check_age(age) を作ってください。
def check_age(age):
    if age >= 18:
        print("大人です")
    else:
        print("未成年です")
        
check_age(18)
check_age(16)



def check_age(age):
    if age >= 18:
        return "大人です"
    else:
        return "未成年です"
    
check_age_result = check_age(20)
print(result)

check_age_result = check_age(10)
print(result)


#点数を引数として受け取り、その点数が合格（60点以上）か不合格（60点未満）かを判断して表示する関数 check_score(score) を作ってください。
def check_score(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"
        
result = check_score(60)
print(result)

result = check_score(50)
print(result)

#数字を引数として受け取り、その数が偶数か奇数かを判断して表示する関数 check_even_or_odd(number) を作ってください。
def check_even_or_odd(number):
    if number % 2 == 0:
        return "偶数"
    else:
        return "奇数"
    
    
check_even_result = check_even_or_odd(6)
print(check_even_result)

check_odd_result = check_even_or_odd(5)
print(check_odd_result)


#文字列を引数として受け取り、その文字列が5文字以上か、5文字未満かを判断して表示する関数 check_spell(text) を作ってください。
def check_spell(text):
    if len(text) >= 5:
        return "5文字以上"
    else:
        return "5文字未満"
    
check_spell_result = check_spell("ミセスグリーンアップル")
print(check_spell_result)

check_spell_result = check_spell("時計")
print(check_spell_result)

#【問題文】点数を引数として受け取り、次の条件で判定する関数 judge_score(score) を作ってください。・80点以上 → 「優秀です」・60点以上80点未満 → 「合格です」・60点未満 → 「不合格です」
def judge_score(score):
    if score >= 80:
        return "優秀です"
    elif score >= 60:
        return "合格です"
    else:
        return "不合格です"
    
    
judge_score_result = judge_score(100)
print(judge_score_result)

judge_score_result = judge_score(79)
print(judge_score_result)

judge_score_result = judge_score(0)
print(judge_score_result)


#数字を引数として受け取り、その数が正の数、負の数、ゼロのどれかを判断して返す関数 check_number_type(number) を作ってください。
def check_number_type(number):
    if number > 0:
        return "正の数"
    elif number == 0:
        return "ゼロ"
    else:
        return "負の数"
    
check_number_type_result = check_number_type(1)
print(check_number_type_result)

check_number_type_result = check_number_type(0)
print(check_number_type_result)

check_number_type_result = check_number_type(-1)
print(check_number_type_result)


#社員の勤続年数を引数として受け取り、その年数に応じて**「新入社員」（3年未満）、「中堅社員」（3年以上10年未満）、
# 「ベテラン社員」**（10年以上）のどれかを判断して返す関数 check_staff_rank(years) を作ってください。

def check_staff_rank(years):
    if years < 3:
        return "新入社員"
    elif 3 <= years < 10:
        return "中堅社員"
    else:
        return "ベテラン社員"


check_staff_rank_result = check_staff_rank(2)
print(check_staff_rank_result)

check_staff_rank_result = check_staff_rank(5)
print(check_staff_rank_result)

check_staff_rank_result = check_staff_rank(10)
print(check_staff_rank_result)


def judge_score(score):
    excellent_comment = "優秀です"
    good_comment = "合格です"
    bad_comment = "不合格です"
    
    if score >= 80:
        return excellent_comment
    elif score >= 60:
        return good_comment
    else:
        return bad_comment
    
judge_score_result = judge_score(80)
print(judge_score_result)


#数字を引数として受け取り、その数が偶数、奇数、ゼロのどれかを判断して返す関数 check_number_type(number) を作ってください。
def check_number_type(number):
    even_number_comment = "偶数"
    odd_number_comment ="奇数"
    zero_number_comment = "ゼロ"
    
    if number == 0:
        return zero_number_comment
    elif number % 2 == 0:
        return odd_number_comment
    else:
        return even_number_comment
    
check_number_type_result = check_number_type(5)
print(check_number_type_result)

check_number_type_result = check_number_type(0)
print(check_number_type_result)


#時刻（hour）を引数として受け取り、その時刻が午前（6時から11時）、午後（12時から17時）、夜（18時から23時）、深夜（0時から5時）のどれかを判断して返す関数 get_time_of_day(hour) を作ってください。
def get_time_of_day(hour):
    am_time_comment = "午前"
    after_time_comment = "午後"
    night_time_comment = "夜"
    mid_night_comment = "深夜"
    
    if  6 <= hour <= 11:
        return am_time_comment
    elif 12 <= hour <= 17:
        return after_time_comment
    elif 18 <= hour <= 23:
        return night_time_comment
    else:
        return mid_night_comment
    
get_time_result = get_time_of_day(5)
print(get_time_result)


#数字を引数として受け取り、その数が3の倍数、5の倍数、どちらでもないのどれかを判断して返す関数 check_multiples(number) を作ってください。
def check_multiples(number):
    three_time_comment = "3の倍数"
    five_time_comment = "５の倍数"
    other_time_comment = "どちらでもない"
    
    if number % 3 == 0:
        return three_time_comment
    elif number % 5 == 0:
        return five_time_comment
    else:
        return other_time_comment
    
check_multiples_result = check_multiples(4)
print(check_multiples_result)

#購入金額を引数として受け取り、条件に応じて割引の有無を判定する関数 check_discount(price) を作ってください。
def check_discount(price):
    #10000円以上は20%off
    twenty_off_comment = "20%割引"
    #5000円以上は１0%off
    ten_off_comment = "10%割引"
    #それ以外は割引なし！
    proper_price_comment = "割引なし"
    
    if price >= 10000:
        #20％offの割引価格
        final_price = int(price * 0.8)
        #最終価格と割引の適用はどれかを表示
        return f'{final_price}円,{twenty_off_comment}'
    elif price >= 5000:
        #10％offの割引価格
        final_price = int(price * 0.9)
        return f'{final_price}円,{ten_off_comment}'
    else:
        return f'{price} 円,{proper_price_comment}'
    
check_discount_result = check_discount(10000)
print(check_discount_result)


def check_discount(price):
    #10000円以上は20%off
    twenty_off_comment = "20%割引"
    #5000円以上は１0%off
    ten_off_comment = "10%割引"
    #それ以外は割引なし！
    proper_price_comment = "割引なし"
    
    if price >= 10000:
        return twenty_off_comment
    elif price >= 5000:
        return ten_off_comment
    else:
        return proper_price_comment
    

check_discount_result = check_discount(10000)
print(check_discount_result)


#10000円以上は20%off
twenty_off_comment = "20%割引"
#5000円以上は１0%off
ten_off_comment = "10%割引"
#それ以外は割引なし！
proper_price_comment = "割引なし"

def check_discount(price):   
    if price >= 10000:
        #20％offの割引価格
        final_price = int(price * 0.8)
        #最終価格と割引の適用はどれかを表示
        return f'{final_price}円,{twenty_off_comment}'
    elif price >= 5000:
        #10％offの割引価格
        final_price = int(price * 0.9)
        return f'{final_price}円,{ten_off_comment}'
    else:
        return f'{price} 円,{proper_price_comment}'
    
check_discount_result = check_discount(10000)
print(check_discount_result)

#購入金額を引数として受け取り、条件に応じて割引の有無を判定する関数 check_discount(price) を作ってください。
twenty_off_comment = "20%割引"
ten_off_comment = "10%割引"
proper_price_comment = "割引なし"

def check_discount(price):
    if price >= 10000:
        final_price = int(price * 0.8)
        return f'{final_price}円,{twenty_off_comment}'
    elif price >= 5000:
        final_price = int(price * 0.9)
        return f'{final_price}円,{ten_off_comment}'
    else:
        f'{price}円,{proper_price_comment}'
        
check_discount_result = check_discount(6000)
print(check_discount_result)

#あなたは、レストランの料理の注文を管理しています。料理の数を引数として受け取り、注文の量に応じてサービスの有無を判定する関数 check_service(order_count) を作ってください。
# 10皿以上 ➡️ 「ドリンクサービス」　 5皿以上10皿未満 ➡️ 「デザートサービス」　# 5皿未満 ➡️ 「サービスなし」

ten_over_comment = "ドリンクサービス"
five_over_comment = "デザートサービス"
order_comment = "サービスなし"

def check_service(order_count):
    if order_count >= 10:
        return f'{order_count}皿注文,{ten_over_comment}'
    elif order_count >= 5:
        return f'{order_count}皿注文,{five_over_comment}'
    else:
        return f'{order_count}皿注文,{order_comment}'
    
order_count_result = check_service(12)
print(order_count_result)

#購入金額を引数として受け取り、条件に応じて割引後の最終価格を計算して返す関数 online_price(price) を作ってください。
#10,000円以上 ➡️ 15%割引 5,000円以上10,000円未満 ➡️ 5%割引 5,000円未満 ➡️ 割引なし

fifteen_off_comment = "15%割引"
five_off_comment = "5%割引"
proper_price_comment = "割引なし"

def online_price(price):
    if price >= 10000:
        final_price = int(price * 0.85)
        return f'{final_price}円,{fifteen_off_comment}'
    elif price >= 5000:
        final_price = int(price * 0.95)
        return f'{final_price}円,{five_off_comment}'
    else:
        return f'{price}円,{proper_price_comment}'
    
online_price_result = online_price(7500)
print(online_price_result)

#「Good morning!」と表示する関数 say_good_morning を定義し、それを呼び出してください。
def say_good_morning():
    print('Good morning!')
    
say_good_morning()

#2つの数字を引数として受け取り、それらを足し算して結果を戻り値として返す関数を作りましょう。その関数を呼び出して、戻り値をターミナルに出力してください。
def add_numbers(x,y):
    final_answer = x + y
    return final_answer

add_numbers_result = add_numbers(10,20)
print(add_numbers_result)


#2つの引数 item（品物名）と price（価格）を受け取り、f文字列（f-string）を使って次のような商品情報を表示する関数を作成してください。「○○は、□□円です。」
def buy_items(item,price):
    message = f'{item}は、{price}円です。'
    return message
    
buy_item_message = buy_items('シャインマスカット',5000)
print(buy_item_message)

# お皿に乗ったフルーツのリストです
fruits = ["りんご", "みかん", "いちご"]
def add_fruits(new_fruits):
    for fruit in new_fruits:
        fruits.append(fruit)

add_fruits(["バナナ", "ぶどう"])
for fruit in fruits:
    print(fruit)
    

# おもちゃ箱に入っている動物のリストです
animals = ["ねこ", "いぬ", "うさぎ"]
def add_animals(new_animals):
    for animal in new_animals:
        animals.append(animal)
        
add_animals(["くま", "パンダ"])
for animal in animals:
    print(animal)


# お皿に乗っているフルーツの値段のリストです
prices = [100, 250, 80, 500]
def add_tax(prices):
    tax_included_prices = []
    for price in prices:
        tax_price = price * 1.1
        tax_included_prices.append(tax_price)
    return tax_included_prices

tax_included_prices_result = add_tax(prices)
print(tax_included_prices_result)


# お客さんごとの買い物リストです
shopping_lists = [["牛乳", "パン"], ["りんご", "バナナ", "いちご"], ["卵", "チーズ"]]
def add_customer(shopping_lists):
    shopping_lists.append(["オレンジ", "ブロッコリー"])
        
add_customer(shopping_lists)
print(shopping_lists)


## お店の商品の値段のリストです
prices = [1500, 2000, 3500, 500]

def apply_discount(prices):
    sale_prices = []
    
    for price in prices:
        final_price = price * 0.7
        sale_prices.append(final_price)
    return sale_prices

apply_discount_result = apply_discount(prices)
print(apply_discount_result)



def fruits_list(new_fruit_list):
    fruits = []
    for fruit in new_fruit_list:
        fruits.append(fruit)
    return fruits

new_fruit_list_result = fruits_list(['りんご','バナナ','いちご','メロン'])
print(new_fruit_list_result)



#新しいリストに追加する場合
def animals_list(new_animal_list):
    animals = []
    for animal in new_animal_list:
        animals.append(animal)
    return animals

animal_list_result = animals_list(['ねこ','いぬ','うさぎ','きつね'])
print(animal_list_result)


#復習①
# お皿に乗っているフルーツの値段のリストです
prices = [100, 250, 80, 500]
def add_tax(prices):
    add_tax_list = []
    for price in prices:
        final_price = price * 1.1
        add_tax_list.append(final_price)
    return add_tax_list

add_tax_result = add_tax(prices)
print(add_tax_result)

#いくつかの新しいフルーツをまとめて受け取り、お皿のリストにすべて追加する関数 add_fruits(new_fruits) を作ってください。この関数を使って、["バナナ", "ぶどう"] をお皿のリストに追加してください。
#すべてのフルーツを追加したあと、お皿のリストの中身をすべて表示してください。

fruits = ["りんご", "みかん", "いちご"]
def add_fruits(new_fruits):
    for fruit in new_fruits:
        fruits.append(fruit)
        
add_fruits(["バナナ", "ぶどう"])
print(fruits)


#上記のリストのすべての値段を30%引きにした新しいリストとして返す関数 apply_discount(prices) を作成してください。この関数を使って、割引後のリストを変数 sale_prices に代入し、そのリストの中身をすべて表示してください。
# お店の商品の値段のリストです
prices = [1500, 2000, 3500, 500]
def apply_discount(prices):
    sale_prices = []
    for price in prices:
        final_price = price * 0.7
        sale_prices.append(final_price)
    
    return sale_prices

sale_prices_result = apply_discount(prices)
print(sale_prices_result)


#リストに追加
# お皿に乗ったフルーツのリストです
fruits = ["りんご", "みかん", "いちご"]
def add_fruits(new_fruits):
    for fruit in new_fruits:
        fruits.append(fruit)
        
add_fruits(["バナナ", "ぶどう"])
for fruit in fruits:
    print(fruit)
    
    
    
fruits = ["りんご", "みかん", "いちご"]
def add_fruits(new_fruits):
    for fruit in new_fruits:
        fruits.append(fruit)
        
add_fruits(["バナナ", "ぶどう"])
print(fruits)