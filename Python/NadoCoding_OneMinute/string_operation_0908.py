# 문자열 처리
print("문자열 처리")
hello = "Hello"
world = "World"

str = hello + " " + world
print(str)  # Hello World

hello += " " + world # hello = hello + " " + world # 산술연산자 모두 가능
print(hello)  # Hello World

# 문자열 여러줄 처리
print("문자열 여러줄 처리")

fruit = "Apple\nBanana\nCherry"
print(fruit)  # Apple
              # Banana
              # Cherry

fruit2 = """Apple
Banana
Cherry"""
print(fruit2)  # Apple
                # Banana
                # Cherry

# len 함수
print("len 함수")

temp1 = "abcde"
print(len(temp1))  # 5

temp2 = "안녕하세요"
print(len(temp2))  # 5

temp3 = "ab cd e"
print(len(temp3))  # 7