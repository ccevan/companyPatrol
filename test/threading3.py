import threading
import time

g_num = 0

def work1(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("----in work1, g_num is %d---"%g_num)


def work2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("----in work2, g_num is %d---"%g_num)


print("---线程创建之前g_num is %d---"%g_num)

mutex = threading.Lock()


t1 = threading.Thread(target=work1, args=(1000000,))
t1.start()
t1.setName("这是线程1")
print("t1的现场名字{}".format(t1.getName()))
t2 = threading.Thread(target=work2, args=(1000000,))
t2.start()
print("t2的线程名字{}".format(t2.getName()))

# while len(threading.enumerate()) != 1:
#     time.sleep(1)
t1.join()
t2.join()
print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)