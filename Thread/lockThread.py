import threading
import time

threadLock = threading.Lock()

class mythread(threading.Thread):
    def __init__(self,threadId,name,delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.delay = delay

    def run(self):
        print(f'开启线程:{self.name}')
        threadLock.acquire()
        printTime(self.name,self.delay,3)
        threadLock.release()
        print(f'退出线程:{self.name}')
    # def run(self):
    #     print(f'开启线程:{self.name}')
    #     printTime(self.name,self.delay,3)
    #     print(f'退出线程:{self.name}')

def printTime(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print(f'{threadName}:{time.ctime(time.time())}')
        counter -= 1

t1 = mythread(1,'t1',1)
t2 = mythread(2,'t2',2)

t1.start()
t2.start()

threads = []
threads.append(t1)
threads.append(t2)

for t in threads:
    t.join()
print('退出主线程!')



