# 電卓アプリの作成
"""
電卓アプリケーション
このプログラムは基本的な四則演算（加算、減算、乗算、除算）を行います。
ユーザーから二つの数字と演算子を入力として受け取り、結果を表示する機能を実装しています。
関数:
    add(x, y): 二つの数値を加算します。
    subtract(x, y): 二つの数値を減算します。
    multiply(x, y): 二つの数値を乗算します。
    divide(x, y): 二つの数値を除算します。ゼロ除算の場合はエラーメッセージを返します。
    calculator(): ユーザーからの入力を受け取り、適切な演算を行い結果を表示します。
使用方法:
    このスクリプトを直接実行すると、ユーザーに数値と演算子の入力を求め、結果を表示します。
"""
# このプログラムは基本的な四則演算（加算、減算、乗算、除算）を行います。
# ユーザーから二つの数字と演算子を入力として受け取り、結果を表示する機能を実装してください。
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "エラー！ゼロによる除算。"
    return x / y

def calculator():
    try:
        num1 = float(input("最初の数字を入力してください: "))
        operator = input("演算子を入力してください (+, -, *, /): ")
        num2 = float(input("次の数字を入力してください: "))

        if operator == '+':
            print(f"結果: {add(num1, num2)}")
        elif operator == '-':
            print(f"結果: {subtract(num1, num2)}")
        elif operator == '*':
            print(f"結果: {multiply(num1, num2)}")
        elif operator == '/':
            print(f"結果: {divide(num1, num2)}")
        else:
            print("無効な演算子です。")
    except ValueError:
        print("無効な入力です。数値を入力してください。")

if __name__ == "__main__":
    calculator()