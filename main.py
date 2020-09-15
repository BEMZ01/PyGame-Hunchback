import pygame
import random
pygame.init()
#init pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
COLORS = [(0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255)]
#prepare colors

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hunchback 1983")
#open window

carryOn = True
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
              carryOn = False
    
     # --- Game logic
     
     # --- Drawing code
     # First, clear the screen to white. 
    screen.fill(WHITE)
     #The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, random.choice(COLORS), [55, 200, 100, 70],0)
    pygame.draw.line(screen, random.choice(COLORS), [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, random.choice(COLORS), [20,20,250,100], 2)
 
 
     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()