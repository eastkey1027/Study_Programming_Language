# 인덱스 (배열[0]부터 시작하여 배열[배열길이-1]로 취급)
lang = "PYTHON"

print("인덱스")
print(lang[0])  # P
print(lang[-6])  # P
print(lang[5])  # N
print(lang[-1])  # N

# 슬라이싱 (배열[시작인덱스:끝인덱스+1])
print("슬라이싱")
print(lang[1:3])  # YT
print(lang[3:5])  # HO
print(lang[:3])   # PYT
print(lang[-3:])  # HON
print(lang[:-3])  # PYT

# 슬라이싱을 활용한 전체 출력
print("전체 출력")
print(lang[0:6])  # PYTHON
print(lang[:])    # PYTHON
print(lang[0:])   # PYTHON
print(lang[:6])   # PYTHON
print(lang[-6:])  # PYTHON
# print(lang[:0]) # 공백 출력 - lang[0]은 'P'값으로 정해져 있으므로, 직전인 -1까지 출력하라는 의미가 아니라 공백 출력