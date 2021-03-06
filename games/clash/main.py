import pygame
import time
import windowFramework
import os
from PIL import Image


#class layout (time, damage, towers...)
#class heroes
#class level

pygame.init()
relog = pygame.time.Clock()

global esquivar
global golpear
global init

esquivar = False
golpear = False
init = False


class level_frame:
    def __init__(self, width, height, window):
        self.width, self.height = width, height
        self.window = window

        self.dirt = pygame.image.load("tools/map/dirt.png")
        self.dirtWidth, self.dirtHeight = self.dirt.get_width(), self.dirt.get_height()
        self.dirtX, self.dirtY = 0, (self.height/2 - self.dirtHeight/2) 

        pathMap = "tools/map"
        self.mountain = pygame.image.load("{}/mountain.png".format(pathMap))
        self.mountain = pygame.transform.scale(self.mountain, (1200, 200))
        self.mountainWidth, self.mountainHeight = self.mountain.get_width(), self.mountain.get_height()
        self.xMountain, self.yMountain = 0, 0 

        self.yDownMountain = self.height - self.mountainHeight

    def draw(self):
        self.window.blit(self.dirt, (self.dirtX, self.dirtY))
        self.window.blit(self.mountain, (self.xMountain, self.yMountain))
        self.window.blit(self.mountain, (self.xMountain, self.yDownMountain)) 

    def getY(self):
        return self.yDownMountain

class heroes_frame:
    def __init__(self, width, height, window):
        pygame.sprite.Sprite.__init__(self)

        self.width, self.height = width, height
        self.window = window
        self.xInicial, self.yInicial = 100, (self.height/2 - level.dirtY/2)
        self.x, self.y = self.xInicial, self.yInicial

        self.count = 0
        self.end = False
        self.run = False 
        pathIdle = "tools/sprites/ninja/idle"
        pathWalk = "tools/sprites/ninja/walk"
        self.idle = Image.open("{}/idle1.png".format(pathIdle))
        self.idleWidth, self.idleHeight = self.idle.size
        
        self.idle = [pygame.image.load("{}/idle1.png".format(pathIdle)), pygame.image.load("{}/idle1.png".format(pathIdle)), pygame.image.load("{}/idle1.png".format(pathIdle)),
                    pygame.image.load("{}/idle1.png".format(pathIdle)), pygame.image.load("{}/idle2.png".format(pathIdle)), pygame.image.load("{}/idle2.png".format(pathIdle)),
                    pygame.image.load("{}/idle2.png".format(pathIdle)), pygame.image.load("{}/idle2.png".format(pathIdle)), pygame.image.load("{}/idle3.png".format(pathIdle)),
                    pygame.image.load("{}/idle3.png".format(pathIdle)), pygame.image.load("{}/idle3.png".format(pathIdle)), pygame.image.load("{}/idle3.png".format(pathIdle))] 

        self.walk = [pygame.image.load("{}/walk1.png".format(pathWalk)), pygame.image.load("{}/walk1.png".format(pathWalk)), pygame.image.load("{}/walk2.png".format(pathWalk)),
                    pygame.image.load("{}/walk2.png".format(pathWalk)), pygame.image.load("{}/walk2.png".format(pathWalk)), pygame.image.load("{}/walk2.png".format(pathWalk)),
                    pygame.image.load("{}/walk3.png".format(pathWalk)), pygame.image.load("{}/walk3.png".format(pathWalk)), pygame.image.load("{}/walk4.png".format(pathWalk)), 
                    pygame.image.load("{}/walk4.png".format(pathWalk)), pygame.image.load("{}/walk5.png".format(pathWalk)), pygame.image.load("{}/walk5.png".format(pathWalk))]

        self.heroe = pygame.image.load("{}/idle1.png".format(pathIdle))
        self.rect = self.heroe.get_rect() 
        self.rect.x = self.x
        self.rect.y = self.y

        self.collision = False
        self.layout = layout_frame(window, width, height, self.rect.x, self.rect.y)
        

    def movement(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_SPACE]:
            self.run = True
       

        if self.run:
            if self.rect.x < self.width - self.idleWidth:
                if not(self.end):
                    self.rect.x += 10

            else:
                self.end = True

            if self.end:
                self.rect.x -= 10
                
                if self.rect.x < 0:
                    self.end = False
        
        global esquivar
        if esquivar:
            self.rect.y += 50
            esquivar = False


        return self.run
    

    def draw(self):
        if not(self.run) and not(self.end): 
            self.window.blit(self.idle[self.count], (self.rect.x, self.rect.y))
            self.count += 1

        else:
            if not(self.end):
                self.window.blit(self.walk[self.count], (self.rect.x, self.rect.y))
                self.count += 1

        if self.count == 12:
            self.count = 0


    def collide(self, enemy):
        global init
        if self.rect.colliderect(enemy):
            self.collision = True

        if self.collision:
            self.rect.x = self.width/2 - 200 #temp data
            init = True
            self.collision = False
            self.run = False

        return self.run
            
        

