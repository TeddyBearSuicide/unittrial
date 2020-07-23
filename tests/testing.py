import sys
import time

sys.stdout.write("start")

for x in range(0, 5):
    b = "Loading" + "." * x
    sys.stdout.write('\r'+b)
    time.sleep(1)

