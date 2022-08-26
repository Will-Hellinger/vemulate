import time, pygame

def whileLoopAntiCrash():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()

def wait(waitTime, unit):
  time.sleep(waitTime)
  whileLoopAntiCrash()

class Color():
  BLACK = "BLACK"
  WHITE = "WHITE"
  RED = "RED"
  GREEN = "GREEN"
  BLUE = "BLUE"
  YELLOW = "YELLOW"
  ORANGE = "ORANGE"
  PURPLE = "PURPLE"
  CYAN = "CYAN"
  TRANSPARENT = "TRANSPARENT"

class FontType():
  MONO12 = "Arial"
  MONO15 = "Arial"
  MONO20 = "Arial"
  MONO30 = "Arial"
  MONO40 = "Arial"
  MONO60 = "Arial"
  PROP20 = "Arial"
  PROP30 = "Arial"
  PROP40 = "Arial"
  PROP60 = "Arial"

SECONDS = 'seconds'
PERCENT = 'percent'
MSEC = 'msec'
