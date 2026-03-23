import pygame

def init(screen_size):
    pygame.init()

    # Set up display
    SIZE = (screen_size, screen_size)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("SPACE")

    return screen

def screen_init(screen):
    screen.fill((0, 0, 0))

def draw(screen, position, mass):
    pygame.draw.circle(screen, (255,255,255), position, 5)

def screen_update(screen):
    pygame.display.flip()

