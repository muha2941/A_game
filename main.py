import pygame
import sys
from configuration import *
from sprites import *
import os
current_dir = os.path.dirname(__file__)

class Spritesheet:
    def __init__(self,path):
        self.spritesheet=pygame.image.load(path).convert()
   
    def get_image(self, x, y, width, height):
        sprite= pygame.Surface([width,height])
        sprite.blit(self.spritesheet,(0,0),(x,y,width,height))

        return sprite
class Game:
    def __init__(self):
        self.screen= pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock=pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet(os.path.abspath(os.path.join(current_dir, '..', '..', 'terrain.png')).replace('\\', '/'))
        self.player_spritesheet = Spritesheet(os.path.abspath(os.path.join(current_dir, '..', '..', 'terrain.png')).replace('\\', '/'))
        self.running=True

    def createTilemap(self):
        for i,row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self,i,j)
                if column=="B":
                    Block(self,j,i)
                elif column=="W":
                    Water(self,i,j)
                

    def create(self):
        self.all_sprites =pygame.sprite.LayeredUpdates()
        self.createTilemap()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running==False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

game = Game()
game.create()

while game.running:
    game.main()

pygame.quit()
sys.exit
