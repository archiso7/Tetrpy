import Controller
from functools import partial

def on_press(key):
    Inputs = {
        "left": partial(Controller.movePiece,[0,-1]), 
        "down": partial(Controller.movePiece,[1,0]), 
        "right": partial(Controller.movePiece,[0,1]), 
        "x": partial(Controller.rotatePiece,1), 
        "z": partial(Controller.rotatePiece,-1),
        "space": Controller.dropPiece,
    }
    if key in ["left", "down", "right", "x", "z", "space"]:
        Inputs[key]()