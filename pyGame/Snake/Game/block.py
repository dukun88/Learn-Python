import pygame

class Block():

    def __init__(self,arena,posA,aX=1,aY=1,col=(255,0,0)):
        self.pos = posA
        self.aX = aX
        self.aY = aY
        self.col = col
        self.winddow = arena.get_window()
        self.lebar = arena.get_mKolom()
        self.tinggi = arena.get_mBaris()
        self.arena = arena
        arena.assign(self)

    def move(self,aX,aY):
        self.aX = aX
        self.aY = aY
        self.pos = (self.pos[0]+self.aX, self.pos[1]+self.aY)
    
        if self.pos[0] == self.arena.get_jKolom():
            self.pos = (0,self.pos[1])
        elif self.pos[0] < 0:
            self.pos = (self.arena.get_jKolom()-1,self.pos[1])

        if self.pos[1] == self.arena.get_jBaris():
            self.pos = (self.pos[0],0)
        elif self.pos[1] < 0:
            self.pos = (self.pos[0],self.arena.get_jBaris()-1)

    def draw(self):
        startX = self.lebar*self.pos[0]
        startY = self.tinggi*self.pos[1]

        pygame.draw.rect(self.winddow, self.col,(startX,startY,self.lebar,self.tinggi))