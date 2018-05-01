#testing out some stuff for rock boy
import sys
from random import randint
import pygame as game
from settings import Settings
from rockboy import RockBoy as boy
from rock import Rock
from fonts import Fonts
from tiles import Tile
import gameFunctions as gf

def runGame():
    """Runs the game, duh!"""
    #initialize window and such
    settings = Settings()
    game.init()
    game.font.init()
    screen = game.display.set_mode((settings.screenWidth,settings.screenHeight))
    game.display.set_caption(settings.title)
    
    character = boy(screen)

    game.display.set_icon(character.image)
    
    font = Fonts(character)

    total = 2

    #create a path
    pathList = []
    for i in range(0,20):
        path = Tile('OverworldPath.png',screen.get_rect().centerx,screen.get_rect().bottom - (i*32),screen,0)
        pathList.append(path)

    #create a wall
    wallList = []
    for i in range(0,8):
        for j in range(0,8,2):
            wall = Tile('OverworldWall.png',(screen.get_rect().centerx*1.5)+(i*32),(screen.get_rect().centery*1.5)+(j*32),screen,1)
            wallList.append(wall)
    for i in range(0,15):
        wall = Tile('OverworldWall.png',240,0+(32*i),screen,1)
        wallList.append(wall)
    for i in range(0,4):
        wall = Tile('OverworldWall.png',272+(32*i),96+(32*i),screen,1)
        wallList.append(wall)

    #generate some rocks
    rockList = []
    for i in range (0,total):
        randX = randint(0,1200-32)
        randY= randint(0,800-32)
        rock = Tile('OverworldRock.png',randX,randY,screen,1)
        rockList.append(rock)

    usedMinerals = []
    mineral = -1

    bossPresent = False
    bossCounter = 0
        
    #main loop for game
    while True:
        if len(usedMinerals)%total == 0 and bossPresent == False and len(usedMinerals) != 0:
            boss1 = Tile('BossRock.png',583,120,screen,1)
            bossPresent = True
            bossCounter += 1
            while len(rockList) > 0:
                rockList.pop()
            rockList.append(boss1)
          
        if character.stage == "OVERWORLD":
            character.walkAnimate()
            character.checkCollision(wallList)
            if character.checkCollision(rockList) == True:
                while True:
                    mineral = randint(1,10)
                    if mineral not in usedMinerals:
                        break
                if bossPresent == True:
                    enemy = Rock(11*bossCounter,screen)
                else:
                    enemy = Rock(mineral,screen)
                character.stage = "BATTLE"
                character.setBattleImage("Battle.png")
            character.updatePos()
        if character.stage == "BATTLE":
            gf.checkEvents(character,font,enemy,rockList,mineral,usedMinerals,bossPresent)
            gf.updateScreen(settings, screen, character, pathList, wallList, rockList, font, enemy)
        else:
            gf.checkEvents(character,font)
            gf.updateScreen(settings, screen, character, pathList, wallList, rockList, font)
        #print(character.hp)
                
runGame()
 
