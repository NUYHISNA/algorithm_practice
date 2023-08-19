# my_values = []
# my_values.append(1)
# my_values.append(2)

# for value in my_values:
#     print(value)

# match_value = 2

# if match_value in my_values:
#     print('there exists value')
# else:
#     print('there exists no value')


# import random

# lotto_numbers = []

# for _ in range(6):
#     value = random.randint(1, 50)
#     if value in lotto_numbers:
#         continue
#     lotto_numbers.append(value)
lotto_numbers = []
import random


def lotto_list():
    lotto_numbers = []
    while True:
        value = random.randint(1, 50)
        if value in lotto_numbers:
            continue
        lotto_numbers.append(value)
        if len(lotto_numbers) == 6:
            break
        
    return lotto_numbers

result = lotto_list()
print(f"{result} - The End")