from itertools import count
from PIL import Image
from string import ascii_lowercase
import numpy as np
import json
import os
import random

# generates the wave function for a given image with an n x m states


def generateStates(img, n, m):

    img = Image.open(img)

    width, height = img.size
    stateWidth = width/n
    stateHeight = height/m

    states = {}

    c = 0
    for (i, j) in [(i, j) for i in range(n) for j in range(m)]:
        top = j*stateWidth
        left = i*stateHeight
        bottom = top + stateWidth
        right = left + stateWidth

        s = img.crop((left, top, right, bottom))
        s.save("stateImages/" + ascii_lowercase[c] + ".png")

        pixels = np.array(s)

        adj = [pixels[0].tolist(), [pixels[y][len(pixels[0])-1].tolist()
                                    for y in range(len(pixels))], pixels[len(pixels)-1].tolist(), [pixels[y][0].tolist() for y in range(len(pixels))]]

        states.update(
            {ascii_lowercase[c]: {"img": "stateImages/" + ascii_lowercase[c] + ".png", "adj": adj}})

        c += 1

        for x in range(3):
            s = s.rotate(90)
            pixelsNew = np.array(s)
            currentAdj = [states[state]["adj"] for state in states]
            adj = [pixelsNew[0].tolist(), [pixelsNew[y][len(pixelsNew[0])-1].tolist()
                                           for y in range(len(pixelsNew))], pixelsNew[len(pixelsNew)-1].tolist(), [pixelsNew[y][0].tolist() for y in range(len(pixelsNew))]]
            if adj not in currentAdj:
                s.save("stateImages/" + ascii_lowercase[c] + ".png")
                states.update(
                    {ascii_lowercase[c]: {"img": "stateImages/" + ascii_lowercase[c] + ".png", "adj": adj}})
                c += 1

    with open("states.json", "w") as f:
        json.dump(states, f)

    return states


def generateWave(states, w, h):
    return [[list(states) for x in range(w)] for y in range(h)]


#directions = [(2, (0, -1)), (3, (1, 0)),(0, (0, 1)), (1, (-1, 0))]

def propogate(wave, states, x, y):  # updates the wave based off of a collapse event
    # initalizes the stack of updated cells with the first element being the collapsed cell
    stack = [(x, y)]
    # the list used to iterate through the nesw directions. the first value of the tuple is the index value of the opposite cell adjecencies. So if we want the adjacencies of the cell to the north while our current cell is below we want the 3 list in the adjacencies list which corosponds to a 2 index value
    directions = [(2, (0, -1)), (3, (1, 0)), (0, (0, 1)), (1, (-1, 0))]
    while len(stack) > 0:  # while the stack has updated cells in it
        # get the last value in the stack to update other cells
        current = stack.pop(-1)
        # if the cell is collapsed, so if there is only 1 possible state
        if len(wave[current[1]][current[0]]) == 1:
            # get all adjacencies of collapsed cell and the state of that collapsed cell
            currentAdj = states[wave[current[1]][current[0]][0]]['adj']
            # iterate through the all cells around whilist iterating through the corosponding adjaciencies of each cell
            for direction in enumerate(directions):
                # gets the corosponding adjacencies of current cell. so if we are on the cell to the north we need the north adjaciencies to compare with
                currentRelAdj = currentAdj[direction[0]]
                other = (current[0] + direction[1][1][0],
                         current[1] + direction[1][1][1])  # gets the x and y cords of other cell
                # checks if other is valid cell
                if other[0] < len(wave[0]) and other[0] >= 0 and other[1] < len(wave) and other[1] >= 0:
                    # get possibilities of other cell
                    otherPos = wave[other[1]][other[0]].copy()
                    # for all possible states in other cell
                    for pos in wave[other[1]][other[0]]:
                        # gets the relative adjacencies of the other cell. so if we are on the cell to the north we need the south adjaciencies to compare with
                        posRelAdj = states[pos]['adj'][direction[1][0]]
                        # if the other relative adjacency is not the same as our current one remove it from possible states
                        if currentRelAdj != posRelAdj:
                            if len(otherPos) > 1:
                                otherPos.remove(pos)
                                if other not in stack:
                                    stack.append(other)
                    wave[other[1]][other[0]] = otherPos

    return wave


def collapse(wave, states, x, y):
    wave[y][x] = [random.choice(wave[y][x])]
    return wave


def is_collapsed(wave):
    for row in wave:
        for state in row:
            if len(state) > 1:
                return False
    return True


def getLeastEntropy(wave, states):
    min = 999999
    minList = []
    for y in range(len(wave)):
        for x in range(len(wave[0])):
            if len(wave[y][x]) < min and len(wave[y][x]) != 1:
                min = len(wave[y][x])
    for y in range(len(wave)):
        for x in range(len(wave[0])):
            if len(wave[y][x]) == min:
                minList.append((x, y))

    return random.choice(minList)


def generateImage(wave, states, w, h, pixelSize, name):
    img = Image.new("RGB", (w*pixelSize, h*pixelSize))
    for y in range(h):
        for x in range(w):
            if len(wave[y][x]) > 0:
                state = wave[y][x][0]
                img.paste(Image.open(states[state]["img"]),
                          (x*pixelSize, y*pixelSize))
    img.save(name)
    img.show()


def printWave(wave):
    for y in wave:
        print(y)
    print("\n")


for x in range(20):
    s = generateStates("mesh.png", 2, 1)

    width = 10
    height = 10

    wave = generateWave(s, width, height)

    i = 0
    while not is_collapsed(wave):
        i += 1
        min = getLeastEntropy(wave, s)
        wave = collapse(wave, s, min[0], min[1])
        wave = propogate(wave, s, min[0], min[1])
        print(i*100/(width*height))

    printWave(wave)
    generateImage(wave, s, width, height, 24, "wave" + str(x) + ".png")
