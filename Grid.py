from Node import Node

class Grid:
    # init, you can create an empty grid if you specify initialize with true
    def __init__(self, height=0, width=0, initialize=False):
        self.root = None
        self.height = height
        self.width = width

        if initialize:
            self.root = Node()
            current = self.root
            for i in range(width):
                current.right = Node()

                more = current
                for i in range(height):
                    more.bottom = Node()
                    more.bottom.top = more
                    if more.left != None:
                        if more.left.bottom != None:
                            more.bottom.left = more.left.bottom
                            more.left.bottom.right = more.bottom
                    more = more.bottom
                current = current.right

    def printgrid(self):
        current = self.root
        while current != None:
            more = current
            while more != None:
                print(more, end="")
                more = more.right
            current = current.bottom
            print("", end="\n")
            


a = Grid(5,5,True)
a.printgrid()
print(a.root.bottom.right)
