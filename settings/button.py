from .setup import *

# A class to represent the color, erase, and clear buttons
class Button():
	def __init__(self, x, y, width, height, color, text = None, text_color = BLACK):
		self.x = x 
		self.y = y 
		self.width = width 
		self.height = height
		self.color = color

# Optional parameters, specifically for the erase and clear buttons, as they contain text
		self.text = text
		self.text_color = text_color

	def update_operation(self, win):

# Creates boxes wtih outlines around the buttons 
		pygame.draw.rect(win, self.color, ((self.x, self.y), (self.width, self.height)))
			
		pygame.draw.rect(win, BLACK, ((self.x, self.y), (self.width, self.height)), 2)

		if self.text:
			button_font = return_font(20)

			render_font_surface = button_font.render(self.text, 1, self.text_color)
			win.blit(render_font_surface, (self.x + self.width // 2 - (render_font_surface.get_width() // 2), 
				self.y + self.height // 2 - (render_font_surface.get_height() // 2)))

	def check_if_clicked(self, cursor_pos):
		x, y = cursor_pos

# Checks if user cursor is not within the boundaries of the button
		if not (x >= self.x and x <= self.x + self.width):
			return False

		elif not (y >= self.y and y <= self.y + self.height):
			return False

# Otherwise, returns true
		else:
			return True