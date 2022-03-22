import random

import Screen
import Vars
import Controller
import Input

def Update():
    autoFall()
    Input.on_press()
    Controller.startLock()

def Start():
    Vars.PieceQ = 2*random.sample(Vars.PiecesLst, len(Vars.PiecesLst))
    Screen.game_space()
    Controller.newPiece()

def autoFall():
    if(Vars.fallTimer == 0):
        Controller.movePiece([1,0])
    elif(Vars.fallTimer == Vars.fallTime):
        Vars.fallTimer = -1
    Vars.fallTimer += 1