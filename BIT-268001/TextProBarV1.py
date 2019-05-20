# TextProBarV1.py
import time
scale = 10
print("-----执行开始-----")
for i in range(scale + 1):
    a = (i/scale) * 100
    b = i * '*'
    c = (scale-i) * '.'
    print("{:^3.0f}%[{}->{}]".format(a, b, c))
    time.sleep(0.1)
print("-----执行结束-----")
