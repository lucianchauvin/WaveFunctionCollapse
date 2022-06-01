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


#directions = [(2, (0, 1)), (3, (1, 0)),(0, (0, -1)), (1, (-1, 0))]

def propogate(wave, states, x, y):  # broken https://www.youtube.com/watch?v=2SuvO4Gi7uY&t=766s
    print(wave)
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
            if len(wave[y][x]) < min:
                min = len(wave[y][x])
    for y in range(len(wave)):
        for x in range(len(wave[0])):
            if len(wave[y][x]) == min:
                minList.append((x, y))

    return random.choice(minList)


def generateImage(wave, states, w, h, pixelSize):
    img = Image.new("RGB", (w*pixelSize, h*pixelSize))
    for y in range(h):
        for x in range(w):
            if len(wave[y][x]) > 0:
                state = wave[y][x][0]
                img.paste(Image.open(states[state]["img"]),
                          (x*pixelSize, y*pixelSize))
    img.save("wave.png")


s = generateStates("mesh.png", 3, 1)

width = 4
height = 5

wave = generateWave(s, width, height)

while not is_collapsed(wave):
    min = getLeastEntropy(wave, s)
    wave = collapse(wave, s, min[0], min[1])
    wave = propogate(wave, s, min[0], min[1])

print(wave)
generateImage(wave, s, width, height, 3)
