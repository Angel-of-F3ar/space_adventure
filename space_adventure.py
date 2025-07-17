import time
from game_tools import *
from captains_logs import logs
from flight_logs import flight_logs

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


def engine_bay():
    global terminal_used

    if terminal_used:
        print("\nYou cautiously walk into the engine bay.")
        print("You know there are two creatures lurking around the ship.")
        time.sleep(6)
        print("It seems like the Captain was already preparing everything to escape.")
        time.sleep(5)
        print("You should get the lights working.")
        time.sleep(3)
    else:
        print("\nYou step into the engine bay. Something creaks behind you...")
        time.sleep(3)
        print("Why did you come here?")
        print("Wouldn't escaping have made more sense?")
        time.sleep(5)
        print("Still... something draws you in.")
        time.sleep(6)
        print("It feels off. Like you're being watched.")
        time.sleep(4)

    print("\nWhat will you do?")
    print("1. Go to the Control Room.")
    print("2. Go to the Escape Pods.")
    print("3. Look around.")

    # Show Option 4 only if terminal was used and flight log 25 was read
    if terminal_used and read_flight_log_25:
        print("4. Work on the access conduit panel E-14.")

    # Show Option 5 only if player has the paper
    if terminal_used and "paper" in game_inventory:
        print("5. Inspect the paper from the control room.")

    choice = input("Choose an option (1-3" +
                   ("/4" if terminal_used and read_flight_log_25 else "") +
                   ("/5" if terminal_used and "paper" in game_inventory else "") +
                   "): ")

    if choice == "1":
        control_room()
    elif choice == "2":
        escape_pod()
    elif choice == "3":
        look_around()
    elif choice == "4" and terminal_used and read_flight_log_25:
        work_on_panel()
    elif choice == "5" and terminal_used and "paper" in game_inventory:
        inspect_paper()
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


def inspect_paper():
    global inspected_paper

    print("\nYou unfold the crumpled piece of paper again, hands trembling slightly.")
    time.sleep(3)
    print("You flip it over... there's something scrawled on the back.")
    time.sleep(3)
    print("A code — six digits. Smudged, but still readable.")
    time.sleep(2)
    print("695204")
    time.sleep(3)
    print("You stare at it for a moment, heart racing.")
    time.sleep(3)
    print("This has to be the access code the Captain mentioned in his logs.")
    time.sleep(3)
    print("The way out… it’s finally possible.")
    time.sleep(3)

    inspected_paper = True

    if read_flight_log_25:
        print("You glance at the panel across the room. Time to reroute power — if you remember the steps.")
        time.sleep(3)

    print("\n1. Look around.")
    if read_flight_log_25:
        print("2. Work on the access conduit panel E-14.")

    choice = input("What will you do? (1" + ("/2" if read_flight_log_25 else "") + "): ")

    if choice == "1":
        look_around()
    elif choice == "2" and read_flight_log_25:
        work_on_panel()
    else:
        print("Invalid choice.")
        inspect_paper()

def work_on_panel():
    global inspected_paper  

    print("\nYou kneel before the access conduit panel E-14.")
    time.sleep(3)
    print("Wires hang loose, sparking softly. The diagnostics screen is dark but responsive.")
    time.sleep(3)
    print("You remember the procedure from Flight Log 25... rerouting power should bring the systems back online.")
    time.sleep(4)

    print("You begin rerouting circuits... fingers working quickly, heart pounding.")
    time.sleep(3)
    print("One wrong move and you could fry the entire console.")
    time.sleep(3)

    print("Reconnecting power lines... bypassing breaker node...")
    time.sleep(2)
    print("Overriding backup relay...")
    time.sleep(2)

    print("*BZZZZZZZT*")
    print("The screen flickers... and then—")
    time.sleep(2)
    print("Lights flood the engine bay, buzzing and humming back to life.")
    time.sleep(2)

    print("But the sound… the sound wakes something up.")
    time.sleep(3)
    print("A figure rises from the shadows — its features shifting, reshaping...")
    time.sleep(3)
    print("It's... your husband. At least, it looks like him.")
    time.sleep(3)
    print("But you *know* he's gone. This thing is not him.")
    time.sleep(3)

    print("\nA keypad screen near the sealed vault lights up.")
    print("It’s now or never.")

    print("1. Stare at the creature.")
    print("2. Run to the keypad.")

    choice = input("What will you do? (1/2): ")

    if choice == "1":
        dead("You freeze, eyes locked on the thing that wears your husband's face.\n" \
             "It smiles — not kindly. You're too late.")
    elif choice == "2":
        if inspected_paper:
            print("\nYou sprint to the keypad, hands shaking as you enter the code...")
            time.sleep(2)
            print("6... 9... 5... 2... 0... 4")
            time.sleep(2)
            print("*Access Granted*")
            time.sleep(2)
            print("The vault door hisses and slides open. You're in.")
            time.sleep(2)
            final_room()
        else:
            dead("You reach the keypad — but your mind blanks.\n" \
                 "No code. No time.\n" \
                 "You hear it charge. Then nothing.")
    else:
        print("Invalid choice.")
        work_on_panel()

