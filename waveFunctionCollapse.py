from PIL import Image
from string import ascii_lowercase
import numpy as np
import json


# generates the wave function for a given image with an n x m states
def generateWaveFunction(img, n, m):

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

        print(left, top, right, bottom)

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


generateWaveFunction("img.png", 4, 1)
