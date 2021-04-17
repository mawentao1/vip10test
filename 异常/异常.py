# try:
#     print(num)
# except NameError:
#     print('有错误')
#
# try:
#     print(num)
# except Exception:
#     print('有错误')
#
# try:
#     print(num)
# except (NameError,ImportError,IndexError) as msg:
#     print(msg)

# try:
# #   open('read.txt',r)
#     print(1)
# except Exception as msg:
#     print(msg)
# else:
#     print('我是else,没有异常时执行的代码')
# finally:
#     print('有或者没有异常也要执行的代码')


import time

try:
    f = open('test.txt')

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件的过程中，产⽣了异常，那么就会捕获到
        # ⽐如 按下了 ctrl+c
        print('意外终⽌止了了读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")

