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
    
    character = boy(screen)

    #main loop for game
    while True:
        gf.checkEvents(character)
        if character.stage == "OVERWORLD":
            character.updatePos()
        gf.updateScreen(settings, screen, character)
                
runGame()
 
