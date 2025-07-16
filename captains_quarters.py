import time
from game_tools import dead, game_inventory

def captains_quarters():
    print("\nYou enter the captains quartes.")
    time.sleep(5)
    print("It was unlocked?!")
    time.sleep(5)
    print("IT IS...")
    time.sleep(5)
    print("Clean and a bit dusty, but untouched.")
    time.sleep(5)
    print("There on his desk is the captains terminal...")
    time.sleep(5)
    print("already booted")
    time.sleep(5)
    print("You see a key fob on the bed as well. That doesnt look like yours.")
    time.sleep(5)
    print("You wonder if you should grab it.")
    time.sleep(5)
    print("1. Sit down at the terminal.")
    print("2. Grab the fob.")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        print("\nYou decide to sit at the terminal first, eyes scanning the screen for answers.")
        time.sleep(4)
        terminal_accessed()
    elif choice == "2":
        print("\nYou decide to grab the fob first — better safe than sorry.")
        game_inventory.append("fob")
        time.sleep(3)
        print("You tuck it into your pocket and sit at the terminal.")
        time.sleep(4)
        terminal_accessed()
    else:
        print("Invalid Chopice.")
        captains_quarters()


def terminal_accessed():
    pass