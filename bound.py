import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Skybound")
clock = pygame.time.Clock()
test_font = pygame.font.Font('firstgame_repo/font/Pixeltype.ttf', 50)

# Surfaces and assets
sky_surface = pygame.image.load('firstgame_repo/Sky.png')
ground_surface = pygame.image.load('firstgame_repo/ground.png')
text_surface = test_font.render('My game', False, 'black')
player_surf = pygame.image.load('firstgame_repo/player_stand.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_speed = 5

# Cookie and rock setup
cookie_surf = pygame.image.load('firstgame_repo/cookie.png').convert_alpha()
cookie_surf = pygame.transform.scale(cookie_surf, (50, 50))

rock_surf = pygame.image.load('firstgame_repo/rock.png').convert_alpha()
rock_surf = pygame.transform.scale(rock_surf, (50, 50))

cookie_rect = cookie_surf.get_rect(midtop=(randint(0, 750), 0))
rock_rect = rock_surf.get_rect(midtop=(randint(0, 750), -100))

# Lists for multiple cookies and rocks
cookies = []
rocks = []

# Game variables
score = 0
lives = 3
game_over = False
game_active = False
game_paused = False

# Fonts
score_font = pygame.font.Font('firstgame_repo/font/Pixeltype.ttf', 30)

# Timers
cookie_timer = pygame.USEREVENT + 1
rock_timer = pygame.USEREVENT + 2
pygame.time.set_timer(cookie_timer, 1500)
pygame.time.set_timer(rock_timer, 2000)

cookie_fall_speed = 2
rock_fall_speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Start the game
        if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            game_active = True
            game_over = False
            score = 0
            lives = 3
            cookies.clear()
            rocks.clear()
            player_rect.midbottom = (80, 300)

        # Pause/unpause
        if game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_paused = not game_paused

        # Spawning falling objects
        if event.type == cookie_timer and game_active and not game_paused:
            new_cookie = cookie_surf.get_rect(midtop=(randint(0, 750), 0))
            cookies.append(new_cookie)

        if event.type == rock_timer and game_active and not game_paused:
            new_rock = rock_surf.get_rect(midtop=(randint(0, 750), 0))
            rocks.append(new_rock)

        # Restart from game over
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game_active = False
            game_over = False

    if game_active and not game_paused and not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed

        # Keep player within bounds
        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.right > 800:
            player_rect.right = 800

        # Update cookies
        for cookie in cookies[:]:
            cookie.y += cookie_fall_speed
            if cookie.top > 400:
                cookies.remove(cookie)
            elif player_rect.colliderect(cookie):
                cookies.remove(cookie)
                score += 1

        # Update rocks
        for rock in rocks[:]:
            rock.y += rock_fall_speed
            if rock.top > 400:
                rocks.remove(rock)
            elif player_rect.colliderect(rock):
                rocks.remove(rock)
                lives -= 1

        # Game over check
        if lives <= 0 or score >= 10:
            game_over = True

    # Draw background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    if game_active and not game_over:
        for cookie in cookies:
            screen.blit(cookie_surf, cookie)
        for rock in rocks:
            screen.blit(rock_surf, rock)
        screen.blit(player_surf, player_rect)

    # Score and Lives display
    score_text = score_font.render(f"Score: {score}", False, 'black')
    lives_text = score_font.render(f"Lives: {lives}", False, 'black')
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (700, 10))

    # Game over message
    if game_over:
        if score >= 10:
            game_over_text = test_font.render("You Won! Level Cleared!", False, 'black')
        else:
            game_over_text = test_font.render("Game Over!", False, 'red')
        screen.blit(game_over_text, (250, 150))
        restart_text = score_font.render("Press R to Restart", False, 'black')
        screen.blit(restart_text, (270, 200))

    # Start screen
    if not game_active and not game_over:
        start_text = test_font.render("Press S to Start", False, 'black')
        screen.blit(start_text, (250, 180))

    # Pause screen
    if game_paused and not game_over:
        pause_text = test_font.render("Paused - Press Space", False, 'blue')
        screen.blit(pause_text, (220, 180))

    pygame.display.update()
    clock.tick(60)
