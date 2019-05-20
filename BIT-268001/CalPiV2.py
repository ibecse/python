# CalPiV2.py
from random import random
from time import perf_counter
DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(DARTS):
    x, y = random(), random()
    if pow((x**2 + y**2), 0.5) <= 1:
        hits += 1
pi = 4 * (hits/DARTS)
print("Pi={}".format(pi))
print("RunTime={:.5f}s".format(perf_counter() - start))
