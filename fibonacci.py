#FIBONACCI
import time
num0 = 0
num1 = 1
hi = 0
print("Press Control-C to stop.")
try:
    while True:
        num = num0 + num1
        if hi == 0:
            num0 = num
            hi = 1
        else:
            num1 = num
            hi = 0
        print(num, end=", ", flush=True)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Thanks for using Palc's FIBONACCI function!")
except:
    print("an error occured.")