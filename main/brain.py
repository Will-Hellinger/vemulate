import time
import pygame

SECONDS: str = 'seconds'
PERCENT: str = 'percent'
MSEC: str = 'msec'


def while_loop() -> None:
    """
    The main loop of the program.

    :return: None
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def wait(wait_time, unit: str) -> None:
    """
    Waits for a certain amount of time.
  
    :param wait_time: The amount of time to wait.
    :param unit: The unit of time to wait.
    :return: None
    """

    while_loop()

    if unit == SECONDS:
        time.sleep(wait_time)
    elif unit == MSEC:
        time.sleep(wait_time / 1000)


class Color:
    BLACK: str = "BLACK"
    WHITE: str = "WHITE"
    RED: str = "RED"
    GREEN: str = "GREEN"
    BLUE: str = "BLUE"
    YELLOW: str = "YELLOW"
    ORANGE: str = "ORANGE"
    PURPLE: str = "PURPLE"
    CYAN: str = "CYAN"
    TRANSPARENT: str = "TRANSPARENT"


class FontType:
    MONO12: str = "Arial"
    MONO15: str = "Arial"
    MONO20: str = "Arial"
    MONO30: str = "Arial"
    MONO40: str = "Arial"
    MONO60: str = "Arial"
    PROP20: str = "Arial"
    PROP30: str = "Arial"
    PROP40: str = "Arial"
    PROP60: str = "Arial"


class Brain:
    def __init__(self):
        self.start_time = time.time()
        self.screen_resolution = (239, 479)  # This is 240 x 480
        self.surface = None
        self.screen_row = 1
        self.screen_column = 1
        self.fill_color = Color.BLACK
        self.pen_color = Color.WHITE
        self.pen_width = 10
        self.font = FontType.MONO20
        self.ports = {str(i): False for i in range(1, 23)}  # Simplified port initialization
        self.ports.update({chr(i): False for i in range(65, 73)})  # Add ports A-H
        self.screen = self.screen(self)  # Initialize screen as an instance attribute
        self.timer = self.Timer(self.start_time)  # Initialize timer as an instance attribute

        pygame.init()
        self.surface = pygame.display.set_mode([self.screen_resolution[1], self.screen_resolution[0]])
        pygame.display.set_caption("Brain")


    def request_port(self, port: str, port_type: str) -> bool:
        """
        Requests the port to use.

        :param port: The port to request.
        :return: Whether the port is available.
        """

        while_loop()

        if port_type == "full" and not port.isnumeric():
            raise Exception("Invalid port type.")

        if port_type == "three_wire" and port.isnumeric():
            raise Exception("Invalid port type.")

        if self.ports.get(port) == False:
            self.ports[port] = True
            return True
        
        return False
    

    class screen:
        def __init__(self, brain):
            self.brain = brain
            self.screen_resolution = brain.screen_resolution
            self.screen_row = brain.screen_row
            self.screen_column = brain.screen_column
            self.fill_color = brain.fill_color
            self.pen_color = brain.pen_color
            self.pen_width = brain.pen_width
            self.font = brain.font


        def print(self, text: str) -> None:
            """
            Prints text to the screen.

            :param text: The text to print to the screen.
            :return: None
            """

            while_loop()

            text = str(text) # Ensure text is a string

            f = pygame.font.Font('freesansbold.ttf', int((self.screen_resolution[0]) / 12))
            self.brain.surface.blit(f.render(text, True, self.pen_color), (0, int(self.screen_resolution[0]) / 12 * (int(self.screen_row) - 1)))
            pygame.display.flip()
        

        def set_cursor(self, row: int = 1, column: int = 1) -> None:
            """
            Sets the cursor to a specific position.

            :param row: The row to set the cursor to.
            :param column: The column to set the cursor to.
            :return: None
            """

            while_loop()

            self.screen_row = row
            self.screen_column = column
        

        def next_row(self) -> None:
            """
            Moves the cursor to the next row.

            :return: None
            """

            while_loop()

            self.screen_row += 1
        

        def clear_screen(self) -> None:
            """
            Clears the screen.

            :return: None
            """

            while_loop()

            self.brain.surface.fill(self.fill_color)
            pygame.display.flip()
        

        def clear_row(self, row: int = 1) -> None:
            """
            Clears a specific row.

            :param row: The row to clear.
            :return: None
            """

            while_loop()

            pygame.draw.rect(self.brain.surface, self.fill_color, (0, int(self.screen_resolution[0]) / 12 * (row - 1), self.screen_resolution[1], int(self.screen_resolution[0]) / 12))
            pygame.display.flip()

        
        def draw_pixel(self, x: int = 0, y: int = 0) -> None:
            """
            Draws a pixel to the screen.

            :param x: The x position of the pixel.
            :param y: The y position of the pixel.
            :return: None
            """

            while_loop()

            pygame.draw.line(self.brain.surface, self.pen_color, [x, y], [x, y], int(self.pen_width / 10))
            pygame.display.flip()
        

        def draw_line(self, start_x: int = 0, start_y: int = 0, stop_x: int = 10, stop_y: int = 10) -> None:
            """
            Draws a line to the screen.

            :param start_x: The x position of the start of the line.
            :param start_y: The y position of the start of the line.
            :param stop_x: The x position of the end of the line.
            :param stop_y: The y position of the end of the line.
            :return: None
            """

            while_loop()

            pygame.draw.line(self.brain.surface, self.pen_color, [start_x, start_y], [stop_x, stop_y], int(self.pen_width / 10))
            pygame.display.flip()


        def draw_rectangle(self, x: int = 0, y: int = 0, width: int = 10, height: int = 10) -> None:
            """
            Draws a rectangle to the screen.

            :param x: The x position of the rectangle.
            :param y: The y position of the rectangle.
            :param width: The width of the rectangle.
            :param height: The height of the rectangle.
            :return: None
            """

            while_loop()

            pygame.draw.rect(self.brain.surface, self.pen_color, pygame.Rect(x, y, width, height))
            pygame.draw.rect(self.brain.surface, self.fill_color, pygame.Rect(x + int(self.pen_width / 10), y + int(self.pen_width / 10), width - (int(self.pen_width / 10) * 2), height - (int(self.pen_width / 10) * 2)))
            pygame.display.flip()
        

        def draw_circle(self, x: int = 0, y: int = 0, radius: int = 10) -> None:
            """
            Draws a circle to the screen.

            :param x: The x position of the circle.
            :param y: The y position of the circle.
            :param radius: The radius of the circle.
            :return: None
            """

            while_loop()

            pygame.draw.circle(self.brain.surface, self.pen_color, (x, y), radius)
            pygame.draw.circle(self.brain.surface, self.fill_color, (x, y), radius - int(self.pen_width / 10))
            pygame.display.flip()
        

        def set_font(self, font_type: str = FontType.MONO20) -> None:
            """
            Sets the font of the text.

            :param font_type: The font to set the text to.
            :return: None
            """

            while_loop()

            self.font = font_type
        

        def set_pen_width(self, pen_width: int = 10) -> None:
            """
            Sets the width of the pen.

            :param pen_width: The width of the pen.
            :return: None
            """

            while_loop()

            self.pen_width = pen_width
        

        def set_pen_color(self, color: str = Color.RED) -> None:
            """
            Sets the color of the pen.

            :param color: The color of the pen.
            :return: None
            """

            while_loop()

            self.pen_color = color
        

        def set_fill_color(self, color: str = Color.RED) -> None:
            """
            Sets the color of the fill.

            :param color: The color of the fill.
            :return: None
            """

            while_loop()

            self.fill_color = color


    class Timer:
        def __init__(self, start_time: float = time.time()):
            self.start_time = start_time

        def time(self) -> float:
            """
            Returns the time since the start of the program.

            :return: The time since the start of the program.
            """

            while_loop()

            return round(time.time() - self.start_time)
            
        
        def clear(self) -> None:
            """
            Clears the timer.

            :return: None
            """

            while_loop()

            self.start_time = time.time()