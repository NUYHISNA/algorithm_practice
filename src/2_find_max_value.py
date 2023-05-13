"""
작성 날짜: 23.05.13
설명: 리스트 내의 최댓값 찾기
"""


lists = [17, 92, 18, 33, 58, 7, 33, 42]

max_value = 0

for i in lists:
    if max_value < i:
        max_value = i

print(max_value)    