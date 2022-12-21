import threading
import time 

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadId,name,delay):
        threading.Thread.__init__(self)
        self.name = name
        self.threadId = threadId
        self.delay = delay

    def run(self):
        print(f'开始线程{self.name}')
        print_time(self.name,self.delay,5)
        print(f'退出线程{self.name}')

    
def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print(f'{threadName}:{time.ctime(time.time())}')
        counter -= 1

t1 = myThread(1,'thread-1',1)
t2 = myThread(2,'thread-2',2)

t1.start()
t2.start()
t1.join()
t2.join()
print('退出主线程!')


