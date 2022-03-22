import copy
import json

import Vars

def display():
    pieceColour = {
        0: "\033[48;5;235m  \033[0m",
        1: "\033[48;5;220m  \033[0m",
        2: "\033[48;5;45m  \033[0m",
        3: "\033[48;5;208m  \033[0m",
        4: "\033[48;5;20m  \033[0m",
        5: "\033[48;5;160m  \033[0m",
        6: "\033[48;5;40m  \033[0m",
        7: "\033[48;5;63m  \033[0m",
        8: "\033[48;5;248m  \033[0m",
    }
    tl = [[pieceColour[i] for i in n] for n in Vars.screen]
    ts = '\n'.join(list(map(''.join, tl)))
    print('\033[0;0H' + ts)
    #print('\033[2J' + '\033[0;0H' + ts)
    #print(ts)

def game_space():
    Vars.setScreen = [[0 for i in range(Vars.width)] for i in range(Vars.height-5)]
    Vars.screen = copy.deepcopy(Vars.setScreen)

def makeGhostPiece():
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    pieceCoords = [[(8 if i != 0 else 0) for i in n] for n in pieceCoords]
    Vars.ghostPiecePos = copy.deepcopy(Vars.piecePos)
    newPos = copy.deepcopy(Vars.ghostPiecePos)
    for s in range(len(Vars.setScreen[Vars.ghostPiecePos[0]:19])):
        safeMove = True
        newPos[0] += 1
        for i in range(4):
            for n in range(4):
                if(pieceCoords[i][n] != 0):
                    try:
                        tl = Vars.setScreen[newPos[0]+i][newPos[1]+n]
                        if(tl != 0):
                            safeMove = False
                    except: safeMove = False
        if(safeMove): Vars.ghostPiecePos[0] = newPos[0]
        else:
            Vars.ghostPiecePos[0] = newPos[0]-1
            break
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] != 0):
                Vars.screen[Vars.ghostPiecePos[0]+i][Vars.ghostPiecePos[1]+n] = pieceCoords[i][n]
    # display()