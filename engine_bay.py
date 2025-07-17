import time
from captains_quarters import terminal_used
from control_room import control_room
from escape_pod import escape_pod
from game_tools import dead, game_inventory, read_flight_log_25,inspected_paper

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

