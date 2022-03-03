import random
import keyboard as kb
import time

import Screen
import Vars
import Controller
import Input

def Update():
    Screen.display()
    key = kb.read_key()
    Input.on_press(key)
    time.sleep(0.05)

def Start():
    Vars.PieceQ = random.sample(Vars.PiecesLst, len(Vars.PiecesLst))
    Screen.game_space()
    Controller.newPiece()