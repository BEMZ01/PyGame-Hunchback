import pygame
import random
import time
pygame.init()
#init pygame

y = 500
x = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
COLORS = [(0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255)]
#prepare colors

#open window
def init_screen_and_clock(x, y):
    global screen, display, clock
    pygame.init()
    WINDOW_SIZE = (x, y)
    pygame.display.set_caption('Hunchback 1983')
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    clock = pygame.time.Clock()


def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts


def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_fps():
    "Data that will be rendered and blitted in _display"
    render(
        fonts[0],
        what=str(int(clock.get_fps())),
        color="black",
        where=(0, 0))

def render_menu(x, y):
  display_surface = pygame.display.set_mode((0, 0))
  image = pygame.image.load(r'assets/visual/logo.PNG') 
  display_surface.blit(image, (0, 0))


init_screen_and_clock(x, y)
# This create different font size in one line
fonts = create_fonts([32, 16, 14, 8])
for x in range(0, 10):
    time.sleep(0.05)
    screen.fill(random.choice(COLORS))
    pygame.display.flip()
loop = 1
while loop:
    screen.fill(BLACK)
    display_fps()
    render_menu(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
