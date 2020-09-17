import pygame
import random
import time
pygame.init()
try:
  pygame.mixer.init()
  audio = True
except pygame.error:
  audio = False
#init pygame
# set varibles
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
        color="white",
        where=(0, 0))


def render_menu(x, y):
  display_surface = pygame.display.set_mode((0, 0))
  image = pygame.image.load(r'assets/visual/logo.PNG') 
  display_surface.blit(image, (0, 0))
  message_display("Press SPACE to play.", 500, 750)

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x/2),(y/2))
    gameDisplay.blit(TextSurf, TextRect)

init_screen_and_clock(x, y)
gameDisplay = pygame.display.set_mode((x,y))
# This create different font size in one line
fonts = create_fonts([32, 16, 14, 8])
for x in range(0, 10):
    time.sleep(0.05)
    screen.fill(random.choice(COLORS))
    pygame.display.flip()

def menu():
  loop = 1
  tick = 0
  while loop:
    tick += 1
    screen.fill(BLACK)
    render_menu(x, y)
    display_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return(1)
    clock.tick(60)
    pygame.display.flip()
    if tick == 44:
      tick = 0
  return(0) # there was an error

def game():
  loop = 1
  tick = 0
  while loop:
    tick += 1
    screen.fill(BLACK)
    display_fps()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        loop = 0
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          jump = 1
        elif event.key == pygame.K_a:
          xmove = -5
        elif event.key == pygame.K_d:
          xmove = 5
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
          jump = 0
        elif (event.key == pygame.K_a) or (event.key == pygame.K_d):
          xmove = 0
    clock.tick(60)
    pygame.display.flip()
    if tick == 44:
      tick = 0
  return(0)

print("Audio -", audio)
print("Enter Menu")
if menu() == 1:
  print("Enter Game")
  game()
print("goodbye")
pygame.quit()
