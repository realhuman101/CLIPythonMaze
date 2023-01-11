import random

def surroundingCells(maze: list[list[str]], randWall: list[int]):
	sCells = 0
	if (maze[randWall[0]-1][randWall[1]] == ' '):
		sCells += 1
	if (maze[randWall[0]+1][randWall[1]] == ' '):
		sCells += 1
	if (maze[randWall[0]][randWall[1]-1] == ' '):
		sCells += 1
	if (maze[randWall[0]][randWall[1]+1] == ' '):
		sCells += 1

	return sCells

def makeMaze(width: int, height: int) -> list[list[str]]:
	cell = ' '
	unvisited = '-'
	maze = []

	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		maze.append(line)

	startingHeight = int(random.random()*height)
	startingWidth = int(random.random()*width)
	if (startingHeight == 0):
		startingHeight += 1
	if (startingHeight == height-1):
		startingHeight -= 1
	if (startingWidth == 0):
		startingWidth += 1
	if (startingWidth == width-1):
		startingWidth -= 1

	maze[startingHeight][startingWidth] = cell
	walls = []
	walls.append([startingHeight - 1, startingWidth])
	walls.append([startingHeight, startingWidth - 1])
	walls.append([startingHeight, startingWidth + 1])
	walls.append([startingHeight + 1, startingWidth])

	maze[startingHeight-1][startingWidth] = '█'
	maze[startingHeight][startingWidth - 1] = '█'
	maze[startingHeight][startingWidth + 1] = '█'
	maze[startingHeight + 1][startingWidth] = '█'

	while walls:
		randWall = walls[int(random.random()*len(walls))-1]

		if (randWall[1] != 0):
			if (maze[randWall[0]][randWall[1]-1] == '-' and maze[randWall[0]][randWall[1]+1] == ' '):
				sCells = surroundingCells(maze, randWall)

				if (sCells < 2):
					maze[randWall[0]][randWall[1]] = ' '

					if (randWall[0] != 0):
						if (maze[randWall[0]-1][randWall[1]] != ' '):
							maze[randWall[0]-1][randWall[1]] = '█'
						if ([randWall[0]-1, randWall[1]] not in walls):
							walls.append([randWall[0]-1, randWall[1]])

					if (randWall[0] != height-1):
						if (maze[randWall[0]+1][randWall[1]] != ' '):
							maze[randWall[0]+1][randWall[1]] = '█'
						if ([randWall[0]+1, randWall[1]] not in walls):
							walls.append([randWall[0]+1, randWall[1]])

					if (randWall[1] != 0):	
						if (maze[randWall[0]][randWall[1]-1] != ' '):
							maze[randWall[0]][randWall[1]-1] = '█'
						if ([randWall[0], randWall[1]-1] not in walls):
							walls.append([randWall[0], randWall[1]-1])
				

				for wall in walls:
					if (wall[0] == randWall[0] and wall[1] == randWall[1]):
						walls.remove(wall)

				continue

		if (randWall[0] != 0):
			if (maze[randWall[0]-1][randWall[1]] == '-' and maze[randWall[0]+1][randWall[1]] == ' '):

				sCells = surroundingCells(maze, randWall)
				if (sCells < 2):
					maze[randWall[0]][randWall[1]] = ' '

					if (randWall[0] != 0):
						if (maze[randWall[0]-1][randWall[1]] != ' '):
							maze[randWall[0]-1][randWall[1]] = '█'
						if ([randWall[0]-1, randWall[1]] not in walls):
							walls.append([randWall[0]-1, randWall[1]])

					if (randWall[1] != 0):
						if (maze[randWall[0]][randWall[1]-1] != ' '):
							maze[randWall[0]][randWall[1]-1] = '█'
						if ([randWall[0], randWall[1]-1] not in walls):
							walls.append([randWall[0], randWall[1]-1])

					if (randWall[1] != width-1):
						if (maze[randWall[0]][randWall[1]+1] != ' '):
							maze[randWall[0]][randWall[1]+1] = '█'
						if ([randWall[0], randWall[1]+1] not in walls):
							walls.append([randWall[0], randWall[1]+1])

				for wall in walls:
					if (wall[0] == randWall[0] and wall[1] == randWall[1]):
						walls.remove(wall)

				continue

		if (randWall[0] != height-1):
			if (maze[randWall[0]+1][randWall[1]] == '-' and maze[randWall[0]-1][randWall[1]] == ' '):

				sCells = surroundingCells(maze, randWall)
				if (sCells < 2):
					maze[randWall[0]][randWall[1]] = ' '

					if (randWall[0] != height-1):
						if (maze[randWall[0]+1][randWall[1]] != ' '):
							maze[randWall[0]+1][randWall[1]] = '█'
						if ([randWall[0]+1, randWall[1]] not in walls):
							walls.append([randWall[0]+1, randWall[1]])
					if (randWall[1] != 0):
						if (maze[randWall[0]][randWall[1]-1] != ' '):
							maze[randWall[0]][randWall[1]-1] = '█'
						if ([randWall[0], randWall[1]-1] not in walls):
							walls.append([randWall[0], randWall[1]-1])
					if (randWall[1] != width-1):
						if (maze[randWall[0]][randWall[1]+1] != ' '):
							maze[randWall[0]][randWall[1]+1] = '█'
						if ([randWall[0], randWall[1]+1] not in walls):
							walls.append([randWall[0], randWall[1]+1])

				for wall in walls:
					if (wall[0] == randWall[0] and wall[1] == randWall[1]):
						walls.remove(wall)

				continue

		if (randWall[1] != width-1):
			if (maze[randWall[0]][randWall[1]+1] == '-' and maze[randWall[0]][randWall[1]-1] == ' '):

				sCells = surroundingCells(maze, randWall)
				if (sCells < 2):
					maze[randWall[0]][randWall[1]] = ' '

					if (randWall[1] != width-1):
						if (maze[randWall[0]][randWall[1]+1] != ' '):
							maze[randWall[0]][randWall[1]+1] = '█'
						if ([randWall[0], randWall[1]+1] not in walls):
							walls.append([randWall[0], randWall[1]+1])
					if (randWall[0] != height-1):
						if (maze[randWall[0]+1][randWall[1]] != ' '):
							maze[randWall[0]+1][randWall[1]] = '█'
						if ([randWall[0]+1, randWall[1]] not in walls):
							walls.append([randWall[0]+1, randWall[1]])
					if (randWall[0] != 0):	
						if (maze[randWall[0]-1][randWall[1]] != ' '):
							maze[randWall[0]-1][randWall[1]] = '█'
						if ([randWall[0]-1, randWall[1]] not in walls):
							walls.append([randWall[0]-1, randWall[1]])

				for wall in walls:
					if (wall[0] == randWall[0] and wall[1] == randWall[1]):
						walls.remove(wall)

				continue

		for wall in walls:
			if (wall[0] == randWall[0] and wall[1] == randWall[1]):
				walls.remove(wall)

	for i in range(height):
		for j in range(width):
			if (maze[i][j] == '-'):
				maze[i][j] = '█'

	for i in range(width):
		if (maze[1][i] == ' '):
			maze[0][i] = ' '
			break

	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == ' '):
			maze[height-1][i] = ' '
			break

	return maze
