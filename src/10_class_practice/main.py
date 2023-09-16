import cat
import schedule
import time

my_cat = cat.Cat("Kiki", "3_year_old", "black", "food_fish", "toy_mouth", "haggard")
print(my_cat.name)
print(my_cat.needed_food_range)
print(my_cat.color)
print(f"{my_cat.name} 배고픈 정도: {my_cat.needed_food_range}")

my_cat.feed()
print(f"{my_cat.name} 배고픈 정도: {my_cat.needed_food_range}")
print(f"{my_cat.name} 몸무게: {my_cat.weight}")

def hello_print():
    print("Hello!!")
    
schedule.every(1).weeks.do(my_cat.changed_sick_status)
schedule.every(5).seconds.do(my_cat.cat_feed)
while True:
    schedule.run_pending()
    time.sleep(1)
    
