import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Skybound")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('firstgame_repo/Sky.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
             
    pygame.display.update() 
    clock.tick(60)