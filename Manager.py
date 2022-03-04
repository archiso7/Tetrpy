import random
import time

import Screen
import Vars
import Controller
import Input

def Update():
    #Screen.display()
    Input.on_press()
    time.sleep(0.05)

def Start():
    Vars.PieceQ = random.sample(Vars.PiecesLst, len(Vars.PiecesLst))
    Screen.game_space()
    Controller.newPiece()