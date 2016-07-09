from pygame.locals import*
import pygame
import time
import random

purple=(50,30,100)
green=(30,200,150)
pink=(220,30,150)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("georgia",48)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def show_text2(msg,x,y,color):
    fontobj=pygame.font.SysFont("georgia",12)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def menu():
    kirbymenu=pygame.transform.scale(pygame.image.load('kirby'+str(random.randint(1,19))+'.png'),(60,60))
    for n in range(0,500,1):
        screen.blit(kirbymenu,(random.randint(0,600),random.randint(65,400)))
    pygame.draw.rect(screen,(32,221,3),(250,100,100,50))
    pygame.draw.rect(screen,(211,4,66),(250,300,100,50))
    show_text("Start",255,95,(0,0,0))
    show_text("Quit",255,295,(0,0,0))
    show_text("Kirby",250,25,(255,70,40))
    show_text2("Developed by: Ryan Tseng",500,460,(255,255,255))
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                if 250<=event.pos[0]<=350 and 100<=event.pos[1]<=200:
                    print('press')
                if 250<=event.pos[0]<=350 and 300<=event.pos[1]<=350:
                    print('press')
            elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
                if 250<=event.pos[0]<=350 and 100<=event.pos[1]<=200:
                    screen.fill((0,0,0))
                    game()
                if 250<=event.pos[0]<=350 and 300<=event.pos[1]<=350:
                    screen.fill((0,0,0))
                    pygame.quit()
                    exit()
class kirby:
    def __init__(self,x,y):
        self.img=[]
        self.x=x
        self.y=y
        self.i=0
        for n in range(0,19,1):
            self.img.append(pygame.image.load('kirby'+str(n+1)+'.png'))
    def kirbyrefresh(self):
        screen.blit(self.img[self.i],(self.x,self.y))
    def moveright(self):
        self.x=self.x+10
        self.i=self.i+1
        if self.i>14:
            self.i=0
    def moveup(self):
        self.y=self.y-15
        self.i=self.i+1
        if self.i<15:
            self.i=14
        if self.i==18:
            self.i=15
class platforms:
    def __init__(self):
        self.r1=(0,420,100,480)
        self.r2=(100,300,100,480)
        self.r3=(200,200,150,480)
        self.r4=(350,100,645,480)
    def DrawPlatform(self):
        pygame.draw.rect(screen,(225,225,225),self.r1)
        pygame.draw.rect(screen,purple,self.r2)
        pygame.draw.rect(screen,green,self.r3)
        pygame.draw.rect(screen,pink,self.r4)
    def RedrawPlatform(self):
        self.r1=(0,300,random.randint(100,160),480)
        self.r2=(random.randint(170,190),random.randint(201,300),random.randint(80,140),480)
        self.r3=(random.randint(330,360),random.randint(101,200),random.randint(50,120),480)
        self.r4=(random.randint(470,520),random.randint(50,100),640,480)
def game():
    img=[]
    k1=kirby(0,400)
    n=0
    k=15
    x=0
    w=3
    up=0
    right=0
    y=400
    l=[]
    s=0
    j=0
    h=0
    t=3
    for n in range(0,3,1):
        l.append(pygame.image.load('kirby1.png'))

    fpsclock=pygame.time.Clock()
    for n in range(0,19,1):
        img.append(pygame.image.load('kirby'+str(n+1)+'.png'))
    p=platforms()

    while True:
        k1.kirbyrefresh()
        for a in range(len(l)):
            screen.blit(l[a],(10+30*a,10))
        pygame.display.update()
        fpsclock.tick(10)
        for event in pygame .event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    up=1
                if event.key==K_RIGHT:
                    right=1
            elif event.type==KEYUP:
                if event.key==K_RIGHT:
                   right=0
                if event.key==K_UP:
                    up=0
        screen.fill((0,0,0))
        p.DrawPlatform()

        if k1.y==0:
            k1.x=0
            k1.y=p.r1[1]+20
        if 0<k1.x+15<p.r1[2]:
            if k1.y+20<p.r1[1]:
                k1.y=k1.y+5
        if p.r2[0]<k1.x+20<p.r3[0]:
            if k1.y+20<p.r2[1]:
                k1.y=k1.y+5
        if p.r3[0]<k1.x+20<p.r4[0]:
            if k1.y+20<p.r3[1]:
                k1.y=k1.y+5
        if p.r4[0]<k1.x+20<p.r4[0]+p.r4[2]:
            if k1.y+20<p.r4[1]:
                k1.y=k1.y+5

        if p.r1[2]<k1.x<p.r2[0]:
            k1.y=k1.y+5
        if p.r2[0]+p.r2[2]<k1.x<p.r3[0]:
            k1.y=k1.y+5
        if p.r3[0]+p.r3[2]<k1.x<p.r4[0]:
            k1.y=k1.y+5
            
        if right and (k1.x+20<p.r2[0]): 
            k1.moveright()
        if right and (k1.y < p.r2[1]and k1.x+20<p.r3[0]):
            k1.moveright()
        if right and (k1.y<p.r3[1] and k1.x+20<p.r4[0]):
            k1.moveright()
        if right and (k1.y<p.r4[1] and k1.x+20<700):
            k1.moveright()
            
        if up:
            k1.moveup()
        show_text("score:"+str(s),100,10,(100,220,0))
        if k1.y>480:
            k1.x=0
            k1.y=250
            l.pop(0)
            t=t-1
        if t==0:
            t=3
            k1.x=0
            k1.y=250
            p.RedrawPlatform()
            for n in range(0,3,1):
                l.append(pygame.image.load('kirby1.png'))
            s=0
            screen.fill((0,0,0))
            menu()
        if k1.x>640:
            s=s+50
            k1.x=0
            k1.y=270
            p.RedrawPlatform()
            
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('menu')

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            exit()
    menu()
    
