import threading

class Threaing_test(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


send = Threaing_test(name='Sending message')
receive = Threaing_test(name='Receive message')


send.start()
receive.start()