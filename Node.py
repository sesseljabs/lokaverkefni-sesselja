class Node:
    def __init__(self):
        self.state = False
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def chngstate(self):
        self.state = not self.state

    def check(self):
        total = 0
        if self.top != None:
            total += int(self.top.state)
            if self.top.right!= None:
                total += int(self.top.right.state)
            if self.top.left != None:
                total += int(self.top.left.state)
        if self.bottom != None:
            total += int(self.bottom.state)
            if self.bottom.right != None:
                total += int(self.bottom.right.state)
            if self.bottom.left != None:
                total += int(self.bottom.left.state)
        if self.right != None:
            total += int(self.right.state)
        if self.left != None:
            total += int(self.left.state)
                
        return total
    def delete(self):
        if self.top:
            if self.top.bottom:
                self.top.bottom = None
        if self.left:
            if self.left.right:
                self.left.right = None
        if self.right:
            if self.right.left:
                self.right.left = None
        if self.bottom:
            if self.bottom.top:
                self.bottom.top = None
        self = None
    def __str__(self):
        if self.state:
            return " ■ "
        else:
            return " # "

