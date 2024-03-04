import os
import time
import pygame

SECONDS: str = 'seconds'
PERCENT: str = 'percent'
MSEC: str = 'msec'


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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


class Color():
    BLACK: str = "BLACK"
    WHITE: str = "WHITE"
    RED: str = "RED"
    GREEN: str = "GREEN"
    BLUE: str = "BLUE"
    YELLOW: str = "YELLOW"
    ORANGE: str = "ORANGE"
    PURPLE: str = "PURPLE"
    CYAN: str = "CYAN"
    TRANSPARENT: str = "TRANSPAREN"


class FontType():
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