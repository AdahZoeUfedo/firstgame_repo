import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Skybound")
clock = pygame.time.Clock()
test_font = pygame.font.Font('firstgame_repo/font/Pixeltype.ttf', 50)

sky_surface=pygame.image.load('firstgame_repo/Sky.png')
ground_surface=pygame.image.load('firstgame_repo/ground.png')
text_surface = test_font.render('My game', False, 'black')
player_surf=pygame.image.load('firstgame_repo/player_stand.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
    screen.blit(sky_surface,(0,0))  
    screen.blit(ground_surface,(0,300)) 
    screen.blit(text_surface,(300,50)) 
    screen.blit(player_surf,(80,220)) 
           
    pygame.display.update() 
    clock.tick(60)