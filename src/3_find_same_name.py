"""
23.06.10
동명이인 찾기
"""

names = ["Tom", "Jenny", "Mike", "Tom"]

for idx, name in enumerate(names):
    # print(idx, name)
    for find_value in names[idx+1:]:
        if name == find_value:
            print(f"{find_value}은 동명이인입니다")
