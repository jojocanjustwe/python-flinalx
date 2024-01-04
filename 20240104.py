# 定義一個為 FriedChickenStore 的類別
class FriedChickenStore:
    # 類別初始化
    def __init__(self, name, address, business_hours, chicken_menu, income):
        self.name = name
        self.address = address
        self.business_hours = business_hours
        self.chicken_menu = chicken_menu
        self.total_income = income
# 店名
    def get_store_name(self):
        return self.name
# 地址
    def get_location(self):
        return self.address
#營業時間
    def get_business_hours(self):
        return self.business_hours
#菜單
    def get_chicken_menu(self):
        return self.chicken_menu
#總收入
    def get_total_income(self):
        return self.total_income

#建立3個副函式並定義四個物件分別回傳3個副函式
restaurant1 = FriedChickenStore("ChickenKing1", "馬來路39號", "10:00 AM - 10:00 PM", ["雞翅", "炸雞腿", "蒜香雞翅"], 5000)
restaurant2 = FriedChickenStore("ChickenKing2", "中華路11號", "11:00 AM - 11:00 PM", ["雞翅", "炸雞腿", "蒜香雞翅"], 6000)
restaurant3 = FriedChickenStore("ChickenKing3", "中正路30號", "12:00 PM - 12:00 AM", ["雞翅", "炸雞腿", "蒜香雞翅"], 7000)
restaurant4 = FriedChickenStore("ChickenKing4", "中華北路10號", "01:00 PM - 01:00 AM", ["雞翅", "炸雞腿", "蒜香雞翅"], 8000)

#列印各類別資訊
print("店的名稱：", restaurant1.get_store_name())
print("店的地址：", restaurant1.get_location())
print("店的營業時間：", restaurant1.get_business_hours())

print("店的名稱：", restaurant2.get_store_name())
print("店的地址：", restaurant2.get_location())
print("店的營業時間：", restaurant2.get_business_hours())

print("店的名稱：", restaurant3.get_store_name())
print("店的地址：", restaurant3.get_location())
print("店的營業時間：", restaurant3.get_business_hours())

print("店的名稱：", restaurant4.get_store_name())
print("店的地址：", restaurant4.get_location())
print("店的營業時間：", restaurant4.get_business_hours())



