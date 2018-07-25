#
# from multiprocessing import Process
# import time
# import os
#
#
# def comeon():
#     while True:
#         print("hello world")
#         print("now the pid is {}".format(os.getpid()))
#         print("now the ppid is {}".format(os.getppid()))
#         print('the pid name is {}'.format(p1.name))
#         time.sleep(1)
#
# if __name__ == '__main__':
#
#     # for i in range(5):
#     p1 = Process(target=comeon)
#     p1.name = "heihei"
#
#     p1.start()
#
#
#

def tt(**kwargs):
    print(kwargs)
    # print(**kwargs)

tt(name="changhao",age=12)