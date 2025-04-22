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
