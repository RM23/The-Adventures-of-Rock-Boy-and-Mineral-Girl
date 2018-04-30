#file for storing the many fonts used in the game in different menus

import pygame as game

class Fonts():
    def __init__(self,character):
        
        self.red = (200,0,0)
        self.green = (0,200,0)
        self.white = (255,255,255)
        
        #fonts for character select screen
        self.selectFont = game.font.SysFont('Comic Sans MS', 48)
        self.selectText = self.selectFont.render('CHARACTER SELECT', False, (255,255,255))
        self.rockText = self.selectFont.render('[R]ock Boy', False, (255,255,255))
        self.mineralText = self.selectFont.render('[M]ineral Girl', False, (255,255,255))

        #fonts for battle
        self.battleFont = game.font.SysFont('Comic Sans MS', 32)
        self.menuFont = game.font.SysFont('Comic Sans MS', 24)
        self.battleText = self.battleFont.render('IDENTIFY THAT MINERAL!', False, (255,255,255))
        self.menuText = self.menuFont.render('Red = RUN!; Yellow = Taunt; Green = Acid Test; Blue = Streak/Scratch', False, (255,255,255))

        #fonts for pause menu
        self.pauseFont = game.font.SysFont('Comic Sans MS', 32)
        self.statFont = game.font.SysFont('Comic Sans MS', 24)
        self.pauseText = self.pauseFont.render('GAME PAUSED', False, (255,255,255))
        self.statTextHP = self.statFont.render('HP: ' + str(character.hp), False, self.red)
        self.statTextEXP = self.statFont.render('EXP: ' + str(character.exp), False, self.white)
        self.statTextLVL = self.statFont.render('LVL: ' + str(character.lvl), False, self.white)
        self.statTextPWR = self.statFont.render('PWR: ' + str(character.power), False, self.green)

        

    def updatePower(self,character):
        self.statTextPWR = self.statFont.render('PWR: ' + str(character.power), False, self.green)

    def updateHP(self,character):
        self.statTextHP = self.statFont.render('HP: ' + str(character.hp), False, self.red)

    def updateEXP(self,character):
        self.statTextEXP = self.statFont.render('EXP: ' + str(character.exp), False, self.white)

    def updateLVL(self,character):
        self.statTextLVL = self.statFont.render('LVL: ' + str(character.lvl), False, self.white)
    
