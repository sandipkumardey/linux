import queue
import threading
import time

buffer = queue.Queue(maxsize=5)

def producer():
    item = 1
    while True:
        buffer.put(item)
        print(f"Produced: {item}")
        item += 1
        time.sleep(1)

def consumer():
    while True:
        item = buffer.get()
        print(f"Consumed: {item}")
        time.sleep(2)

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()
p.join()
c.join()



"""
This program simulates the Producer-Consumer problem using threading and a queue.

The `producer` thread generates and adds items to a shared queue, with a 1-second delay between each item.
The `consumer` thread consumes items from the queue with a 2-second delay per item.

The queue is thread-safe, ensuring synchronization between producer and consumer. Both threads run concurrently,
producing and consuming items while maintaining the queue's fixed size (5). Threads are managed using Python's `threading` module.
"""
