#Holds all important functions that control the operation of the game itself

import sys
import pygame as game
from fonts import Fonts
from random import randint

def checkEvents(char,font,enemy=0,rock=0,mineral=0,mineralList=0,boss=0):
    """Responds to keyboard and mouse events"""
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            sys.exit()
        elif event.type == game.KEYDOWN:
            checkKeyDown(event,char,font,enemy,rock,mineral,mineralList,boss)
        elif event.type == game.KEYUP:
            checkKeyUp(event,char,font,enemy,rock,mineral,mineralList,boss)
                    
def checkKeyDown(event,char,font,enemy,rock,mineral,mineralList,boss):
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
            char.name = "Rock"
            char.setImage("RockBoy.png", "RockSelect.png")
            char.name = "Rock"
        elif event.key == game.K_m:
            #select mineral girl
            char.name = "Mineral"
            char.setImage("MineralGirl.png", "MineralSelect.png")
        elif event.key == game.K_RETURN:
            #advance to overworld
            char.stage = "OVERWORLD"
    elif char.stage == "BATTLE":
        if char.battleStage == "MENU":
            if event.key == game.K_r:
                #return to overworld
                if char.power >= 2:
                    char.powerDown()
                    font.updatePower(char)
                    char.stage = "OVERWORLD"
                    char.battleStage = "MENU"
                    char.rect.left = char.rect.left+64
                    char.stopMovement()
                else:
                    char.setBattleImage("BattleHurt.png")
                    char.battleStage = "PLAYER_ACTION"
                    font.menuText = font.menuFont.render("You couldn't get away!",False,(255,255,255))
            elif event.key == game.K_y:
                #taunt
                char.battleStage = "PLAYER_ACTION"
                char.setBattleImage("BattleTaunt.png")
                char.powerUp(2)
                font.updatePower(char)
                font.menuText = font.menuFont.render('You started dancing to taunt the enemy!',False,(255,255,255))
            elif event.key == game.K_i:
                char.battleStage = "IDENTIFY"
                char.setBattleImage("BattleInfo.png")
                font.menuText = font.menuFont.render('Enter the name of the mineral into the shell!',False,(255,255,255))
            elif event.key == game.K_g:
                playerAction(char,font)
                if enemy.acid == 0:
                    font.menuText = font.menuFont.render('The mineral was not affected by the acid.',False,(255,255,255))
                elif enemy.acid == 1:
                    font.menuText = font.menuFont.render('The mineral effervesced strongly!',False,(255,255,255))
                elif enemy.acid == 2:
                    font.menuText = font.menuFont.render('The mineral effervesced weakly!',False,(255,255,255))
            elif event.key == game.K_s:
                playerAction(char,font,'The mineral produced a ' + enemy.streak + " streak!")
            elif event.key == game.K_h:
                playerAction(char,font)
                if enemy.hardness >= 5.5:
                    font.menuText = font.menuFont.render('The mineral left a scratch on the glass plate!',False,(255,255,255))
                else:
                    font.menuText = font.menuFont.render('The mineral could not scratch the glass plate!',False,(255,255,255))
            elif event.key == game.K_o:
                playerAction(char,font,'Shining a light revealed the mineral to be ' + enemy.opacity + '!')
            elif event.key == game.K_c:
                playerAction(char,font,'Tiny pieces of the mineral appear to have ' + enemy.cleavage + ' cleavage!')
            elif event.key == game.K_f:
                playerAction(char,font,'You smashed the mineral, revealing ' + enemy.fracture + ' fracture!')
            elif event.key == game.K_t:
                playerAction(char,font,'Bening the mineral, you felt a ' + enemy.tenacity + ' tenacity!')
            elif event.key == game.K_m:
                playerAction(char,font)
                if enemy.magnetic == 0:
                    font.menuText = font.menuFont.render('The mineral is not attracted to the magnet.',False,(255,255,255))
                else:
                    font.menuText = font.menuFont.render('The mineral is attracted to the magnet!',False,(255,255,255))
            elif event.key == game.K_k:
                char.battleStage = "PLAYER_ACTION"
                char.setBattleImage("BattleInfo.png")
                char.powerDown(5)
                font.updatePower(char)
                font.menuText = font.menuFont.render("SUPER KNOWLEDGE ACTIVATED: " + enemy.knowledge,False,(0,220,170))
                
        elif char.battleStage == "PLAYER_ACTION":
            if event.key == game.K_RETURN:
                char.battleStage = "ENEMY_ACTION"
                if boss == True:
                    damage = randint(3,5)
                else:
                    damage = randint(0,int(enemy.hardness))
                if damage == 0:
                    char.setBattleImage("BattleWin.png")
                    font.menuText = font.menuFont.render('The mystery mineral attacked but missed! Whew!',False, (255,255,255))
                else:
                    char.setBattleImage("BattleHurt.png")
                    font.menuText = font.menuFont.render('The mystery mineral attacked! You took ' + str(damage) + ' damage!',False,(255,255,255))
                    char.hp -= damage
                    if char.hp < 0:
                        char.hp = 0
                    font.updateHP(char)
        elif char.battleStage == "ENEMY_ACTION":
            if event.key == game.K_RETURN:
                if char.hp == 0:
                    char.battleStage = "LOSE"
                    font.menuText = font.menuFont.render("Oh no! You're done for! Press enter to return to main menu.",False,(255,255,255))
                else:
                    char.battleStage = "MENU"
                    char.setBattleImage("Battle.png")
                    font.menuText = font.menuFont.render('Red = RUN!; Yellow = Taunt; Green = Acid Test; Blue = Streak/Scratch', False, (255,255,255))
        elif char.battleStage == "LOSE":
            if event.key == game.K_RETURN:
                char.stage = "CHARACTER_SELECT"
                char.battleStage = "MENU"
                char.stopMovement()
                char.hp = 10
                font.updateHP(char)
                #font.statTextHP = font.statFont.render('HP: ' + str(char.hp), False, (255,255,255))
                font.menuText = font.menuFont.render('Red = RUN!; Yellow = Taunt; Green = Acid Test; Blue = Streak/Scratch', False, (255,255,255))
        elif char.battleStage == "IDENTIFY":
            name = input('Name: ')
            if name.lower() == enemy.name:
                char.setBattleImage("BattleWin.png")
                if boss == True:
                    change = 50
                else:
                    change = 3*enemy.hardness
                char.exp += change
                font.updateEXP(char)
                #font.statTextEXP = font.statFont.render('EXP: ' + str(char.exp), False, (255,255,255))
                font.menuText = font.menuFont.render("That's right! It's " + enemy.name + "! You gained " + str(change) + " exp!", False, (255,255,255))
                char.battleStage = "WIN"
            else:
                char.battleStage = "PLAYER_ACTION"
                font.menuText = font.menuFont.render("Uh oh, looks like that's not right!", False, (255,255,255))
        elif char.battleStage == "WIN":
            boss = False
            if event.key == game.K_RETURN:
                if char.exp >= char.lvl*10:
                    char.exp = char.exp - (char.lvl*10)
                    char.lvl = char.lvl+1
                    char.hp = 10 + 2*(char.lvl-1)
                    char.powerCap += 1
                    #font.statTextLVL = font.statFont.render('LVL: ' + str(char.lvl), False, (255,255,255))
                    #font.statTextHP = font.statFont.render('HP: ' + str(char.hp), False, (255,255,255))
                    #font.statTextEXP = font.statFont.render('EXP: ' + str(char.exp), False, (255,255,255))
                    font.menuText = font.menuFont.render("LEVEL UP! MAX HP + 2! MAX PWR + 1!", False, (255,255,255))
                    font.updateEXP(char)
                    font.updateHP(char)
                    font.updateLVL(char)
                    char.battleStage = "LEVEL_UP" 
                else:
                    char.stage = "OVERWORLD"
                    char.battleStage = "MENU"
                    font.menuText = font.menuFont.render('Red = RUN!; Yellow = Taunt; Green = Acid Test; Blue = Streak/Scratch', False, (255,255,255))
                    char.stopMovement()
                    char.removeRock(rock)
                    mineralList.append(mineral)
        elif char.battleStage == "LEVEL_UP":
            if event.key == game.K_RETURN:
                char.stage = "OVERWORLD"
                char.battleStage = "MENU"
                font.menuText = font.menuFont.render('Red = RUN!; Yellow = Taunt; Green = Acid Test; Blue = Streak/Scratch', False, (255,255,255))
                char.stopMovement()
                char.removeRock(rock)
                mineralList.append(mineral)
        #elif char.battleStage == "LEVEL_UP":
            
    elif char.stage == "PAUSE":
        if event.key == game.K_RETURN:
            char.stage = "OVERWORLD"
            char.stopMovement()
                        
