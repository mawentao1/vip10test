# class Washer():
#
#     def __init__(self):
#         self.width=500
#         self.height=800
#
#     def wash(self):
#         print(f'haier1的宽度是{haier1.width}')
#         print(f'haier1的高度是{haier1.height}')
#
# haier1=Washer()
# haier1.wash()
#
class Washer():
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def __str__(self):
        return '这是洗衣机的说明书'

    def __del__(self):
        print('我被删除了')

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')
haier1=Washer(10,20)
haier1.print_info()
haier2=Washer(30,900)
haier2.print_info()
print(haier2)

del haier1
