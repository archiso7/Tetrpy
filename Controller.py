import json
import copy
from random import sample
import sys

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
                if pieceCoords[i][n] not in [0, -1]:
                    try:
                        tl = Vars.setScreen[Vars.piecePos[0]+i][Vars.piecePos[1]+n]
                        if (tl not in [0, -1]) or (Vars.piecePos[1]+n < 0):
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
                if pieceCoords[i][n] not in [0, -1]:
                    try:
                        tl = Vars.setScreen[newPos[0]+i][newPos[1]+n]
                        if (tl not in [0, -1]) or (newPos[1]+n < 0):
                            safeMove = False
                    except: safeMove = False
                    try:
                        tmp = Vars.setScreen[newPos[0]+i+1]
                        try:
                            if (tmp[newPos[1]+n] not in [0, -1]):
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
            Vars.lockTime = 50
        Vars.lockTimer = 1
        startLock()

def makePiece(piece:str, rot):
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[piece][rot]
    Vars.screen = copy.deepcopy(Vars.setScreen)
    Screen.makeGhostPiece()
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] not in [0, -1]):
                Vars.screen[Vars.piecePos[0]+i][Vars.piecePos[1]+n] = pieceCoords[i][n]
    Screen.display()

def newPiece():
    Vars.lockTimer = 0
    Vars.lockTime = 50
    Vars.piecePos = [0,4]
    Vars.Piece = Vars.PieceQ[0]
    Vars.PieceQ.pop(0)
    if(len(Vars.PieceQ) == 7):
        Vars.PieceQ += sample(Vars.PiecesLst, len(Vars.PiecesLst))
    Screen.displayQ()
    makePiece(Vars.Piece, Vars.PieceRot)

def lockPiece():
    Vars.lockTime = 50
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    for i in range(4):
        for n in range(4):
            if(pieceCoords[i][n] not in [0, -1]):
                Vars.setScreen[Vars.piecePos[0]+i][Vars.piecePos[1]+n] = pieceCoords[i][n]
    lineClear()
    if(Vars.piecePos[0] < 6):
        sys.exit()
    newPiece()

def dropPiece():
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    newPos = Vars.piecePos
    for s in range(len(Vars.setScreen[Vars.piecePos[0]:len(Vars.screen)-1])):
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
        if(safeMove): Vars.piecePos[0] = newPos[0]
        else:
            Vars.piecePos[0] = newPos[0]-1
            break
    lockPiece()

def lineClear():
    for i in range(len(Vars.setScreen)):
        if 0 not in Vars.setScreen[i] and -1 not in Vars.setScreen[i]:
            Vars.setScreen.pop(i)
            Vars.setScreen.insert(6, [0 for i in range(Vars.width)])

def holdPiece():
    Vars.PieceRot = "N"
    Vars.holdScreen = [[(-1 if s not in [6] else (9 if i > 5 else -2)) for s in range(7)] for i in range(Vars.height)]
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece]["N"]
    for i in range(4):
        for n in range(4):
            if(pieceCoords[i][n] not in [0, -1]):
                Vars.holdScreen[i+6][1+n] = pieceCoords[i][n]
    if(Vars.heldPiece == ""):
        Vars.heldPiece = Vars.Piece
        newPiece()
    else:
        tp = Vars.heldPiece
        Vars.heldPiece = Vars.Piece
        Vars.Piece = tp
        Vars.piecePos = [0,4]
        makePiece(Vars.Piece, Vars.PieceRot)

def startLock():
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    newPos = [x + y for x, y in zip(Vars.piecePos, [1,0])]
    safePlace = False
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] not in [0, -1]):
                try:
                    tl = Vars.setScreen[newPos[0]+i][newPos[1]+n]
                    if tl not in [0, -1]:
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
        Vars.lockTime = 50
        Vars.locking = False