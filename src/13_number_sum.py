"""
my_list = [1, 2, 3, 4, 5]
x = 0
for i in my_list:
    x = x + i

print(x)
"""

def mySum(my_list):
    x = 0
    for i in my_list:
        x = x + i

    return x

my_list = [1, 2, 3, 4, 5]
result = mySum(my_list)
print(result)