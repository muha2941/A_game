from configuration import *
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x,y):

        self.game=game
        self._layer=BLOCKS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self.groups)
        self.x,self.y= x*TILESIZE,y*TILESIZE
        
        self.width,self.height=TILESIZE,TILESIZE

        self.image= self.game.terrain_spritesheet.get_image(991,541, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y  = self.x,self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x,y):

        self.game=game
        self._layer=GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self.groups)
        self.x,self.y=x*TILESIZE,y*TILESIZE
        
        self.width,self.height=TILESIZE,TILESIZE

        self.image= self.game.terrain_spritesheet.get_image(447,353, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y  = self.x,self.y
"""
class Water(pygame.sprite.Sprite):
    def __init__(self, game, x,y):

        self.game=game
        self._layer=WATER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self.groups)
        self.x,self.y=TILESIZE,TILESIZE
        
        self.width,self.height=TILESIZE,TILESIZE

        self.image= self.game.terrain_spritesheet.get_image(900,100, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y  = self.x,self.y
"""