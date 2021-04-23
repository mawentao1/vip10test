# class Furniture():
#     def __init__(self, name, area):
#         # 家具名字
#         self.name = name
#         # 家具占地⾯面积
#         self.area = area
# class Home():
#     def __init__(self, address, area):
#         # 地理理位置
#         self.address = address
#         # 房屋⾯面积
#         self.area = area
#         # 剩余⾯面积
#         self.free_area = area
#         # 家具列列表
#         self.furniture = []
#
#     def __str__(self):
#         return f'房⼦子坐落于{self.address}, 占地⾯面积{self.area}, 剩余⾯面积 {self.free_area}, 家具有{self.furniture}'
#
#     def add_furniture(self, item):
#         """容纳家具"""
#         if self.free_area >= item.area:
#             self.furniture.append(item.name)
#             # 家具搬⼊入后，房屋剩余⾯面积 = 之前剩余⾯面积 - 该家具⾯面积
#             self.free_area -= item.area
#         else:
#             print('家具太⼤大，剩余⾯面积不不⾜足，⽆无法容纳')
# bed = Furniture('双⼈人床', 6)
# jia1 = Home('北北京', 1200)
# print(jia1)
# jia1.add_furniture(bed)
# print(jia1)
# sofa = Furniture('沙发', 10)
# jia1.add_furniture(sofa)
# print(jia1)
#
# ball = Furniture('篮球场', 1500)
# jia1.add_furniture(ball)
# print(jia1)



##########
class Furniture():
    def __init__(self,name,area):
        self.area=area
        self.name=name
class House():
    def __init__(self, address, area):
        # 地理理位置
        self.address = address
        # 房屋⾯面积
        self.area = area
        # 剩余⾯面积
        self.free_area = area
        # 家具列列表
        self.furniture = []

    def __str__(self):
        return f'房子位于{self.address},占地面积{self.area},剩余面积{self.free_area}, 家具有{self.furniture}'
    def add_furniture(self,item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area-=item.area
        else:
            print('家具太大，剩余面积不够，无法容纳')

bed = Furniture('双人床', 6)
jia1 = House('北京', 1200)
print(jia1)
jia1.add_furniture(bed)
print(jia1)
sofa = Furniture('沙发', 10)
jia1.add_furniture(sofa)
print(jia1)

ball = Furniture('篮球场', 1500)
jia1.add_furniture(ball)
print(jia1)
