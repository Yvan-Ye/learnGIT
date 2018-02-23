#!/usr/bin/python
# -*- coding: utf-8 -*-

# task_worker.py 

import time, sys, queue
from multiprocessing.managers import BaseManager

#create QueueManager class that inherit BaseManager :
class QueueManager(BaseManager):
    pass

#register only provide name due to that only get Queue from network : 
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#connect to server, as machine that running task_master.py:
server_addr ='127.0.0.1'
print('Connect to server %s... ' % server_addr)

#keep same port and password to task_master.py :
m =QueueManager(address = (server_addr, 5000),authkey =b'abc')

#connect from network :
m.connect()

#get Queue's object :
task = m.get_task_queue()
result = m.get_result_queue()

#get task  from task queue , and write in result to result queue :
for i in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d * %d...' % (n,n))
        r = '%d * %d = %d ' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.empty:
        print('task queue is empty.')
        
#deal with result :
print('worker exit.')

