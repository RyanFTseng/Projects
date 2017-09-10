from pygame.locals import* 
import pygame
import time
import random

def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",26)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def menu():
    pygame.draw.rect(screen,(32,221,3),(250,100,100,50))
    pygame.draw.rect(screen,(211,4,66),(250,300,100,50))
    show_text("Start",255,95,(0,0,0))
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        if 250<=event.pos[0]<=350 and 100<=event.pos[1]<=200:
            print('press')
        if 250<=event.pos[0]<=350 and 300<=event.pos[1]<=350:
            print('press')
    elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
        if 250<=event.pos[0]<=350:
            screen.fill((0,0,0))
            game()


screen=pygame.display.set_mode((640,480))
pygame.init()
menu()
