from Node import Node
import os
from time import sleep

class Grid:
    # init, you can create an empty grid if you specify initialize with true
    def __init__(self, height=0, width=0):
        self.root = None
        self.height = height
        self.width = width

        self.root = Node()
        current = self.root
        for i in range(width):

            more = current
            for j in range(height-1):
                more.bottom = Node()
                more.bottom.top = more
                if more.top != None:
                    if more.top.left != None:
                        more.left = more.top.left.bottom
                if more.left != None:
                    if more.left.bottom != None:
                        more.bottom.left = more.left.bottom
                        more.left.bottom.right = more.bottom
                more = more.bottom
            prev = current
            if i < width-1:
                current.right = Node()
                current = current.right
                current.left = prev
    
    def copylist(self, listi): # has to be nested list with the same width and height as specified
        x = 0
        y = 0
        current = self.root
        while current != None:
            
            more = current
            x = 0
            while more != None:
                more.state = bool(listi[y][x])
                more = more.right
                x+=1
            current = current.bottom
            y+=1
    def listfromfile(self, filename): #takes grid from txt file
        # file has to be txt with 0 or 1 depending on state and a space between all numbers
        with open(filename,'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].rstrip("\n")
                lines[i] = lines[i].split(sep=" ")
                lines[i] = list(map(int,lines[i]))


            self.copylist(lines)
    
    def frame(self): # calculates every node
        new = [[0 for i in range(self.width)] for i in range(self.height)]
        x = 0
        y = 0
        current = self.root
        while current != None:
            more = current
            x = 0
            while more != None:
                num = more.check()
                if more.state == True:
                    if num < 2:
                        new[y][x] = 0
                    elif num > 3:
                        new[y][x] = 0
                    else:
                        new[y][x] = 1
                elif more.state == False:
                    if num == 3:
                        new[y][x] = 1
                    else:
                        new[y][x] = 0
                more = more.right
                x+=1
            current = current.bottom
            y+=1
        current = self.root
        for i in range(len(new)):
            more = current
            for j in range(len(new[i])):
                more.state = bool(new[i][j])

                more = more.right
            current = current.bottom


    def printgrid(self): # prints the grid
        current = self.root
        while current != None:
            more = current
            while more != None:
                print(more, end="")
                more = more.right
            current = current.bottom
            print("", end="\n")

    def gridrun(self, generations=-1): #optional, generation specifies how often to update, -1 means forever
        count = 0
        while count <= generations or generations == -1:
            self.printgrid()
            sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.frame()

