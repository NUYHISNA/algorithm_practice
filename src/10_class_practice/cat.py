import random

class Cat:
    def __init__(self, cat_name, cat_age, cat_color, cat_favoritefood, cat_favoritetoy, cat_cham):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
        self.favoritefood = cat_favoritefood
        self.favoritetoy = cat_favoritetoy
        self.cham = cat_cham
        self.needed_food_range = 10
        self.weight = 5
        self.sick = False
        
    def feed(self):
        self.needed_food_range += 5
        self.weight += 0.5
        print("냠냠")
        
    def notice_sick(self):
        if self.sick == True:
            print("아픔")   
            
    def changed_sick_status(self):
        sick_value = random.randint(0, 1)
        print(sick_value)
        if sick_value == 0:
            self.sick = True
        else:
            self.sick = False
            
    def cat_caring(self):
        print(f"{self.name}를 돌보시오.")
        self.sick = False
        
    def cat_feed(self):
        self.needed_food_range -= 1
        if self.needed_food_range == -15:
            print("죽음")
        elif self.needed_food_range == 4:
            print("배고파요 :(")
        