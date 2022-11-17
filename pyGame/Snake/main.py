import pygame
from Game import Arena,Block,Snake

pygame.init()

arena = Arena(400,400,20,20)

snake = Snake(arena,(10,10))
snake.addTail((9,10))
isRun = True
aX = 0
aY = 0
while isRun:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    keys = pygame.key.get_pressed()

    for key in keys:
        if keys[pygame.K_RIGHT]:
            aX = 1 
            aY = 0
        elif keys[pygame.K_LEFT]:
            aX = -1
            aY = 0
        elif keys[pygame.K_UP]:
            aX = 0
            aY = -1
        elif keys[pygame.K_DOWN]:
            aX = 0
            aY = 1
    
    snake.move(aX,aY)
    arena.render(10)    

pygame.quit()

