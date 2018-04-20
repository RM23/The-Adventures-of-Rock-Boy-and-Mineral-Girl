#file for storing the many fonts used in the game in different menus

import pygame as game

class Fonts():
    def __init__(self,character):
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
        self.statTextHP = self.statFont.render('HP: ' + str(character.hp), False, (255,255,255))
        self.statTextEXP = self.statFont.render('EXP: ' + str(character.exp), False, (255,255,255))
        self.statTextLVL = self.statFont.render('LVL: ' + str(character.lvl), False, (255,255,255))

