import random

from regex import R

wfc = {
    "A": {
        "img": "╬",
        "adjacency": [["A","C"], ["A","B"], ["A", "C"], ["A","B"]],
    },
    "B": {
        "img": "═",
        "adjacency": [["B","D"], ["A", "B"], ["B","D"], ["A", "B"]],
    },
    "C":{
        "img": "║",
        "adjacency": [["C","A"], ["C","D"], ["C","A"], ["C","D"]],
    },
    "D":{
        "img": " ",
        "adjacency": [["B","D"], ["C","D"], ["B","D"], ["C","D"]],
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


tiles = [[None for x in range(50)] for x in range(20)]

tiles[0][0] = random.choice(list(wfc))  

for(x, y) in [(x, y) for x in range(50) for y in range(20)]:
    tiles[y][x] = collapse(tiles, x, y)

tilesWithImg = "\n".join(["".join([wfc[tile]["img"] for tile in row]) for row in tiles])

print(tilesWithImg[random.randint(0, (len(tilesWithImg)-1)^2)])