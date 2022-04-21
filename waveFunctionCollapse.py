import imghdr
import random

from regex import R
from sympy import to_cnf

wfc = {
    "A": {
        "img": "╬",
        "adjacency": [["A","C" ], ["A","B" ], ["A", "C"], ["A","B"]],
    },
    "B": {
        "img": "═",
        "adjacency": [["B","D"], ["A", "B", "E"], ["B","D"], ["A", "B"]],
    },
    "C":{
        "img": "║",
        "adjacency": [["C","A"], ["C","D"], ["C","A"], ["C","D"]],
    },
    "D":{
        "img": " ",
        "adjacency": [["B","D"], ["C","D"], ["B","D"], ["C","D"]],
    },
    "E":{
        "img": "╣",
        "adjacency": [["C","A"], ["C","D"], ["C","A"], ["A","B"]],
    },
    "F":{
        "img" : "╠",
        "adjacency": [["C","E","A"], ["B","A","E"], ["a"], ["F","G"]],
    }
}


def collapse(tiles, x, y):
    if(tiles[y][x] != None):
        return tiles[y][x]

    possibleStates = wfc.copy()

    idkHowToExplainThis = [(2, (0, 1)), (3, (1, 0)), (0, (0, -1)), (1,(-1, 0))]
    
    for direction in idkHowToExplainThis:
        try:
            tile = tiles[y+direction[1][1]][x+direction[1][0]]
            if tile is not None:
                for state in wfc:
                    if state not in wfc[tile]["adjacency"][direction[0]] and state in possibleStates:
                        possibleStates.pop(state)
        except:
            pass

    if len(possibleStates) == 0:
        print("NO POSSIBLE STATES")
        return None
    # print(possibleStates, x, y)
    return random.choice(list(possibleStates))


def printTiles(tiles):
    for row in tiles:
        print(row)


tiles = [[None for x in range(125)] for x in range(20)]

tiles[0][0] = random.choice(list(wfc))  

for r in range(20):
    for c in range(125):
        tiles[r][c] = collapse(tiles, c, r)

tilesWithImg = "\n".join(["".join([wfc[tile]["img"] for tile in row]) for row in tiles])

print(tilesWithImg)