import Controller
from functools import partial
import keyboard as kb

def on_press():
    keyLst = ["left", "down", "right", "x", "z", "c", "space"]
    Inputs = {
        "left": partial(Controller.movePiece,[0,-1]), 
        "down": partial(Controller.movePiece,[1,0]), 
        "right": partial(Controller.movePiece,[0,1]), 
        "x": partial(Controller.rotatePiece,1), 
        "z": partial(Controller.rotatePiece,-1),
        "c": Controller.holdPiece,
        "space": Controller.dropPiece,
    }

    keyPressed = [0 for i in range(len(keyLst))]

    for key in keyLst:
        if kb.is_pressed(key) and (keyPressed[keyLst.index(key)] == 0):
            Inputs[key]()
            keyPressed[keyLst.index(key)] = 1
        else:
            keyPressed[keyLst.index(key)] = 0