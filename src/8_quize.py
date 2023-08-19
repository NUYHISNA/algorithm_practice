for i in range(5):
    print("*" * (i+1))
      
def add(a, b, works):
    if works:
        return a + b

def test_list():
    my_list = [1, 2, 3, 4]
    return my_list

result = add(1, 11, False)
print(result)
list_result = test_list()
print(list_result)
