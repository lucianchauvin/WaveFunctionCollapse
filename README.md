# WaveFunctionCollapse
Credit and idea comes from: https://github.com/mxgmn/WaveFunctionCollapse <- This is basically the same thing but in ascii characters and explained way worse :D

Generates all posible states and adjacencies. Iterates through a 2D array, collapsing the wave funcion (obeserving a state) at each position and placing the observed state at the position. Shown in ASCII characters.

# ToDo
* Create a function to auto generate adjacencies for given states. 
* ^To do this I will need to make this work with images instead of with ASCII characters
    * Was thinking I could just get the average of each edge and use that for the adjacencies
* Re-design the way the wave function is collapsed and how possible states are stored
    * Currently I do some "inefficent" python list manipulation to check each adjacent cell and then collapse the wave function. What I want to do instead is generate and NxN matrix with all possible states stored at each location. Then a random position is collapsed, propogating through all possible tiles and changing their possible states

All being implemented in "waveFunctionCollapse.py" instead of ASCII one. 

# Examples

States: ┌, ┐, └,┘

```raw
┌┐└┘┌┘┌┘┌┐┌┘└┘┌┘└┐┌┐┌┘└┐┌┐┌┐┌┐└┘┌┐└┐┌┐└┘└┘┌┐┌┐└┐┌┘┌┘┌┘└┐┌┐┌┘┌┘┌┘┌┐└┘└┐┌┐└┘┌┘└┘└┐┌┘└┐└┐┌┘┌┐┌┘┌┘┌┐└┐┌┘└┘┌┐└┐└┐└┐└┘┌┘┌┘┌┘└┐┌┘┌┐└┐└┘┌┘┌┐┌┐┌┘┌┐└┘┌┘┌┐└┘┌┘┌┘└┘└┘┌┘┌┐┌┘└┘┌┐┌┐└
└┘┌┐└┐└┐└┘└┐┌┐└┐┌┘└┘└┐┌┘└┘└┘└┘┌┐└┘┌┘└┘┌┐┌┐└┘└┘┌┘└┐└┐└┐┌┘└┘└┐└┐└┐└┘┌┐┌┘└┘┌┐└┐┌┐┌┘└┐┌┘┌┘└┐└┘└┐└┐└┘┌┘└┐┌┐└┘┌┘┌┘┌┘┌┐└┐└┐└┐┌┘└┐└┘┌┘┌┐└┐└┘└┘└┐└┘┌┐└┐└┘┌┐└┐└┐┌┐┌┐└┐└┘└┐┌┐└┘└┘┌
┐┌┘└┐└┐└┐┌┐└┘└┐└┘┌┐┌┐└┘┌┐┌┐┌┐┌┘└┐┌┘┌┐┌┘└┘└┐┌┐┌┘┌┐└┐└┐└┘┌┐┌┐└┐└┐└┐┌┘└┘┌┐┌┘└┐└┘└┘┌┐└┘┌┘┌┐└┐┌┐└┐└┐┌┘┌┐└┘└┐┌┘┌┘┌┘┌┘└┐└┐└┐└┘┌┐└┐┌┘┌┘└┐└┐┌┐┌┐└┐┌┘└┐└┐┌┘└┐└┐└┘└┘└┐└┐┌┐└┘└┐┌┐┌┘
└┘┌┐└┐└┐└┘└┐┌┐└┐┌┘└┘└┐┌┘└┘└┘└┘┌┐└┘┌┘└┘┌┐┌┐└┘└┘┌┘└┐└┐└┐┌┘└┘└┐└┐└┐└┘┌┐┌┘└┘┌┐└┐┌┐┌┘└┐┌┘┌┘└┐└┘└┐└┐└┘┌┘└┐┌┐└┘┌┘┌┘┌┘┌┐└┐└┐└┐┌┘└┐└┘┌┘┌┐└┐└┘└┘└┐└┘┌┐└┐└┘┌┐└┐└┐┌┐┌┐└┐└┘└┐┌┐└┘└┘┌
┐┌┘└┐└┐└┐┌┐└┘└┐└┘┌┐┌┐└┘┌┐┌┐┌┐┌┘└┐┌┘┌┐┌┘└┘└┐┌┐┌┘┌┐└┐└┐└┘┌┐┌┐└┐└┐└┐┌┘└┘┌┐┌┘└┐└┘└┘┌┐└┘┌┘┌┐└┐┌┐└┐└┐┌┘┌┐└┘└┐┌┘┌┘┌┘┌┘└┐└┐└┐└┘┌┐└┐┌┘┌┘└┐└┐┌┐┌┐└┐┌┘└┐└┐┌┘└┐└┐└┘└┘└┐└┐┌┐└┘└┐┌┐┌┘
┘└┐┌┘┌┘┌┘└┘┌┐┌┘┌┐└┘└┘┌┐└┘└┘└┘└┐┌┘└┐└┘└┐┌┐┌┘└┘└┐└┘┌┘┌┘┌┐└┘└┘┌┘┌┘┌┘└┐┌┐└┘└┐┌┘┌┐┌┐└┘┌┐└┐└┘┌┘└┘┌┘┌┘└┐└┘┌┐┌┘└┐└┐└┐└┐┌┘┌┘┌┘┌┐└┘┌┘└┐└┐┌┘┌┘└┘└┘┌┘└┐┌┘┌┘└┐┌┘┌┘┌┐┌┐┌┘┌┘└┘┌┐┌┘└┘└┐
┌┐└┘┌┘┌┘┌┐┌┘└┘┌┘└┐┌┐┌┘└┐┌┐┌┐┌┐└┘┌┐└┐┌┐└┘└┘┌┐┌┐└┐┌┘┌┘┌┘└┐┌┐┌┘┌┘┌┘┌┐└┘└┐┌┐└┘┌┘└┘└┐┌┘└┐└┐┌┘┌┐┌┘┌┘┌┐└┐┌┘└┘┌┐└┐└┐└┐└┘┌┘┌┘┌┘└┐┌┘┌┐└┐└┘┌┘┌┐┌┐┌┘┌┐└┘┌┘┌┐└┘┌┘┌┘└┘└┘┌┘┌┐┌┘└┘┌┐┌┐└
└┘┌┐└┐└┐└┘└┐┌┐└┐┌┘└┘└┐┌┘└┘└┘└┘┌┐└┘┌┘└┘┌┐┌┐└┘└┘┌┘└┐└┐└┐┌┘└┘└┐└┐└┐└┘┌┐┌┘└┘┌┐└┐┌┐┌┘└┐┌┘┌┘└┐└┘└┐└┐└┘┌┘└┐┌┐└┘┌┘┌┘┌┘┌┐└┐└┐└┐┌┘└┐└┘┌┘┌┐└┐└┘└┘└┐└┘┌┐└┐└┘┌┐└┐└┐┌┐┌┐└┐└┘└┐┌┐└┘└┘┌
┐┌┘└┐└┐└┐┌┐└┘└┐└┘┌┐┌┐└┘┌┐┌┐┌┐┌┘└┐┌┘┌┐┌┘└┘└┐┌┐┌┘┌┐└┐└┐└┘┌┐┌┐└┐└┐└┐┌┘└┘┌┐┌┘└┐└┘└┘┌┐└┘┌┘┌┐└┐┌┐└┐└┐┌┘┌┐└┘└┐┌┘┌┘┌┘┌┘└┐└┐└┐└┘┌┐└┐┌┘┌┘└┐└┐┌┐┌┐└┐┌┘└┐└┐┌┘└┐└┐└┘└┘└┐└┐┌┐└┘└┐┌┐┌┘
┘└┐┌┘┌┘┌┘└┘┌┐┌┘┌┐└┘└┘┌┐└┘└┘└┘└┐┌┘└┐└┘└┐┌┐┌┘└┘└┐└┘┌┘┌┘┌┐└┘└┘┌┘┌┘┌┘└┐┌┐└┘└┐┌┘┌┐┌┐└┘┌┐└┐└┘┌┘└┘┌┘┌┘└┐└┘┌┐┌┘└┐└┐└┐└┐┌┘┌┘┌┘┌┐└┘┌┘└┐└┐┌┘┌┘└┘└┘┌┘└┐┌┘┌┘└┐┌┘┌┘┌┐┌┐┌┘┌┘└┘┌┐┌┘└┘└┐
┐┌┘└┐└┐└┐┌┐└┘└┐└┘┌┐┌┐└┘┌┐┌┐┌┐┌┘└┐┌┘┌┐┌┘└┘└┐┌┐┌┘┌┐└┐└┐└┘┌┐┌┐└┐└┐└┐┌┘└┘┌┐┌┘└┐└┘└┘┌┐└┘┌┘┌┐└┐┌┐└┐└┐┌┘┌┐└┘└┐┌┘┌┘┌┘┌┘└┐└┐└┐└┘┌┐└┐┌┘┌┘└┐└┐┌┐┌┐└┐┌┘└┐└┐┌┘└┐└┐└┘└┘└┐└┐┌┐└┘└┐┌┐┌┘
┘└┐┌┘┌┘┌┘└┘┌┐┌┘┌┐└┘└┘┌┐└┘└┘└┘└┐┌┘└┐└┘└┐┌┐┌┘└┘└┐└┘┌┘┌┘┌┐└┘└┘┌┘┌┘┌┘└┐┌┐└┘└┐┌┘┌┐┌┐└┘┌┐└┐└┘┌┘└┘┌┘┌┘└┐└┘┌┐┌┘└┐└┐└┐└┐┌┘┌┘┌┘┌┐└┘┌┘└┐└┐┌┘┌┘└┘└┘┌┘└┐┌┘┌┘└┐┌┘┌┘┌┐┌┐┌┘┌┘└┘┌┐┌┘└┘└┐
┐┌┘└┐└┐└┐┌┐└┘└┐└┘┌┐┌┐└┘┌┐┌┐┌┐┌┘└┐┌┘┌┐┌┘└┘└┐┌┐┌┘┌┐└┐└┐└┘┌┐┌┐└┐└┐└┐┌┘└┘┌┐┌┘└┐└┘└┘┌┐└┘┌┘┌┐└┐┌┐└┐└┐┌┘┌┐└┘└┐┌┘┌┘┌┘┌┘└┐└┐└┐└┘┌┐└┐┌┘┌┘└┐└┐┌┐┌┐└┐┌┘└┐└┐┌┘└┐└┐└┘└┘└┐└┐┌┐└┘└┐┌┐┌┘
└┘┌┐└┐└┐└┘└┐┌┐└┐┌┘└┘└┐┌┘└┘└┘└┘┌┐└┘┌┘└┘┌┐┌┐└┘└┘┌┘└┐└┐└┐┌┘└┘└┐└┐└┐└┘┌┐┌┘└┘┌┐└┐┌┐┌┘└┐┌┘┌┘└┐└┘└┐└┐└┘┌┘└┐┌┐└┘┌┘┌┘┌┘┌┐└┐└┐└┐┌┘└┐└┘┌┘┌┐└┐└┘└┘└┐└┘┌┐└┐└┘┌┐└┐└┐┌┐┌┐└┐└┘└┐┌┐└┘└┘┌
┌┐└┘┌┘┌┘┌┐┌┘└┘┌┘└┐┌┐┌┘└┐┌┐┌┐┌┐└┘┌┐└┐┌┐└┘└┘┌┐┌┐└┐┌┘┌┘┌┘└┐┌┐┌┘┌┘┌┘┌┐└┘└┐┌┐└┘┌┘└┘└┐┌┘└┐└┐┌┘┌┐┌┘┌┘┌┐└┐┌┘└┘┌┐└┐└┐└┐└┘┌┘┌┘┌┘└┐┌┘┌┐└┐└┘┌┘┌┐┌┐┌┘┌┐└┘┌┘┌┐└┘┌┘┌┘└┘└┘┌┘┌┐┌┘└┘┌┐┌┐└
┘└┐┌┘┌┘┌┘└┘┌┐┌┘┌┐└┘└┘┌┐└┘└┘└┘└┐┌┘└┐└┘└┐┌┐┌┘└┘└┐└┘┌┘┌┘┌┐└┘└┘┌┘┌┘┌┘└┐┌┐└┘└┐┌┘┌┐┌┐└┘┌┐└┐└┘┌┘└┘┌┘┌┘└┐└┘┌┐┌┘└┐└┐└┐└┐┌┘┌┘┌┘┌┐└┘┌┘└┐└┐┌┘┌┘└┘└┘┌┘└┐┌┘┌┘└┐┌┘┌┘┌┐┌┐┌┘┌┘└┘┌┐┌┘└┘└┐
┌┐└┘┌┘┌┘┌┐┌┘└┘┌┘└┐┌┐┌┘└┐┌┐┌┐┌┐└┘┌┐└┐┌┐└┘└┘┌┐┌┐└┐┌┘┌┘┌┘└┐┌┐┌┘┌┘┌┘┌┐└┘└┐┌┐└┘┌┘└┘└┐┌┘└┐└┐┌┘┌┐┌┘┌┘┌┐└┐┌┘└┘┌┐└┐└┐└┐└┘┌┘┌┘┌┘└┐┌┘┌┐└┐└┘┌┘┌┐┌┐┌┘┌┐└┘┌┘┌┐└┘┌┘┌┘└┘└┘┌┘┌┐┌┘└┘┌┐┌┐└
┘└┐┌┘┌┘┌┘└┘┌┐┌┘┌┐└┘└┘┌┐└┘└┘└┘└┐┌┘└┐└┘└┐┌┐┌┘└┘└┐└┘┌┘┌┘┌┐└┘└┘┌┘┌┘┌┘└┐┌┐└┘└┐┌┘┌┐┌┐└┘┌┐└┐└┘┌┘└┘┌┘┌┘└┐└┘┌┐┌┘└┐└┐└┐└┐┌┘┌┘┌┘┌┐└┘┌┘└┐└┐┌┘┌┘└┘└┘┌┘└┐┌┘┌┘└┐┌┘┌┘┌┐┌┐┌┘┌┘└┘┌┐┌┘└┘└┐
┐┌┘└┐└┐└┐┌┐└┘└┐└┘┌┐┌┐└┘┌┐┌┐┌┐┌┘└┐┌┘┌┐┌┘└┘└┐┌┐┌┘┌┐└┐└┐└┘┌┐┌┐└┐└┐└┐┌┘└┘┌┐┌┘└┐└┘└┘┌┐└┘┌┘┌┐└┐┌┐└┐└┐┌┘┌┐└┘└┐┌┘┌┘┌┘┌┘└┐└┐└┐└┘┌┐└┐┌┘┌┘└┐└┐┌┐┌┐└┐┌┘└┐└┐┌┘└┐└┐└┘└┘└┐└┐┌┐└┘└┐┌┐┌┘
└┘┌┐└┐└┐└┘└┐┌┐└┐┌┘└┘└┐┌┘└┘└┘└┘┌┐└┘┌┘└┘┌┐┌┐└┘└┘┌┘└┐└┐└┐┌┘└┘└┐└┐└┐└┘┌┐┌┘└┘┌┐└┐┌┐┌┘└┐┌┘┌┘└┐└┘└┐└┐└┘┌┘└┐┌┐└┘┌┘┌┘┌┘┌┐└┐└┐└┐┌┘└┐└┘┌┘┌┐└┐└┘└┘└┐└┘┌┐└┐└┘┌┐└┐└┐┌┐┌┐└┐└┘└┐┌┐└┘└┘┌
```

