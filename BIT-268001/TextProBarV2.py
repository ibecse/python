# TextProBarV2.py
import time
scale = 100
for i in range(scale + 1):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)
