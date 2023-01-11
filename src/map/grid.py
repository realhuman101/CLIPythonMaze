from . import maze

class grid:
    def __init__(self, width: int, height: int) -> None:
        self.size = (width, height)
        self.maze = maze.makeMaze(width, height)
        self.clear()

    def clear(self) -> None:
        self.board = [i[:] for i in self.maze]

    def change(self, x, y, value) -> None:
        self.board[y][x] = value
        
    def newMaze(self) -> list[list[str]]:
        self.maze = maze.makeMaze(self.width, self.height)
        return self.maze

    def print(self) -> None:
        print('\n'.join([''.join(i) for i in self.board]))
