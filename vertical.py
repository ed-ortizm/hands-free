# script for vertical movement
import sys

import pyautogui as ag

y = sys.argv[1]
y = int(y)

ag.move(0, y, duration=1.)
