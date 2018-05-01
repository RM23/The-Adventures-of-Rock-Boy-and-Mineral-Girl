#holds the class definition for tile class
import pygame as game
import sys

class Tile():
    """Class for tiles, different graphics with different effects that appear in the overworld"""
    def __init__(self,fileName,posx,posy,screen,solid):
        """Initializes the tile"""
        #set whether or not characters can walk through this type of tile
        self.solid = solid
        
        self.image = game.image.load(fileName)
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.rect.left = posx
        self.rect.top = posy

    def blit(self):
        """Draws tile at location specified at posx and posy"""
        self.screen.blit(self.image,self.rect)
