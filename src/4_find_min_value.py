'''
23/06/24
최솟값 찾기
'''

def find_min_value(my_list):
    min_value = my_list[0]
    for i in my_list:
        if min_value > i:
            min_value = i

    return min_value

my_list = [1, 10, 7, 3]
result = find_min_value(my_list)
print(result)