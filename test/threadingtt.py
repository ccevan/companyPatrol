
import threading
import time


class Mythread(threading.Thread):

    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "this is {} @ {} times".format(self.name,str(i))
            print(msg)

if __name__ == '__main__':
    for i in range(5):
        th = Mythread()
        th.start()

    while True:

        print("now the threading's number is {}".format(len(threading.enumerate())))
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(0.5)
