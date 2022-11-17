import pygame
class Arena():

    def __init__(self,wArena,hArena,jBaris,jKolom):
        pygame.init()
        self.wArena = wArena
        self.hArena = hArena
        self.jBaris = jBaris
        self.jKolom = jKolom 
        self.mKolom = self.wArena // self.jBaris
        self.mBaris = self.hArena // self.jKolom
        self.clock = pygame.time.Clock()
        self.objects = []

        self.window = pygame.display.set_mode((self.wArena,self.hArena))

    def assign(self,object):
        self.objects.append(object)

    def get_window(self):
        return self.window

    def get_mKolom(self):
        return self.mKolom

    def get_mBaris(self):
        return self.mBaris

    def get_jKolom(self):
        return self.jKolom

    def get_jBaris(self):
        return self.jBaris

    def drawGrid(self):

        for barisKe in range(self.jBaris):
            x = self.mBaris*barisKe
            y = self.mKolom*barisKe
            pygame.draw.line(self.window,(182, 226, 161),(x,0),(x,self.hArena))
            pygame.draw.line(self.window,(182, 226, 161),(0,y),(self.wArena,y))   

    def render(self,fps):
        self.window.fill((182, 226, 161))
        for obj in self.objects:
            obj.draw()

        self.drawGrid()
        pygame.display.update()
        pygame.time.delay(100)
        self.clock.tick(fps)