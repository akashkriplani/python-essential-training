from multiProcess import Process
import time
import threading


def longSquare(num, results):
    time.sleep(1)
    results[num] = num ** 2

results = {}
processes = [Process(target=longSquare, args=(n, results)) for n in range(0, 10)]
[p.start() for p in processes]
[p.join() for p in processes]

print(results)

results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)