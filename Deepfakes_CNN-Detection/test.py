from threading import Thread
from multiprocessing import Process, Queue as mQueue
from queue import Queue
import time


def single_test():
    my_sum = 0
    for i in range(1, 10000000):
        my_sum += i
    print("单线程结果:", my_sum)


def thread_test():

    def sum_func(q, start, end):
        my_sum = 0
        for i in range(start, end):
            my_sum += i
        q.put(my_sum)

    def run_thread():
        q = Queue()
        t1 = Thread(target=sum_func, args=(q, 1, 5000000))
        t2 = Thread(target=sum_func, args=(q, 5000000, 10000000))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        my_sum = 0
        while not q.empty():
            my_sum += q.get()
        print("多线程结果:", my_sum)

    run_thread()


def process_test():
    def sum_process_func(q, start, end):
        my_sum = 0
        for i in range(start, end):
            my_sum += i
        q.put(my_sum)
    def run_process():
        q = mQueue()
        p1 = Process(target=sum_process_func, args=(q, 1, 5000000))
        p2 = Process(target=sum_process_func, args=(q, 5000000, 10000000))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        my_sum = 0
        while not q.empty():
            my_sum += q.get()
        print("多进程结果:", my_sum)

    run_process()


if __name__ == "__main__":
    t0 = time.time()
    single_test()
    t1 = time.time()
    thread_test()
    t2 = time.time()
    process_test()
    t3 = time.time()
    print(f"单线程耗时:{t1-t0}s")
    print(f"多线程耗时:{t2-t1}s")
    print(f"多进程耗时:{t3-t2}s")

