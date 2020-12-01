from Node import Node

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
    
    def frame(self):
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


    def printgrid(self):
        current = self.root
        while current != None:
            more = current
            while more != None:
                print(more, end="")
                more = more.right
            current = current.bottom
            print("", end="\n")
            


listi = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]
a = Grid(5,5)
a.copylist(listi)
a.printgrid()
a.frame()
print("\n\n")
a.printgrid()

