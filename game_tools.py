import time
import sys

game_inventory = []

terminal_unlocked = False

read_flight_log_25 = False

inspected_paper = False

def dead(reason="You died!"):
    print(f"\n{reason}")
    time.sleep(2)
    print("GAME OVER")
    time.sleep(1)
    sys.exit()