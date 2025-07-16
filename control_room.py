import time
from game_tools import dead
from escape_pod import escape_pod

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
    print("\nYou take in the state of the room, wondering why the Captain hasn’t moved.")
    time.sleep(3)
    print('You whisper, "Captain Dairus?"...')
    time.sleep(6)
    print("Wait — why did you whisper?")
    time.sleep(5)
    print("Something inside you feels wrong. You instinctively knew not to make noise.")
    time.sleep(6)
    print("Slowly, you walk over to the chair...")
    time.sleep(5)
    print("There’s no Captain.")
    time.sleep(2)
    print("There’s half of one.")
    time.sleep(3)
    print("The entire lower half is gone.")
    time.sleep(2)
    print("The uniform is shredded. The upper half slumps forward — lifeless.")
    time.sleep(4)
    print("You stumble back, mouth open, but no sound comes out.")
    time.sleep(5)
    print("1. Take a moment to examine what’s left of the Captain.")
    print("2. Run out screaming.")
    print("3. Hurry to the escape pod.")

    choice = input("What will you do? (1/2/3): ")

    if choice == "1":
        examine()
    elif choice == "2":
        run_out()
    elif choice == "3":
        escape_pod()
    else:
        print("Invalid choice.")
        walk_over()


def run_out():
    print("\nYou turn and bolt out of the control room — panic drowning all sense of reason.")
    time.sleep(3)
    print("You crash into a console, knocking it over. A metal tray clatters across the floor.")
    time.sleep(4)
    print("Heart racing. Breathing erratic. You don't even know where you're running.")
    time.sleep(4)
    print("What happened to the Captain?")
    time.sleep(2)
    print("What is going on?!")
    time.sleep(3)
    print("You hear it.")
    print("Somewhere behind you.")
    time.sleep(2)
    print("What is that sound?")
    time.sleep(2)
    print("You keep running — past flickering lights, overturned crates, leaking vents.")
    time.sleep(4)
    print("You think of the escape pod.")
    time.sleep(2)
    print("But instinct? Gone.")
    time.sleep(2)
    print("Calm? Gone.")
    time.sleep(2)
    print("You've made too much noise.")
    time.sleep(3)
    print("Something is coming.")
    time.sleep(2)
    print("You try to go faster — but the hallway begins to spin...")
    time.sleep(4)
    print("Why does it feel like you're falling?")
    time.sleep(3)
    print("Wait...")
    print("Why are you seeing the hallway from the floor?")
    time.sleep(4)
    print("Your body collapses just ahead of you.")
    time.sleep(3)
    print("Everything goes black.")
    time.sleep(3)
    dead()


def examine():
    print("\nSomething tells you to remain calm and figure out what’s going on.")
    print("For the first time since waking up, your mind feels... clear.")
    time.sleep(3)
    print("You lean over the Captain’s body.")
    time.sleep(7)
    print("You find nothing...")
    time.sleep(5)
    print("Is that doubt creeping in?")
    time.sleep(5)
    print("Then you notice — the Captain is holding something.")
    time.sleep(6)
    print('"Cheryl2042"...')
    time.sleep(6)
    print("Who is Cheryl?")
    time.sleep(2)
    print("1. Why does that matter? Toss the paper and go to the escape pod.")
    print("2. Take a moment to think about this logically.")
    print("3. Toss the paper and head to the engine bay.")

    choice = input("What will you do? (1/2/3): ")

    if choice == "1":
        escape_pod()
    elif choice == "2":
        take_time()
    elif choice == "3":
        engine_bay()
    else:
        print("Invalid choice.")
        examine()

def take_time():
    print("\nYou stare at the paper, thinking... wondering... Who is Cheryl?")
    time.sleep(2)
    print("Does that really matter?... No.")
    time.sleep(2)
    print("What matters is what it means.")
    time.sleep(6)
    print("You walk over to the small window that looks out into space.")
    time.sleep(3)
    print("Have we not reached our destination yet?")
    time.sleep(2)
    print("Wait... why am I even awake? Shouldn’t I be in cryo sleep?")
    time.sleep(7)
    print("You let the paper slip from your fingers.")
    print("You’re not ready for the answers — not yet.")
    time.sleep(3)
    print("Maybe it’s time to figure out what really happened.")
    time.sleep(3)
    print("1. Look for a working terminal")
    print("2. Go to the Captain’s quarters")
    print("3. Investigate the rest of the ship")

    choice = input("What’s the sensible thing to do? (1/2/3): ")

    if choice == "1":
        find_terminal()
    elif choice == "2":
        captains_quarters()
    elif choice == "3":
        investigate()
    else:
        print("Invalid choice.")
        take_time()

def find_terminal():
    print("\nYou scan the control room, looking for a terminal that isn’t broken.")
    time.sleep(3)
    print("One catches your eye — the screen is black, but something’s different.")
    time.sleep(3)
    print("It’s on. The backlight is faint, but... alive.")
    time.sleep(3)
    print("You tap the keyboard, trying to wake it.")
    time.sleep(3)
    print("You smack the side — a small stack of items clatters to the floor.")
    print("The terminal flickers to life!")
    time.sleep(3)
    print("That nostalgic boot-up chime plays.")
    time.sleep(3)
    print("SKREEEEE.")
    time.sleep(3)
    print("Wait... that’s not the terminal.")
    time.sleep(3)
    print("The screen flashes: ACCESS NOT GRANTED.")
    time.sleep(3)
    print("Not granted!? What the hell?!")
    time.sleep(3)
    print("You start hammering keys, trying to bypass the block — nothing works.")
    time.sleep(3)
    print("Out of pure frustration, you slap the terminal.")
    time.sleep(3)
    print("Hard.")
    time.sleep(2)
    print("It tips off the console and crashes to the floor.")
    time.sleep(3)
    print("BAM.")
    time.sleep(2)
    print("CLANG.")
    time.sleep(2)
    print("EEEEEIIIIIR.")
    time.sleep(3)
    print("SKREEEEEEEEE.")
    time.sleep(3)
    print("Wait... that wasn’t the terminal.")
    time.sleep(3)
    print("You step cautiously toward the doorway...")
    time.sleep(3)
    dead("Before you even knew what happened, your body split clean down the middle.\n"
         "Something was behind you the entire time.\n"
         "But how?... Choices. Choices.")


def investigate():
    print("\nYou leave the control room, stepping into the corridor.")
    time.sleep(3)
    print("The lights flicker, casting long shadows across the floor.")
    time.sleep(3)
    print("You think about checking the cargo bay, or maybe engineering...")
    time.sleep(3)
    print("A distant hissing sound echoes — maybe a vent. Maybe not.")
    time.sleep(4)
    print("You move slowly, carefully — but your foot catches on a loose cable.")
    time.sleep(3)
    print("You stumble forward — and everything turns sideways.")
    time.sleep(2)
    print("A split-second of disorientation...")
    time.sleep(2)
    print("Then pain.")
    time.sleep(2)
    print("Warmth across your chest.")
    time.sleep(3)
    print("You look down — something’s sticking out of you.")
    time.sleep(4)
    print("You didn’t even see it.")
    time.sleep(2)
    print("You collapse.")
    time.sleep(2)
    print("There’s no time to scream.")
    time.sleep(3)
    dead("The ship stays silent. Whatever waits in the dark didn’t even have to try.")



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




       