"""
홀짝게임
1.유저의 입력을 받아 (홀 or 짝)
2.컴퓨터는 랜덤으로 홀 짝 경우 만들기
3.맞춘 횟수만 저장
4.총 게임은 3판만 진행
5.맞춘 횟수 보여주기
"""

import random

user_input = input("홀 or 짝 입력: ")

if user_input == "홀":
    user_value = 0
elif user_input == "짝":
    user_input = 1
else:
    print("홀 or 짝으로 다시 입력해주세요")
    exit()


computer_random_value = random.randint(0, 1)

if computer_random_value == 0:
    computer_value = "홀"
elif user_input == "1":
    computer_value = "짝"


if user_input == computer_random_value:
    print(f"정답입니다. 유저:{user_input} 컴퓨터:{computer_random_value}")
else:
    print(f"오답입니다. 유저:{user_input} 컴퓨터:{computer_random_value}")