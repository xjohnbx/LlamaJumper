import pygame
from Classes import Llama
from Constants import SCREEN_WIDTH
def handle_input(llama: Llama):
    keys = pygame.key.get_pressed()  # Get the state of all keys
    if keys[pygame.K_LEFT]:  # If left arrow is pressed
        llama.move_left()
    if keys[pygame.K_RIGHT]:  # If right arrow is pressed
        llama.move_right()
    if keys[pygame.K_SPACE]:  # If spacebar is pressed
        llama.jump()

    if llama.rect.left < 0:
        llama.rect.x = 0
    if llama.rect.right > SCREEN_WIDTH:
        llama.rect.x = 800 - llama.rect.width