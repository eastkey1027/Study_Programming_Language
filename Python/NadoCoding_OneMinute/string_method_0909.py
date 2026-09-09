# 문자열 메소드
# 문자열변수.메소드()

letter1 = "how are YOU?"

# 대소문자 변환 메소드
print(letter1.lower())  # 모두 소문자로 변환  how are you?
print(letter1.upper())  # 모두 대문자로 변환  HOW ARE YOU?
print(letter1.capitalize())  # 첫 글자만 대문자로 변환  How are you?
print(letter1.title())  # 각 단어의 첫 글자만 대문자로 변환  How Are You?
print(letter1.swapcase())  # 대문자는 소문자로, 소문자는 대문자로 변환  HOW ARE you?

# 문자열 내용을 기준으로 처리하는 메소드

print(letter1.split())  # 공백을 기준으로 문자열을 나누어 리스트로 반환  ['how', 'are', 'YOU?'] # [], '', ,도 같이 출력됨
print(letter1.count("how"))  # 문자열에서 특정 문자열의 개수를 반환  1
print(letter1.startswith("how"))  # 문자열이 특정 문자열로 시작하는지 여부를 boolean형식으로 반환  True
print(letter1.endswith("you?"))  # 문자열이 특정 문자열로 끝나는지 여부를 boolean형식으로 반환  False
print(letter1.find("are"))  # 문자열에서 특정 문자열의 위치를 반환, 없으면 -1 반환  4

# 문자열 내용을 변환하는 메소드

letter2 = "   how are you?..."

print(letter2.strip())  # 문자열의 앞뒤 공백만 제거  how are you?
print(letter2.strip('.'))  # 문자열의 앞뒤 특정 문자를 제거     how are you  # how 앞에 공백은 제거되지 않음
print(letter2.strip(' '))  # 문자열의 앞뒤 공백만 제거, 문자열 사이에 중간 공백은 제거되지 않음 = print(letter2.strip())  how are you?...

letter3 = "I'm a student."

print(letter3.replace("student", "teacher"))  # 문자열에서 특정 문자열을 다른 문자열로 변환  I'm a teacher.
print(letter2.replace(' ', ''))  # line 25에서 문자열 사이 공백을 제거 하고 싶을 때 replace()를 사용하면 됨  howareyou?...
print(letter3.center(18, '-'))  # 문자열을 특정 길이로 맞추고, 나머지 공간을 특정 문자로 채움  --I'm a student.--
print(letter3.center(12, '-'))  # 문자열 길이가 지정한 길이보다 작으면 그대로 출력  I'm a student.

'''
더 많은 함수는 검색창에 'python 내장형' 이라고 검색한 후, 공식 홈페이지에서 확인 가능
'''