# python의 경우 GIL에 의해 멀티 스레드를 사용해서 i/o의 관점에서만 멀티 처리가 가능하고 
# 실제 cpu를 통한 연산에는 멀티 처리가 되지 않는다. 
# 따라서 분석을 분산 처리하기 위해서는 멀티 프로세서를 구성하여 사용한다.


######################################################################################
# sample code 1>
from multiprocessing import Process, Queue

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return

if __name__ == "__main__":
    START, END = 0, 10000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END//2, result))
    th2 = Process(target=work, args=(2, END//2, END, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    print(f"Result: {total}")



######################################################################################
# sample code 2>
from multiprocessing import Process
import sys

rocket = 0

def func1():
    global rocket
    print('start func1')
    while rocket < 1000000:
        rocket += 1
    print('end func1')

def func2():
    global rocket
    print('start func2')
    while rocket < 1000000:
        rocket += 1
    print('end func2')

if __name__=='__main__':
     p1 = Process(target = func1)
     p1.start()
     p2 = Process(target = func2)
     p2.start()