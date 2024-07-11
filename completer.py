import os
import random
import sys

import pygame
import pygetwindow as gw

from directkeys import *

__version__ = "1.0.0"

strafe_time = 3

sound_directory = 'sounds'
finishing_sounds = [
    os.path.join(sound_directory, 'finished.mp3'),
    os.path.join(sound_directory, 'finished1.mp3'),
    os.path.join(sound_directory, 'finished2.mp3'),
    os.path.join(sound_directory, 'finished3.mp3'),
    os.path.join(sound_directory, 'finished4.mp3')
]


def main():
    if "--version" in sys.argv:
        print(__version__)
        return
    print("Running application version", __version__)
    try:
        window_setup()

        while True:
            bring_window_to_front("Lake Isabella Gold Getter")

            need_tutorial()

            start_again_test()

    except Exception as e:
        print(f"FATAL ERROR! Error Message: {e}")


def window_setup():
    ctypes.windll.kernel32.SetConsoleTitleW("Lake Isabella Gold Getter")
    time.sleep(1)
    os.system("cls")


def main_run():
    chest_amount = get_chest_amount()

    display_approx_time(chest_amount)

    get_user_ready()

    do_glitch(chest_amount)

    finished_message()
    return chest_amount


def get_chest_amount():
    while True:
        try:
            chest_amount = int(input("How many chests' worth? (100 Max): "))
            if 1 <= chest_amount <= 100:
                return chest_amount
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def display_approx_time(chest_amount):
    approx_time = chest_amount * (strafe_time * 2)
    print(f"Total time approx: {approx_time}secs | {round(approx_time / 60, 1)}mins")


def get_user_ready():
    input("Press ENTER when you are in position in-game.")
    print("Switching to RDR2 in 5 seconds..")
    print("----------------------------------------------------------------------------------------------------")
    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)
    bring_window_to_front("Red Dead Redemption 2")
    time.sleep(1)


def do_glitch(chest_amount):
    for i in range(chest_amount):
        PressKey(DIK_A)
        time.sleep(strafe_time)
        ReleaseKey(DIK_A)
        PressKey(DIK_D)
        time.sleep(strafe_time - 0.2)
        ReleaseKey(DIK_D)
        print(f"{i + 1} treasure(s) generated.")


def finished_message():
    bring_window_to_front("Lake Isabella Gold Getter")
    print("----------------------------------------------------------------------------------------------------")
    print("Successfully got your gold!")
    print("----------------------------------------------------------------------------------------------------")
    time.sleep(0.3)
    play_sound(resource_path(pick_random_sound()))


def start_again_test():
    redo_answer = input("Go again? (y/n): ")
    if redo_answer == "y" or redo_answer == "Y":
        print("Restarting...")
        time.sleep(0.5)
        os.system("cls")
    elif redo_answer == "n" or redo_answer == "N":
        print("See you soon!")
        time.sleep(0.3)
        sys.exit()
    else:
        print("Unrecognised answer, quitting anyway!")
        time.sleep(0.3)
        sys.exit()


def need_tutorial():
    tutorial_answer = input("Do you need a full run down of the glitch? (y/n): ")
    if tutorial_answer == "y" or tutorial_answer == "Y":
        input("\nRequirements: \n-1 Friend to go AFK\n-1 Other map that is not Lake Isabella\n-At least 1 "
              "Dynamite\nPress ENTER when finished with each step.")
        input("\nStep 1: Go to Lake Isabella (North West from Valentine)")
        input("\nStep 2: Open your Lake Isabella Treasure Map\nWe want the chest to spawn in the middle of the frozen "
              "lake\nIt should be just next to a large rock\n(If it does not spawn where we want, open another map "
              "and then Lake Isabella again, repeat till correct Location)")
        print("\n**YOU NEED YOUR FRIEND TO BE STOOD WITHIN 20 PACES OF THE CHEST, THEY CAN STILL FISH ETC**\n**"
              "THEY MUST REMAIN CLOSE TO THE CHEST**")
        input("\nStep 3: Equip Dynamite, walk in to the front of the chest (So your legs are touching it)\nThen without"
              " aiming, press your 'Shoot' button to place Dynamite on the front of the chest\nWalk a few steps away "
              "and shoot the Dynamite")
        input("\nStep 4: You should be facing the chest with the large rock behind it, from here do a 180\nLeave your "
              "friend by the chest and walk about 30-40 paces down the frozen lake\nYou should see a small rock and "
              "tree towards the edge of the lake")
        input("\nStep 5: Go in to 1st Person and equip any weapon, you should see the grey reticle in the middle of "
              "your screen\nNow standing just towards the edge of the lake, line up your reticle to the middle of "
              "the tree trunk.\nOn your map, the arrow for North should be in-line with the top right of the Health "
              "Bar Circle")
        input("\nStep 5a: Now we decide how much treasure you want! (The following is the normal program)")

    print("")
    chest_amount = main_run()

    if tutorial_answer == "y" or tutorial_answer == "Y":
        input("\nStep 7: Now walk back over to the chest. DO NOT OPEN IT")
        input("\nStep 8: Open another map (This lets you keep the Lake Isabella map)")
        input("\nStep 9: Now collect treasure (use this tool)")
        collect_treasure(chest_amount)
        input("\n*OPTIONAL* Just after taking the last treasure, quickly disconnect"
              " from internet or shutdown your game\nLaunch Red Dead again and you will see the treasure is in the "
              "same location ready to rinse again!\n")
    else:
        collect_treasure(chest_amount)


def collect_treasure(chest_amount):
    input("\nPress ENTER when you are in front of the chest, with the 'R' to collect option.")
    print("Switching to RDR2 in 5 seconds..")
    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)
    bring_window_to_front("Red Dead Redemption 2")
    time.sleep(1)
    for i in range(chest_amount):
        PressKey(DIK_R)
        time.sleep(strafe_time)
        ReleaseKey(DIK_R)
        time.sleep(0.5)
        print(f"{i + 1} treasure(s) collected.")
    bring_window_to_front("Lake Isabella Gold Getter")
    play_sound(resource_path(pick_random_sound()))
    print("All your treasure chest's have been collected!\n")


def bring_window_to_front(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)
        # noinspection PySimplifyBooleanCheck
        if window != []:
            try:
                window[0].activate()
                # print("Brought '", window_title, "' to the Front.")
            except Exception as e:
                print(f"Error: {e}")
                window[0].minimize()
                window[0].restore()
                # print("Brought '", window_title, "' to the Front.")
        else:
            print("Window not found.")
    except Exception as e:
        print(f"Error: {e}")


def resource_path(relative_path):
    try:
        # noinspection PyProtectedMember
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def pick_random_sound():
    return random.choice(finishing_sounds)


def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


if __name__ == "__main__":
    main()