def checkKeyUp(event,char,font,enemy,rock,mineral,mineralList,boss):
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

def playerAction(char,font,text="default"):
    char.battleStage = "PLAYER_ACTION"
    char.setBattleImage("BattleInfo.png")
    char.powerUp()
    font.updatePower(char)
    font.menuText = font.menuFont.render(text,False,(255,255,255))
    
def updateScreen(settings, screen, character, paths, walls, rocks, font, enemy = 0):
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
        if character.moving():
            character.walkBlit()
        else:
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
        screen.blit(font.statTextHP, (screen.get_rect().left + 10,screen.get_rect().bottom - 160))
        screen.blit(font.statTextPWR, (screen.get_rect().left + 100,screen.get_rect().bottom - 160))
        character.battleBlit()
        enemy.blit()
        
    elif character.stage == "PAUSE":
        screen.blit(font.pauseText, (screen.get_rect().left,screen.get_rect().top))
        screen.blit(font.statTextHP, (screen.get_rect().left,screen.get_rect().top + 32))
        screen.blit(font.statTextPWR, (screen.get_rect().left,screen.get_rect().top + 56))
        screen.blit(font.statTextEXP, (screen.get_rect().left,screen.get_rect().top + 80))
        screen.blit(font.statTextLVL, (screen.get_rect().left,screen.get_rect().top + 104))
        
        
    #actually display drawn window
    game.display.flip()
