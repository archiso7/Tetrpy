import Controller
from functools import partial
import keyboard as kb

def on_press():
    Inputs = {
        "left": partial(Controller.movePiece,[0,-1]), 
        "down": partial(Controller.movePiece,[1,0]), 
        "right": partial(Controller.movePiece,[0,1]), 
        "x": partial(Controller.rotatePiece,1), 
        "z": partial(Controller.rotatePiece,-1),
        "c": Controller.holdPiece,
        "space": Controller.dropPiece,
    }
    for key in ["left", "down", "right", "x", "z", "c", "space"]:
        if kb.is_pressed(key):
            Inputs[key]()