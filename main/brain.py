import time
import pygame
from main.tools import *


class Brain:
    start_time: float = time.time()
    screen_resolution: tuple = (239, 479) # This is 240 x 480
    surface = None
    screen_row: int = 1
    screen_column: int = 1
    fill_color: Color = Color.BLACK
    pen_color: Color = Color.WHITE
    pen_width: int = 10
    font: FontType = FontType.MONO20

    pygame.init()
    clear()
    surface = pygame.display.set_mode([screen_resolution[1], screen_resolution[0]])
    pygame.display.set_caption("Brain")

    ports: dict = {
        "A" : False, 
        "B" : False, 
        "C" : False, 
        "D" : False, 
        "E" : False, 
        "F": False, 
        "G": False, 
        "H": False
        }
    
    for i in range(1, 22):
        ports[str(i)] = False


    @staticmethod
    def request_port(port: str) -> bool:
        """
        Requests the port to use.

        :param port: The port to request.
        :return: Whether the port is available.
        """

        while_loop()

        if Brain.ports.get(port) == False:
            Brain.ports[port] = True
            return True
        
        return False
    

    class screen:
        @staticmethod
        def print(text: str) -> None:
            """
            Prints text to the screen.

            :param text: The text to print to the screen.
            :return: None
            """

            while_loop()

            f = pygame.font.Font('freesansbold.ttf', int((Brain.screen_resolution[0]) / 12))
            Brain.surface.blit(f.render(text, True, Brain.pen_color), (0, int(Brain.screen_resolution[0]) / 12 * (int(Brain.screen_row) - 1)))
            pygame.display.flip()
        

        @staticmethod
        def set_cursor(row: int = 1, column: int = 1) -> None:
            """
            Sets the cursor to a specific position.

            :param row: The row to set the cursor to.
            :param column: The column to set the cursor to.
            :return: None
            """

            while_loop()

            Brain.screen_row = row
            Brain.screen_column = column
        

        @staticmethod
        def next_row() -> None:
            """
            Moves the cursor to the next row.

            :return: None
            """

            while_loop()

            Brain.screen_row += 1
        

        @staticmethod
        def clear_screen() -> None:
            """
            Clears the screen.

            :return: None
            """

            while_loop()

            Brain.surface.fill(Brain.fill_color)
            pygame.display.flip()
        

        @staticmethod
        def clear_row(row: int = 1) -> None:
            """
            Clears a specific row.

            :param row: The row to clear.
            :return: None
            """

            while_loop()

            pygame.draw.rect(Brain.surface, Brain.fill_color, (0, int(Brain.screen_resolution[0]) / 12 * (row - 1), Brain.screen_resolution[1], int(Brain.screen_resolution[0]) / 12))
            pygame.display.flip()

        
        @staticmethod
        def draw_pixel(x: int = 0, y: int = 0) -> None:
            """
            Draws a pixel to the screen.

            :param x: The x position of the pixel.
            :param y: The y position of the pixel.
            :return: None
            """

            while_loop()

            pygame.draw.line(Brain.surface, Brain.pen_color, [x, y], [x, y], int(Brain.pen_width / 10))
            pygame.display.flip()
        

        @staticmethod
        def draw_line(start_x: int = 0, start_y: int = 0, stop_x: int = 10, stop_y: int = 10) -> None:
            """
            Draws a line to the screen.

            :param start_x: The x position of the start of the line.
            :param start_y: The y position of the start of the line.
            :param stop_x: The x position of the end of the line.
            :param stop_y: The y position of the end of the line.
            :return: None
            """

            while_loop()

            pygame.draw.line(Brain.surface, Brain.pen_color, [start_x, start_y], [stop_x, stop_y], int(Brain.pen_width / 10))
            pygame.display.flip()


        @staticmethod
        def draw_rectangle(x: int = 0, y: int = 0, width: int = 10, height: int = 10) -> None:
            """
            Draws a rectangle to the screen.

            :param x: The x position of the rectangle.
            :param y: The y position of the rectangle.
            :param width: The width of the rectangle.
            :param height: The height of the rectangle.
            :return: None
            """

            while_loop()

            pygame.draw.rect(Brain.surface, Brain.pen_color, pygame.Rect(x, y, width, height))
            pygame.draw.rect(Brain.surface, Brain.fill_color, pygame.Rect(x + int(Brain.pen_width / 10), y + int(Brain.pen_width / 10), width - (int(Brain.pen_width / 10) * 2), height - (int(Brain.pen_width / 10) * 2)))
            pygame.display.flip()
        

        @staticmethod
        def draw_circle(x: int = 0, y: int = 0, radius: int = 10) -> None:
            """
            Draws a circle to the screen.

            :param x: The x position of the circle.
            :param y: The y position of the circle.
            :param radius: The radius of the circle.
            :return: None
            """

            while_loop()

            pygame.draw.circle(Brain.surface, Brain.pen_color, (x, y), radius)
            pygame.draw.circle(Brain.surface, Brain.fill_color, (x, y), radius - int(Brain.pen_width / 10))
            pygame.display.flip()
        

        @staticmethod
        def set_font(font_type: str = FontType.MONO20) -> None:
            """
            Sets the font of the text.

            :param font_type: The font to set the text to.
            :return: None
            """

            while_loop()

            Brain.font = font_type
        

        @staticmethod
        def set_pen_width(pen_width: int = 10) -> None:
            """
            Sets the width of the pen.

            :param pen_width: The width of the pen.
            :return: None
            """

            while_loop()

            Brain.pen_width = pen_width
        

        @staticmethod
        def set_pen_color(color: str = Color.RED) -> None:
            """
            Sets the color of the pen.

            :param color: The color of the pen.
            :return: None
            """

            while_loop()

            Brain.pen_color = color
        

        @staticmethod
        def set_fill_color(color: str = Color.RED) -> None:
            """
            Sets the color of the fill.

            :param color: The color of the fill.
            :return: None
            """

            while_loop()

            Brain.fill_color = color


    class Timer:
        @staticmethod
        def time() -> float:
            """
            Returns the time since the start of the program.

            :return: The time since the start of the program.
            """

            while_loop()

            return round(time.time() - Brain.start_time)
            
        
        @staticmethod
        def clear() -> None:
            """
            Clears the screen.

            :return: None
            """

            while_loop()

            Brain.start_time = time.time()