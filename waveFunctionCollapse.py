import random

wfc = {
    "A": {
        "img": "┼",
        "adjacency": [["A", "C", "E", "F", ], ["A", "B", "E", ], ["A", "C", "E", "F"], ["A", "B", "F"]],
    },
    "B": {
        "img": "─",
        "adjacency": [["B", "D"], ["A", "B", "E", ], ["B", "D", ], ["A", "B", "F"]],
    },
    "C": {
        "img": "│",
        "adjacency": [["C", "A", "F", "E", ], ["C", "D", "F"], ["C", "A", "E", "F"], ["C", "D", "E"]],
    },
    "D": {
        "img": " ",
        "adjacency": [["B", "D"], ["C", "D", "F"], ["B", "D", ], ["C", "D", ]],
    },
    "E": {
        "img": "┤",
        "adjacency": [["C", "A", "F", ], ["C", "D", "F"], ["C", "A", "F"], ["A", "B", "F"]],
    },
    "F": {
        "img": "├",
        "adjacency": [["C", "E", "A", ], ["B", "A", "E", ], ["A", "C", "E"], ["E", "C", "D", ]],
    },
}

# wfc = {
#     "A": {
#         "img": "┌",
#         "adjacency": [["C", "D"], ["B", "D"], ["C", "D"], ["B", "D"]],
#     },
#     "B": {
#         "img": "┐",
#         "adjacency": [["C", "D"], ["A", "C"], ["C", "D"], ["A", "C"]],
#     },
#     "C": {
#         "img": "└",
#         "adjacency": [["A", "B"], ["B", "D"], ["A", "B"], ["B", "D"]],
#     },
#     "D": {
#         "img": "┘",
#         "adjacency": [["A", "B"], ["C", "A"], ["A", "B"], ["C", "A"]],
#     },
# }


def collapse(tiles, x, y):
    if(tiles[y][x] != None):
        return tiles[y][x]

    possibleStates = wfc.copy()

    idkHowToExplainThis = [(2, (0, 1)), (3, (1, 0)),
                           (0, (0, -1)), (1, (-1, 0))]

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
        print("----NO POSSIBLE STATES----")
        return None
    # print(possibleStates, x, y)
    return random.choice(list(possibleStates))


def printTiles(tiles):
    for row in tiles:
        print(row)

tiles = [[None for x in range(160)] for x in range(20)]

tiles[0][0] = "F"

for r in range(20):
    for c in range(160):
        tiles[r][c] = collapse(tiles, c, r)

tilesWithImg = "\n".join(["".join([wfc[tile]["img"]
                        for tile in row]) for row in tiles])

print(tilesWithImg)
