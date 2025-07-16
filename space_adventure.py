import time
from escape_pod import escape_pod

def intro():
    print("You wake up on a dark, cold spaceship. Lights flicker around you.")
    print("You have three choices:")
    print("1. Search the control room")
    print("2. Explore the engine bay")
    print("3. Try the escape pod")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        control_room()
    elif choice == "2":
        engine_bay()
    elif choice == "3":
        escape_pod()
    else:
        print("Invalid choice Please try again.\n")
        intro() # recursively call to retry input

def control_room():
    print("\nYou stumble into the control room... it's eerily quiet.")

def engine_bay():
    print("\nYou move towards the engine bay. Something creaks behind you...")








#Start the game
if __name__ == "__main__":
    intro()