import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CELL_SIZE = 40
COLS = SCREEN_WIDTH // CELL_SIZE
ROWS = SCREEN_HEIGHT // CELL_SIZE

# Цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)

# Настройки окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра с шарами")

# Сетка для хранения состояния шаров (0 - пусто, 1 - красный, 2 - зеленый)
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = GRAY
            if grid[row][col] == 1:
                color = RED
            elif grid[row][col] == 2:
                color = GREEN
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def generate_ball():
    return random.choice([1, 2])  # 1 - красный шар, 2 - зеленый шар

def drop_ball(column, ball_color):
    for row in range(ROWS-1, -1, -1):
        if grid[row][column] == 0:
            grid[row][column] = ball_color
            return True
    return False  # Если колонка полностью заполнена

def check_winner():
    # Проверка горизонтальных, вертикальных и диагональных линий
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] != 0:
                if check_line(row, col, 1, 0) or check_line(row, col, 0, 1) or check_line(row, col, 1, 1) or check_line(row, col, 1, -1):
                    return grid[row][col]
    return 0

def check_line(row, col, delta_row, delta_col):
    color = grid[row][col]
    count = 0
   
