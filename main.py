import pygame
import random
import time
import os 
import logging
from datetime import datetime
try: # linux
  logging.basicConfig(filename='logs/'+str(datetime.now())+'.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
except OSError: # windows
  logging.basicConfig(filename='logs/'+str(datetime.now()).replace(":", ";")+'.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.basicConfig(filename='logs/latest.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
def pprint(text):
  print(text)
  logging.debug(str(datetime.now())+" -\t"+str(text))
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
COLORS = [(0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 0, 255)]
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
for x in range(0, 100):
    time.sleep(0.01)
    screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pygame.display.flip()

def player(x,y):
  display_surface = pygame.display.set_mode((0, 0))
  image = pygame.image.load(r'assets/visual/hero/idle.PNG') 
  display_surface.blit(image, (x, y))

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
                if event.key == pygame.K_ESCAPE:
                  loop = 0
                  break
    clock.tick(16)
    pygame.display.flip()
    if tick == 44:
      tick = 0
  return(0) # there was an error

def game():
  playerx = 100
  playery = 400
  tempy = 0
  x = 0
  y = 0
  isJump = False
  jumpCount = 4
  loop = 1
  tick = 0
  while loop:
    tick += 1
    screen.fill(BLACK)
    if playery < 0:
      playery = 0
    if playerx > 0 and playerx < 701:
      player(playerx, playery)
    else:
      playerx = 0
      player(playerx, playery)
    display_fps()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
      loop = 0
      break
    if keys[pygame.K_a]:
      x = -10
    elif keys[pygame.K_d]:
      x = 10
    if keys[pygame.K_w]:
      isJump = True
    else:
      x = 0
    if not isJump:
      tempy = playery
    if jumpCount >= -4 and isJump:
      y -= (jumpCount * abs(jumpCount)) * 0.5
      jumpCount -= 1
    else: # This will execute if our jump is finished
      jumpCount = 4
      isJump = False
      playery = tempy
      # Resetting our Variables
    playery += y
    playerx += x
    clock.tick(120)
    pygame.display.flip()
    if tick == 44:
      tick = 0
  return(0)

pprint("Audio -"+str(audio))
pprint("Enter Menu")
try:
  if menu() == 1:
    pprint("Enter Game")
    game()
except Exception as err:
  pprint("Crashed! Error "+str(err))
pprint("Produced by BEMZ for A Level Computer Science.")
pygame.quit()