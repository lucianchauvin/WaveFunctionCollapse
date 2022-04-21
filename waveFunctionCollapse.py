import random

wfc = {
    "A": {
        "img": "blank.png",
        "adjacency": [["A", "B"], ["A"], ["A", "B"], ["A"]],
    },
    "B": {
        "img": "bar.png",
        "adjacency": [["A", "B"], ["B", "C"], ["A", "B"], ["B"]],
    },
    "C": {
        "img": "corrner.png",
        "adjacency": [["A", "B"], ["A"], [], ["B"]],
    },
}


def collapse(tiles, x, y):
    if(tiles[y][x] != None):
        return tiles[y][x]

    possibleStates = wfc.copy()

    idkHowToExplainThis = [(2, (0, 1)), (3, (1, 0)), (0, (0, -1)), (1,(-1, 0))]

    
    for direction in idkHowToExplainThis:
        if y < len(tiles)-1 and x < len(tiles[0])-1:
            tile = tiles[y+direction[1][1]][x+direction[1][0]]
            if tile is not None:
                for state in wfc:
                    print(state, wfc[tile]["adjacency"][direction[0]])
                    if state not in wfc[tile]["adjacency"][direction[0]]  and state in possibleStates:
                        possibleStates.pop(state)

    if len(possibleStates) == 0:
        print("NO POSSIBLE STATES")
        return None
    print(possibleStates, x, y)
    return random.choice(list(possibleStates))


def printTiles(tiles):
    for row in tiles:
        print(row)


tiles = [[None for x in range(10)] for x in range(10)]

tiles[0][0] = "B"

for(x, y) in [(x, y) for x in range(10) for y in range(10)]:
    tiles[y][x] = collapse(tiles, x, y)

printTiles(tiles)


# print(collapse(tiles, 1, 0))
