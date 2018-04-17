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
            char.movingRight = False
            char.movingLeft = False
            char.movingUp = False
            char.movingDown = False
                        
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
                        
def updateScreen(settings,screen,character,paths,walls, rocks):
    """Updates the images on the screen and flips the new screen"""
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
        selectFont = game.font.SysFont('Comic Sans MS', 48)
        selectText = selectFont.render('CHARACTER SELECT', False, (255,255,255))
        rockText = selectFont.render('[R]ock Boy', False, (255,255,255))
        mineralText = selectFont.render('[M]ineral Girl', False, (255,255,255))
        screen.blit(selectText,(screen.get_rect().centerx,screen.get_rect().centery))
        screen.blit(rockText,(screen.get_rect().centerx,screen.get_rect().centery + 75))
        screen.blit(mineralText,(screen.get_rect().centerx,screen.get_rect().centery + 150))
        character.selectBlit()

    elif character.stage == "BATTLE":
        screen.fill(settings.battleBg)
        battleFont = game.font.SysFont('Comic Sans MS', 32)
        menuFont = game.font.SysFont('Comic Sans MS', 24)
        battleText = battleFont.render('IDENTIFY THAT MINERAL!', False, (255,255,255))
        menuText = menuFont.render('Red = RUN!; Yellow = Taunt; Green = Acid Test; Blue = Streak/Scratch', False, (255,255,255))
        screen.blit(menuText, (screen.get_rect().left,screen.get_rect().top+32))
        screen.blit(battleText, (screen.get_rect().left,screen.get_rect().top))
        
        
    #actually display drawn window
    game.display.flip()
