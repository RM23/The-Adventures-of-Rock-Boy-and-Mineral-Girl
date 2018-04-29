#Holds all important functions that control the operation of the game itself

import sys
import pygame as game
from fonts import Fonts

def checkEvents(char):
    """Responds to keyboard and mouse events"""
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            sys.exit()
        elif event.type == game.KEYDOWN:
            checkKeyDown(event,char)
        elif event.type == game.KEYUP:
            checkKeyUp(event,char)
                    
def checkKeyDown(event,char):
    """Handles events that occur when player presses keys down"""
    if char.stage == "OVERWORLD":
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
            #move character up
            char.movingUp = True
            if char.movingDown:
                char.movingDown = False
        elif event.key == game.K_RETURN:
            char.stage = "PAUSE"
    elif char.stage == "CHARACTER_SELECT":
        if event.key == game.K_r:
            #select rockboy
            char.setImage("RockBoy.png", "RockSelect.png")
        elif event.key == game.K_m:
            #select mineral girl
            char.setImage("MineralGirl.png", "MineralSelect.png")
        elif event.key == game.K_RETURN:
            #advance to overworld
            char.stage = "OVERWORLD"
    elif char.stage == "BATTLE":
        if event.key == game.K_r:
            #return to overworld
            char.stage = "OVERWORLD"
            char.rect.left = char.rect.left+64
            char.stopMovement()
    elif char.stage == "PAUSE":
        if event.key == game.K_RETURN:
            char.stage = "OVERWORLD"
            char.stopMovement()
                        
def checkKeyUp(event, char):
    """Handles events that occur when player releases keys"""
    if char.stage == "OVERWORLD":
        if event.key == game.K_RIGHT:
            char.movingRight = False
        elif event.key == game.K_LEFT:
            char.movingLeft = False
        elif event.key == game.K_DOWN:
            char.movingDown = False
        elif event.key == game.K_UP:
            char.movingUp = False
                        
def updateScreen(settings, screen, character, paths, walls, rocks, enemy = 0):
    """Updates the images on the screen and flips the new screen"""
    font = Fonts(character)
    #fill screen with background color
    screen.fill(settings.bgColor)

    if character.stage == "OVERWORLD":
        #draw path tiles
        for i in paths:
            i.blit()

        #draw wall tiles
        for i in walls:
            i.blit()

        #draw rock tiles
        for i in rocks:
            i.blit()

        #draw character
        character.blit()

    elif character.stage == "CHARACTER_SELECT":
        screen.blit(font.selectText,(screen.get_rect().centerx,screen.get_rect().centery))
        screen.blit(font.rockText,(screen.get_rect().centerx,screen.get_rect().centery + 75))
        screen.blit(font.mineralText,(screen.get_rect().centerx,screen.get_rect().centery + 150))
        character.selectBlit()

    elif character.stage == "BATTLE":
        screen.fill(settings.battleBg)
        screen.blit(font.menuText, (screen.get_rect().left,screen.get_rect().top+32))
        screen.blit(font.battleText, (screen.get_rect().left,screen.get_rect().top))
        enemy.blit()
    elif character.stage == "PAUSE":
       
        screen.blit(font.pauseText, (screen.get_rect().left,screen.get_rect().top))
        screen.blit(font.statTextHP, (screen.get_rect().left,screen.get_rect().top + 32))
        screen.blit(font.statTextLVL, (screen.get_rect().left,screen.get_rect().top + 56))
        screen.blit(font.statTextEXP, (screen.get_rect().left,screen.get_rect().top + 80))

        
        
    #actually display drawn window
    game.display.flip()
