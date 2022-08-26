import os, pygame, threading, time
from extras import *

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

startTime = time.time()

screenReslution = [239, 479]
screenScale = 1

pygame.init()
clear()
surface = pygame.display.set_mode([(screenReslution[1] * screenScale), (screenReslution[0] * screenScale)])
pygame.display.set_caption("Brain")

#Looks

screenRow = 1
screenColumn = 1

fillColor = Color.BLACK
penColor = Color.WHITE
penWidth = 10
font = FontType.MONO20

class screen():
  global surface, screenRow, screenColumn, screenReslution, screenScale, fillColor, penColor, penWidth, startTime

  def screenScaling(scale):
    whileLoopAntiCrash()
    global surface, screenRow, screenReslution, screenScale
    screenScale = scale
    surface = pygame.display.set_mode([(screenReslution[1] * screenScale), (screenReslution[0]) * screenScale])
    
  def print(text):
    whileLoopAntiCrash()
    global surface, screenRow, screenColumn, screenReslution, screenScale, fillColor, penColor, penWidth 
    f = pygame.font.Font('freesansbold.ttf',int((screenReslution[0] * screenScale)/12))
    surface.blit(f.render(text,True,penColor),(0,int((screenReslution[0] * screenScale)/12)*(int(screenRow)-1)))
    pygame.display.flip()

  def set_cursor(row = 1, column = 1):
    whileLoopAntiCrash()
    global screenRow, screenColumn
    screenRow = row
    screenColumn = column
    
  def next_row():
    whileLoopAntiCrash()
    global screenRow
    screenRow += 1
        
  def clear_screen():
    whileLoopAntiCrash()
    global surface, fillColor
    surface.fill(fillColor)
    pygame.display.flip()

  def clear_row(row = 1):
    whileLoopAntiCrash()
    global fillColor
    pygame.draw.rect(surface, fillColor, pygame.Rect(0, (((screenReslution[0] * screenScale)/12)*(row-1)), (screenReslution[1] * screenScale), ((screenReslution[0] * screenScale)/12)))
    pygame.display.flip()

  def draw_pixel(x = 0, y = 0):
    whileLoopAntiCrash()
    global surface, screenScale, penColor, penWidth
    pygame.draw.line(surface, penColor,[(x * screenScale), (y * screenScale)], [(x * screenScale), (y * screenScale)], (int(penWidth/10) * screenScale))
    pygame.display.flip()

  def draw_line(start_x = 0, start_y = 0, stop_x = 10, stop_y = 10):
    whileLoopAntiCrash()
    global surface, screenScale, penColor, penWidth
    pygame.draw.line(surface, penColor,[(start_x * screenScale), (start_y * screenScale)], [(stop_x * screenScale), (stop_y * screenScale)], (int(penWidth/10) * screenScale))
    pygame.display.flip()
    
  def draw_rectangle(x = 0, y = 0, width = 10, height = 10):
    whileLoopAntiCrash()
    global surface, screenScale, fillColor, penColor, penWidth
    pygame.draw.rect(surface, penColor, pygame.Rect((x * screenScale), (y * screenScale), (width * screenScale), (height * screenScale)))
    pygame.draw.rect(surface, fillColor, pygame.Rect((x * screenScale) + (int(penWidth/10) * screenScale), (y * screenScale) + (int(penWidth/10) * screenScale), (width * screenScale) - ((int(penWidth/10) * screenScale) * 2), (height * screenScale) - ((int(penWidth/10) * screenScale) * 2)))
    pygame.display.flip()

  def draw_circle(x = 0, y = 0, radius = 10):
    whileLoopAntiCrash()
    global surface, screenRow, screenColumn, screenReslution, screenScale, fillColor, penColor, penWidth
    pygame.draw.circle(surface, penColor, ((x * screenScale), (y * screenScale)), (radius * screenScale))
    pygame.draw.circle(surface, fillColor, ((x * screenScale), (y * screenScale)), (radius * screenScale) - (int(penWidth/10) * screenScale))
    pygame.display.flip()

  def set_font(font_type = FontType.MONO20):
    whileLoopAntiCrash()
    global font
    font = font_type
        
  def set_pen_width(pen_width = 10):
    whileLoopAntiCrash()
    global penWidth
    penWidth = pen_width

  def set_pen_color(color = Color.RED):
    whileLoopAntiCrash()
    global penColor
    penColor = color

  def set_fill_color(color = Color.RED):
    whileLoopAntiCrash()
    global fillColor
    fillColor = color

#Sensing

  def pressing():
    whileLoopAntiCrash()
    if pygame.mouse.get_pressed()[0]:
      return True

  def x_position():
    whileLoopAntiCrash()
    return str(pygame.mouse.get_pos()[0])

  def y_position():
    whileLoopAntiCrash()
    return pygame.mouse.get_pos()[1]

class timer():

  def clear():
    whileLoopAntiCrash()
    global startTime
    startTime = time.time()

  def time(units):
    whileLoopAntiCrash()
    global startTime
    return round(time.time()-startTime)