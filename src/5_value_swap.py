def value_swap(a, b):
    '''
    값 교환 
    '''
    temp = a 
    a = b
    b = temp
    return a, b


x = 10
y = 20
# 현재 출력 : x-10 y-20
print(f'x: {x}, y: {y}')

# temp = 0
# x = y
# y = 10

# 기대되는 값 : x-20 y-10
print(f'x: {x}, y: {y}')

res1, res2 = value_swap(x, y)
print(f'x: {res1}, y:{res2}')