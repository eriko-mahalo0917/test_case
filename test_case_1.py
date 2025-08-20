def say_hello():
    print('こんにちは！')
say_hello()

#関数のmultiply_numberに引数a,b
def multiply_numbers(a,b):
#result一時的にの保存する変数だからa✕ｂをする　変数の箱！自分で決めてOK
    result = a * b
#returnで戻り値
    return  result
#productは変数で箱！他の名前にしてもいい　自分で決めてOK
product = multiply_numbers(3, 5)
print(product)
