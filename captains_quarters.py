import time
from game_tools import dead, game_inventory
from captains_logs import logs

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
    while True:

        print("Captain Dairus's Terminal")
        print("=====MENU======")
        print("1. Captains Logs")
        print("2. Flight Logs")
        print("3. Exit Terminal")

        choice = input("Select an option: (1/2/3): ")

        if choice == "1":
            captains_logs()
        elif choice == "2":
            flight_logs()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid Choice.")


def captains_logs():
    max_attempts = 3
    password = "Cheryl2042"

    while max_attempts > 0:
        print("Password: ")
        time.sleep(2)
        print("1. Attempt Password.")
        print("2. Exit Captains Logs")

        choice = input("What will you do? (1/2): ")

        if choice == "1":
            guess = input("Enter password: ")
            if guess == password:
                access_granted()
                break
            else:
                max_attempts -= 1
                print(f"Incorrect. Attempts remaining: {max_attempts}")
        elif choice == "2":
            print("You step away from the terminal...")
            break
        else:
            print("Invalid choice.")

    if max_attempts == 0:
        sound_alarm()


def sound_alarm():
    print("You messed up.")
    time.sleep(5)
    print("Red lights begin flashing in the room... and in the hallway.")
    time.sleep(5)
    print('You think, "Great security system... but why is it this loud?"')
    time.sleep(5)
    print("The blaring siren drowns out everything — even your own thoughts.")
    time.sleep(5)
    print("You get up and head toward the door...")
    time.sleep(5)
    dead("Wait... isn't tha—")

def access_granted():
    pass