import pygame as game

class RockBoy():
    """class for rock boy, the star of the show!"""

    #constants for character state
    def __init__(self,screen):
        self.screen = screen

        #load rock image and get its rect
        self.image = game.image.load('RockBoy.png')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()

        #start rock boy at bottom left corner
        self.rect.left = self.screenRect.left
        self.rect.bottom = self.screenRect.bottom

        #flags for continuous movement
        self.movingRight = False
        self.movingLeft = False
        self.movingDown = False
        self.movingUp = False

        #variable for state of character

        #variable for movement speed
        self.speed = 3

    def updatePos(self):
        """Update character's position based on movement flag"""
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.rect.centerx += self.speed
        elif self.movingLeft and self.rect.left > self.screenRect.left:
            self.rect.centerx -= self.speed
        if self.movingDown and self.rect.bottom < self.screenRect.bottom:
            self.rect.centery += self.speed
        elif self.movingUp and self.rect.top > self.screenRect.top:
            self.rect.centery -= self.speed
            
    def blit(self):
        """Draw rock at current location"""
        self.screen.blit(self.image,self.rect)
