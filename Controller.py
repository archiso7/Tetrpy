import json
import copy
from random import randint
import time

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
        time.sleep(1)
        Vars.locking = False
        lockPiece()

def makePiece(piece:str, rot):
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[piece][rot]
    Vars.screen = copy.deepcopy(Vars.setScreen)
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] != 0):
                Vars.screen[Vars.piecePos[0]+i][Vars.piecePos[1]+n] = pieceCoords[i][n]
    Screen.display()

def newPiece():
    Vars.piecePos = [1,4]
    Vars.Piece = Vars.PieceQ[0]
    Vars.PieceQ.pop(0)
    Vars.PieceQ.append(Vars.PiecesLst[randint(0, len(Vars.PiecesLst)-1)])
    makePiece(Vars.Piece, Vars.PieceRot)

def lockPiece():
    pieceStr = open("Pieces.json")
    piecesDict = json.load(pieceStr)
    pieceCoords = piecesDict[Vars.Piece][Vars.PieceRot]
    for i in range(4): 
        for n in range(4):
            if(pieceCoords[i][n] != 0):
                Vars.setScreen[Vars.piecePos[0]+i][Vars.piecePos[1]+n] = pieceCoords[i][n]
    newPiece()

def dropPiece():
    pass