from Game import Block

class Snake():
    body = []
    def __init__(self,arena,start):
        self.arena = arena
        self.head = Block(arena,start)
        self.body.append(self.head)

    def addTail(self,pos):
        nBody = Block(self.arena,pos)
        self.body.append(nBody)

    def move(self,aX,aY):
        for aBody in self.body:
            aBody.move(aX,aY)
    
    def draw(self):
        for aBody in self.body:
            aBody.draw()