from configuration import *
import pyautogui as gui
from os import listdir, remove, replace, makedirs
from os.path import isfile, join, exists
import shutil
from time import sleep

gui.PAUSE = 2  # units: seconds


### pygui clicks ###
# click csv option only once
def first_step():
    sleep(inicial_sleep)
    back(6)  # go to beginning
    # set csv option once
    gui.click(x=screen_dict['action_0'][0], y=screen_dict['action_0'][1])  # click fold description (column #1 / left)
    gui.click(x=screen_dict['csv_option'][0], y=screen_dict['csv_option'][1])  # csv option
    gui.click(x=screen_dict['save_as_text'][0], y=screen_dict['save_as_text'][1])  # text-bar
    gui.typewrite('csv_test')  # typewrite file name
    gui.press('enter')  # enter
    # delete test range and all hands from monker ranges
    monker_hands = [f for f in listdir(monker_Path) if isfile(join(monker_Path, f))]
    for monker_hand_file in monker_hands:
        remove(monker_Path / monker_hand_file)  # delete hands


def back(clicks):
    for click in range(clicks):
        gui.click(x=screen_dict["res_1"][0], y=screen_dict["res_1"][1])


def fold(clicks):
    for click in range(clicks):
        gui.click(x=screen_dict["res_2"][0], y=screen_dict["res_2"][1])


def enter_search_syntax(_suit_value):
    gui.click(x=screen_dict['search_area'][0],
              y=screen_dict['search_area'][1])  # click in search bar at bottom of screen
    gui.hotkey('ctrl', 'a')  # select-all
    gui.typewrite(_suit_value)  # typewrite ppt rank and suit components
    sleep(load_sleep)


def save_to_monker(_suit_key, _actions):
    for i in range(_actions):
        gui.click(x=screen_dict['action_' + str(i)][0],
                  y=screen_dict['action_' + str(i)][1])  # click pot description (column #3 / right)
        gui.click(x=screen_dict['include_0_hands'][0], y=screen_dict['include_0_hands'][1])
        gui.press('tab')
        gui.typewrite(str(i) + '_' + _suit_key)  # typewrite file name
        gui.press('enter')  # enter
        sleep(save_sleep)


def move_to_tree(_seat, _suit_dic_key, _suit_key):
    move_to = base_Path / _seat / _suit_dic_key / _suit_key
    if not exists(move_to):  # if path not exist then make it
        makedirs(move_to)
    files = [f for f in listdir(monker_Path) if isfile(join(monker_Path, f))]  # list files in monker directory
    for f in files:  # move each file
        replace(monker_Path / f, move_to / f)
