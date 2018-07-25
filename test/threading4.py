
import threading

class Mythread1(threading.Thread):
    def run(self):
        mutex1.acquire()
        print("this is the thread1 is runiinng")

        mutex2.acquire()
        print("hello,get the mutex2")
        mutex2.release()
        mutex1.release()

class Mythread2(threading.Thread):
    def run(self):
        mutex2.acquire()
        print("this is the thread2 is running")
        mutex1.acquire()
        print("hello mutex1 is acquire")
        mutex1.release()
        mutex2.release()




mutex1 = threading.Lock()
mutex2 = threading.Lock()

for i in range(10):

    th1 = Mythread1()
    th2 = Mythread2()
    th1.start()
    th2.start()

