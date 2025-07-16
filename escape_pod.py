import time
from game_tools import dead
from control_room import control_room
# from engine_bay import engine_bay

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
    time.sleep(1.5)
    print("BANG!")
    time.sleep(1.5)
    print("You hear an eerie cry coming from somewhere in the ship . Your heart rate shoots up.")
    time.sleep(2)
    print("You broke the pod door - there's no time to fix it.")
    time.sleep(1)
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

def look_to_hide():
    print("\nYou're heart is racing as you look for a place to hide.")
    time.sleep(2)
    print("The noises are getting louder, whatever is out there is getting closer.")
    time.sleep(2)
    print("You need to find somewhere to hide, the noise is getting louder.")
    time.sleep(1)
    print("1. There's a floor vent — dark, narrow, but maybe safe.")
    print("2. A metal desk with just enough clearance for your body.")
    print("3. A half-open supply closet. You’d have to slam it shut.")

    choice = input("Where will you hide? (1/2/3): ")

    if choice == "1":
        vent_space()
    elif choice == "2":
        dead("You hear something enter the room.\n" \
        "It draws closer...\n" \
        "Suddenly you feel something cold on your chest. You look down...\n" \
        "You seem to be impaled by something, looks like a....")
    elif choice == "3":
        dead("You slammed the closet shut.\n A monster rushes towards the closet, it looks like....!")
    else:
        print("Invalid Choice.")
        look_to_hide()

def prepare():
    print("\nYou're scared but something in you is telling you to defend yourself.")
    print("You look around hastily... fumbling through drawers and junk.")
    time.sleep(5)
    print("SKREEEEEE")
    print("\nWHAT WAS THAT?!")
    time.sleep(3)
    print("You're heart is beating so fast you feel like its going to pop out!")
    time.sleep(3)
    print("SKREEEEEE")
    time.sleep(1.5)
    print("It was louder, closer...")
    time.sleep(2)
    print("You see an emergency ax on the ground.")
    time.sleep(1)
    print("1. Grab it!")
    time.sleep(3)
    print("2. Why would you look for another option. GRAB IT!")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        dead("You try to grab it!... but due to how fast your heart was racing you failed to notice how clammy your hands got...\n" \
        "It slips-\n" \
        "SKREEEEEE-")
    elif choice == "2":
        dead("Due to you indecisiveness, well... we all know what happens here. Trust your gut next time.")
    else:
        print("Invalid Choice.")
        prepare()


def find_item():
    print("\nYou start to think of how you can dislodge whatever is holding the door.")
    print("For some reason... you're calm?")
    time.sleep(3)
    print("You start to wonder...")
    time.sleep(2)
    print("Why am I calm?")
    time.sleep(5)
    print("Wait — where is everyone?")
    time.sleep(1)
    print("Is this why I'm so calm?...")
    time.sleep(5)
    print("For now, you focus on the problem at hand. You look around.")
    time.sleep(3)
    print("You see a metal pole nearby — could be just right.")
    print("You grab it, and try...")
    print("1. Carefully dislodge the item and open the escape pod.")
    print("2. Call out first... then try, banging the pole in the process.")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        inspect_pod()
    elif choice == "2":
        dead('You yell out, "HELLO!"...\n'
             'You manage to dislodge the item — but the noise masks something else.\n'
             'You turn back to call out once more...\n'
             '"HELL—"')
    else:
        print("Invalid Choice.")
        find_item()

def inspect_pod():
    print("\nYou’ve managed to dislodge the item. You begin to open the pod when it... squeaks.")
    print("You immediately freeze.")
    time.sleep(5)
    print("SKREEEEEEEE")
    time.sleep(5)
    print("You wonder what that could be — oddly, you're still calm.")
    time.sleep(3)
    print("SKREEEEEEEE...")
    time.sleep(3)
    print("It’s getting louder. You have to decide:")
    print("1. Hide inside the pod")
    print("2. Find somewhere else to hide")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        enter_pod()
    elif choice == "2":
        look_to_hide()
    else:
        print("Invalid Choice.")
        inspect_pod()


def enter_pod():
    print("\nYou manage to enter the pod and close the door... Wait...")
    time.sleep(5)
    print("It won't latch...")
    time.sleep(5)
    print("You start to hear noises outside the pod, in the room.")
    time.sleep(6)
    print("That calmness you had...")
    time.sleep(6)
    print("Is fading...")
    time.sleep(6)
    print("Heart racing...")
    time.sleep(6)
    print("1. Wait it out as long as you can?")
    print("2. Make a run for it?")
    time.sleep(3)
    print("tick tock...")
    time.sleep(4)
    print("tick tock...")
    time.sleep(4)

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\nYou thought you would be safe...")
        time.sleep(3)
        print("The door rips off the hinges, metal screams, and your eyes meet—")
        time.sleep(3)
        dead("IS THA—\n\nDid you choose the right starting route?\nChoices have consequences...")
    elif choice == "2":
        print("\nYou hesitate...")
        time.sleep(2)
        print("Noises getting louder...")
        time.sleep(2)
        dead("SKREEE—")
    else:
        print("Invalid Choice.")
        enter_pod()




def vent_space():
    print("\nYou manage to get into the vent space. You hear sounds in the room above, but can't see anything...")
    time.sleep(3)
    print("It's dark...")
    time.sleep(3)
    print("Dusty...")
    time.sleep(3)
    print("And cold down here.")
    print("Should you stay and wait, or try to move on?")
    print("1. Stay still and wait out whatever is making noise.")
    print("2. Move down the vent path.")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        dead("You try to remain still...\n" \
        "waiting...\n" \
        "you feel air on your neck?...\n" \
        "No, not air... You feel death...")
    elif choice == "2":
        dead("\nYou move along the vent tunnels, still hearing the sound in the room you left.\n" \
        "maybe you're safe...\n You turn the corner... WHAT IS Tha-")
    else:
        print("Invalid Choice")
        vent_space()