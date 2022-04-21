import random

wfc = {
    "A": {
        "img": "blank.png",
        "adjacency": [["A", "B"], ["A"], ["A", "B"], ["A"]],
    },
    "B": {
        "img": "bar.png",
        "adjacency": [["A", "B"], ["B"], ["A", "B"], ["B"]],
    },
    # "C": {
    #     "img": "corrner.png",
    #     "adjacency": [["A", "B"], ["A"], [], ["B"]],
    # },
}


def collapse(tiles, x, y):
    possibleStates = wfc.copy()

    if tiles[y][x] is not None:
        return tiles[y][x]

    idkHowToExplainThis = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in enumerate(idkHowToExplainThis):
        try:
            tile = tiles[y+direction[1][1]][x+direction[1][0]]
            for state in wfc:
                if state not in wfc[tile]["adjacency"][direction[0]] and state in possibleStates:
                    possibleStates.pop(state)
        except:
            pass

    if len(possibleStates) == 0:
        print("NO POSSIBLE STATES")
        return None
    print(possibleStates, x, y)
    return random.choice(list(possibleStates))


def printTiles(tiles):
    for row in tiles:
        for tile in row:
            if tile is None:
                print(" ", end="")
            else:
                print(tile, end="")
        print()


tiles = [[None for x in range(10)] for x in range(10)]

tiles[0][0] = "B"

for(x, y) in [(x, y) for x in range(10) for y in range(10)]:
    tiles[y][x] = collapse(tiles, x, y)

printTiles(tiles)
