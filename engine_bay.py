import time
from captains_quarters import terminal_used
from control_room import control_room
from escape_pod import escape_pod
from game_tools import dead, game_inventory, read_flight_log_25

def engine_bay():
    print("\nYou step into the engine bay. Something creaks behind you...")
    time.sleep(3)
    print("Why did you come here?")
    print("Wouldn't escaping have made more sense?")
    time.sleep(5)
    print("Still... something draws you in.")
    time.sleep(6)
    print("It feels off. Like you're being watched.")
    time.sleep(4)
    print("1. Go to the Control Room.")
    print("2. Go to the Escape Pods.")
    print("3. Look around.")

    choice = input("What will you do? (1/2/3): ")

    if choice == "1":
        control_room()
    elif choice == "2":
        escape_pod()
    elif choice == "3":
        look_around()
    else:
        print("Invalid choice.")
        engine_bay()


def look_around():
    print("\nYou begin feeling your way through the engine bay — it's pitch black.")
    time.sleep(4)
    print("You know how to fix the lights back home, but this? This is different.")
    time.sleep(4)
    print("You bump into cold metal, cables, maybe even tools. Hard to tell.")
    time.sleep(4)
    print("Suddenly, something crashes to the floor in the far corner.")
    time.sleep(4)
    print("A chill grips your spine. Danger.")
    time.sleep(3)

    print("1. Freeze in place.")
    print("2. Run for the door.")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        dead("You freeze. Maybe it'll go away.\n"
             "But then... footsteps.\n"
             "Close. Too close.\n"
             "You never see what took you.")
    elif choice == "2":
        dead("You bolt. No time to think, just run.\n"
             "But something's faster.\n"
             "Your scream is cut short.\n"
             "Something wet hits the floor.")
    else:
        print("Invalid choice.")
        look_around()