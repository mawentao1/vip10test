#打印小猫爱吃鱼，小猫要喝水
#分析：类》猫   属性：吃鱼，喝水    方法：吃，喝
class Cat():
    def __init__(self,fish,water):
        self.fish=fish
        self.water=water
    def __str__(self):
        return '这是小猫的喜好'
    def eat(self):
        print(f'小猫爱吃{self.fish}'+','+f'小猫要喝{self.water}')
    # def drink(self):
    #     print(f'小猫要喝{self.water}')

cat=Cat('鱼','水')
cat.eat()
print(cat)


#小明爱跑步，爱吃东西
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
#分析：类：小明，小红    属性：姓名，原体重，跑步后的体重，吃东西后的体重   方法：跑步，吃东西
class Xiaomei():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return f'{self.name}体重是{self.weight}公斤'

class Xiaoming():
    def __init__(self,name,weight,w1,w2):
        self.name=name
        self.weight=weight
        self.w1 = w1
        self.w2 = w2
    def __str__(self):
        return f'{self.name}体重是{self.weight}公斤'
    def run(self):
        print(f'{self.name}爱跑步'+','+f'{self.name}爱吃东西')
        print(f'每次跑步会减肥{self.w1}公斤')
    def eat(self):
       # print(f'{self.name}爱吃东西')
        print(f'每次吃东西会增重{self.w2}公斤')
ming=Xiaoming('小明',75,0.5,1)
print(ming)
ming.run()
ming.eat()
mei=Xiaomei('小美',45)
print(mei)


# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
分析：类--》士兵，枪    属性--》        方法---》发射子弹 装子弹