
import threading
import time

def dosometing(name):
    for i in range(10):
        time.sleep(1)
        print(name)
        print("this is the {}".format(str(i)))


if __name__ == '__main__':
    name = "changhao"
    th = threading.Thread(target=dosometing,args=(name,))
    th.start()