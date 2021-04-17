#类的外面创建属性
# class Washer():
#     def wash(self):
#         print('我会洗衣服')
#
# haier1=Washer()
#对象名.属性
# haier1.width=500
# haier1.height=800
# print(f'haier1的宽度是{haier1.width}')
# print(f'haier1的高度是{haier1.height}')

#类的里面创建属性 self.属性名
class Washer():
    def print_info(self):
        print(f'haier1的宽度是{haier1.width}')
        print(f'haier1的高度是{haier1.height}')
        print(f'haier1的高度是{haier2.height}')
#创建对象
haier1=Washer()
haier2=Washer()
haier1.width=500
haier1.height=800
haier1.print_info()
haier2.print_info()
