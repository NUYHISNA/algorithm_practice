import cat

my_cat = cat.Cat("Kiki", "3_year_old", "black", "food_fish", "toy_mouth", "haggard")
print(my_cat.name)
print(my_cat.needed_food_range)
print(my_cat.color)
print(f"{my_cat.name} 배고픈 정도: {my_cat.needed_food_range}")

my_cat.feed()
print(f"{my_cat.name} 배고픈 정도: {my_cat.needed_food_range}")
print(f"{my_cat.name} 몸무게: {my_cat.weight}")

