import pygame
import random
from Enums import Colors
from Constants import *

class Llama:
    def __init__(self, x, y):
        self.image = pygame.Surface((40, 40)) # TODO: Llama image
        self.image.fill(Colors.BLACK.value)
        self.rect = self.image.get_rect(center=(x, y))
        self.is_jumping = False
        self.jump_count = 0
        self.apex_reached = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 0
    
    def update_jump(self):
        if self.is_jumping:
            if self.jump_count < JUMP_HEIGHT and not self.apex_reached:
                self.rect.y -= 10
                self.jump_count += 10
                if self.jump_count >= JUMP_HEIGHT:
                    self.apex_reached = True
            
            elif self.apex_reached:
                self.jump_count -= 10
                self.rect.y += 10

            if self.jump_count <= 0 and self.apex_reached:
                self.is_jumping = False
                self.jump_count = 0
                self.apex_reached = False

    def move_left(self):
        self.rect.x -= MOVE_SPEED
    
    def move_right(self):
        self.rect.x += MOVE_SPEED

class Platform:
    def __init__(self, x, y, is_static=False):
        self.width = RECT_WIDTH
        self.height = RECT_INITIAL_HEIGHT 
        self.shrink_counter = 0
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = Colors.BLUE.value
        self.is_static = is_static

    def shrink(self):
        if not self.is_static:
            self.shrink_counter += 1
            if self.shrink_counter >= REDUCE_SPEED:   
                if self.height > 0:
                    self.height -= REDUCE_AMOUNT
                    self.rect.height = self.height
                    if self.height <= RECT_INITIAL_HEIGHT / 3:
                        self.color = Colors.RED.value
                    elif self.height <= RECT_INITIAL_HEIGHT * 2 /3:
                        self.color = Colors.YELLOW.value
                    else:
                        self.color = Colors.GREEN.value

            if self.shrink_counter == REDUCE_SPEED:
                self.shrink_counter = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class PlatformManager:
    def __init__(self):
        self.platforms = [Platform(350, 500), Platform(600, 450, is_static=True)]
        self.current_shrink = 0
    
    def update_platforms(self):
        for platform in self.platforms:
            platform.shrink()

            if platform.height <= 0 and not platform.is_static:
                self._handle_platform_shrink()
    
    def _handle_platform_shrink(self):
        tempShrink = self.current_shrink
        if self.current_shrink == 0:
            self.current_shrink = 1
        else:
            self.current_shrink = 0

        new_x = random.randint(0, SCREEN_WIDTH - RECT_WIDTH)
        new_y = random.randint(0, SCREEN_HEIGHT - RECT_INITIAL_HEIGHT)
        self.platforms[tempShrink] = Platform(new_x, new_y, is_static=True)
        self.platforms[tempShrink].height = RECT_INITIAL_HEIGHT
        self.platforms[self.current_shrink].is_static = False