#FIBONACCI
import time
num0 = 0
num1 = 1
while True:
    print(num0, ", ", num1, end=", ", sep="")
    num0 += 1
    num1 += 1
    time.sleep(0.5)