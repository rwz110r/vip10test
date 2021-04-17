import time
# try:
#     print(num)
# except (ImportError,NameError) as msg:
#     print(msg)
# else:
#     print('没问题继续执行')
# finally:
#     print('有没有问题我都执行')

# try:
#     f = open('1.txt')
#
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     except:
#         # 如果在读取⽂文件的过程中，产⽣生了了异常，那么就会捕获到
#         # ⽐比如 按下了了 ctrl+c
#         print('意外终⽌止了了读取数据')
#     finally:
#         f.close()
#         print('关闭⽂文件')
# except:
#     print("没有这个⽂文件")

# class washer():
#     def print_info(self):
#         # print(f'haier1的高度是{self.height}')
#         # print(f'haier1的宽度是{self.weith}')
#         print(f'haier2的重量是{self.weight}')
# # haier1 = washer()
# # # haier1.height = '200'
# # # haier1.weith = '300'
# # # haier1.print_info()
# haier2 = washer()
# haier2.weight = 200
# haier2.print_info()
# class washer():
#     def __init__(self,weight,height,brand):
#         self.weight =weight
#         self.height =height
#         self.brand  =brand
#     def print_info(self):
#         print(f'重{self.weight},高{self.height},品牌{self.brand}')
# bingxiang =washer(20,30,'西门子')
# bingxiang.print_info()
# class Teacher:
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#     def Tech(self,course):
#         print(f'{self.name}老师,性别是{self.sex},教的课程是{course}',)
# teacher1 = Teacher('任伟忠','男')
# teacher1.Tech('计算机基础')
#家 属性:面积,方法:搬
#家具属性:面积
class function():
    def __init__(self,fsize,name):
        self.fsize = fsize
        self.name = name
class Home():
    def __init__(self):
        self.hsize = 100
        self.freesize = self.hsize
        self.funiture = []
    def PutInto(self,item):
        if self.hsize>= item.fsize:
            self.funiture.append(item.name)
            self.freesize -= item.fsize
        else:
            print('剩余面积不足')
    def __str__(self):
        return f'剩余面积{self.freesize}'
bed1 = function(4,'bed')
home1 = Home()
home1.PutInto(bed1)
print(Home())


