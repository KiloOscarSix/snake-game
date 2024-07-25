import random
from canvas import Canvas
from config import COLS, ROWS, TILE_SIZE
from tile import Tile


class Food(Tile):
    def __init__(self) -> None:
        self.x = 10 * TILE_SIZE
        self.y = 10 * TILE_SIZE

    def create(self) -> None:
        self.x = random.randint(0, COLS - 1) * TILE_SIZE
        self.y = random.randint(0, ROWS - 1) * TILE_SIZE

    def draw(self, canvas: Canvas) -> None:
        canvas.create_rectangle(
            self.x, self.y, self.x + TILE_SIZE, self.y + TILE_SIZE, fill="red"
        )
