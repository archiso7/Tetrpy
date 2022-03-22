import json
import copy
from random import randint

import Vars
import Screen

def rotatePiece(direction):
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    rotationLst = ["N", "E", "S", "W"]
    newRot = rotationLst[((rotationLst.index(Vars.PieceRot)+direction) % len(rotationLst))]
    pieceCoords = piecesDict[Vars.Piece][newRot]    
    safeMove = True
    for i in range(4): 
        for n in range(4):
                if pieceCoords[i][n] != 0:
                    try:
                        tl = Vars.setScreen[Vars.piecePos[0]+i][Vars.piecePos[1]+n]
                        if (tl != 0) or (Vars.piecePos[1]+n < 0):
                            safeMove = False
                    except: safeMove = False
    if(safeMove):
        Vars.PieceRot = newRot
    makePiece(Vars.Piece, Vars.PieceRot)

def movePiece(direction):
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    newPos = [x + y for x, y in zip(Vars.piecePos, direction)]
    safeMove = True
    lock = False
    for i in range(4): 
        for n in range(4):
                if pieceCoords[i][n] != 0:
                    try:
                        tl = Vars.setScreen[newPos[0]+i][newPos[1]+n]
                        if (tl != 0) or (newPos[1]+n < 0):
                            safeMove = False
                    except: safeMove = False
                    try:
                        tmp = Vars.setScreen[newPos[0]+i+1]
                        try:
                            if (tmp[newPos[1]+n] != 0):
                                lock = True
                                Vars.locking = True
                        except: pass
                    except:
                        lock = True
                        Vars.locking = True
    if(safeMove): 
        Vars.piecePos = newPos
    makePiece(Vars.Piece, Vars.PieceRot)
    if(lock):
        if Vars.locking:
            Vars.lockTime /= 2
        else:
            Vars.lockTime = 75
        Vars.lockTimer = 1
        startLock()

def makePiece(piece:str, rot):
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[piece][rot]
    Vars.screen = copy.deepcopy(Vars.setScreen)
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] != 0):
                Vars.screen[Vars.piecePos[0]+i][Vars.piecePos[1]+n] = pieceCoords[i][n]
    Screen.makeGhostPiece()
    Screen.display()

def newPiece():
    Vars.lockTimer = 0
    Vars.lockTime = 75
    Vars.piecePos = [1,4]
    Vars.Piece = Vars.PieceQ[0]
    Vars.PieceQ.pop(0)
    Vars.PieceQ.append(Vars.PiecesLst[randint(0, len(Vars.PiecesLst)-1)])
    makePiece(Vars.Piece, Vars.PieceRot)

def lockPiece():
    Vars.lockTime = 75
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    for i in range(4):
        for n in range(4):
            if(pieceCoords[i][n] != 0):
                Vars.setScreen[Vars.piecePos[0]+i][Vars.piecePos[1]+n] = pieceCoords[i][n]
    lineClear()
    newPiece()

def dropPiece():
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    newPos = Vars.piecePos
    for s in range(len(Vars.setScreen[Vars.piecePos[0]:19])):
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
        if(safeMove): Vars.piecePos[0] = newPos[0]
        else:
            Vars.piecePos[0] = newPos[0]-1
            break
    lockPiece()

def lineClear():
    for i in range(len(Vars.setScreen)):
        if 0 not in Vars.setScreen[i]:
            Vars.setScreen.pop(i)
            Vars.setScreen.insert(0, [0 for i in range(Vars.width)])

def holdPiece():
    Vars.PieceRot = "N"
    if(Vars.heldPiece == ""):
        Vars.heldPiece = Vars.Piece
        newPiece()
    else:
        tp = Vars.heldPiece
        Vars.heldPiece = Vars.Piece
        Vars.Piece = tp
        Vars.piecePos = [1,4]
        makePiece(Vars.Piece, Vars.PieceRot)

def startLock():
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    newPos = [x + y for x, y in zip(Vars.piecePos, [1,0])]
    safePlace = False
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] != 0):
                try:
                    tl = Vars.setScreen[newPos[0]+i][newPos[1]+n]
                    if tl != 0:
                        safePlace = True
                except: safePlace = True
    if(Vars.lockTimer > 0) and safePlace:
        if(Vars.lockTimer >= Vars.lockTime):
            Vars.locking = False
            lockPiece()
        else:
            Vars.lockTimer += 1
    else:
        Vars.lockTimer = 0
        Vars.lockTime = 75
        Vars.locking = False