class enemies_frame:
    def __init__(self, window, width, height):
        pygame.sprite.Sprite.__init__(self)
        

        pathIdle = "tools/sprites/ninja/idle"
        pathWalk = "tools/sprites/ninja/walk"
        self.idle = Image.open("{}/idle1.png".format(pathIdle))
        self.idleWidth, self.idleHeight = self.idle.size
        
        self.window = window
        self.width, self.height = width, height

        self.idleLeft = [pygame.image.load("{}/idle1flop.png".format(pathIdle)), pygame.image.load("{}/idle1flop.png".format(pathIdle)), 
                    pygame.image.load("{}/idle1flop.png".format(pathIdle)), pygame.image.load("{}/idle1flop.png".format(pathIdle)), 
                    pygame.image.load("{}/idle2flop.png".format(pathIdle)), pygame.image.load("{}/idle2flop.png".format(pathIdle)), 
                    pygame.image.load("{}/idle2flop.png".format(pathIdle)), pygame.image.load("{}/idle2flop.png".format(pathIdle)), 
                    pygame.image.load("{}/idle2flop.png".format(pathIdle)), pygame.image.load("{}/idle2flop.png".format(pathIdle)), 
                    pygame.image.load("{}/idle3flop.png".format(pathIdle)), pygame.image.load("{}/idle3flop.png".format(pathIdle)), 
                    pygame.image.load("{}/idle3flop.png".format(pathIdle)), pygame.image.load("{}/idle3flop.png".format(pathIdle))] 

        self.walkLeft = [pygame.image.load("{}/walk1flop.png".format(pathWalk)), pygame.image.load("{}/walk1flop.png".format(pathWalk)), 
                    pygame.image.load("{}/walk2flop.png".format(pathWalk)), pygame.image.load("{}/walk2flop.png".format(pathWalk)), 
                    pygame.image.load("{}/walk2flop.png".format(pathWalk)), pygame.image.load("{}/walk2flop.png".format(pathWalk)),
                    pygame.image.load("{}/walk3flop.png".format(pathWalk)), pygame.image.load("{}/walk3flop.png".format(pathWalk)), 
                    pygame.image.load("{}/walk4flop.png".format(pathWalk)), pygame.image.load("{}/walk4flop.png".format(pathWalk)), 
                    pygame.image.load("{}/walk5flop.png".format(pathWalk)), pygame.image.load("{}/walk5flop.png".format(pathWalk))]
        
        self.x, self.y = (self.width - 100) - self.idleWidth, self.height/2 - level.dirtY/2,

        self.enemy = pygame.image.load("{}/idle1flop.png".format(pathIdle))
        self.enemyRect = self.enemy.get_rect() 
        self.enemyRect.x = self.x 
        self.enemyRect.y = self.y

        self.count = 0
        self.runE = False

        
    def start(self):

        halfScreen = self.width/2
        if hero.run:

            if self.enemyRect.x >= halfScreen + (self.idleWidth / 4):
                self.enemyRect.x -= 10
                self.runE = True

            else:
                self.runE = False

        #print (halfScreen + self.idleWidth, self.enemyRect.x)





    def draw(self):
        if not (self.runE):
            self.window.blit(self.idleLeft[self.count], (self.enemyRect.x, self.enemyRect.y))
            self.count += 1

        else:
            self.window.blit(self.walkLeft[self.count], (self.enemyRect.x, self.enemyRect.y))
            self.count += 1

        if self.count == 12:
            self.count = 0

