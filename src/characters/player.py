from ..exceptions import *

class player:
	def __init__(self, width: int, height: int, startX: int, startY: int, maze: list[list[str]]) -> None:
		self.CHARACTERS = {key:f"\033[36m{pos}\033[0m" for key, pos in {
			'w': '⇑',
			'a': '⇐',
			's': '⇓',
			'd': '⇒'
		}.items()}

		self.char = self.CHARACTERS['w']

		self.x, self.y = startX,startY
		self.size = (width, height)

		self.maze = maze

	def move(self, key: str) -> None:
		self.char = self.CHARACTERS[key]

		match key:
			case 'w':
				self.y -= 1

				if 0 <= self.y < self.size[1]:
					if self.maze[self.y][self.x] == '█':
						self.y += 1
			case 'a':
				self.x -= 1

				if 0 <= self.x < self.size[0]:
					if self.maze[self.y][self.x] == '█':
						self.x += 1
			case 's':
				self.y += 1

				if 0 <= self.y < self.size[1]:
					if self.maze[self.y][self.x] == '█':
						self.y -= 1
			case 'd':
				self.x += 1

				if 0 <= self.x < self.size[0]:
					if self.maze[self.y][self.x] == '█':
						self.x -= 1

		if self.x < 0:
			self.x = 0
		elif self.x >= self.size[0]:
			self.x = self.size[0]-1

		if self.y < 0:
			self.y = 0
		elif self.y >= self.size[1]:
			self.y = self.size[1]-1

		if self.y == self.size[1]-1:
			raise ReachedEnd
