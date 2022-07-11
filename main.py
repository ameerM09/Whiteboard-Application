from settings import *

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption(CAPTION)

def create_drawing_grid(rows, columns, color):
	drawing_grid = []

	for x in range(rows):
		drawing_grid.append([])

		for _ in range(columns):
			drawing_grid[x].append(color)

	return drawing_grid

def render_drawing_grid(rows, columns, drawing_grid):

# Gathers rows and columns
	for x, row in enumerate(drawing_grid):
		for y, pixel in enumerate(row):
			pygame.draw.rect(WIN, pixel, (y * PIXEL_VALUE, x * PIXEL_VALUE, PIXEL_VALUE, PIXEL_VALUE))

	if RENDER_GRID:
		for x in range(rows + 1):
			pygame.draw.line(WIN, BLACK, (0, x * PIXEL_VALUE), (WIN_WIDTH, x * PIXEL_VALUE))

		for y in range(columns + 1):
			pygame.draw.line(WIN, BLACK, (y * PIXEL_VALUE, 0), (y * PIXEL_VALUE, WIN_HEIGHT - MENU_HEIGHT))

def get_cursor_pos_location(cursor_pos):

# Creates a pixel grid for the pen color
	x, y = cursor_pos

	row = y // PIXEL_VALUE
	column = x // PIXEL_VALUE

	if row >= ROWS:
		raise IndexError 

	return row, column

def render_elements(func_buttons):
	WIN.fill(BG_COLOR)

	for func_button in func_buttons:
		func_button.update_operation(WIN)

def main_loop():
	run = True

# Button objects
	func_buttons = [
		Button(10, WIN_HEIGHT - MENU_HEIGHT // 2 - 45, 35, 35, BLACK),
		Button(70, WIN_HEIGHT - MENU_HEIGHT // 2 - 45, 35, 35, RED),
		Button(130, WIN_HEIGHT - MENU_HEIGHT // 2 - 45, 35, 35, ORANGE),
		Button(190, WIN_HEIGHT - MENU_HEIGHT // 2 - 45, 35, 35, YELLOW),

		Button(10, WIN_HEIGHT - MENU_HEIGHT // 2 , 35, 35, GREEN),
		Button(70, WIN_HEIGHT - MENU_HEIGHT // 2 , 35, 35, BLUE),
		Button(130, WIN_HEIGHT - MENU_HEIGHT // 2, 35, 35, PURPLE),
		Button(190, WIN_HEIGHT - MENU_HEIGHT // 2 , 35, 35, PINK),

		Button(250, WIN_HEIGHT - MENU_HEIGHT // 2 - 25, 80, 50, WHITE, 'Erase', BLACK),
		Button(340, WIN_HEIGHT - MENU_HEIGHT // 2 - 25, 80, 50, WHITE, 'Clear', BLACK)
	]

	PEN_COLOR = BLACK

	drawing_grid = create_drawing_grid(ROWS, COLUMNS, BG_COLOR)

	while run:
		CLOCK.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				sys.exit()

# Checks for the left-mouse-button being clicked on screen
			if pygame.mouse.get_pressed()[0]:
				cursor_pos = pygame.mouse.get_pos()

				try:
					row, column = get_cursor_pos_location(cursor_pos)
					drawing_grid[row][column] = PEN_COLOR

				except IndexError:
					for func_button in func_buttons:
						if func_button.check_if_clicked(cursor_pos):
							PEN_COLOR = func_button.color

# Checks if the user clicked on the clear button and refills the screen with black if done so
							if func_button.text == 'Clear':
								drawing_grid = create_drawing_grid(ROWS, COLUMNS, BG_COLOR)

								PEN_COLOR = BLACK

		render_elements(func_buttons)

		render_drawing_grid(ROWS, COLUMNS, drawing_grid)

		pygame.display.update()

main_loop()

# Module cannot be imported
if __name__ == '__main__':
	main_loop()