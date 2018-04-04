#testing out some stuff for rock boy
import sys
import pygame as game
from settings import Settings
from rockboy import RockBoy as boy
import gameFunctions as gf

def runGame():
    """Runs the game, duh!"""
    #initialize window and such
    settings = Settings()
    game.init()
    game.font.init()
    screen = game.display.set_mode((settings.screenWidth,settings.screenHeight))
    game.display.set_caption(settings.title)
    stage = "CHARACTER_SELECT"

    #select character
    selectFont = game.font.SysFont('Comic Sans MS', 30)
    selectText = selectFont.render('CHARACTER SELECT', False, (255,255,255))
    
    while True:

        select = input('CHARACTER SELECT:\n[R]ock Boy\n[M]ineral Girl').lower()
        if select == 'r':
            fileName = 'RockBoy.png'
            break
        elif select == 'm':
            fileName = 'MineralGirl.png'
            break

    character = boy(screen,fileName)

    #main loop for game
    while True:
        gf.checkEvents(character, stage)
        character.updatePos()
        gf.updateScreen(settings, screen, character, stage)
        screen.blit(selectText,(screen.get_rect().centerx,screen.get_rect().centery))
                
runGame()
 
