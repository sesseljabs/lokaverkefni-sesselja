from Node import Node
from Grid import Grid
import os
from time import sleep

# þetta er að mestu example hvernig þetta virkar, en keyrir gosper's glider gun

listi = [ # dæmi um lista
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]


a = Grid(18,38)
a.listfromfile("grid.txt")
a.gridrun()