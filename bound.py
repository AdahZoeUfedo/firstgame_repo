import pygame
from sys import exit
from random import randint

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

# Cookie and rock setup
cookie_surf = pygame.image.load('firstgame_repo/cookie.png').convert_alpha()
cookie_surf = pygame.transform.scale(cookie_surf, (50, 50))

rock_surf = pygame.image.load('firstgame_repo/rock.png').convert_alpha()
rock_surf = pygame.transform.scale(rock_surf, (50, 50))

cookie_rect = cookie_surf.get_rect(midtop=(randint(0, 750), 0))
rock_rect = rock_surf.get_rect(midtop=(randint(0, 750), -100))

cookie_fall_speed = 5
rock_fall_speed = 7

# Game variables
score = 0
lives = 3
game_over = False

# Font for score and lives
score_font = pygame.font.Font('firstgame_repo/font/Pixeltype.ttf', 30)

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
        
    # Move cookie and rock downward
    cookie_rect.y += cookie_fall_speed
    rock_rect.y += rock_fall_speed

    # Reset position if off-screen
    if cookie_rect.top > 400:
        cookie_rect.midtop = (randint(0, 750), 0)
    if rock_rect.top > 400:
        rock_rect.midtop = (randint(0, 750), 0)
    
    # Collision detection for catching cookies
    if player_rect.colliderect(cookie_rect):
        score += 1
        cookie_rect.midtop = (randint(0, 750), 0)  # Reset cookie position

    # Collision detection for hitting rocks
    if player_rect.colliderect(rock_rect):
        lives -= 1
        rock_rect.midtop = (randint(0, 750), 0)  # Reset rock position

    # Check game over condition
    if lives <= 0:
        game_over = True

    # Check if player caught 10 cookies
    if score >= 10:
        game_over = True
                         
    screen.blit(sky_surface,(0,0))  
    screen.blit(ground_surface,(0,300)) 
    screen.blit(text_surface,(300,50)) 
    screen.blit(cookie_surf, cookie_rect)
    screen.blit(rock_surf, rock_rect)
    screen.blit(player_surf, player_rect)
    
    # Display score and lives
    score_text = score_font.render(f"Score: {score}", False, 'black')
    lives_text = score_font.render(f"Lives: {lives}", False, 'black')
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (700, 10))
    
     # Display game over message
    if game_over:
        if score >= 10:
            game_over_text = test_font.render("You Win! Level Cleared!", False, 'green')
        else:
            game_over_text = test_font.render("Game Over!", False, 'red')
        screen.blit(game_over_text, (250, 150))

           
    pygame.display.update() 
    clock.tick(60)
 