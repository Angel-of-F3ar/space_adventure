import time
import sys

def dead(reason="You died!"):
    print(f"\n{reason}")
    time.sleep(2)
    print("GAME OVER")
    time.sleep(1)
    sys.exit()