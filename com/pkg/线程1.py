import time,threading
'''def run_proc():

    for n in range(0,2):
        print('Run  process %s ...' % threading.current_thread().name)
print('Run  process %s ...' % threading.current_thread().name)
t = threading.Thread(target= run_proc  , name= 'LoopThread' )
t.start()
t.join()
print(threading.main_thread().name)
t = threading.Thread(target= run_proc  ,name=None  )
t.start()
time.sleep(2)    #sleep
t = threading.Thread(target= run_proc  ,name=None  )
t.start()
t.join(timeout=1)'''
balance = 0
lock = threading.Lock()
# 创建全局ThreadLocal对象:
local_school = threading.local()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        change_it(n)
        lock.release()
    print(threading.current_thread().name)

t1 = threading.Thread(target=run_thread,name='1', args=(5,))
t2 = threading.Thread(target=run_thread,name='2', args=(8,))
'''t1 = threading.Thread(target = run_thread(5),name='1')
t2 = threading.Thread(target = run_thread(8))'''
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)