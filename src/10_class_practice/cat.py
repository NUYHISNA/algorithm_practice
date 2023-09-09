class Cat:
    def __init__(self, cat_name, cat_age, cat_color, cat_favoritefood, cat_favoritetoy, cat_cham):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color
        self.favoritefood = cat_favoritefood
        self.favoritetoy = cat_favoritetoy
        self.cham = cat_cham
        self.needed_food_range = 5
        self.weight = 5
        self.sick = False
        
    def feed(self):
        self.needed_food_range += 5
        self.weight += 0.5
        print("냠냠")
        
    def notice_sick(self):
        if self.sick == True:
            print("아픔")   