import copy

width = 10 # set the width of the game space
height = 25 # set the height of the game space
screen = []
setScreen = []
piecePos = [0,4]
Piece = ""
PieceRot = "N"
PiecesLst = ["O","I","L","J","Z","S","T"]
PieceQ = []
locking = False
heldPiece = ""
lockTimer = 0
lockTime = 75
keyLst = ["left", "down", "right", "x", "z", "c", "space"]
keyPressed = [0 for i in range(len(keyLst))]
fallTimer = 1
fallTime = 10
ghostPiecePos = copy.deepcopy(piecePos)