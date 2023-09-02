class User:
    def __init__(self, user_name, user_age):
        self.name = user_name
        self.age = user_age
        self.address = "경기도 화성시 반월동"
        self.my_image = "my_image.png"
        self.goal = "서비스 만들기"
        self.favorit_food = ["마라탕", "서브웨이"]
        
    def age_plus(self):
        self.age = self.age + 1
        
    def change_address(self, change_address):
        self.address = change_address
        
    def add_favorit_food(self, food):
        self.favorit_food.append(food)
        
    def eat_my_food(self):
        for food in self.favorit_food:
            print(f"Good my food {food}")
            
user1 = User("안시현", 15)
user1.eat_my_food()
print(user1.age)
user1.age_plus()
print(user1.age) 