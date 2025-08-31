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