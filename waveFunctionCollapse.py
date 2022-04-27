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
    for (j, i) in [(i, j) for i in range(n) for j in range(m)]:
        top = j*stateWidth
        left = i*stateHeight
        bottom = (j+1)*stateWidth
        right = (i+1)*stateHeight

        s = img.crop((left, top, right, bottom))
        s.save("stateImages/" + ascii_lowercase[c] + ".png")

        pixels = np.array(s)

        adj = [pixels[0].tolist(), [pixels[y][len(pixels[0])-1].tolist()
                                    for y in range(len(pixels))], pixels[len(pixels)-1].tolist(), [pixels[y][0].tolist() for y in range(len(pixels))]]

        states.update(
            {ascii_lowercase[c]: {"img": "stateImages/" + ascii_lowercase[c] + ".png", "adj": adj}})

        c += 1

    with open("states.json", "w") as f:
        json.dump(states, f)


generateWaveFunction("img.png", 3, 3)
