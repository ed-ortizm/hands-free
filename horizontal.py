# script for horizontal movement
import sys

import pyautogui as ag

x = sys.argv[1]
x = int(x)

ag.move(x, 0, duration=1.)
