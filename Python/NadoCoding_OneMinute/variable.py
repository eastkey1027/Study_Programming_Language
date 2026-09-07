# 변수

# 변수 선언
price1 = 10000
price2 = 20000
message = "Allowance"
print(price1, price2, message)

# 변수 이름 규칙
#1. 변수 이름은 문자, 숫자, 언더스코어(_)로 구성 가능
name_123 = "LDG"
_name_456 = "JHJ"
print(name_123, _name_456)

#2. 변수는 공백이나 특수문자(!, @, #, $, %, ^, &, *, (, ), -, + 등) 사용 불가
#na me = "LDG" / $_name = "JHJ" 사용불가

#3. 변수는 숫자를 맨처음으로 사용 할 수 없음
#123name = "LDG" / 1_name = "JHJ" 사용불가

#4. 변수는 대소문자를 구분함
name = "Hong"
NAME = "Kim"
Name = "Park"
print(name, NAME, Name)

#5. 변수는 예약어를 사용할 수 없음
# 예약어란 파이썬에서 이미 사용하고 있는 단어를 의미함
# True, False, for, while, if, continue, break, class ... 등
# True = 'python' 사용불가

#6. 변수 이름 설정 시 소문자 단어나 _를 사용하여 단어를 구분하는 것이 가독성이 좋음
variable = "variable" # VARIABLE 보다 소문자로
my_name = "dong_geon" # myname, myName 보다 _를 사용하여 구분하는 것이 가독성이 좋음
print(variable, my_name)