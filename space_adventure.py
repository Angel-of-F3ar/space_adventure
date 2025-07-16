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

def escape_pod():
    print("\nYou approach the escape pod. The door hisses open.")
    print("The door stops part of the way from opening, not enough for you to fit in. ")
    print("1. Do you try opening it?")
    print("2. Do you peek inside?")
    print("3. Do you leave to the control room?")
    print("4. Do you leave to the engine bay?")

    choice = input("What do you do? (1/2/3/4): ")

    if choice == "1":
        force_open()
    elif choice == "2":
        peek_in()
    elif choice == "3":
        control_room()
    elif choice == "4":
        engine_bay()
    else:
        print("Invalid Choice.")
        escape_pod()

def force_open():
    print("\nAs you force the door open to the pod you wind up breaking part of the hinge creating a loud noise!")
    print("BANG!")
    print("You hear an eerie cry coming from somewhere in the ship . Your heart rate shoots up.")
    print("You broke the pod door so you dont have time to fix it.")
    print("1. Do you try to hide?")
    print("2. Do you look for something to defend youself with?")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        look_to_hide()
    elif choice == "2":
        prepare()
    else:
        print("Invalid Choice.")
        force_open()

def peek_in():
    print("\nYou peek inside and see that there is something holding the door from opening.")
    print("1. Look for something to dilodge the item.")
    print("2. Force it open.")

    choice = input("What do you do? (1/2)")

    if choice == "1":
        find_item()
    elif choice == "2":
        force_open()
    else:
        print("Invalid Choice.")
        peek_in()

#Start the game
if __name__ == "__main__":
    intro()