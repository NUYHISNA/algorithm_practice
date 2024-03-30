"""
input: Python
output: ythonPpost
1. 맨 앞에 글자는 맨뒤에 붙여주기
2. 맨 뒤에 특정단어(ex.post) 붙여주기
"""

def encrypt_char(my_char, p):
    # print(my_char[0], my_char[1:])
    enc_char = my_char[1:] + my_char[0] + p
    print(enc_char)

my_wanted_char = "coffee"
enc_word = "good"
encrypt_char(my_wanted_char, enc_word)