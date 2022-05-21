# The threads which are always going to run in the background that provides supports to main or non-daemon threads, those background executing threads are considered as Daemon Threads. The Daemon Thread does not block the main thread from exiting and continues to run in the background. This article is based on threading in python, here we discuss daemon thread with examples.
# 
# There is one of the best examples of a daemon thread is Garbage Collector because we assume that the main thread is executing or running, at that time any memory problem occurs then immediately python virtual machine(PVM) is going to execute Garbage Collector. The Garbage Collector is going to execute in the background and destroy all the useless objects and then free memory by default will be provided, once there is free memory will available then the main thread is going to be executed without any problem.
# 
# Normal Thread learning the Flow of Non-Daemon Thread
# This example simplifies the flow of a non-daemon thread where we have created a thread_1() name function which having some lines of instructions to execute which reveal how the non-daemon thread is executed when the main thread terminates. At the next we have created the thread T of function thread_1() which is currently considered as a non-active thread, now we start the thread T, and we also have temporarily stopped the execution of the main thread for 5secs. Of time, between this 5sec. Thread T continues its execution and when the main thread is going to be executed after 5sec. Where it stops its work but there is a thread T still is in execution because it is a non-daemon thread and executes their instruction until their completion. 


import threading
import time

def print_a():
    print("starting of thread a")
    print("threading.currentThread().name : ",threading.currentThread().name)
    time.sleep(2)
    print("finishing of thread : ",threading.currentThread().name)

def print_b():
    print("starting of thread b")
    print("threading.currentThread().name : ",threading.currentThread().name)
    time.sleep(2)
    print("finishing of thread : ",threading.currentThread().name)

a=threading.Thread(target=print_a,name='A_thread',daemon=true)
b=threading.Thread(target=print_b,name='B_thread')

a.start()
b.start()
