#定义一个老师类，老师的姓名，性别，教学课程。老师可以去教学。实现：xx老师，性别xx，教xx课
#分析：类=老师 属性：姓名，性别，教学课程  方法（行为）：教学
# class Teacher():
#     def __init__(self,name,sex,course):
#         self.name=name
#         self.sex=sex
#         self.course=course
#     def teach(self):
#         print(f'{self.name}老师，性别{self.sex},教{self.course}课')
# T=Teacher('小米','男','语文')
# T.teach()

#将小于房子剩余面积的家具摆放到房子中
# 分析：
# 类》房子和家具    房子的属性：占地面积和剩余面积  家具的属性：家具名和家具占地面积
# 命名家具的列表
class House():
    def __init__(self,area,address):
        self.area=area
        self.address=address
        self.free_area=area
        self.furniture=[]
class Furniture():
    def __init__(self,area,name):
        self.area=area
        self.name=name
    def __str__(self):
        return f'房子位于{self.address},占地面积{self.area},剩余面积{self.free_area}, 家具有{self.furniture}'
    def add_Furniture(self,item):
        if self.free_area>item.area:
            self.furniture.append(item.name)
            self.free_area=item.area
        else:
            print('家具太大，剩余面积不够，无法容纳')

bed = Furniture('双⼈人床', 6)
jia1 = Home('北北京', 1200)
print(jia1)
jia1.add_furniture(bed)
print(jia1)
sofa = Furniture('沙发', 10)
jia1.add_furniture(sofa)
print(jia1)

ball = Furniture('篮球场', 1500)
jia1.add_furniture(ball)
print(jia1)


