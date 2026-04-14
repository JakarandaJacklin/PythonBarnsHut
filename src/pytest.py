import pygame
import sys
import simulator
import time
import numpy as np

sys.setrecursionlimit(20000)

simulator.changeQuads([0,0], 800)
bodies = simulator.initBodies(200, 1, 15, 0, 800) #mass 1-15
simulator.changeG(0.01)#0.01)
simulator.changeMerge(False, 0.2)#0.2)



pygame.init() #

# Set the window size
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window") #

# Game loop condition
running = True


def drawQuads(tree, screen):
    x = tree.pos[0]
    y = tree.pos[1]
    size = tree.size

    pygame.draw.rect(screen, (255, 131, 255), (x, y, size, size), width=1, border_radius=0)
    pygame.draw.circle(screen, (235, 52, 116), tree.COM, 2)


    if tree.Children != []:
        for i in tree.Children:
            drawQuads(i, screen)

while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Game logic (optional for a blank window)
    tree = simulator.step(bodies)

    # 3. Drawing
    screen.fill((0, 0, 0)) # Fill the screen with black
    for i in bodies:
        pygame.draw.circle(screen, (255, 255, 255), i.position, np.sqrt(i.mass))
    drawQuads(tree, screen)
    # Draw other game elements here...

    # 4. Update the display to show the new frame
    pygame.display.flip() # or pygame.display.update()

# Quit Pygame and the program
pygame.quit()
sys.exit()