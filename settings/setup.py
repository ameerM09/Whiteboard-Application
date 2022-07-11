# Module to set up constant variables used in 'main.py'
import pygame
import sys
import os

pygame.init()
pygame.font.init()

WIN_WIDTH = 903
WIN_HEIGHT = 1003

CAPTION = 'Whiteboard Application'

ERASE_BUTTON_WIDTH = 202.75
ERASE_BUTTON_HEIGHT = 92.5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
ORANGE = (255, 115, 0)
PURPLE = (165, 0, 215)
PINK = (215, 100, 175)

FPS = 60

CLOCK = pygame.time.Clock()

ROWS = WIN_WIDTH // 17
COLUMNS = WIN_HEIGHT // 17

MENU_HEIGHT = 100

PIXEL_VALUE = WIN_WIDTH // ROWS

BG_COLOR = WHITE

RENDER_GRID = False

def return_font(font_size):
	return pygame.font.SysFont('Comicsans', font_size)