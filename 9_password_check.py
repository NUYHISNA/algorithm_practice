def password_count(my_password):
    count_lower = 0
    count_number = 0
    count_space = 0 
    count_upper = 0
    
my_words = "Hello python11"

for word in my_words:
    if word.islower():
        count_lower = count_lower + 1
    if word.isnumeric():
        count_number = count_number + 1 
    if word.isspace():
        count_space = count_space + 1
    if word.isupper():
        count_upper = count_upper + 1   
         
print(f"count_lower: {count_lower}")
print(f"count_number: {count_number}")
print(f"count_space: {count_space}")
print(f"count_upper: {count_upper}")

password_count(my_words)

def password_valid(user_password):
    is_valid = True
    for word in user_password:
        if word.isspace():
            is_valid = False
    
    if len(user_password) < 8:
        is_valid = False
        
    return is_valid

my_words = "Hello python11"