States: ┼, ─, │, ' ', ┤, ├

```raw
┼┼┤├┼─┼─┤ │ │ │├┼─┼─┤├──┤││   ││ ├─┼┤│├┼─┼┼┤│ ├┼┼┼─┼┼───┤││├┤││││├┼┤├┤ │├──┤│├┤ ├┼─┤  │ │├┼┼┤  │├┤├┤│├┤├┼┤│├┤├┤│ │ ├┤│├┼┤├┼─┤│  ├┤ │││ │││││   ├┤ ├───┤  ├┤│├┼┤├┤     ├
┤││││ │ ├─┼─┤ ││├─┼─┼┼──┼┤│   ├┤ │ ├┼┤│├─┤├┼┤ │││├─┼┤   │││││├┼┼┼┤├┼┤│ ├┤  ├┤│├─┤│ ├──┤ │││││  ├┼┼┼┼┤││││├┤│││├┤ ├─┤│││├┼┼┤ ││  │├─┤││ ├┼┼┼┼───┼┼─┤   │  ││││├┼┤│     │
┼┼┼┤│ ├─┼─┤ ├─┼┼┼─┤ ││  ├┼┤   │├─┤ ││├┤│ ││││ ││├┼─┤│   ├┼┤│├┤││├┼┼┤├┤ ││  │├┤│ ││ │  ├─┼┼┼┤│  │├┼┼┤├┤│├┤││├┼┼┼┼─┤ │├┼┼┼┤│├─┤│  ├┤ │├┼─┤││││   ├┼─┼───┼──┼┤│││││├─────┤
││││├─┼─┼─┼─┼─┤│├─┼─┤├──┼┼┼───┼┤ ├─┼┼┤││ │├┼┼─┤├┼┼─┼┼───┼┼┼┤││├┼┼┼┤├┼┼─┼┼──┼┤├┤ │├─┤  │ ├┤│││  ││├┤│││├┤├┤││├┤├┤ │ ├┼┤│├┼┼┼─┼┤  │├─┼┼┼─┼┤│├┼───┤│ │   │  ├┼┤├┤│├┼─────┼
├┤├┼┤ │ │ ├─┤ │││ ├─┼┤  ├┤├───┼┼─┤ ││├┼┼─┤││├─┼┼┼┤ ├┼───┤││││├┼┼┼┼┼┼┼┤ ├┤  ││││ ├┤ ├──┤ │├┤│├──┼┤│├┤├┼┤├┼┼┼┼┼┼┤│ ├─┤├┼┼┤├┤│ ├┼──┼┼─┤││ ├┼┤││   ├┼─┼───┤  │├┼┤││││     ├
┼┼┼┤├─┤ ├─┼─┼─┤│├─┤ ├┼──┤├┼───┤├─┼─┼┼┼┼┼─┼┤├┤ ├┼┤│ ││   │├┤│├┤├┼┤├┤├┼┼─┤│  ├┼┼┤ ││ │  │ ├┤├┼┼──┤├┤│├┤├┼┤│├┤├┤││├─┼─┼┼┤│││├┼─┤│  ├┤ │├┤ │├┼┤│   │├─┼───┼──┤││├┼┼┤├─────┤
│├┼┼┤ ├─┼─┤ ├─┼┤│ │ ││  │││   ││ ├─┼┤│├┤ ├┼┼┼─┼┤│├─┤├───┤││├┼┼┤├┼┼┼┤│├─┼┤  │││├─┤│ ├──┤ │├┼┼┤  │││││││├┼┤│├┼┼┤├┼─┤ │├┼┤├┤││ ││  ││ ├┼┼─┤│├┼┤   ├┼─┼───┼──┼┤├┤├┼┼┼─────┼
┤│├┼┼─┼─┼─┼─┤ │├┤ ├─┤│  ├┤├───┼┤ │ │├┤││ │├┤├─┤│├┤ ├┤   ││├┤├┼┼┼┼┤││││ │├──┼┤├┤ ││ │  ├─┼┼┤││  ├┼┤│├┼┤││├┤│├┤││├─┼─┼┤│├┼┼┼┼─┤│  │├─┼┼┤ ├┤││├───┤├─┼───┤  │├┤├┼┤├┼─────┼
│├┼┤├─┼─┼─┼─┼─┼┤│ │ │├──┼┼┤   ││ ├─┤││├┼─┼┼┼┼─┼┤││ │├───┤│││││├┼┤├┼┤├┤ ││  │├┤├─┤│ ├──┼─┼┼┼┤│  │├┼┼┤├┼┤├┤├┼┼┼┼┤│ │ │├┤││││├─┼┼──┼┼─┼┤│ ││├┼┤   ││ │   ├──┤││││├┤├─────┤
┤│├┼┼─┤ │ │ │ ├┼┤ │ ├┤  │││   ├┼─┤ │├┼┼┤ ├┤│├─┤├┤│ ├┤   ││││├┼┼┼┼┼┼┼┼┼─┤├──┤│├┤ ├┤ │  │ ├┤├┼┤  ├┼┼┤││├┼┼┼┼┤├┼┼┼┼─┤ ├┤├┤││││ ├┤  ││ │││ │││├┼───┼┤ ├───┤  ├┤├┼┼┤├┤     │
┼┤│├┼─┼─┤ ├─┼─┤├┼─┤ │├──┤├┤   ││ ├─┤││││ │├┤│ ├┼┼┤ ││   ├┼┼┼┤│├┼┤│├┤││ ││  │├┤│ ││ ├──┼─┼┼┤│├──┤├┼┼┼┼┼┼┤├┤├┤├┼┼┼─┼─┤├┼┼┤├┤├─┼┼──┤├─┤│├─┤│││├───┼┼─┼───┼──┼┼┼┤├┼┤│     │
│├┼┤├─┼─┼─┤ ├─┼┤│ ├─┼┼──┼┼┼───┤│ │ ├┼┼┤├─┤│││ │││├─┤├───┼┤├┼┼┼┼┼┼┼┼┼┤│ ├┤  ├┼┼┼─┼┤ │  │ ├┤├┤│  ├┼┤││├┤│├┼┼┼┼┤│├┼─┼─┼┤││││├┼─┼┤  ││ │││ ├┼┼┼┼───┤│ ├───┼──┤├┼┼┼┤├┤     ├
┤│├┼┼─┤ ├─┼─┤ │││ │ ││  │├┤   ││ │ ││├┼┤ │├┤├─┼┼┼┤ ││   ├┼┤│├┼┤├┤├┼┤││ │├──┤││├─┼┼─┼──┼─┼┼┼┼┤  │├┼┤├┼┼┼┤│├┤│├┼┤│ │ ││├┼┤│││ ││  ├┤ ││├─┼┼┼┤├───┼┼─┼───┤  ││├┼┤│││     │
│├┤├┼─┼─┼─┼─┼─┤├┼─┼─┼┼──┼┼┼───┤│ │ ├┼┤├┼─┤│││ ││├┼─┤│   │││├┤│├┤├┼┼┼┤├─┼┼──┼┤├┼─┼┤ ├──┤ ├┤│││  │││├┤││├┼┤││├┼┼┼┼─┤ ├┼┤│├┼┤├─┼┤  │├─┼┤│ ├┼┼┼┼───┤│ ├───┼──┤││├┼┤├┤     ├
┤│││├─┼─┼─┼─┤ ├┤│ ├─┼┤  ├┤│   ││ │ │├┼┼┤ ├┤││ │││├─┼┼───┼┼┤│├┤│├┤├┤├┼┼─┼┤  ││││ │├─┤  ├─┼┼┤│├──┤├┼┤││├┤├┼┼┼┤├┤││ ├─┼┼┼┼┤├┼┼─┤│  ││ ├┼┤ │├┼┼┼───┼┼─┼───┼──┼┼┤││││├─────┼
┼┤├┼┼─┤ ├─┼─┼─┤││ │ │├──┤├┤   ││ │ ├┤├┤├─┼┼┼┼─┼┤││ │├───┼┤│├┼┼┤│││││├┼─┼┼──┤││├─┤│ │  │ ├┼┼┼┼──┼┤├┼┼┼┤││├┤├┼┼┼┤├─┤ ├┤│├┼┤││ │├──┤│ │││ │││├┼───┼┼─┼───┼──┼┤├┤││├┼─────┤
┤│││├─┼─┤ ├─┼─┼┼┤ │ ││  ││├───┤│ ├─┼┼┼┼┤ ├┤├┼─┼┼┤│ ││   │├┼┤├┼┼┤││├┼┼┼─┼┤  │├┤│ │├─┼──┼─┤│││├──┤│││├┤│├┼┤├┤├┼┼┼┼─┼─┼┼┤│├┼┤│ ├┤  ├┤ │├┤ │├┼┤│   ││ │   │  ├┼┤││├┤│     │
┼┼┼┤│ │ ├─┤ ├─┼┼┼─┼─┼┼──┤││   │├─┤ ├┤├┤│ │││├─┼┤││ ││   ││├┼┤├┤│├┤│├┼┤ ├┼──┼┼┼┤ ├┼─┼──┼─┼┤├┼┤  ├┤│││├┤││││││││├┼─┤ ├┼┼┤│├┼┼─┼┼──┼┼─┼┤│ ├┤├┼┼───┤├─┼───┼──┼┼┼┼┤│││     │
┼┤├┼┼─┼─┼─┼─┼─┤├┼─┼─┤├──┼┼┼───┤│ │ │││││ ├┤├┤ ├┼┼┤ ├┼───┼┤│├┼┤│├┤├┤│││ ││  ├┼┤│ │├─┤  │ ├┼┤││  ││├┼┼┼┼┤│├┼┼┼┼┤││ │ ││├┼┤│││ ├┤  ├┤ │├┼─┼┼┤│├───┼┼─┤   ├──┤├┼┤│││├─────┼
│├┤│├─┤ ├─┤ │ ├┤│ ├─┼┤  │├┤   ├┼─┼─┼┼┼┼┤ │││├─┤├┤├─┤│   │├┤│├┼┼┼┼┤│├┤├─┼┤  │││├─┤│ │  ├─┤│├┤│  │├┼┤│├┤│├┤├┤│││├┤ │ │││││├┤├─┼┼──┤├─┼┼┤ │├┼┼┤   │├─┼───┤  ├┤├┼┼┼┼┼─────┼
```
