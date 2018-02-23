#!/usr/bin/python
# -*- coding: utf-8 -*-

#task_master.py 

# import model

import random,time, queue
# import function from model 
from multiprocessing.managers import BaseManager 

# send task queue(Queue type is first in first out ) :
task_queue = queue.Queue()
# receive result queue :
result_queue = queue.Queue()

# from BaseManager(method : start/get_server/connect/shutdown/register/address) inherit class :
class QueueManager(BaseManager):
    pass
    
#registe the queue to network , and callable varibale releate Queue object :
QueueManager.register(' get_task_queue', callable = lambda : task_queue)
QueueManager.register(' get_result_queue', callable = lambda : result_queue)

#bind port 5000 , set password 'abc':
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。Python对bytes类型的数据用带b前缀的单引号或双引号表示：
manager = QueueManager(address=('', 5000),authkey=b'abc')

#start Queue :
manager.start()

#get Queue object by network:
task = manager.get_task_queue()
result = manager.get_result_queue()

#put some task :
for i in range(10):
    n =random.randint(0,10000)
    print('Put task %d...' % n )
    task.put(n)

# read result from result queue :
print('Try get results ...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result : %s' % r )
#close 
manager.shutdown()
print('master exit.')
