from pygame.locals import*
import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('menu')
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen,(32,221,3),(300,100,100,100),10)
    pygame.draw.rect(screen,(211,4,66),(300,300,100,100),10)
