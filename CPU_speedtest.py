import random
import time
import multiprocessing

# run 3 consecutive speed tests
for i in range(3):
    start = time.time()
    # create and manipulate a large matrix of random numbers
    x = [[random.random() for col in range(10000)] for row in range(10000)]
    result = {k:v for v,k in zip(sorted(x), range(10000))}
    print("run {}: | speed: {} seconds".format(i, round(time.time() - start, 2)))

print("\nverify number of CPU threads:", multiprocessing.cpu_count())