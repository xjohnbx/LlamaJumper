import pygame
import sys
import random
from Classes import Llama, Platform, PlatformManager
from Constants import SCREEN_HEIGHT, SCREEN_WIDTH, LIVES, FPS, RECT_INITIAL_HEIGHT
from Enums import Colors
from input_handler import handle_input

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Llama Jumper')

clock = pygame.time.Clock()

# Game Init
llama = Llama(400, 500)
platform_manager = PlatformManager()
score = 0
lives = LIVES


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input(llama)
    llama.update_jump()
 
    platform_manager.update_platforms()

    screen.fill(Colors.WHITE.value)
    for platform in platform_manager.platforms:
        platform.draw(screen)

    screen.blit(llama.image, llama.rect)
    
        # Text Stuff
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, Colors.BLACK.value)
    lives_text = font.render(f'Lives: {lives}', True, Colors.BLACK.value)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()