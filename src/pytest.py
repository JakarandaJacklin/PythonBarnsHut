import pygame
import sys
import simulator
import time
import numpy as np

sys.setrecursionlimit(20000)

simulator.changeQuads([0,0], 800)
bodies = simulator.initBodies(800, 1, 15, 0, 800)
simulator.changeG(0.01)



pygame.init() #

# Set the window size
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window") #

# Game loop condition
running = True




while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Game logic (optional for a blank window)
    simulator.step(bodies)

    # 3. Drawing
    screen.fill((0, 0, 0)) # Fill the screen with black
    for i in bodies:
        pygame.draw.circle(screen, (255, 255, 255), i.position, np.sqrt(i.mass))
    # Draw other game elements here...

    # 4. Update the display to show the new frame
    pygame.display.flip() # or pygame.display.update()

# Quit Pygame and the program
pygame.quit()
sys.exit()
