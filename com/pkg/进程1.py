from multiprocessing import Process
import os
from multiprocessing import Pool #进程池
import time, random
import subprocess #启动一个子进程，然后控制其输入和输出
# 子进程要执行的代码
def run_proc(name):

    print('Run child process %s (%s)...' % (name, os.getpid()))
"""
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) #执行函数和函数
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')"""


"""if __name__ == '__main__':   #

    print("parents name " + str(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print("chi start")
    p.start()
    p.join    #进程间的同步     
    print("chi end")"""
'''
def run_proc(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':   #批量创建
    print('Parent process %s .' % os.getpid())
    p = Pool()     #限制
    for i in range(7):
        p.apply_async(run_proc, args=(i,))   #执行函数和函数
    p.close()  #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之
    p.join()   #前必须先调用close()，调用close()之后就不能继续添加新的Process了。'''

r = run_proc("test")
r = subprocess.call([])