class layout_frame:
    def __init__(self, window, width, height, heroX, heroY):
        self.window = window
        self.width, self.height = width, height

        path = "tools/images"
        self.golpearWindow = pygame.image.load("{}/golpear_window.jpg".format(path))
        self.golpearRect = self.golpearWindow.get_rect()

        self.golpearHeight = self.golpearWindow.get_height()
        self.golpearWidth = self.golpearWindow.get_width()

        self.esquivarWindow = pygame.image.load("{}/esquivar_window.jpg".format(path))
        self.esquivarRect = self.esquivarWindow.get_rect()

        self.esquivarHeight = self.esquivarWindow.get_height()
        self.esquivarWidth = self.esquivarWindow.get_width()

        self.level = level_frame(width, height, window)
        self.yDownMountain = level.getY()

        self.golpearRect.x, self.golpearRect.y =  200, (self.height - self.yDownMountain/2) + (self.golpearHeight/2)
        self.esquivarRect.x, self.esquivarRect.y  = self.width - (self.esquivarWidth + 200), (self.height - self.yDownMountain/2) + (self.esquivarHeight/2)

        pathBar = "tools/sprites/barra_stat"
        self.barStatus = [pygame.image.load("{}/vida_100.jpg".format(pathBar)), pygame.image.load("{}/vida_75.jpg".format(pathBar)), 
                        pygame.image.load("{}/vida_50.jpg".format(pathBar)), pygame.image.load("{}/vida_25.jpg".format(pathBar)),
                        pygame.image.load("{}/vida_0.jpg".format(pathBar))]

        self.barCountH = 0
        self.barCountE = 0


    def draw(self):
        global init
        if init:
            self.window.blit(self.golpearWindow, (self.golpearRect.x, self.golpearRect.y))
            self.window.blit(self.esquivarWindow, (self.esquivarRect.x, self.esquivarRect.y))

        self.window.blit(self.barStatus[self.barCountH], (hero.rect.x, hero.rect.y - 50)) #puedes llamar directamente a la variable contenedora de la clase y ejecutar.
        self.window.blit(self.barStatus[self.barCountE], (enemy.enemyRect.x, enemy.enemyRect.y - 50)) #puedes llamar directamente a la variable contenedora de la clase y ejecutar.
                                                                                    
    def checkCollision(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #print(pos)

                if pos[0] > self.golpearRect.x and pos[0] < (self.golpearRect.x + self.golpearWidth):
                    if pos[1] > self.golpearRect.y and pos[1] < (self.golpearRect.y + self.golpearHeight):
                        self.barCountE += 1
                        

                        #CODIGO EJECUTAR GOLPEO
                
                if pos[0] > self.esquivarRect.x and pos[0] < (self.esquivarRect.x + self.esquivarWidth):
                    if pos[1] > self.esquivarRect.y and pos[1] < (self.esquivarRect.y + self.esquivarHeight):
                        global esquivar
                        esquivar = True

                        #CODIGO EJECUTAR ESQUIVE

                
window = windowFramework.window()
level = level_frame(window.width, window.height, window.window)
hero = heroes_frame(window.width, window.height, window.window) 
enemy = enemies_frame(window.window, window.width, window.height)
layout = layout_frame(window.window, window.width, window.height, hero.rect.x, hero.rect.y)

while not window.endFrame():
    level.draw()
    hero.draw()
    hero.movement()
    hero.collide(enemy.enemyRect)
    layout.draw()
    layout.checkCollision()
    enemy.draw()
    enemy.start()
    window.updateFrame()
    window.fillWindow()
    relog.tick(20)

