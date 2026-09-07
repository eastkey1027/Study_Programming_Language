# boolean 형변환
# 숫자 자료형
a = 1
b = 0
c = -1

print("숫자 자료형")
print(bool(a)) # True
print(bool(b)) # False
print(bool(c)) # True

# 문자열 자료형
d = "hello"
e = ' '
f = ""

print("문자열 자료형")
print(bool(d)) # True
print(bool(e)) # True
print(bool(f)) # False

# None 자료형
g = None

print("None 자료형")
print(bool(g)) # False