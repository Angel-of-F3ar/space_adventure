import time
from game_tools import dead

def control_room():
    print("\nYou stumble into the control room... it's eerily quiet.")
    time.sleep(2)
    print("Dust clings to shattered monitors and rusted consoles.")
    time.sleep(2)
    print("You scan the room and freeze.")
    time.sleep(2)
    print("A figure sits slumped in the captain’s chair — motionless.")
    time.sleep(3)
    print("Wait... is that—CAPTAIN?!")
    time.sleep(4)

    print("1. Call out to the Captain")
    print("2. Walk up and turn the chair around")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        call_out()
    elif choice == "2":
        walk_over()
    else:
        print("Invalid choice.")
        control_room()


def call_out():
    print("\nYou feel a rush of excitement in your chest — like butterflies.")
    print("You call out without hesitation.")
    time.sleep(5)
    print("CAAAPTAIIIN!!!")
    time.sleep(6)
    print("As your voice echoes through the ship, something darts across the far corridor.")
    time.sleep(5)
    print("Butterflies... gone.")
    time.sleep(6)
    print("Your breathing quickens.")
    print("Heart pounding...")
    time.sleep(7)
    print("SKREEEEE.")
    time.sleep(2)
    print("It still sounds far away...")
    time.sleep(5)
    print("1. Run to the captain for help")
    print("2. Look for something to fight with")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        dash()
    elif choice == "2":
        scramble()
    else:
        print("Invalid choice.")
        call_out()


def walk_over():
    pass

def scramble():
    print("\nYou're scared, but something in you is screaming — fight back.")
    print("You look around hastily... fumbling through drawers and scattered junk.")
    time.sleep(5)
    print("SKREEEEEE")
    time.sleep(1)
    print("\nWHAT WAS THAT?!")
    time.sleep(3)
    print("Your heart is pounding so hard, you feel like it's going to burst from your chest.")
    time.sleep(3)
    print("SKREEEEEE")
    time.sleep(1.5)
    print("It's louder this time... closer.")
    time.sleep(2)
    print("You spot a pistol lying on the ground.")
    time.sleep(1)
    print("1. Grab it!")
    time.sleep(3)
    print("2. Why would you look for another option? GRAB IT!")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        dead("You reach for the pistol — fast. But your clammy hands betray you...\n"
             "It slips—\n"
             "SKREEEEEE—")
    elif choice == "2":
        dead("You snatch it up, heart racing... you turn, aim—\n"
             "*Click* *Click*\n"
             "Empty.")
    else:
        print("Invalid choice.")
        scramble()


def dash():
    print("\nYou sprint toward the Captain’s chair — your only hope now.")
    time.sleep(3)
    print("Each footstep echoes like a warning through the hollow ship.")
    time.sleep(3)
    print("You reach out...")
    time.sleep(2)
    print("You spin the chair around—")
    time.sleep(4)
    print("There’s no Captain.")
    time.sleep(2)
    print("There’s half of one.")
    time.sleep(3)
    print("The entire lower half is gone.")
    time.sleep(2)
    print("The uniform is shredded. The upper half slumps forward — lifeless.")
    time.sleep(4)
    print("You stumble back, mouth open, but no sound comes out.")
    time.sleep(4)
    print("You hear it.")
    print("Closer now.")
    time.sleep(2)
    print("SKREEEEEEEEE.")
    time.sleep(3)
    print("1. Dive under the control console")
    print("2. Look for something to fight with")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        dead('You dive under the console...\nYou feel something wet around your thigh...\n'
             'You look — it’s gone.\n"MY LE—"')
    elif choice == "2":
        scramble()
    else:
        print("Invalid choice.")
        dash()




       