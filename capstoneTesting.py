#testing out some stuff for rock boy
import sys
import pygame as game
from settings import Settings
from rockboy import RockBoy as boy
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

    #create a path
    pathList = []
    for i in range(0,10):
        path = Tile('OverworldPath.png',screen.get_rect().centerx,screen.get_rect().centery + (i*32),screen,0)
        pathList.append(path)

    #create a wall
    wallList = []
    for i in range(0,8):
        for j in range(0,8,2):
            wall = Tile('OverworldWall.png',(screen.get_rect().centerx*1.5)+(i*32),(screen.get_rect().centery*1.5)+(j*32),screen,1)
            wallList.append(wall)

    #main loop for game
    while True:
        gf.checkEvents(character)
        if character.stage == "OVERWORLD":
            character.checkCollision(wallList)
            character.updatePos()
        gf.updateScreen(settings, screen, character, pathList, wallList)
                
runGame()
 