def final_room():
    global inspected_paper

    print("\nThe access panel blinks green. The door hisses open.")
    time.sleep(3)
    print("You stumble inside, sealing it shut behind you.")
    time.sleep(3)
    print("The hum of the engine core surrounds you... but it’s not the only sound.")
    time.sleep(4)
    print("Your breath catches in your throat.")
    time.sleep(5)
    print("“Why are you running from me?” it whispers, voice almost tender.")
    time.sleep(5)

    if "fob" not in game_inventory:
        print("You reach for the console... but it won’t respond.")
        time.sleep(3)
        print("It needs the captain’s fob.")
        time.sleep(3)
        print("The creature gets in. You don’t even have time to scream.")
        dead("Somewhere deep in the ship, the engines begin to die down... again.")
        return

    print("Your hand trembles as you hold up the captain’s fob.")
    time.sleep(3)
    print("The launch interface flickers to life.")
    time.sleep(3)
    print("Two coordinates are preloaded — Earth… and Sucaytre, the colony planet.")
    time.sleep(4)
    print("“Come home,” it says again, in his voice.")
    time.sleep(3)
    print("You make your choice.")

    print("\n1. Set course for Earth.")
    print("2. Set course for Sucaytre.")

    choice = input("Where will you go? (1/2): ")

    if choice == "1":
        print("\nYou punch in Earth’s coordinates.")
        time.sleep(3)
        print("Engines roar to life. The ship jerks forward.")
        time.sleep(3)
        print("But something’s wrong. Systems blink. Warning lights flash red.")
        time.sleep(3)
        print("A hull breach — silent, invisible.")
        time.sleep(4)
        print("You never even see the stars again.")
        dead("No one returns to Earth.")
    elif choice == "2":
        print("\nYou override the default and choose Sucaytre.")
        time.sleep(3)
        print("Engines whine, then stabilize.")
        time.sleep(3)
        print("The creature slams against the sealed glass behind you, snarling — no longer pretending.")
        time.sleep(4)
        print("You don’t look back.")
        time.sleep(3)
        print("Stars stretch into lines as you slip into jump speed...")
        time.sleep(5)
        print("\n\nTo be continued.")
    else:
        print("Invalid choice.")
        final_room()

def control_room():
    global terminal_used

    if terminal_used:
        print("\nYou return to the control room.")
        time.sleep(3)
        print("Something's... off.")
        time.sleep(3)
        print("The captain’s body is gone.")
        time.sleep(3)

        if "paper" not in game_inventory:
            print("You notice a crumpled piece of paper under the terminal — the one you dropped earlier.")
            time.sleep(3)
            print("You pick it up and tuck it away.")
            game_inventory.append("paper")
        else:
            print("Nothing else catches your attention.")
        time.sleep(3)

    else:
        print("\nYou stumble deeper into the room... it's eerily quiet.")
        time.sleep(3)
        print("Dust clings to shattered monitors and rusted consoles.")
        time.sleep(3)
        print("You scan the room and freeze.")
        time.sleep(3)
        print("A figure sits slumped in the captain’s chair — motionless.")
        time.sleep(3)
        print("Wait... is that—CAPTAIN?!")
        time.sleep(4)

    
    print("1. Call out to the Captain")
    print("2. Walk up and turn the chair around")
    
    if terminal_used:
        print("3. Head to the Engine Bay")

    choice = input("What do you do? (1/2" + ("/3" if terminal_used else "") + "): ")

    if choice == "1":
        call_out()
    elif choice == "2":
        walk_over()
    elif choice == "3" and terminal_used:
        engine_bay()
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

terminal_used = False

def captains_quarters():
    global terminal_used

    print("\nYou enter the captains quartes.")
    time.sleep(5)

    if terminal_used:
        print("The terminal screen is dark now. Unresponsive.")
        if "fob" not in game_inventory:
            print("You glance at the bed... the fob is gone.")
        else:
            print("Nothing else left to do here.")
        return

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
            flight_log_access()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid Choice.")

#============ This part happens AFTER exiting the terminal ============
    global terminal_used
    terminal_used = True

    print("\nYou step away from the terminal.")
    time.sleep(2)

    if "fob" not in game_inventory:
        print("You glance at the bed... the fob is gone.")
    else:
         print("The room feels quieter now. Almost too quiet.")

    time.sleep(3)
    print("\nWhat now?")
    print("1. Go to the control room.")
    print("2. Head toward the engine bay.")

    next_choice = input("Where will you go? (1/2/3): ")

    if next_choice == "1":
        control_room()
    elif next_choice == "2":
        engine_bay()
    else:
        print("Invalid choice.")


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
        terminal_unlocked = True  
    else:
        terminal_unlocked = False


def flight_log_access():
    global read_flight_log_25
    read_logs = set()

    while True:
        print("\n--- Flight Logs ---")
        for log_title in flight_logs:
            status = "(READ)" if log_title in read_logs else ""
            print(f"{log_title} {status}")

        print("Type the log name (e.g., 'Flight Log 21') to read it or type 'exit' to leave.")
        choice = input("Your choice: ")

        if choice.lower() == "exit":
            print("You exit the flight logs.")
            break
        elif choice in flight_logs:
            print(f"\n{flight_logs[choice]}\n")
            read_logs.add(choice)
            time.sleep(2)

            if choice == "Flight Log 25":
                read_flight_log_25 = True
        else:
            print("Invalid choice.")        

#Start the game
if __name__ == "__main__":
    intro()