import time
from game_tools import dead, game_inventory, terminal_unlocked
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
    global terminal_unlocked  # declare you're modifying the global variable
    read_logs = set()

    while True:
        print("\n--- Captain's Logs ---")
        for log_title in logs:
            if log_title == "Log 68" and len(read_logs) < 4:
                print(f"{log_title}: [LOCKED]")
            elif log_title in read_logs:
                print(f"{log_title} (READ)")
            else:
                print(log_title)

        print("Type the log name (e.g., 'Log 64') to read it or type 'exit' to leave.")
        choice = input("Your choice: ")

        if choice.lower() == "exit":
            print("Exiting logs...")
            break
        elif choice in logs:
            if choice == "Log 68" and len(read_logs) < 4:
                print("You must read the other logs before accessing this one.")
            else:
                print(f"\n{logs[choice]}\n")
                read_logs.add(choice)
                time.sleep(2)
        else:
            print("Invalid Choice.")

    # After loop ends, check if all logs were read
    if "Log 68" in read_logs:
        print("You've seen everything you needed...")
        terminal_unlocked = True  # <- correctly updates the global flag
    else:
        terminal_unlocked = False
