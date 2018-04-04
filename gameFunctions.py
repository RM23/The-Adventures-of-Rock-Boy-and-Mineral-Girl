#Holds all important functions that control the operation of the game itself

import sys
import pygame as game

def checkEvents(char,stage):
    """Responds to keyboard and mouse events"""
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            sys.exit()
        elif event.type == game.KEYDOWN:
            checkKeyDown(event,char,stage)
        elif event.type == game.KEYUP:
            checkKeyUp(event,char,stage)
                    
def checkKeyDown(event, char,stage):
    """Handles events that occur when player presses keys down"""
    if event.key == game.K_RIGHT:
        #move character right
        char.movingRight = True
        if char.movingLeft:
            char.movingLeft = False
    elif event.key == game.K_LEFT:
        #move character left
        char.movingLeft = True
        if char.movingRight:
            char.movingRight = False
    elif event.key == game.K_DOWN:
        #move character down
        char.movingDown = True
        if char.movingUp:
            char.movingUp = False
    elif event.key == game.K_UP:
        char.movingUp = True
        if char.movingDown:
            char.movingDown = False
                        
def checkKeyUp(event, char,stage):
    """Handles events that occur when player releases keys"""
    if event.key == game.K_RIGHT:
        char.movingRight = False
    elif event.key == game.K_LEFT:
        char.movingLeft = False
    elif event.key == game.K_DOWN:
        char.movingDown = False
    elif event.key == game.K_UP:
        char.movingUp = False
                    
def updateScreen(settings, screen, character,stage):
    """Updates the images on the screen and flips the new screen"""
    #fill screen with background color
    screen.fill(settings.bgColor)
    character.blit()

    #actually display drawn window
    game.display.flip()
