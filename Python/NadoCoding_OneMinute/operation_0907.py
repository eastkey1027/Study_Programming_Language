# 산술 연산자
print("산술 연산자")
print(5 + 2) # 덧셈  7
print(5 - 2) # 뺄셈  3
print(5 * 2) # 곱셈  10
print(5 / 2) # 나눗셈  2.5
print(5 // 2) # 몫  2
print(5 % 2) # 나머지  1
print(5 ** 2) # 거듭제곱  25

# 비교 연산자
print("비교 연산자")
print(5 > 2) # 크다  True
print(5 >= 2) # 크거나 같다  True
print(5 < 2) # 작다  False
print(5 <= 2) # 작거나 같다  False
print(5 == 2) # 같다  False
print(5 != 2) # 같지 않다  True

# 논리 연산자
print("논리 연산자")
print(5 > 2 and 3 < 7) # 두 조건이 모두 참일 때 True 반환  True
print(5 > 2 or 3 > 7) # 두 조건 중 하나라도 참이면 True 반환  True
print(not(5 > 2)) # 조건이 참이면 False, 거짓이면 True 반환  False

# 멤버 연산자
print("멤버 연산자")
print('c' in 'cat') # 문자열 안에 포함되어 있으면 True 반환  True
print('c' not in 'cat') # 문자열 안에 포함되어 있지 않으면 True 반환  False