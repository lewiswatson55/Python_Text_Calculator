#FIBONACCI
import time
import logging
try:
    def main(Comandeer):
        global _
        _ = Comandeer
except Exception as ename:
    logging.info("??? MISSING TRANSLATION _ DEFINE FIBO ERROR %s" % ename)

def FibMain():
    print(_("Press Control-C to stop."))
    print("0, 1", end=", ")
    try:
        num0 = 0
        num1 = 1
        hi = 0
        while True:
            num = num0 + num1 #set variable num to the sum of num0 and num1.
            if hi == 0:
                num0 = num
                hi = 1
            else: #every other time this loops it will run this instead of the previous block
                num1 = num # set num1 to num
                hi = 0 #next time it wont do this block it'll do the previous one
            print(num, end=", ", flush=True) #print the current number
            time.sleep(0.5)
    except KeyboardInterrupt: #if ctrl-c
        print(_("Thanks for using Palc's FIBONACCI function!"))
    except Exception as e: #if an error occurs
        print(_("An error occured."))
        logging.err("Exception %s in FIBONACCI" % e)

if __name__ == "__main__":
    def _(thestring):
        return thestring
    FibMain()