import copy
import json

import Vars

def display():
    pieceColour = {
        -2: "\033[0m ",
        -1: "\033[0m  ",
        0: "\033[48;5;234m  \033[0m",
        1: "\033[48;5;220m  \033[0m",
        2: "\033[48;5;45m  \033[0m",
        3: "\033[48;5;208m  \033[0m",
        4: "\033[48;5;20m  \033[0m",
        5: "\033[48;5;160m  \033[0m",
        6: "\033[48;5;40m  \033[0m",
        7: "\033[48;5;63m  \033[0m",
        8: "\033[48;5;238m  \033[0m",
        9: "\033[48;5;248m \033[0m",
    }
    display = [Vars.holdScreen[i] + Vars.screen[i] + Vars.bagScreen[i] for i in range(len(Vars.screen))]

    tl = [[pieceColour[i] for i in n] for n in display]
    ts = '\n'.join(list(map(''.join, tl)))
    
    print('\033[0;0H' + ts)
    # print('\033[0;0H' + '\033[2J' + ts)
    # print(ts)

def game_space():
    Vars.setScreen = [[(0 if i > 5 else -1) for s in range(Vars.width)] for i in range(Vars.height)]
    Vars.screen = copy.deepcopy(Vars.setScreen)
    Vars.holdScreen = [[(-1 if s not in [6] else (9 if i > 5 else -2)) for s in range(7)] for i in range(Vars.height)]
    Vars.bagScreen = [[(-1 if s not in [0] else (9 if i > 5 else -2)) for s in range(7)] for i in range(Vars.height)]

def makeGhostPiece():
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    pieceCoords = [[(8 if i not in [0, -1] else 0) for i in n] for n in pieceCoords]
    Vars.ghostPiecePos = copy.deepcopy(Vars.piecePos)
    newPos = copy.deepcopy(Vars.ghostPiecePos)
    for s in range(len(Vars.setScreen[Vars.ghostPiecePos[0]:len(Vars.screen)-1])):
        safeMove = True
        newPos[0] += 1
        for i in range(4):
            for n in range(4):
                if(pieceCoords[i][n] not in [0, -1]):
                    try:
                        tl = Vars.setScreen[newPos[0]+i][newPos[1]+n]
                        if(tl not in [0, -1]):
                            safeMove = False
                    except: safeMove = False
        if(safeMove): Vars.ghostPiecePos[0] = newPos[0]
        else:
            Vars.ghostPiecePos[0] = newPos[0]-1
            break
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] not in [0, -1]):
                Vars.screen[Vars.ghostPiecePos[0]+i][Vars.ghostPiecePos[1]+n] = pieceCoords[i][n]

def displayQ():
    Vars.bagScreen = [[(-1 if s not in [0] else (9 if i > 5 else -2)) for s in range(7)] for i in range(Vars.height)]
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    for s in range(5):
        pieceCoords = piecesDict[Vars.PieceQ[s]]["N"]
        for i in range(4):
            for n in range(4):
                if(pieceCoords[i][n] not in [0, -1]):
                    Vars.bagScreen[i+(s*4)+6][2+n] = pieceCoords[i][n]