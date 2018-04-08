#Holds all important functions that control the operation of the game itself

import sys
import pygame as game

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
    elif char.stage == "CHARACTER_SELECT":
        if event.key == game.K_r:
            #select rockboy
            char.setImage("RockBoy.png")
        elif event.key == game.K_m:
            #select mineral girl
            char.setImage("MineralGirl.png")
        elif event.key == game.K_RETURN:
            #advance to overworld
            char.stage = "OVERWORLD"
                        
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
                        
def updateScreen(settings,screen,character):
    """Updates the images on the screen and flips the new screen"""
    #fill screen with background color
    screen.fill(settings.bgColor)

    if character.stage == "OVERWORLD":
        character.blit()
    elif character.stage == "CHARACTER_SELECT":
        selectFont = game.font.SysFont('Comic Sans MS', 48)
        selectText = selectFont.render('CHARACTER SELECT', False, (255,255,255))
        rockText = selectFont.render('[R]ock Boy', False, (255,255,255))
        mineralText = selectFont.render('[M]ineral Girl', False, (255,255,255))
        screen.blit(selectText,(screen.get_rect().centerx,screen.get_rect().centery))
        screen.blit(rockText,(screen.get_rect().centerx,screen.get_rect().centery + 75))
        screen.blit(mineralText,(screen.get_rect().centerx,screen.get_rect().centery + 150))
        character.blit()
        
    #actually display drawn window
    game.display.flip()
