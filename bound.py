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
player_rect = player_surf.get_rect(midbottom=(80, 300))

player_speed =5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
    
    # Movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Keep player within screen bounds
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800
                 
    screen.blit(sky_surface,(0,0))  
    screen.blit(ground_surface,(0,300)) 
    screen.blit(text_surface,(300,50)) 
    screen.blit(player_surf, player_rect)
           
    pygame.display.update() 
    clock.tick(60)